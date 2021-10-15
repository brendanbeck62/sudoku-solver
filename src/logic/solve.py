from board.board import Board

def solve(board):
  print("Solving.....")
  return backtrack(board, 0, 0)


# procedure backtrack(c) is
#   if reject(P, c) then return
#   if accept(P, c) then output(P, c)
#   s ← first(P, c)
#   while s ≠ NULL do
#       backtrack(s)
#       s ← next(P, s)

def backtrack(board, curr_row, curr_col):

  if curr_col == (board.NUM_COLS):
    curr_row += 1
    curr_col = 0

  # base case
  # the logic here is a little goofy, since +=1 the row before checking,
  # this is the only time curr_row will equal the row size (last row is row size -1)
  if (curr_row == board.NUM_ROWS):
    return True

  # check if the cell is already filled, move on if so
  if board.get_cell(curr_row, curr_col) > 0:
    return backtrack(board, curr_row, curr_col + 1)

  # try each number in the current cell, and if one one works add it to the board, and move to next cell
  for num in range(1, 10, 1):
    if (board.validate_placement(curr_row, curr_col, num)):

      # set it on the board
      board.set_cell(curr_row, curr_col, num)

      if backtrack(board, curr_row, curr_col + 1):
        return True

      # if no values work in this cell, set it back to empty
      board.set_cell(curr_row, curr_col, 0)

  # if the cell has no valid number, return false
  return False