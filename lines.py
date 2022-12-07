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


