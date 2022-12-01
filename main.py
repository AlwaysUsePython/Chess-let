import graphics
import pygame

graphics.setup()

running = True

screen = pygame.display.set_mode((1000, 640))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    graphics.drawBoard("rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR", screen)
    pygame.display.update()