import random
import re

from Match import *
from Game import *
from Board import *
from Player import *
from util import *

# Create players, the match, and randomize the player who will start
player1 = Player(input("What is the name of player 1? "))
player2 = Player(input("What is the name of player 2? "))
match = Match(player1, player2)
match.setStarter(random.choice(match.players))

# Play games until one player has 3 wins
while match.isWinner() == False:

    # Init board, game, and render the board
    board = Board()
    game = Game(board)
    print(match)
    print(board)

    # Game loop - continue until there's a tie or someone wins
    while True:

        # Prompt for the cell to play the symbol in, and put the
        # symbol in the cell, and then re-render the board
        cellNumber = getIntInput("Select a cell for your move " + match.currentPlayer.name + " (" + match.currentPlayer.symbol + ")", board.getValidMoves())
        board.play(cellNumber, match.currentPlayer.symbol)
        print(board)

        # Determine if the move resulted in a player win, if so,
        # break the game loop
        if game.isWinner(match.currentPlayer):
            match.currentPlayer.wins += 1
            game.winner = match.currentPlayer
            match.setStarter(match.otherPlayer)
            break

        # Determine if the game was a tie, or would be a tie, and if
        # so, break the game loop
        if game.isTie():
            match.ties += 1
            match.setStarter(match.currentPlayer)
            break

        # If no winner/tie, move to the next player
        match.nextPlayer()

    # Print the end of game summary
    print(game)

# Print the end of match summary
print(match)
