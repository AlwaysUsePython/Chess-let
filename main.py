import graphics
import movement
import pygame

graphics.setup()

running = True

board = "rnbqkbnrpppppppp______________________________p_PPPPPPPPRNBQKBNR"

screen = pygame.display.set_mode((1000, 640))

legalMoves = "I"*64

highlights = "_"*64

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if pos[0] <= 640:
                row = pos[1] // 80
                col = pos[0] // 80

                legalMoves = movement.getLegalMoves(board, row, col)

                if board[row*8+col] != "_":
                    highlights = ["_"]*64
                    highlights[row*8+col] = "G"
                    highlights = "".join(highlights)

                else:
                    highlights = "_"*64

    graphics.drawBoard(board, legalMoves, screen, highlights)
    pygame.display.update()