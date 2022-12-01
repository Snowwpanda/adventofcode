import numpy as np


def check_bingo(board):
    for row in board:
        if sum(row) == -5:
            return True
    for col in board.T:
        if sum(col) == -5:
            return True
    return False


def value_board(board):
    result = sum([p for row in board for p in row if p > 0])
    return result


def mark_number(board, mark):
    for row in board:
        for i in range(len(row)):
            if row[i] == mark:
                row[i] = -1
    if check_bingo(board):
        value = value_board(board) * mark
        board *= 0
        board -= 2
        return value
    return -1


def write_ouput(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    print(out)
    f.close()


def task4():
    f = open("input.txt", "r")
    bingo = f.read()
    f.close()
    bingo = bingo.splitlines()
    numbers = np.array([int(n) for n in bingo[0].split(',')])
    bingo = bingo[2:]
    boards = np.array([[[int(i1) for i1 in l1], [int(i2) for i2 in l2], [int(i3) for i3 in l3], [int(i4) for i4 in l4],
                        [int(i5) for i5 in l5]]
                       for [l1, l2, l3, l4, l5] in
                       [[bingo[j].split(), bingo[j + 1].split(), bingo[j + 2].split(), bingo[j + 3].split(),
                         bingo[j + 4].split()] for j in range(0, len(bingo), 6)]])
    print(numbers, "\n", boards)
    mark_number(boards[0], 31)
    wins = 0
    for mark in numbers:
        for board in boards:
            res = mark_number(board, mark)
            if res != -1:
                wins += 1
                if wins == 1:
                    write_ouput(res, 1)
                elif wins == len(boards):
                    write_ouput(res, 2)
                    break
        else:
            # Continue if the inner loop wasn't broken.
            continue
        # Inner loop was broken, break the outer.
        break
    print(boards)
    return -1


task4()
