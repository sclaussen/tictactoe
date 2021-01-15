import re

class Board:
    cells = None

    def __init__(self):
        self.cells = [ [ '1', '2', '3' ], [ '4', '5', '6' ], [ '7', '8', '9' ] ]

    def play(self, cellNumber, symbol):
        if cellNumber == 1:
            self.cells[0][0] = symbol
        if cellNumber == 2:
            self.cells[0][1] = symbol
        if cellNumber == 3:
            self.cells[0][2] = symbol
        if cellNumber == 4:
            self.cells[1][0] = symbol
        if cellNumber == 5:
            self.cells[1][1] = symbol
        if cellNumber == 6:
            self.cells[1][2] = symbol
        if cellNumber == 7:
            self.cells[2][0] = symbol
        if cellNumber == 8:
            self.cells[2][1] = symbol
        if cellNumber == 9:
            self.cells[2][2] = symbol

    def isTie(self):
        for row in range(3):
            for column in range(3):
                if re.search(r"[0-9]", self.cells[row][column]):
                    return False
        return True

    def isWinner(self, symbol):
        # Check rows
        if self.isSymbol(1, symbol) and self.isSymbol(2, symbol) and self.isSymbol(3, symbol):
            return True
        if self.isSymbol(4, symbol) and self.isSymbol(5, symbol) and self.isSymbol(6, symbol):
            return True
        if self.isSymbol(7, symbol) and self.isSymbol(8, symbol) and self.isSymbol(9, symbol):
            return True

        # Check columns
        if self.isSymbol(1, symbol) and self.isSymbol(4, symbol) and self.isSymbol(7, symbol):
            return True
        if self.isSymbol(2, symbol) and self.isSymbol(5, symbol) and self.isSymbol(8, symbol):
            return True
        if self.isSymbol(3, symbol) and self.isSymbol(6, symbol) and self.isSymbol(9, symbol):
            return True

        # Check diagonals
        if self.isSymbol(1, symbol) and self.isSymbol(5, symbol) and self.isSymbol(9, symbol):
            return True
        if self.isSymbol(3, symbol) and self.isSymbol(5, symbol) and self.isSymbol(7, symbol):
            return True

        return False

    def isSymbol(self, cellNumber, symbol):
        if cellNumber == 1:
            return self.cells[0][0] == symbol
        if cellNumber == 2:
            return self.cells[0][1] == symbol
        if cellNumber == 3:
            return self.cells[0][2] == symbol
        if cellNumber == 4:
            return self.cells[1][0] == symbol
        if cellNumber == 5:
            return self.cells[1][1] == symbol
        if cellNumber == 6:
            return self.cells[1][2] == symbol
        if cellNumber == 7:
            return self.cells[2][0] == symbol
        if cellNumber == 8:
            return self.cells[2][1] == symbol
        if cellNumber == 9:
            return self.cells[2][2] == symbol

    def getValidMoves(self):
        moves = []
        for row in range(3):
            for column in range(3):
                if re.search(r"[0-9]", self.cells[row][column]):
                    moves.append(self.cells[row][column])
        return moves

    def __str__(self):
        s = "\n"
        for row in range(3):
            for column in range(3):
                s += self.cells[row][column]
                if column == 0 or column == 1:
                    s += " | "
            if row == 0 or row == 1:
                s += "\n----------"
            s += "\n"
        return s
