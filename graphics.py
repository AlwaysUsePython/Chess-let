import pygame
import movement

####### Chess board notation: #######
# White Pieces: RNBQKP
# Black Pieces: rnbqkp
# Blank Space: _
# Initial Board Setup: "rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR"

# Set up the images for later use
imageDict = {}

# initialize pygame
pygame.init()

## LOAD AND RESIZE THE IMAGES ##
def setup():

    # load images
    FlipButton = pygame.image.load("Chess Pieces/Flip Button.png")
    imageDict["FlipButton"] = pygame.transform.scale(FlipButton, (50, 50))
    Correct = pygame.image.load("Chess Pieces/Correct.png")
    imageDict["Correct"] = pygame.transform.scale(Correct, (280, (257/917)*280))
    Hint = pygame.image.load("Chess Pieces/Incorrect.png")
    imageDict["Incorrect"] = pygame.transform.scale(Hint, (280, int((212/973)*280)))

    BBishop = pygame.image.load("Chess Pieces/Black Bishop.png")
    BKing = pygame.image.load("Chess Pieces/Black King.png")
    BKnight = pygame.image.load("Chess Pieces/Black Knight.png")
    BPawn = pygame.image.load("Chess Pieces/Black Pawn.png")
    BQueen = pygame.image.load("Chess Pieces/Black Queen.png")
    BRook = pygame.image.load("Chess Pieces/Black Rook.png")

    WBishop = pygame.image.load("Chess Pieces/White Bishop.png")
    WKing = pygame.image.load("Chess Pieces/White King.png")
    WKnight = pygame.image.load("Chess Pieces/White Knight.png")
    WPawn = pygame.image.load("Chess Pieces/White Pawn.png")
    WQueen = pygame.image.load("Chess Pieces/White Queen.png")
    WRook = pygame.image.load("Chess Pieces/White Rook.png")

    # resize the images to be game pieces
    imageDict["BBishop"] = pygame.transform.scale(BBishop, (80, 80))
    imageDict["BKing"] = pygame.transform.scale(BKing, (80, 80))
    imageDict["BKnight"] = pygame.transform.scale(BKnight, (80, 80))
    imageDict["BPawn"] = pygame.transform.scale(BPawn, (80, 80))
    imageDict["BQueen"] = pygame.transform.scale(BQueen, (80, 80))
    imageDict["BRook"] = pygame.transform.scale(BRook, (80, 80))


    imageDict["WBishop"] = pygame.transform.scale(WBishop, (80, 80))
    imageDict["WKing"] = pygame.transform.scale(WKing, (80, 80))
    imageDict["WKnight"] = pygame.transform.scale(WKnight, (80, 80))
    imageDict["WPawn"] = pygame.transform.scale(WPawn, (80, 80))
    imageDict["WQueen"] = pygame.transform.scale(WQueen, (80, 80))
    imageDict["WRook"] = pygame.transform.scale(WRook, (80, 80))

    # and the mini ones
    imageDict["mBBishop"] = pygame.transform.scale(BBishop, (40, 40))
    imageDict["mBKing"] = pygame.transform.scale(BKing, (40, 40))
    imageDict["mBKnight"] = pygame.transform.scale(BKnight, (40, 40))
    imageDict["mBPawn"] = pygame.transform.scale(BPawn, (40, 40))
    imageDict["mBQueen"] = pygame.transform.scale(BQueen, (40, 40))
    imageDict["mBRook"] = pygame.transform.scale(BRook, (40, 40))

    imageDict["mWBishop"] = pygame.transform.scale(WBishop, (40, 40))
    imageDict["mWKing"] = pygame.transform.scale(WKing, (40, 40))
    imageDict["mWKnight"] = pygame.transform.scale(WKnight, (40, 40))
    imageDict["mWPawn"] = pygame.transform.scale(WPawn, (40, 40))
    imageDict["mWQueen"] = pygame.transform.scale(WQueen, (40, 40))
    imageDict["mWRook"] = pygame.transform.scale(WRook, (40, 40))

## DRAW SQUARE COORDINATES ##
def drawSquareNames(screen, flipped):

    blackSquareColor = (181,136,99)
    whiteSquareColor = (240,217,182)

    font = pygame.font.Font("freesansbold.ttf", 10)

    if not flipped:
        for i in range(8, 0, -1):
            if i % 2 == 0:
                text = font.render(str(i), True, blackSquareColor)
            else:
                text = font.render(str(i), True, whiteSquareColor)
            rect = text.get_rect()
            rect.center = (5, 80*(8-i) + 5)
            screen.blit(text, rect)
        letters = "abcdefgh"
        for i in range(8):
            if i % 2 == 1:
                text = font.render(letters[i], True, blackSquareColor)
            else:
                text = font.render(letters[i], True, whiteSquareColor)
            rect = text.get_rect()
            rect.center = (80*i + 75, 635)
            screen.blit(text, rect)

    else:
        for i in range(0, 8):
            if i % 2 == 0:
                text = font.render(str(i+1), True, blackSquareColor)
            else:
                text = font.render(str(i+1), True, whiteSquareColor)
            rect = text.get_rect()
            rect.center = (5, 80*(i) + 5)
            screen.blit(text, rect)
        letters = "abcdefgh"
        for i in range(8):
            if i % 2 == 1:
                text = font.render(letters[7-i], True, blackSquareColor)
            else:
                text = font.render(letters[7-i], True, whiteSquareColor)
            rect = text.get_rect()
            rect.center = (80*i + 75, 635)
            screen.blit(text, rect)

## DRAW THE PIECES ON THE BOARD IN THE RIGHT SQUARES. INPUT IS BOARD AS A STRING ##
def drawPieces(board, screen, flipped):
    pieceCounter = 0
    for piece in board:

        col = pieceCounter % 8
        row = pieceCounter // 8

        if flipped:
            col = 7 - col
            row = 7 - row

        if piece == "P":
            screen.blit(imageDict["WPawn"], (80*col, 80*row))
        elif piece == "p":
            screen.blit(imageDict["BPawn"], (80*col, 80*row))
        elif piece == "N":
            screen.blit(imageDict["WKnight"], (80*col, 80*row))
        elif piece == "n":
            screen.blit(imageDict["BKnight"], (80*col, 80*row))
        elif piece == "B":
            screen.blit(imageDict["WBishop"], (80*col, 80*row))
        elif piece == "b":
            screen.blit(imageDict["BBishop"], (80*col, 80*row))
        elif piece == "R":
            screen.blit(imageDict["WRook"], (80*col, 80*row))
        elif piece == "r":
            screen.blit(imageDict["BRook"], (80*col, 80*row))
        elif piece == "Q":
            screen.blit(imageDict["WQueen"], (80*col, 80*row))
        elif piece == "q":
            screen.blit(imageDict["BQueen"], (80*col, 80*row))
        elif piece == "K" or piece == "H":
            screen.blit(imageDict["WKing"], (80*col, 80*row))
        elif piece == "k" or piece == "I":
            screen.blit(imageDict["BKing"], (80*col, 80*row))
        pieceCounter += 1

## DRAW THE BOARD IN THE BACKGROUND ##
def drawBackground(screen, correct=None):

    # Dark Gray Window
    mediumGray = (55, 52, 49)
    darkGray = (38, 36, 33)
    buttonGray = (46, 44, 41)

    pygame.draw.rect(screen, darkGray, pygame.Rect(640, 0, 360, 640))
    pygame.draw.rect(screen, mediumGray, pygame.Rect(640, 0, 360, 50))
    if correct == None:
        pass
    elif correct:
        screen.blit(imageDict["Correct"], (680, 320-((257/917)*140)))
    elif not correct:
        screen.blit(imageDict["Incorrect"], (680, 320-(int((212/973)*140))))

    screen.blit(imageDict["FlipButton"], (950, 590))


    # Colors in the black squares
    blackSquareColor = (181,136,99)
    whiteSquareColor = (240,217,182)

    for row in range(8):

        if row % 2 == 0:
            # rows 0, 2, 4, 6 -> white squares start
            startWhite = True
        else:
            startWhite = False

        for col in range(8):

            if col % 2 == 0:
                whiteSquare = startWhite
            else:
                whiteSquare = not startWhite

            if whiteSquare:
                pygame.draw.rect(screen, whiteSquareColor, pygame.Rect(row*80, col*80, 80, 80))
            else:
                pygame.draw.rect(screen, blackSquareColor, pygame.Rect(row*80, col*80, 80, 80))

## DRAW HIGHLIGHTS ##
def drawHighlights(highlights, screen, flipped):
    darkLegalMoveColor = (106, 111, 65)
    lightLegalMoveColor = (135, 151, 107)


    squareCounter = 0
    for square in highlights:
        col = squareCounter % 8
        row = squareCounter // 8

        if flipped:
            col = 7 - col
            row = 7 - row

        if square == "G":
            if (row + col) % 2 == 0:
                pygame.draw.rect(screen, lightLegalMoveColor, pygame.Rect(col*80, row*80, 80, 80))
            else:
                pygame.draw.rect(screen, darkLegalMoveColor, pygame.Rect(col*80, row*80, 80, 80))

        squareCounter += 1

## DRAW CHECKS ##
def drawChecks(board, color, screen, flipped):
    red = (250, 120, 120)

    kingSquare = movement.getKingSquare(color, board)

    if movement.isInCheck(color, board):
        if not flipped:
            pygame.draw.circle(screen, red, (kingSquare%8 * 80 + 40, kingSquare//8 * 80 + 40), 40)
        else:
            pygame.draw.circle(screen, red, ((7-(kingSquare%8))*80+40, (7-kingSquare//8)*80+40), 40)
## DRAWS LEGAL MOVES ##
def drawLegalMoves(legalMoves, screen, flipped):

    darkLegalMoveColor = (106,111,65)
    lightLegalMoveColor = (135,151,107)

    squareCounter = 0
    for square in legalMoves:
        col = squareCounter % 8
        row = squareCounter // 8

        if flipped:
            col = 7 - col
            row = 7 - row

        if square == "L":
            if (row + col) % 2 == 0:
                pygame.draw.circle(screen, lightLegalMoveColor, (col*80+40, row*80+40), 10)
            else:
                pygame.draw.circle(screen, darkLegalMoveColor, (col*80+40, row*80+40), 10)

        elif square == "T":
            if (row + col) % 2 == 0:
                pygame.draw.circle(screen, lightLegalMoveColor, (col*80+40, row*80+40), 40, 5)
            else:
                pygame.draw.circle(screen, darkLegalMoveColor, (col*80+40, row*80+40), 40, 5)
        squareCounter += 1

## DRAW EVERYTHING ##
def drawBoard(board, legalMoves, screen, turn, highlights, flipped, correct=None):
    drawBackground(screen, correct)
    drawHighlights(highlights, screen, flipped)
    drawChecks(board, turn, screen, flipped)
    drawSquareNames(screen, flipped)
    drawPieces(board, screen, flipped)
    drawLegalMoves(legalMoves, screen, flipped)