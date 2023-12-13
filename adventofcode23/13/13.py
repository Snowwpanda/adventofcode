import math

import numpy as np
import re
import time
from collections import Counter


# import plt function


def search_horizontal(grid):
    found = False
    for axis in range(1, grid.__len__()):
        found = True
        for y in range(min(axis, grid.__len__() - axis)):
            if grid[axis - y - 1] != grid[axis + y]:
                found = False
                break
        if found:
            return axis
    return -1


def search_vertical(grid):
    found = False
    for axis in range(1, grid[0].__len__()):
        found = True
        for x in range(min(axis, grid[0].__len__() - axis)):
            if [line[axis - x - 1] for line in grid] != [line[axis + x] for line in grid]:
                found = False
                break
        if found:
            return axis
    return -1


def calculate_mirror(grid):
    x = search_horizontal(grid)
    if x != -1:
        print(f'Horizontal mirror at x={x}')
        return x * 100
    y = search_vertical(grid)
    if y != -1:
        print(f'Vertical mirror at y={y}')
        return y

    print('No mirror found')
    return 0


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # input consists of grids with '.' and '#' characters
    # read in grids one by one
    grid = []
    total = 0
    count = 0
    while lines.__len__() > 0:
        line = lines.pop(0).strip()
        if line == '':
            # assert grid is a square:
            if not all([line.__len__() == grid[0].__len__() for line in grid]):
                print('Grid is not a rectangle!')
                return
            print(f'Grid {count}: ', end='')
            count += 1
            total += calculate_mirror(grid)
            grid = []
        else:
            grid.append([letter for letter in line])
    if grid.__len__() > 0:
        print(f'Grid {count}: ', end='')
        count += 1
        total += calculate_mirror(grid)
        grid = []

    print(f'The total is {total}')
    return


def swap(param):
    if param == '#':
        return '.'
    elif param == '.':
        return '#'
    else:
        print(f'Unknown character {param}')
        return param
    pass



def search_horizontal_smudge(grid):
    for axis in range(1, grid.__len__()):
        smudge = 0
        for y in range(min(axis, grid.__len__() - axis)):
            smudge += sum( [grid[axis - y - 1][i] != grid[axis + y][i] for i in range(grid[0].__len__()) ] )
            if smudge > 1:
                break
        if smudge == 1:
            return axis
    return -1


def search_vertical_smudge(grid):
    for axis in range(1, grid[0].__len__()):
        smudge = 0
        for x in range(min(axis, grid[0].__len__() - axis)):
            smudge += sum( [grid[i][axis - x - 1] != grid[i][axis + x]  for i in range(grid.__len__()) ] )
            if smudge > 1:
                break
        if smudge == 1:
            return axis
    return -1

def calculate_smudge_mirror(grid):
    ax = search_horizontal_smudge(grid)
    if ax != -1:
        print(f'Horizontal mirror at x={ax}')
        return ax * 100
    ax = search_vertical_smudge(grid)
    if ax != -1:
        print(f'Vertical mirror at y={ax}')
        return ax


    print('No smudge found')
    return 0


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # input consists of grids with '.' and '#' characters
    # read in grids one by one
    grid = []
    total = 0
    count = 0
    while lines.__len__() > 0:
        line = lines.pop(0).strip()
        if line == '':
            # assert grid is a square:
            if not all([line.__len__() == grid[0].__len__() for line in grid]):
                print('Grid is not a rectangle!')
                return
            print(f'Grid {count}: ', end='')
            count += 1
            total += calculate_smudge_mirror(grid)
            grid = []
        else:
            grid.append([letter for letter in line])
    if grid.__len__() > 0:
        print(f'Grid {count}: ', end='')
        count += 1
        total += calculate_smudge_mirror(grid)
        grid = []

    print(f'The total is {total}')

    return


if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
