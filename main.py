import pygame 
from datetime import date 

WIDTH = 1280
HEIGHT = 720

# Distance between two plant holder in a row 
plantHolderDiff_x = 320 
# Distance beteween rows 
plantHolderDiff_y = 270

# Buffer to get the first plant centered 
x_buffer = 80
y_buffer = 46

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background_sprite = pygame.image.load('assets/background.png')
background_sprite = pygame.transform.scale(background_sprite, (WIDTH, HEIGHT))

plant = pygame.image.load('assets/plant_template.png')
plant = pygame.transform.scale(plant, (150, 150))


def update_date(current_date):
    # Write current date to the external file
    with open('record.txt', "r") as record:
        line = record.readline().strip()

        year = int(line[:4])
        month = int(line[5:7])
        day = int(line[-2:])
        previous_date = date(year, month, day)

    # Read previously recorded date
    with open('record.txt', "w") as record:
        record.write(f"{current_date}")

    return previous_date

# Caluclate No. of days passed since previously ran 
def get_days_passed():
    current_date = date.today()
    previous_date = update_date(current_date)
    delta = current_date - previous_date

    return delta.days


class Plant:
    # frequency -> in how long the plant have to be watered
    def __init__(self, frequency, days_passed):
        self.frequency = frequency
        self.days_passed = days_passed

    def is_expired(self):
        if self.frequency <= self.days_passed:
            return True
        return False


days_passed = get_days_passed()
plants = [Plant(1, days_passed),
          Plant(2, days_passed),
          Plant(3, days_passed),
          Plant(4, days_passed),
          Plant(5, days_passed),
          Plant(6, days_passed),
          Plant(7, days_passed),
          Plant(8, days_passed),]


def draw():
    screen.blit(background_sprite, (0,0))
    draw_plants()


def draw_plants():
    # Row
    for j in range(2):
        # Column
        for i in range(4):
            # Get all plants and check if expired(Needs watering)
            if not plants[i + (j*2)].is_expired():
                # Draw plant
                screen.blit(plant,
                            (i*plantHolderDiff_x + x_buffer,
                             j*plantHolderDiff_y + y_buffer))


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw()
        pygame.display.update()

    pygame.quit()


main()
