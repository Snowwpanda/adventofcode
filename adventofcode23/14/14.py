import math

import numpy as np
import re
import time
from collections import Counter


# import plt function


def calculate_north_load(grid):
    # go through columns and calculate load
    total_load = 0
    for x in range(len(grid[0])):
        pos = len(grid)
        for y in range(len(grid)):
            if grid[y][x] == '.':
                continue
            elif grid[y][x] == 'O':
                total_load += pos
                pos -= 1
            elif grid[y][x] == '#':
                pos = len(grid) - y - 1
            else:
                print('Unknown character')
                return 0
    return total_load


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    grid = [ list(line) for line in lines]
    # make sure grid as a rectangle
    if not all(len(line) == len(grid[0]) for line in grid):
        print('Grid is not a rectangle')
        return

    # go through columns and calculate load
    total_load = calculate_north_load(grid)

    print(f'Total load: {total_load}')


    return


def cycle_grid(grid):
    # north
    for x in range(len(grid[0])):
        pos = 0
        for y in range(len(grid)):
            if grid[y][x] == '.':
                continue
            elif grid[y][x] == 'O':
                grid[y][x] = '.'
                grid[pos][x] = 'O'
                pos += 1
            elif grid[y][x] == '#':
                pos = y+1
            else:
                print('Unknown character')
                return
    # west
    for y in range(len(grid)):
        pos = 0
        for x in range(len(grid[0])):
            if grid[y][x] == '.':
                continue
            elif grid[y][x] == 'O':
                grid[y][x] = '.'
                grid[y][pos] = 'O'
                pos += 1
            elif grid[y][x] == '#':
                pos = x+1
            else:
                print('Unknown character')
                return
    # south
    for x in range(len(grid[0])):
        pos = len(grid)-1
        for y in range(len(grid)-1, -1, -1):
            if grid[y][x] == '.':
                continue
            elif grid[y][x] == 'O':
                grid[y][x] = '.'
                grid[pos][x] = 'O'
                pos -= 1
            elif grid[y][x] == '#':
                pos = y-1
            else:
                print('Unknown character')
                return
    # east
    for y in range(len(grid)):
        pos = len(grid[0])-1
        for x in range(len(grid[0])-1, -1, -1):
            if grid[y][x] == '.':
                continue
            elif grid[y][x] == 'O':
                grid[y][x] = '.'
                grid[y][pos] = 'O'
                pos -= 1
            elif grid[y][x] == '#':
                pos = x-1
            else:
                print('Unknown character')
                return
    return

def calclulate_load(grid):
    # go through columns and calculate load
    total_load = 0
    for i in range(len(grid)):
        total_load += sum([x == 'O' for x in grid[i]]) * (len(grid) - i)
    return total_load

def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    grid = [list(line) for line in lines]
    # make sure grid as a rectangle
    if not all(len(line) == len(grid[0]) for line in grid):
        print('Grid is not a rectangle')
        return

    # do a cycle
    for i in range(100):
        cycle_grid(grid)

    # make a copy of grid
    grid_copy = [list(line) for line in grid]
    grid_copy_numbers = [Counter(line)['O'] for line in grid_copy]
    print(f"Grid copy numbers: {grid_copy_numbers}")

    cycle = 0
    for i in range(200):
        cycle_grid(grid)
        # count 'O' in every line
        grid_numbers = [ Counter(line)['O'] for line in grid]
        print(calclulate_load(grid), end=' ')
        print(grid_numbers)
        # for line in grid:
        #     print(''.join(line))
        # print('')

        if cycle == 0 and grid_copy_numbers == grid_numbers:
            # compare grid with grid_copy
            if grid == grid_copy:
                print(f'Cycle found at {i+1}')
                cycle = i+1
                break

    if cycle == 0:
        print('No cycle found')
        return


    # go to 1000000000 cycles
    delta = (1000000000 - 100) % cycle
    grid = [list(line) for line in lines]
    print(f'Fresh start')
    for i in range(delta + 100):
        cycle_grid(grid)






    # go through columns and calculate load
    total_load = calclulate_load(grid)
    print(f'Total load: {total_load}')

    return


if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
