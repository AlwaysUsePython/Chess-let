import movement

class GameState:

    def __init__(self, board, move = "white", prev = None, next = None):
        self.board = board
        self.prev = prev
        self.next = next
        self.move = move

    def setNext(self, next):
        self.next = next

    def setPrev(self, prev):
        self.prev = prev

    def getHead(self):
        if self.prev == None:
            return self
        else:
            return self.prev.getHead()

    def getTail(self):
        if self.next == None:
            return self
        else:
            return self.next.getTail()

    def toString(self):
        return (self.board + " " + self.move)

    def getNextMove(self):
        if self.move == "white":
            return "black"
        return "white"

class MoveDatabase:

    def __init__(self, fileName):
        file = open(fileName, "r")

        self.moves = {}

        currentMove = file.readline()

        print("STARTING", fileName)

        lineCounter = 0

        while currentMove != "":

            currentGS = GameState("rnbqkbnrpppppppp________________________________PPPPPPPPRNBQKBNR")

            while currentMove != "end\n" and currentMove != "end":

                loc1 = int(currentMove[0:currentMove.index(" ")])
                loc2 = int(currentMove[currentMove.index(" ")+1:])

                newBoard = movement.makeMove(currentGS.board, loc1, loc2)

                newGS = GameState(newBoard, currentGS.getNextMove(), currentGS)

                try:
                    if [loc1, loc2] not in self.moves[currentGS.toString()]:
                        self.moves[currentGS.toString()].append([loc1, loc2])
                except:
                    self.moves[currentGS.toString()] = [[loc1, loc2]]

                currentGS = newGS
                currentMove = file.readline()

            lineCounter += 1
            print("LOADED LINE #"+str(lineCounter))
            currentMove = file.readline()

        print("LOADED", fileName)

        file.close()

    def getMoves(self, gameState):
        return self.moves[gameState.toString()]