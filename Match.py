from Player import *
from constants import *

class Match:
    status = None
    players = []
    currentPlayer = None
    otherPlayer = None
    ties = 0
    winner = None

    def __init__(self, player1, player2):
        self.status = Status.PLAYING
        self.players.append(player1)
        self.players.append(player2)

    def setStarter(self, player):
        self.currentPlayer = player
        if self.players[0].name == player.name:
            self.players[0].symbol = "X"
            self.players[1].symbol = "O"
            self.otherPlayer = self.players[1]
        else:
            self.players[0].symbol = "O"
            self.players[1].symbol = "X"
            self.otherPlayer = self.players[0]

    def nextPlayer(self):
        if self.currentPlayer == self.players[0]:
            self.currentPlayer = self.players[1]
            self.otherPlayer = self.players[0]
        else:
            self.currentPlayer = self.players[0]
            self.otherPlayer = self.players[1]

    def isWinner(self):
        if self.players[0].wins == 3:
            self.status = Status.WINNER
            self.winner = self.players[0]
            return True
        if self.players[1].wins == 3:
            self.status = Status.WINNER
            self.winner = self.players[1]
            return True
        return False

    def __str__(self):
        s = "\n"
        s += "Match summary:\n"
        s += "  " + self.players[0].name + ": " + str(self.players[0].wins) + "\n"
        s += "  " + self.players[1].name + ": " + str(self.players[1].wins) + "\n"
        s += "  Cat: " + str(self.ties) + "\n"
        if self.status == Status.WINNER:
            s += "\n"
            s += "  " + self.winner.name + " won the match!\n"
        return s
