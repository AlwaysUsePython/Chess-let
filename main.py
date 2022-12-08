import graphics
import movement
import pygame
import lines
import time

graphics.setup()

running = True

gameState = lines.GameState("rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR")

screen = pygame.display.set_mode((1000, 640))

legalMoves = "I"*64

highlights = "_"*64
selected = False
flipped = False

database = lines.MoveDatabase("Queen's Gambit")
computerColor = "black"

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RETURN:
                gameState = lines.GameState("rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR")
                legalMoves = "I" * 64

                highlights = "_" * 64
                selected = False
                flipped = False

            if event.key == pygame.K_LEFT:
                if gameState.prev != None:
                    gameState = gameState.prev

            if event.key == pygame.K_RIGHT:
                if gameState.next != None:
                    gameState = gameState.next

            if event.key == pygame.K_UP:
                gameState = gameState.getHead()

            if event.key == pygame.K_DOWN:
                gameState = gameState.getTail()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            if pos[0] >= 950 and pos[1] >= 590:
                flipped = not flipped

            if pos[0] <= 640:
                row = pos[1] // 80
                col = pos[0] // 80

                if flipped:
                    col = 7 - col
                    row = 7 - row

                if not selected:

                    if gameState.move == "black":
                        goodPieces = "rnbqkp"
                    else:
                        goodPieces = "RNBQKP"

                    if gameState.board[row*8+col] in goodPieces:
                        legalMoves = movement.getLegalMoves(gameState.board, row, col)
                        highlights = ["_"]*64
                        highlights[row*8+col] = "G"
                        highlights = "".join(highlights)
                        selected = True

                    else:
                        highlights = "_"*64
                        legalMoves = "I"*64

                elif selected:
                    if legalMoves[row*8+col] != "I":
                        newBoard = movement.makeMove(gameState.board, highlights.index("G"), row*8+col)
                        print(highlights.index("G"), row*8+col)
                        if gameState.move == "white":
                            newState = lines.GameState(newBoard, "black", gameState)
                            gameState.setNext(newState)
                            gameState = newState
                        else:
                            newState = lines.GameState(newBoard, "white", gameState)
                            gameState.setNext(newState)
                            gameState = newState

                        try:
                            print("BEST MOVES FOR", gameState.move.upper() + ":", database.getMoves(gameState))
                        except:
                            print("This is not part of the database")
                    highlights = "_"*64
                    legalMoves = "I"*64
                    selected = False


    graphics.drawBoard(gameState.board, legalMoves, screen, gameState.move, highlights, flipped)
    pygame.display.update()