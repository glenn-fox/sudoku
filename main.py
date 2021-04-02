from solve import solve, draw_board


def get_board():
    board = []
    for i in range(9):
        line = input("Enter line " + str(i + 1) + ": ")
        line = line.split(" ")
        for j in range(len(line)):
            line[j] = int(line[j])
        board.append(line)
    return board


test_board = [[0, 5, 0, 0, 0, 6, 0, 0, 0],
              [8, 0, 6, 0, 9, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 5, 0, 0, 7],
              [0, 1, 0, 0, 0, 3, 4, 0, 0],
              [0, 3, 0, 7, 0, 4, 0, 9, 0],
              [0, 0, 4, 8, 0, 0, 0, 3, 0],
              [1, 0, 0, 9, 0, 0, 5, 0, 0],
              [0, 0, 0, 0, 4, 0, 2, 0, 8],
              [0, 0, 0, 1, 0, 0, 0, 6, 0]]

evil_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 3, 0, 8, 5],
              [0, 0, 1, 0, 2, 0, 0, 0, 0],
              [0, 0, 0, 5, 0, 7, 0, 0, 0],
              [0, 0, 4, 0, 0, 0, 1, 0, 0],
              [0, 9, 0, 0, 0, 0, 0, 0, 0],
              [5, 0, 0, 0, 0, 0, 0, 7, 3],
              [0, 0, 2, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 4, 0, 0, 0, 9]]

hard_board = [[0, 1, 8, 0, 0, 0, 0, 0, 2],
              [5, 0, 0, 0, 0, 0, 9, 0, 0],
              [0, 0, 0, 6, 0, 0, 0, 5, 4],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [3, 0, 9, 0, 0, 0, 2, 0, 6],
              [2, 0, 6, 7, 8, 0, 0, 0, 0],
              [0, 0, 3, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 7, 9, 1, 0, 0],
              [4, 5, 0, 0, 2, 0, 0, 0, 0]]


# test = get_board()

# draw_board(test)

solved, _ = solve(test_board, False)
draw_board(solved)


# begin_time = datetime.now()
# solved, _ = solve(hard_board, False)
# draw_board(solved)
# end_time = datetime.now()
# print(f"Solved in {end_time-begin_time}")
