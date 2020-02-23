from numpy import matrix


def validate_board(board):
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
        for n in range(1, 10):
            if r.count(n) >= 2:
                return False
    # check col
    for c in range(len(board[0])):
        col_list = []
        for r in range(len(board)):
            col_list.append(board[r][c])
        for n in range(1, 10):
            if col_list.count(n) >= 2:
                return False
    # check box
    """
    0 -> 0-2, 0-2
    1 -> 3-5, 0-2
    2 -> 6-8, 0-2
    3 -> 0-2, 3-5
    4 -> 3-5, 3-5
    5 -> 6-8, 3-5
    6 -> 0-2, 6-8
    7 -> 3-5, 6-8
    8 -> 6-8, 6-8
    """

    return True


def print_board(board):
    print(matrix(board))


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
    print(validate_board(board))


if __name__ == '__main__':
    main()
