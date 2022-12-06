# See graphics.py for board notation

## MAKES MOVE WITH INPUT OF BOARD AND SINGLE COORDINATE LOCATIONS (IN THE STRING) ##
# NOTE: CASTLING NOT YET ADDED #
def makeMove(board, loc1, loc2):
    arrBoard = []
    for piece in board:
        arrBoard.append(piece)

    arrBoard[loc2] = board[loc1]
    arrBoard[loc1] = "_"

    # White short castle
    if board[loc1] == "K" and loc2 == 62:
        arrBoard[61] = "R"
        arrBoard[63] = "_"

    # White long castle
    if board[loc1] == "K" and loc2 == 58:
        arrBoard[59] = "R"
        arrBoard[56] = "_"

    # Black short castle
    if board[loc1] == "k" and loc2 == 6:
        arrBoard[5] = "r"
        arrBoard[7] = "_"

    # Black long castle
    if board[loc1] == "k" and loc2 == 2:
        arrBoard[3] = "r"
        arrBoard[0] = "_"

    return "".join(arrBoard)

## RETURNS BOOLEAN OF WHETHER OR NOT THE KING IS IN CHECK ##
def isInCheck(color, board):

    kingSquare = getKingSquare(color, board)

    for i in range(len(board)):
        if color == "white":
            if board[i] in "rnbkqp":
                map = getLegalMovesIgnoreCheck(board, i//8, i%8)
                if map[kingSquare] == "T":
                    return True
        else:
            if board[i] in "RNBKQP":
                map = getLegalMovesIgnoreCheck(board, i//8, i%8)
                if map[kingSquare] == "T":
                    return True

    return False

## RETURNS THE SQUARE OF THAT KING (SINGLE COORDINATE) ##
def getKingSquare(color, board):
    for i in range(len(board)):
        if color == "white":
            if board[i] == "K":
                return i

        else:
            if board[i] == "k":
                return i

## INPUT OF BOARD + COORDINATES, OUTPUT OF STRING WITH MAP OF LEGAL MOVES ##
# Map Format: "L" is legal, "I" is illegal
# Note: Passes calculation off to helper methods for each piece
def getLegalMoves(board, row, col):

    if board[row*8+col] in "RNBKQP":
        color = "white"
    else:
        color = "black"

    initialMap = getLegalMovesIgnoreCheck(board, row, col)

    testMap = []
    for item in initialMap:
        testMap.append(item)

    for m in range(len(testMap)):
        if initialMap[m] != "I":
            testBoard = makeMove(board, row*8+col, m)
            if isInCheck(color, testBoard):
                testMap[m] = "I"

            if board[row*8+col] == "K":
                # white short castle
                if col == 4 and m == 62:
                    if isInCheck("white", board):
                        testMap[m] = "I"
                    else:
                        testBoard2 = makeMove(board, row*8+col, 61)
                        if isInCheck("white", testBoard2):
                            testMap[m] = "I"

            if board[row*8+col] == "K":
                # white long castle
                if col == 4 and m == 58:
                    if isInCheck("white", board):
                        testMap[m] = "I"
                    else:
                        testBoard2 = makeMove(board, row*8+col, 59)
                        if isInCheck("white", testBoard2):
                            testMap[m] = "I"

            if board[row*8+col] == "k":
                # black short castle
                if col == 4 and m == 6:
                    if isInCheck("black", board):
                        testMap[m] = "I"
                    else:
                        testBoard2 = makeMove(board, row*8+col, 5)
                        if isInCheck("black", testBoard2):
                            testMap[m] = "I"

            if board[row*8+col] == "k":
                # black long castle
                if col == 4 and m == 2:
                    if isInCheck("black", board):
                        testMap[m] = "I"
                    else:
                        testBoard2 = makeMove(board, row*8+col, 3)
                        if isInCheck("black", testBoard2):
                            testMap[m] = "I"


    return "".join(testMap)

def getLegalMovesIgnoreCheck(board, row, col):

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

    possibleSquares = [(row-2)*8 + col + 1, (row-2)*8 + col - 1, (row+2)*8 + col + 1, (row+2)*8 + col - 1, (row+1)*8+col+2, (row+1)*8+col-2, (row-1)*8+col+2, (row-1)*8+col-2]

    updatedPossibleSquares = []
    for square in possibleSquares:

        if square >= 0 and square <= 63:
            if abs(square % 8 - col) <= 2:
                updatedPossibleSquares.append(square)

    possibleSquares = updatedPossibleSquares


    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():

        for square in possibleSquares:
            if board[square] in "rnbqkp_":
                if board[square] == "_":
                    map[square] = "L"
                else:
                    map[square] = "T"

    else:

        for square in possibleSquares:
            if board[square] in "RNBQKP_":
                if board[square] == "_":
                    map[square] = "L"
                else:
                    map[square] = "T"

    return "".join(map)

def getBishopMap(board, row, col):
    map = ["I"] * 64

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():
        # NE
        blocked = False
        counter = 1
        while not blocked:
            if (row - counter + 1) > 0 and (col+counter-1) < 7 and board[(row - counter) * 8 + col+counter] in "rnbqkp_":
                if board[(row - counter) * 8 + col+counter] == "_":
                    map[(row - counter) * 8 + col+counter] = "L"
                else:
                    map[(row - counter) * 8 + col+counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # NW
        blocked = False
        counter = 1
        while not blocked:
            if (row - counter + 1) > 0 and (col - counter + 1) > 0 and board[
                (row - counter) * 8 + col - counter] in "rnbqkp_":
                if board[(row - counter) * 8 + col - counter] == "_":
                    map[(row - counter) * 8 + col - counter] = "L"
                else:
                    map[(row - counter) * 8 + col - counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # SE
        blocked = False
        counter = 1
        while not blocked:
            if (row + counter - 1) < 7 and (col + counter - 1) < 7 and board[(row + counter) * 8 + col + counter] in "rnbqkp_":
                if board[(row + counter) * 8 + col + counter] == "_":
                    map[(row + counter) * 8 + col + counter] = "L"
                else:
                    map[(row + counter) * 8 + col + counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # SW
        blocked = False
        counter = 1
        while not blocked:
            if (row + counter - 1) < 7 and (col - counter + 1) > 0 and board[(row + counter) * 8 + col - counter] in "rnbqkp_":
                if board[(row + counter) * 8 + col - counter] == "_":
                    map[(row + counter) * 8 + col - counter] = "L"
                else:
                    map[(row + counter) * 8 + col - counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True


    else:
        # NE
        blocked = False
        counter = 1
        while not blocked:
            if (row - counter + 1) > 0 and (col + counter - 1) < 7 and board[
                (row - counter) * 8 + col + counter] in "RNBQKP_":
                if board[(row - counter) * 8 + col + counter] == "_":
                    map[(row - counter) * 8 + col + counter] = "L"
                else:
                    map[(row - counter) * 8 + col + counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # NW
        blocked = False
        counter = 1
        while not blocked:
            if (row - counter + 1) > 0 and (col - counter + 1) > 0 and board[
                (row - counter) * 8 + col - counter] in "RNBQKP_":
                if board[(row - counter) * 8 + col - counter] == "_":
                    map[(row - counter) * 8 + col - counter] = "L"
                else:
                    map[(row - counter) * 8 + col - counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # SE
        blocked = False
        counter = 1
        while not blocked:
            if (row + counter - 1) < 7 and (col + counter - 1) < 7 and board[
                (row + counter) * 8 + col + counter] in "RNBQKP_":
                if board[(row + counter) * 8 + col + counter] == "_":
                    map[(row + counter) * 8 + col + counter] = "L"
                else:
                    map[(row + counter) * 8 + col + counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

        # SW
        blocked = False
        counter = 1
        while not blocked:
            if (row + counter - 1) < 7 and (col - counter + 1) > 0 and board[
                (row + counter) * 8 + col - counter] in "RNBQKP_":
                if board[(row + counter) * 8 + col - counter] == "_":
                    map[(row + counter) * 8 + col - counter] = "L"
                else:
                    map[(row + counter) * 8 + col - counter] = "T"
                    blocked = True

                counter += 1
            else:
                blocked = True

    return "".join(map)

def getKingMap(board, row, col):
    map = ["I"] * 64

    possibleSquares = [row*8+col+1, row*8+col-1, (row-1)*8+col, (row+1)*8+col, (row+1)*8+col+1, (row-1)*8+col-1, (row-1)*8+col+1, (row+1)*8+col-1]

    updatedPossibleSquares = []
    for square in possibleSquares:

        if square >= 0 and square <= 63:
            if abs(square % 8 - col) <= 1:
                updatedPossibleSquares.append(square)

    possibleSquares = updatedPossibleSquares

    # check the color of the piece
    if board[row * 8 + col] != board[row * 8 + col].lower():

        for square in possibleSquares:
            if board[square] in "rnbqkp_":
                if board[square] == "_":
                    map[square] = "L"
                else:
                    map[square] = "T"

        if row == 7 and col == 4 and board[61] == "_" and board[62] == "_" and board[63] == "R":
            map[62] = "L"

        if row == 7 and col == 4 and board[59] == "_" and board[58] == "_" and board[57] == "_" and board[56] == "R":
            map[58] = "L"

    else:

        for square in possibleSquares:
            if board[square] in "RNBQKP_":
                if board[square] == "_":
                    map[square] = "L"
                else:
                    map[square] = "T"

        if row == 0 and col == 4 and board[5] == "_" and board[6] == "_" and board[7] == "r":
            map[6] = "L"

        if row == 0 and col == 4 and board[3] == "_" and board[2] == "_" and board[1] == "_" and board[0] == "r":
            map[2] = "L"

    return "".join(map)

def getQueenMap(board, row, col):
    rookMap = getRookMap(board, row, col)
    bishopMap = getBishopMap(board, row, col)

    queenMap = ""

    for i in range(64):
        if rookMap[i] != "I":
            queenMap += rookMap[i]
        elif bishopMap[i] != "I":
            queenMap += bishopMap[i]
        else:
            queenMap += "I"

    return queenMap