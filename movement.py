# See graphics.py for board notation

## INPUT OF BOARD + COORDINATES, OUTPUT OF STRING WITH MAP OF LEGAL MOVES ##
# Map Format: "L" is legal, "I" is illegal
# Note: Passes calculation off to helper methods for each piece
def getLegalMoves(board, row, col):

    # if it isn't a piece, return all illegal
    if board[row*8+col] == "_":
        return "I"*64

    pieceType = board[row*8+col].lower()

    if pieceType == "p":
        initialMap = getPawnMap(board, row, col)

    elif pieceType == "r":
        initialMap = getRookMap(board, row, col)

    elif pieceType == "n":
        initialMap = getKnightMap(board, row, col)

    elif pieceType == "b":
        initialMap = getBishopMap(board, row, col)

    elif pieceType == "k":
        initialMap = getKingMap(board, row, col)

    else:
        initialMap = getQueenMap(board, row, col)

    return initialMap


def getPawnMap(board, row, col):
    map = ["I"]*64

    # check the color of the pawn
    if board[row*8+col] != board[row*8+col].lower():

        if row == 6:
            if board[32+col] == "_" and board[40+col] == "_":
                map[32+col] = "L"

        if board[(row-1)*8+col] == "_":
            map[(row-1)*8+col] = "L"

        # make sure we don't go off the board
        if col <= 6:
            if board[(row-1)*8+col+1].lower == board[(row-1)*8+col+1].lower and board[(row-1)*8 + col + 1] != "_":
                map[(row-1)*8+col+1] = "T"

        if col >= 1:
            if board[(row-1)*8+col-1].lower == board[(row-1)*8+col-1].lower and board[(row-1)*8 + col - 1] != "_":
                map[(row-1)*8+col-1] = "T"

    else:
        if row == 1:
            if board[24 + col] == "_" and board[16+col] == "_":
                map[24 + col] = "L"

        if board[(row + 1) * 8 + col] == "_":
            map[(row + 1) * 8 + col] = "L"

        # make sure we don't go off the board
        if col <= 6:
            if board[(row + 1) * 8 + col + 1].lower == board[(row + 1) * 8 + col + 1].lower and board[(row+1)*8 + col + 1] != "_":
                map[(row + 1) * 8 + col + 1] = "T"
        if col >= 1:
            if board[(row + 1) * 8 + col + 1].lower == board[(row + 1) * 8 + col - 1].lower and board[(row+1)*8 + col - 1] != "_":
                map[(row + 1) * 8 + col - 1] = "T"

    return "".join(map)

def getRookMap(board, row, col):
    pass

def getKnightMap(board, row, col):
    pass

def getBishopMap(board, row, col):
    pass

def getKingMap(board, row, col):
    pass

def getQueenMap(board, row, col):
    pass
