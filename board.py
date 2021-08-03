import random

NUM_COLS = 9
NUM_ROWS = 9
class Board:
  def __init__(self, board=None):
    if board is not None:
      self.board = board
    else:
      self.board = random_board(3)
  
  def __str__(self):
    return '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in
self.board])
  def random_board(self,numStarters=1):
    self.board = [[0 for i in range(NUM_COLS)] for j in range(NUM_ROWS)]
    self.board[0][0] = random.randint(1,9)
    self.board[3][0] = random.randint(1,9)
    
