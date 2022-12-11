import graphics
import movement
import pygame
import lines
import random

opening = "G6 Modern.txt"

graphics.setup()

running = True

gameState = lines.GameState("rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR")

screen = pygame.display.set_mode((1000, 640))

legalMoves = "I"*64

highlights = "_"*64
selected = False
flipped = False

database = lines.MoveDatabase(opening)

if opening in ["G6 Modern"]:
    computerColor = "white"

else:
    computerColor = "black"

correct = None

if computerColor == "white":
    flipped = True
else:
    flipped = False

newBestMoves = database.getMoves(gameState)

if computerColor == "white":
    chosenMove = newBestMoves[random.randint(0, len(newBestMoves) - 1)]

    newBoard = movement.makeMove(gameState.board, int(chosenMove[0]), int(chosenMove[1]))
    if gameState.move == "white":
        newState = lines.GameState(newBoard, "black", gameState)
        gameState.setNext(newState)
        gameState = newState
    else:
        newState = lines.GameState(newBoard, "white", gameState)
        gameState.setNext(newState)
        gameState = newState

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

                newBestMoves = database.getMoves(gameState)

                if computerColor == "white":
                    chosenMove = newBestMoves[random.randint(0, len(newBestMoves) - 1)]

                    newBoard = movement.makeMove(gameState.board, int(chosenMove[0]), int(chosenMove[1]))
                    if gameState.move == "white":
                        newState = lines.GameState(newBoard, "black", gameState)
                        gameState.setNext(newState)
                        gameState = newState
                    else:
                        newState = lines.GameState(newBoard, "white", gameState)
                        gameState.setNext(newState)
                        gameState = newState

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
                            bestMoves = database.getMoves(gameState.prev)
                            print("move:", [highlights.index("G"), row*8+col])
                            print(bestMoves)
                            found = False
                            for move in bestMoves:
                                if int(move[0]) == highlights.index("G") and int(move[1]) == row*8+col:
                                    found = True

                            if found:
                                correct = True
                            else:
                                correct = False

                            try:
                                newBestMoves = database.getMoves(gameState)

                                print("BEST MOVES FOR", gameState.move.upper() + ":", newBestMoves)

                                if gameState.move == computerColor:

                                    chosenMove = newBestMoves[random.randint(0, len(newBestMoves)-1)]

                                    newBoard = movement.makeMove(gameState.board, int(chosenMove[0]), int(chosenMove[1]))
                                    print(highlights.index("G"), row * 8 + col)
                                    if gameState.move == "white":
                                        newState = lines.GameState(newBoard, "black", gameState)
                                        gameState.setNext(newState)
                                        gameState = newState
                                    else:
                                        newState = lines.GameState(newBoard, "white", gameState)
                                        gameState.setNext(newState)
                                        gameState = newState

                            except Exception as e:
                                print(e)
                                if correct == True:
                                    print("END OF LINE")

                        except:
                            print("This is not part of the database")
                            correct = None
                        print(correct)
                    highlights = "_"*64
                    legalMoves = "I"*64
                    selected = False


    graphics.drawBoard(gameState.board, legalMoves, screen, gameState.move, highlights, flipped, correct)
    pygame.display.update()