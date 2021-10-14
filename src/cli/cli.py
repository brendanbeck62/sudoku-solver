import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(parent)


from src.board import Board
from logic import solve



starting_board_easy = [
[0,0,5,3,6,0,4,0,0],
[9,6,2,0,0,4,0,7,0],
[3,0,4,0,2,9,0,6,0],
[8,2,0,9,4,0,0,1,3],
[0,4,9,0,3,0,0,5,7],
[0,0,0,2,0,0,9,8,0],
[4,0,6,0,0,1,0,0,2],
[0,0,0,6,9,3,0,0,5],
[0,0,3,0,8,0,0,0,0]]

solved_board_easy = [
[1,8,5,3,6,7,4,2,9],
[9,6,2,5,1,4,3,7,8],
[3,7,4,8,2,9,5,6,1],
[8,2,7,9,4,5,6,1,3],
[6,4,9,1,3,8,2,5,7],
[5,3,1,2,7,6,9,8,4],
[4,9,6,7,5,1,8,3,2],
[2,1,8,6,9,3,7,4,5],
[7,5,3,4,8,2,1,9,6]]

def play():
  # Display init board
  the_board = Board(starting_board_easy)
  display_board(the_board, "STARTING BOARD")

  # solve
  if (solve(the_board)):
    # Display finished board
    display_board(the_board, "SOLVED BOARD")
  else:
    print("Unsolvable")


def display_board(the_board, title):
    print("="*40)
    print(title)
    print("="*40)
    print(the_board)

if __name__ == "__main__":
  play()