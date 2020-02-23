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


def validate_list(ls):
    """
    Check if the list has duplicate 1 - 9

    helper function for validate_board()
    :param ls:
    :return: False if the list has duplicate
    """
    for n in range(1, 10):
        if ls.count(n) >= 2:
            return False
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
