import numpy as np
import re
import pathlib as pl
import math

def colinear(A, B):
    return A[0] * B[1] == A[1] * B[0]

def min_distance(A, B, prize):
    if not colinear(A, B):
        # must be unique solution by adapting to new coordinates
        # take inversion of transformation matrix
        A_B_matrix = np.array([[A[0], B[0]], [A[1], B[1]]])
        A_B_inv = np.linalg.inv(A_B_matrix)
        press_a, press_b = np.dot(A_B_inv, prize)
        press_a = int(round(press_a))
        press_b = int(round(press_b))
        # make sure both are positive and were integers
        if (press_a >= 0 and press_b >= 0 and 
            press_a * A[0] + press_b * B[0] == prize[0] and press_a * A[1] + press_b * B[1] == prize[1]):
            # cost of 3 for A and 1 for B
            return int(3 * press_a + press_b)
        else:
            # print("Prize is not reachable")
            return 0

    if colinear(A, B):
        if not colinear(A, prize):
            # print("A, B and prize are colinear, impossible to reach")
            return 0

        # can ignore y coordinate
        # check which is cheaper:
        cheaper_button = A[0] if A[0] > 3* B[0] else B[0]
        expensive_button = A[0] if A[0] <= 3* B[0] else B[0]
        for i in range(prize[0] // cheaper_button + 1, 0, -1):
            rest = prize[0] - i * cheaper_button
            if rest % expensive_button == 0:
                press_a = i if cheaper_button == A[0] else rest // expensive_button
                press_b = i if cheaper_button == B[0] else rest // expensive_button
                return 3 * press_a + press_b
        else:
            # print("Prize is not reachable")
            return 0
    
    return 0


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # group by 4 lines
    games = [lines[i:i+4] for i in range(0, len(lines), 4)]

    # example game:
    # Button A: X+26, Y+66
    # Button B: X+67, Y+21
    # Prize: X=12748, Y=12176

    tokens = 0
    for game in games:
        A = [int(coor) for coor in re.match(r'Button A: X\+(\d+), Y\+(\d+).*', game[0]).groups()]
        B = [int(coor) for coor in re.match(r'Button B: X\+(\d+), Y\+(\d+).*', game[1]).groups()]
        prize = [int(coor) for coor in re.match(r'Prize: X=(\d+), Y=(\d+).*', game[2]).groups()]

        tokens += min_distance(A, B, prize)

    res = tokens
    
    # Print result
    print("Answer Part 1:")
    print(res)


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # group by 4 lines
    games = [lines[i:i+4] for i in range(0, len(lines), 4)]

    # example game:
    # Button A: X+26, Y+66
    # Button B: X+67, Y+21
    # Prize: X=12748, Y=12176

    tokens = 0
    for game in games:
        A = [int(coor) for coor in re.match(r'Button A: X\+(\d+), Y\+(\d+).*', game[0]).groups()]
        B = [int(coor) for coor in re.match(r'Button B: X\+(\d+), Y\+(\d+).*', game[1]).groups()]
        prize = [int(coor) for coor in re.match(r'Prize: X=(\d+), Y=(\d+).*', game[2]).groups()]
        prize = [prize[0] + 10000000000000, prize[1] + 10000000000000]

        tokens += min_distance(A, B, prize)

    res = tokens

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')