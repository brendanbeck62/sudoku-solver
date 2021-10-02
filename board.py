import random

class Board:
  NUM_COLS = 9
  NUM_ROWS = 9

  def __init__(self, board=None):
    if board is not None:
      self.board = board
    else:
      self.random_board(3)

  def __str__(self):
    # TODO: add lines to the board
    return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.board])

  def random_board(self,numStarters=1):
    # TODO: make this actually functional
    # TODO: Decide if random board should actually be solvable
    self.board = [[0 for i in range(self.NUM_COLS)] for j in range(self.NUM_ROWS)]
    self.board[0][0] = random.randint(1,9)
    self.board[3][0] = random.randint(1,9)

  def validate_placement(self, row, col, val):
    return self.__verify_row(row, val) and self.__verify_col(col, val) and self.__verify_square(row, col, val)

  def __verify_row(self, row, val):
    return val not in self.board[row]

  def __verify_col(self, col, val):
    return val not in self.board[col]

  # TODO: Verify square
  def __verify_square(self, row, col, val):
    return 0




  def get_cell(self, row, col):
    return self.board[row][col]
  def set_cell(self, row, col, val):
    self.board[row][col] = val;