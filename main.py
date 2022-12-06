import graphics
import movement
import pygame

graphics.setup()

running = True

board = "rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR"

screen = pygame.display.set_mode((1000, 640))

legalMoves = "I"*64

highlights = "_"*64
selected = False
flipped = True
move = "white"

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if pos[0] >= 950 and pos[1] >= 590:
                flipped = not flipped

            if pos[0] <= 640:
                row = pos[1] // 80
                col = pos[0] // 80

                if not selected:

                    if move == "black":
                        goodPieces = "rnbqkp"
                    else:
                        goodPieces = "RNBQKP"

                    if board[row*8+col] in goodPieces:
                        legalMoves = movement.getLegalMoves(board, row, col)
                        highlights = ["_"]*64
                        highlights[row*8+col] = "G"
                        highlights = "".join(highlights)
                        selected = True

                    else:
                        highlights = "_"*64
                        legalMoves = "I"*64

                elif selected:
                    if legalMoves[row*8+col] != "I":
                        board = movement.makeMove(board, highlights.index("G"), row*8+col)
                        if move == "white":
                            move = "black"
                        else:
                            move = "white"

                    highlights = "_"*64
                    legalMoves = "I"*64
                    selected = False


    graphics.drawBoard(board, legalMoves, screen, move, highlights, flipped)
    pygame.display.update()