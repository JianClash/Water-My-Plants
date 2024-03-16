import pygame 

WIDTH = 1280
HEIGHT = 720

plantHolderDiff_x = 320 
x_buffer = 80
plantHolderDiff_y = 270
y_buffer = 46

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background_sprite = pygame.image.load('assets/background.png')
background_sprite = pygame.transform.scale(background_sprite, (WIDTH, HEIGHT))

plant = pygame.image.load('assets/plant_template.png')
plant = pygame.transform.scale(plant, (150, 150))


def draw():
    screen.blit(background_sprite, (0,0))
    draw_plants()

def draw_plants():
    for j in range(2):
        for i in range(4):
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
