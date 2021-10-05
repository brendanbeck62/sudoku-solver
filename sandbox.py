# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print([x[1] for x in l])


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

print("=============== root ===============")
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in starting_board_easy]))

print(any(0 in x for x in starting_board_easy))


col = 6
row = 7

sublist = [x[:3] for x in starting_board_easy]



print("=============== sublist ===============")
# print(sublist)
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in sublist]))


# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# [[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

print("=============== DX DY ===============")
dx = [3, 4, 5, 9]
dy = [5, 3, 2, 1]
output = [[dx_n * dy_n for dy_n in dy] for dx_n in dx]

print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in output]))