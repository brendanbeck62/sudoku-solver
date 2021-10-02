from board import Board



def solve(board):
  print("Solving")

  print("1 is valid at 0,0: ", board.validate_placement(0, 0, 1))


# procedure backtrack(c) is
#   if reject(P, c) then return
#   if accept(P, c) then output(P, c)
#   s ← first(P, c)
#   while s ≠ NULL do
#       backtrack(s)
#       s ← next(P, s)

def backtrack(board):
  pass
