import random

sudoku_board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]


def generate_board(board):
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    empty_cell = find_empty(board)

    if not empty_cell:
        return True
    else:
        row, col = empty_cell
        random.shuffle(number_list)
    for value in number_list:
        if is_valid(board, value, (row, col)):
            board[row][col] = value
            if generate_board(board):
                return True
            board[row][col] = 0
    return False


def generate_puzzle(board,difficulty):
    if difficulty == 'easy':
        attempts = 25
    elif difficulty == 'medium':
        attempts = 35
    elif difficulty == 'hard':
        attempts = 45
    elif difficulty == 'hardcore':
        attempts = 64
    while attempts > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while board[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

        backup = board[row][col]
        board[row][col] = 0

        copy = []
        for r in range(0, 9):
            copy.append([])
            for c in range(0, 9):
                copy[r].append(board[r][c])

        if not solve(copy):
            board[row][col] = backup
        attempts -= 1



def find_empty(board):
    for y in range(len(board)):  # Going through each row
        for x in range(len(board[0])):  # Going through each column
            if board[y][x] == 0:  # Find empty cells
                return (y, x)  # Return row,column
    return None


def is_valid(board, num, pos):  # num = number being evaluated on empty cell, pos = (row,column)

    # Check each value along row at row y
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check each value along column at column x
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    left_to_right_diag = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
                          # Could also use range to generate diag coordinates for boards bigger than 9x9
                          (7, 7), (8, 8)]
    right_to_left_diag = [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2),
                          (7, 1), (8, 0)]

    # Check left to right diagonal
    if pos in left_to_right_diag:
        for i in range(len(left_to_right_diag)):
            if board[left_to_right_diag[i][0]][left_to_right_diag[i][1]] == num and pos != left_to_right_diag[i]:
                return False

    # Check right to left diagonal
    if pos in right_to_left_diag:
        for i in range(len(right_to_left_diag)):
            if board[right_to_left_diag[i][0]][right_to_left_diag[i][1]] == num and pos != right_to_left_diag[i]:
                return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):  # Find row
        for j in range(box_x * 3, box_x * 3 + 3):  # Find column
            if board[i][j] == num and (
                    i, j) != pos:  # Find numbers excluding current filled in position of testing number
                return False

    return True


def solve(board):
    empty_cell = find_empty(board)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for i in range(1, len(board) + 1):
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == len(board) - 1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


