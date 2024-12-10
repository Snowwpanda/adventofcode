import numpy as np
import re
import pathlib as pl

def calculate_score(grid, start_i, start_j):
    # bfs
    queue = [(start_i, start_j, 0)]
    peaks = set()
    while queue:
        i, j, h = queue.pop(0)
        if h == 9:
            peaks.add((i, j))
            continue
        for i_, j_ in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= i_ < len(grid) and 0 <= j_ < len(grid[0]) and grid[i_][j_] == h + 1:
                queue.append((i_, j_, h + 1))
    
    return len(peaks)


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    grid = [[int(x) for x in line.strip()] for line in lines]

    sum = 0
    for i in range(len(grid)):
        for j, val in enumerate(grid[i]):
            if val == 0:
                sum += calculate_score(grid, i, j)

    res = sum

    # Print result
    print("Answer Part 1:")
    print(res)

def calculate_complex_score(grid, start_i, start_j):
    # bfs
    queue = [(start_i, start_j, 0)]
    trail = 0
    while queue:
        i, j, h = queue.pop(0)
        if h == 9:
            trail += 1
            continue
        for i_, j_ in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= i_ < len(grid) and 0 <= j_ < len(grid[0]) and grid[i_][j_] == h + 1:
                queue.append((i_, j_, h + 1))
    
    return trail



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    grid = [[int(x) for x in line.strip()] for line in lines]

    sum = 0
    for i in range(len(grid)):
        for j, val in enumerate(grid[i]):
            if val == 0:
                sum += calculate_complex_score(grid, i, j)

    res = sum

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')