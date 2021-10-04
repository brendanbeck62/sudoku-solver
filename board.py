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

  def validate_placement(self, col, row, val):
    return self.__verify_row(row, val) and self.__verify_col(col, val) and self.__verify_square(col, row, val)

  def __verify_row(self, row, val):
    return val not in self.board[row]

  def __verify_col(self, col, val):
    # little list comprehension to get the col
    return val not in [x[col] for x in self.board]

  def __verify_square(self, col, row, val):
    for i in range(self.NUM_ROWS // 3):
      for j in range(self.NUM_COLS // 3):
        # enumerate the square a cell is located, horizontal first
        if val == self.board[((row // 3) * self.NUM_ROWS // 3) + i][((col // 3) * self.NUM_COLS // 3) + j]:
          return False
    return True




  def get_cell(self, row, col):
    return self.board[row][col]
  def set_cell(self, row, col, val):
    self.board[row][col] = val;