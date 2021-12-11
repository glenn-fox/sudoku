from solve import solve, draw_board
from timeit import default_timer as timer


def import_board():
    file = open("boards.txt", "r")
    file_lines = file.readlines()
    i = 0
    while i < len(file_lines):
        file_lines[i] = file_lines[i].split(" ")
        i += 1
    print("\nSelect a board:")
    for j, line in enumerate(file_lines):
        print(str(j+1) + ": " + line[0])


def get_board():
    # this is a test
    board = []
    while len(board) != 9:
        line = input("Enter line " + str(len(board) + 1) + ": ")
        line = line.split(" ")
        length = len(line)
        # check for valid line
        new_line = []

        for j in len(line):
            number = int(line[j])
            if 0 <= number <= 9:
                new_line.append(number)
        if len(new_line) == 9:
            board.append(new_line)
        else:
            print("Invalid entry, please re-enter.")
    return board


def get_input():
    user_input = input("Choice: ")

    if user_input.upper() == 'Q':
        return "Q"
    else:
        try:
            user_input = int(user_input)
        except(IOError):
            print("Invalid input!")
            get_input()
    return user_input


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

easy_board = [[0, 3, 4, 6, 7, 8, 9, 0, 0],
              [6, 7, 2, 1, 9, 5, 3, 4, 8],
              [0, 9, 8, 3, 4, 2, 5, 6, 7],
              [8, 5, 9, 7, 6, 1, 4, 2, 3],
              [4, 2, 6, 8, 5, 3, 7, 9, 1],
              [7, 1, 3, 9, 2, 4, 8, 5, 6],
              [9, 6, 1, 5, 3, 7, 2, 8, 4],
              [2, 8, 7, 4, 1, 9, 6, 3, 5],
              [3, 4, 5, 2, 8, 6, 1, 7, 9]]

user_board = []

while True:
    print("\nMain Menu:")
    print("1: Input board")
    print("2: Use test board")
    print("3: Draw board")
    print("4: Solve board")
    user = get_input()
    
    if user == 1:
        user_board = get_board()
    elif user == 2:
        print("\nSelect board: ")
        print("1: Easy")
        print("2: Hard")
        print("3: Evil")
        user = get_input()
        if user == 1:
            user_board = easy_board.copy()
        elif user == 2:
            user_board = hard_board.copy()
        elif user == 3:
            user_board = evil_board.copy()
        else:
            user_board = test_board.copy()
    elif user == 3:
        draw_board(user_board)
    elif user == 4:
        start = timer()
        user_board = solve(user_board)
        end = timer()
        print("Solve took: " + str(end-start) + " seconds!")
    elif user == 5:
        import_board()
    else:
        break

