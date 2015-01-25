"""This module stores the functions and classes needed for a Tic-Tac-Toe game,
including the grid class that stores the current game state, and the functions
that are used to test its functionality. The Tic-Tac-Toe game is played with
two players ("X" and "O"), who take turns marking a 3x3 board with their symbol.
The game ends when one player gets three of their symbol in a straight line, or
the grid is completely filled with symbols.
"""

class TicTacToe:
    """This class stores the internal state of the Tic Tac Toe game, along
    with the operations that are needed to play the game.
    """

    def __init__(self):
        """Initialize the contents of a new Tic Tac Toe game grid.
        """
        self.clear()

    def make_move(self, x, y):
        """Make a move in the position specified by the given X and Y
        coordinates. Switch the player after completing this move.
        """

        # Exception possibilities.
        if x not in [0,1,2]:
            raise InvalidMoveException(x,y)
        if y not in [0,1,2]:
            raise InvalidMoveException(x,y)
        if self.grid.get((x, y)):
            raise InvalidMoveException(x,y)

        # Makes sure what player's turn it is.
        self.grid[(x, y)] = self.current_player
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
            


    def clear(self):
        """Clear the grid for a new game.
        """
        self.grid = {}
        self.current_player = 'X'

    def winner(self):
        """Return the symbol of the player who has won the game
        (either 'X' or 'O'), or None if there's no winner yet.
        A winner is defined as a player with three of their symbols
        in a straight line in the grid.
        """
        result = None
        for x in range(0, 3):
            if self.grid.get((x, 0)) == self.grid.get((x, 1)) == self.grid.get((x, 2)):
                result = self.grid.get((x, 0)) or result
        for y in range(0, 3):
            if self.grid.get((0, y)) == self.grid.get((1, y)) == self.grid.get((2, y)):
                result = self.grid.get((y, 0)) or result
        return result

    def play(self):
        """Start a game with the user, printing out the game grid after
        each turn, until the grid is full or one player has three in a row.
        The game automatically alternates player moves between "X" and "O".
        """
        self.clear()
        print ('Welcome to the Tic Tac Toe game!')
        symbol = None
        while len(self.grid) < 9 and symbol is None:
            print ("It's " + str(self.current_player) + "'s turn.")
            x = input('What column would you like to use? ')
            y = input('What row would you like to use? ')

            # Try to see if exception is in the input.
            try:
                self.make_move(int(x), int(y))
            except InvalidMoveException:
                print (InvalidMoveException(x,y))
            print (self)
            symbol = self.winner()
        if symbol:
            print (symbol + " is the winner!")
        print ('Thanks for playing!')

    def __str__(self):
        """Return a sting representation of this Tic Tac Toe grid.
        This will be a 3x3 grid of characters, either "X", "O" or " "
        (a space character if the grid position is empty). Each row
        is separated by a newline character in the string that is
        returned to the calling program.
        """
        result = ""
        for y in range(0, 3):
            for x in range(0, 3):
                # look up the tuple that contains the current X and Y
                # coordinates, and if a symbol exists at that location,
                # add that symbol to the final output string.
                if self.grid.get((x, y)):
                    result += self.grid.get((x, y))
                else:
                    result += ' '
            # add a new line at the end of every row.
            result += '\n'
        return result


class InvalidMoveException(Exception):
    """ Invalid move class.
    """

    def __init__(self, x, y):
        """ Initialize the contents of the InvalidMoveException.
        """

        self.XXX = x
        self.YYY = y

    def __str__(self):
        """ String for InvalidMoveException
        """
        return 'The position (' + str(self.XXX) + ", " + str(self.YYY) + ") is not a valid move position."


# If this module is the main one being executed, then create
# a TicTacToe object and start the game.
if __name__ == "__main__":
    g = TicTacToe()
    g.play()

