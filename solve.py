from operator import itemgetter


def draw_board(board):
    print("\n")
    for i, line in enumerate(board):
        for j, item in enumerate(line):
            print(item, end=" ")
            if j in [2, 5]:
                print("|", end=" ")
        print("")
        if i in [2, 5]:
            print("------+-------+------")
    print("")


def possible(board, pos, num):
    """Function determines if a number is a possible move for a position on a board.

    Parameters:
    board (array): array that holds the board information
    pos (tuple): position on the board (y, x)
    num (int): number to be tested

    Returns:
    bool:Returning value
    """
    # pos is (y, x)
    # check row
    y = pos[0]
    x = pos[1]
    for item in board[y]:
        if item == num:
            return False

    # check column
    for row in board:
        if row[x] == num:
            return False

    # check square
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3
    for i in list(range(box_y, box_y+3)):
        for j in list(range(box_x, box_x+3)):
            if board[i][j] == num:
                return False

    return True


def is_valid(board):
    # check horizontal lines
    for line in board:
        numbers = []
        for number in line:
            # add numbers in line to list
            # if there are more than one of any number except 0 then the line is not valid
            if number in numbers and number != 0:
                return False
            elif number not in numbers:
                numbers.append(number)

    # check vertical lines
    indexes = list(range(0, 9))
    for index in indexes:
        numbers = []
        for line in board:
            number = line[index]
            if number in numbers and number != 0:
                return False
            elif number not in numbers:
                numbers.append(number)
    # Check squares
    start_i = 0
    start_j = 0
    while start_j <= 6:
        while start_i <= 6:
            numbers = []
            for i in list(range(start_i, start_i + 3)):
                for j in list(range(start_j, start_j + 3)):
                    number = board[i][j]
                    if number in numbers and number != 0:
                        return False
                    elif number not in numbers:
                        numbers.append(number)
            start_i += 3
        start_j += 3
        start_i = 0

    return True


def completed(board):
    if is_valid(board):
        for line in board:
            if 0 not in line:
                continue
            else:
                return False
        return True
    return False


def solve(board):
    for i in list(range(0, 9)):
        for j in list(range(0,9)):
            if board[i][j] == 0:
                for testNum in list(range(1, 10)):
                    if possible(board, (i, j), testNum):
                        board[i][j] = testNum
                        board = solve(board)
                        if completed(board):
                            return board
                    if testNum == 9:
                        board[i][j] = 0
                        return board
    return board

                            
def solve_fast(board, complete):
    global move_list
    if not complete:
        # board, move_list = get_moves(board)
        for move in move_list:
            pos_y = move[0][0]
            pos_x = move[0][1]
            guesses = move[1]
            if board[pos_y][pos_x] == 0:
                for number in guesses:
                    if not complete:
                        if possible(board, (pos_y, pos_x), number):
                            board[pos_y][pos_x] = number
                            if completed(board):
                                return board, True
                            else:
                                board, complete = solve_fast(board, False)
                    if complete:
                        return board, True
                if not complete:
                    board[pos_y][pos_x] = 0
                    return board, False


def get_moves(board): 
    output = []
    for i in list(range(0, 9)):
        for j in list(range(0, 9)):
            number = board[i][j]
            if number == 0:
                coords = (i, j)
                possible_nums = []
                for test_num in list(range(1, 10)):
                    board[i][j] = test_num
                    if is_valid(board):
                        possible_nums.append(test_num)
                board[i][j] = 0
                output.append([coords, possible_nums])
    output.sort(key=lambda x: len(x[1]))
    k = 0
    removed = False
    while k < len(output):
        num_list = output[k][1]
        if len(num_list) == 1:
            coords = output[k][0]
            board[coords[0]][coords[1]] = num_list[0]
            output.pop(0)
            removed = True
            continue
        else:
            break
    if removed:
        board, output = get_moves(board)

    return board, output
