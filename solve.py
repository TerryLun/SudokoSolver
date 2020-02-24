def pick_empty(board):
    """
    pick an empty cell in the board

    :param board: sudoku board
    :return: (x, y) for the empty cell, None if board is full
    """
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                return r, c
    else:
        return None


def validate_board(board):
    """
    validate board size, number range, duplicates in row/col/box

    :param board: sudoku board
    :return: bool T/F
    """
    # check size
    if len(board) != 9:
        return False
    for r in board:
        if len(r) != 9:
            return False
        for n in r:
            if not 0 <= n <= 9:
                return False
    # check row
    for r in board:
        if not validate_list(r):
            return False
    # check col
    for c in range(len(board[0])):
        col_list = []
        for r in range(len(board)):
            col_list.append(board[r][c])
        if not validate_list(col_list):
            return False
    # check box
    """
    box mid points
    1,1  1,4  1,7
    4,1  4,4  4,7  
    7,1  7,4  7,7
    """
    for center_x in range(1, 8, 3):
        for center_y in range(1, 8, 3):
            box_list = []
            for adj_x in range(-1, 2):
                for adj_y in range(-1, 2):
                    box_list.append(board[center_x + adj_x][center_y + adj_y])
            if not validate_list(box_list):
                return False
            box_list.clear()

    return True


def validate_number(board, num, pos):
    """
    Check if the specific number can insert into the specific position

    :param board: sudoku board
    :param num: number to insert to the board
    :param pos: position of the number, tuple: (x, y)
    :return: bool T/F
    """
    # check number
    if not 1 <= num <= 9:
        return False

    x, y = pos
    ls = []

    # row
    for n in board[x]:
        ls.append(n)
    ls.append(num)
    if not validate_list(ls):
        return False
    ls.clear()

    # col
    for r in board:
        ls.append(r[y])
    ls.append(num)
    if not validate_list(ls):
        return False
    ls.clear()

    # box
    box_x_start = (x // 3) * 3
    box_y_start = (y // 3) * 3
    for i in range(box_x_start, box_x_start + 3):
        for j in range(box_y_start, box_y_start + 3):
            ls.append(board[i][j])
    ls.append(num)
    if not validate_list(ls):
        return False

    return True


def validate_list(ls):
    """
    Check if the list has duplicate 1 - 9

    helper function for validate_board() and validate_number()
    :param ls: collection of numbers from a row/col/box
    :return: False if the list has duplicate
    """
    for n in range(1, 10):
        if ls.count(n) >= 2:
            return False
    return True


def print_board(board):
    for r in board:
        print(*r)


def solve(board):
    empty = pick_empty(board)
    # base case
    if not empty:
        return True
    else:
        r, c = empty
    # loop through 1-9
    for num in range(1, 10):
        # check if it can insert into the picked empty space
        if validate_number(board, num, empty):
            # insert the number into the picked empty space
            board[r][c] = num
            # if it reaches the end of this function, that means no number can insert into this space
            # so the previous number is invalid
            if solve(board):
                return True
            # reset this number then go back to the previous number and try next
            board[r][c] = 0
    return False


def main():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    board2 = [
        [0, 0, 0, 0, 8, 0, 0, 0, 0],
        [9, 0, 2, 0, 4, 1, 5, 0, 0],
        [0, 0, 3, 7, 0, 9, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [3, 0, 0, 0, 0, 0, 0, 0, 5],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 5, 0, 7, 3, 0, 0],
        [0, 0, 8, 2, 3, 0, 7, 0, 1],
        [0, 0, 0, 0, 9, 0, 0, 0, 0]
    ]

    print_board(board2)
    print(validate_board(board2))
    solve(board2)
    print_board(board2)
    print(validate_board(board2))


if __name__ == '__main__':
    main()
