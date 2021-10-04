from board import Board



def solve(board):
  print("Solving...")

  print("2 is valid at 6,7: ", board.validate_placement(6, 7, 2))


# procedure backtrack(c) is
#   if reject(P, c) then return
#   if accept(P, c) then output(P, c)
#   s ← first(P, c)
#   while s ≠ NULL do
#       backtrack(s)
#       s ← next(P, s)

def backtrack(board):
  pass
