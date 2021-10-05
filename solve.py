from board import Board



def solve(board):
  print("Solving...")

  # print("2 is valid at 6,7: ", board.validate_placement(6, 7, 2))
  # print("board is solved: ", board.is_solved())
  print(backtrack(board, 0, 0))


# procedure backtrack(c) is
#   if reject(P, c) then return
#   if accept(P, c) then output(P, c)
#   s ← first(P, c)
#   while s ≠ NULL do
#       backtrack(s)
#       s ← next(P, s)

def backtrack(board, curr_col, curr_row):

  # base case
  # if the final cell has a valid number, return true
  if (curr_col == board.NUM_COLS and curr_row == board.NUM_ROWS - 1):
    print("SOLVED!!!")
    return True

  if curr_col == board.NUM_COLS:
    curr_row += 1
    curr_col = 0

  # check if the cell is already filled, move on if so
  if board.get_cell(curr_col, curr_row) > 0:
    return backtrack(board, curr_col + 1, curr_row)

  # try each number in the current cell, and if one one works add it to the board, and move to next cell
  for num in range(1, 9, 1):
    if (board.validate_placement(curr_col, curr_row, num)):

      # set it on the board
      board.set_cell(curr_col, curr_row, num)


      if backtrack(board, curr_col + 1, curr_row):
        return True

      # if no values work in this cell, set it back to empty
      board.set_cell(curr_col, curr_row, 0)

  # if the cell has no valid number, return false
  return False