# See graphics.py for board notation

## MAKES MOVE WITH INPUT OF BOARD AND SINGLE COORDINATE LOCATIONS (IN THE STRING) ##
# NOTE: CASTLING NOT YET ADDED #
def makeMove(board, loc1, loc2):
    arrBoard = []
    for piece in board:
        arrBoard.append(piece)

    arrBoard[loc2] = board[loc1]
    arrBoard[loc1] = "_"

    return "".join(arrBoard)

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

    # check the color of the piece
    if board[row*8+col] != board[row*8+col].lower():

        if row == 6:
            if board[32+col] == "_" and board[40+col] == "_":
                map[32+col] = "L"

        if board[(row-1)*8+col] == "_":
            map[(row-1)*8+col] = "L"

        # make sure we don't go off the board
        if col <= 6:
            if board[(row-1)*8+col+1].lower() == board[(row-1)*8+col+1] and board[(row-1)*8 + col + 1] != "_":
                map[(row-1)*8+col+1] = "T"

        if col >= 1:
            if board[(row-1)*8+col-1].lower() == board[(row-1)*8+col-1] and board[(row-1)*8 + col - 1] != "_":
                map[(row-1)*8+col-1] = "T"

    else:
        if row == 1:
            if board[24 + col] == "_" and board[16+col] == "_":
                map[24 + col] = "L"

        if board[(row + 1) * 8 + col] == "_":
            map[(row + 1) * 8 + col] = "L"

        # make sure we don't go off the board
        if col <= 6:
            if board[(row + 1) * 8 + col + 1].lower() != board[(row + 1) * 8 + col + 1] and board[(row+1)*8 + col + 1] != "_":
                map[(row + 1) * 8 + col + 1] = "T"
        if col >= 1:
            if board[(row + 1) * 8 + col - 1].lower() != board[(row + 1) * 8 + col - 1] and board[(row+1)*8 + col - 1] != "_":
                map[(row + 1) * 8 + col - 1] = "T"

    return "".join(map)

def getRookMap(board, row, col):
    map = ["I"] * 64

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():
        # up
        blocked = False
        counter = 1
        while not blocked:
            if (row-counter+1) > 0 and board[(row-counter)*8+col] in "rnbqkp_":
                if board[(row-counter)*8+col] == "_":
                    map[(row-counter)*8+col] = "L"
                else:
                    map[(row-counter)*8+col] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        #down
        blocked = False
        counter = 1
        while not blocked:
            if (row+counter-1) < 7 and board[(row + counter) * 8 + col] in "rnbqkp_":
                if board[(row + counter) * 8 + col] == "_":
                    map[(row + counter) * 8 + col] = "L"
                else:
                    map[(row + counter) * 8 + col] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        #left
        blocked = False
        counter = 1
        while not blocked:
            if (col-counter+1) > 0 and board[row * 8 + col - counter] in "rnbqkp_":
                if board[row * 8 + col - counter] == "_":
                    map[row * 8 + col - counter] = "L"
                else:
                    map[row * 8 + col - counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        #right
        blocked = False
        counter = 1
        while not blocked:
            if (col+counter-1) < 7 and board[row * 8 + col + counter] in "rnbqkp_":
                if board[row * 8 + col + counter] == "_":
                    map[row * 8 + col + counter] = "L"
                else:
                    map[row * 8 + col + counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

    else:
        # up
        blocked = False
        counter = 1
        while not blocked:
            if (row - counter + 1) > 0 and board[(row - counter) * 8 + col] in "RNBQKP_":
                if board[(row - counter) * 8 + col] == "_":
                    map[(row - counter) * 8 + col] = "L"
                else:
                    map[(row - counter) * 8 + col] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # down
        blocked = False
        counter = 1
        while not blocked:
            if (row + counter - 1) < 7 and board[(row + counter) * 8 + col] in "RNBQKP_":
                if board[(row + counter) * 8 + col] == "_":
                    map[(row + counter) * 8 + col] = "L"
                else:
                    map[(row + counter) * 8 + col] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # left
        blocked = False
        counter = 1
        while not blocked:
            if (col - counter + 1) > 0 and board[row * 8 + col - counter] in "RNBQKP_":
                if board[row * 8 + col - counter] == "_":
                    map[row * 8 + col - counter] = "L"
                else:
                    map[row * 8 + col - counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # right
        blocked = False
        counter = 1
        while not blocked:
            if (col + counter - 1) < 7 and board[row * 8 + col + counter] in "RNBQKP_":
                if board[row * 8 + col + counter] == "_":
                    map[row * 8 + col + counter] = "L"
                else:
                    map[row * 8 + col + counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

    return "".join(map)

def getKnightMap(board, row, col):
    map = ["I"] * 64

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():
        pass

    else:
        pass

    return "".join(map)

def getBishopMap(board, row, col):
    map = ["I"] * 64

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():
        pass

    else:
        pass

    return "".join(map)

def getKingMap(board, row, col):
    map = ["I"] * 64

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():
        pass

    else:
        pass

    return "".join(map)

def getQueenMap(board, row, col):
    map = ["I"] * 64

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():
        pass

    else:
        pass

    return "".join(map)
