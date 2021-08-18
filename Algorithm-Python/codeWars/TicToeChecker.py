def is_solved(board):
    for x in board:
        if x.count(1) == 3:
            return 1
        elif x.count(2) == 3:
            return 2


is_solved([[0, 0, 1],
           [0, 1, 2],
           [2, 1, 0]])
