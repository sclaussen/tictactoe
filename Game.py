import re

from Board import *
from Player import *
from Constants import *

class Game:
    status = None
    board = None
    winner = None

    def __init__(self, board):
        self.status = Status.PLAYING
        self.winner = None
        self.starter = None
        self.board = board

    def isTie(self):
        if self.board.isTie():
            self.status = Status.TIE
            return True
        return False

    def isWinner(self, player):
        if self.board.isWinner(player.symbol):
            self.status = Status.WINNER
            return True
        return False

    def __str__(self):
        s = "\n"
        s += "Game summary:\n"
        if self.status == Status.PLAYING:
            s += "  In progress\n"
            return s
        if self.status == Status.TIE:
            s += "  Cat won the game!\n"
            return s
        if self.status == Status.WINNER:
            s += "  " + self.winner.name + " won the game!\n"
            return s
