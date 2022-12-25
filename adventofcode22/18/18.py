import re
import numpy as np
from functools import cmp_to_key
import sys


def parse_lava(lines):
    lines = [[int(num)+1  for num in line.strip().split(',')] for line in lines]
    grid = np.zeros(np.add(np.max(lines, axis = 0), [2,2,2]))
    for line in lines:
        grid[tuple(line)] = 1
    return grid


def count_sides(grid):
    gridDim = grid.shape
    totalSides = 0
    for i in range(gridDim[0]-1):
        totalSides += np.sum((grid[i] + grid[i+1]) == 1 )
    for i in range(gridDim[1]-1):
        totalSides += np.sum((grid[:,i] + grid[:,i+1]) == 1 )
    for i in range(gridDim[2]-1):
        totalSides += np.sum((grid[:,:,i] + grid[:,:,i+1]) == 1 )
    return totalSides

def count_osutside_sides(grid):
    gridDim = grid.shape
    totalSides = 0
    for i in range(gridDim[0]-1):
        totalSides += np.sum((grid[i] + grid[i+1]) == 3 )
    for i in range(gridDim[1]-1):
        totalSides += np.sum((grid[:,i] + grid[:,i+1]) == 3 )
    for i in range(gridDim[2]-1):
        totalSides += np.sum((grid[:,:,i] + grid[:,:,i+1]) == 3 )
    return totalSides


def solveA(file_name):

    with open(file_name) as my_file:
        ## too lazy for asserting..
        grid = parse_lava(my_file.readlines())
        total = count_sides(grid)

    print('free sides')
    print(total)


def fill_grid(grid):
    gridDim = grid.shape
    grid[(0,0,0)] = 2
    queue = [(0,0,0)]
    directions = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    while queue:
        current = queue.pop(0)
        for dir in directions:
            next = tuple(np.add(current, dir))
            if 0 <= next[0] < gridDim[0] and 0 <= next[1] < gridDim[1] and 0 <= next[2] < gridDim[2]:
                if grid[next] == 0:
                    queue.append(next)
                    grid[next] = 2

    return grid


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        grid = parse_lava(my_file.readlines())
        grid = fill_grid(grid)
        total = count_osutside_sides(grid)

    print('free sides')
    print(total)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
