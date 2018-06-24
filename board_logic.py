import numpy as np
from interface import Interface
# import numpy and set "np" as its variable name

class BoardApp:
    def __init__(self,interface):
        self.raws = 6
        self.columns = 7
        self.board = np.zeros((self.raws,self.columns))        # initialise an array equal to board size
        self.turn = 0                       # set turn to zero
        self.inter = interface

    def run(self):
        while True:
            if self.turn == 0:                          # Get input from user and drop a piece
                col = self.inter.play(0)
                if self.valid_col(col):
                    raw = self.next_row(col)
                    self.drop_piece(raw,col,1)
                    self.inter.draw_piece(col, raw, 1)
                    if self.win(piece=1):               # check if there is a win
                        self.inter.win(0)
                        print("player 1 win")
                        break

            else:
                col = self.inter.play(1)
                if self.valid_col(col):
                    raw = self.next_row(col)
                    self.drop_piece(raw,col,2)
                    self.inter.draw_piece(col,raw,2)
                    if self.win(piece=2):
                        self.inter.win(1)
                        print("palyer 2 win")
                        break

            self.printboard()
            self.change_player()

    def change_player(self):
        self.turn += 1                  # increment by 1
        self.turn = self.turn % 2       # set value to remainder of the division by 2

    def valid_col(self,col):
        return self.board [self.raws-1][col] == 0     # check if the last row in column is empty(valid location)

    def next_row(self,col):
        for r in range(self.raws):          # check for the first empty raw of the
            if self.board [r][col] == 0:    # selected columns and return the index of the row
                return r

    def drop_piece(self,raw,col,piece):
        self.board[raw][col] = piece        # drop a piece in the empty slot (set element with this address to 1 or 2

    def win(self,piece):
        # check for horizontal wins
        for col in range(self.columns - 3):
            for raw in range(self.raws):
                if self.board[raw][col] == self.board[raw][col + 1] == self.board[raw][col + 2] == self.board [raw][col + 3] == piece:
                    return True
        # Check for vertical wins
        for col in range(self.columns):
            for raw in range(self.raws - 3):
                if self.board[raw][col] == self.board[raw + 1][col] == self.board[raw+2][col] == self.board[raw+3][col] == piece:
                    return True
        # check for diagonal 1(positive)
        for col in range(self.columns - 3):
            for raw in range(self.raws - 3):
                if self.board[raw][col] == self.board[raw + 1][col+1] == self.board[raw+2][col+2] == self.board[raw+3][col+3] == piece:
                    return True
        # check for diagonal 2(negative)
        for col in range(self.columns - 3):
            for raw in range(3,self.raws):
                if self.board[raw][col] == self.board[raw - 1][col+1] == self.board[raw-2][col+2] == self.board[raw-3][col+3] == piece:
                    return True

    def printboard(self):
        print(np.flip(self.board, 0))

inter = Interface()
app = BoardApp(inter)
app.run()