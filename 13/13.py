import queue
import numpy as np
from collections import deque


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    f.close()
    return data


def fold_dot(dot, fold):
    if fold[0] == 'x':
        x = int(fold[1])
        dot[0] = min(dot[0], 2 * x - dot[0])
        if dot[0] == x:
            print("error, on the line")
    else:
        y = int(fold[1])
        dot[1] = min(dot[1], 2 * y - dot[1])
    return 0

def task13():
    data = read_input()
    dots = [[int(char) for char in line.split(',')] for line in data[:722]]
    folds = [line.split()[2].split('=') for line in data[723:]]
    print(dots, folds)
    set_dots = set()
    for dot in dots:
        fold_dot(dot, folds[0])
        set_dots.add((dot[0], dot[1]))
    new_dots = len(set_dots)
    set_dots = set()
    for fold in folds[1:]:
        for dot in dots:
            fold_dot(dot, fold)
    for dot in dots:
        set_dots.add((dot[0], dot[1]))
    show_table = np.zeros((40, 6), dtype=int)
    for dot in set_dots:
        show_table[dot[0]][dot[1]] = 1

    print(new_dots)
    write_sol(new_dots, 1)

    print(show_table)
    ##manual readout
    passcode = 'JGAJEFKU'
    print(passcode)
    write_sol(passcode, 2)

task13()
