# import numpy as np
# import re
import pathlib as pl
from pathlib import Path


def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    grid = [[0 if x == '.' else 1 for x in line] for line in input_data.splitlines()]
    
    grids = []
    rightgrid = [row[1:] + [0] for row in grid]
    leftgrid = [[0] + row[:-1] for row in grid]

    for g in [grid, rightgrid, leftgrid]:
        transposeg = list(map(list, zip(*g)))
        upgrid = list( map(list, zip(*[row[1:] + [0] for row in transposeg])))
        downgrid = list( map(list, zip(*[[0] + row[:-1] for row in transposeg])))
        grids.append(g)
        grids.append(upgrid)
        grids.append(downgrid)

    # summarize how many neighbors are occupied (including self)
    neighbors_grid = [[sum(neighbors) for neighbors in zip(*rows)] for rows in zip(*grids)]


    valid_positions = [[ n < 5 and p == 1 for n, p in zip(*rows)] for rows in zip(neighbors_grid, grid)]

    output = sum([sum(row) for row in valid_positions])

    print("Answer Part 1:")
    print(output)


def calc_neighbors(grid):
    
    grids = []
    rightgrid = [row[1:] + [0] for row in grid]
    leftgrid = [[0] + row[:-1] for row in grid]

    for g in [grid, rightgrid, leftgrid]:
        transposeg = list(map(list, zip(*g)))
        upgrid = list( map(list, zip(*[row[1:] + [0] for row in transposeg])))
        downgrid = list( map(list, zip(*[[0] + row[:-1] for row in transposeg])))
        grids.append(g)
        grids.append(upgrid)
        grids.append(downgrid)
    # summarize how many neighbors are occupied (including self)
    return [[sum(neighbors) for neighbors in zip(*rows)] for rows in zip(*grids)]

    
def solveB(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    grid = [[0 if x == '.' else 1 for x in line] for line in input_data.splitlines()]
    

    removed = 0
    while True:
        valid_positions = [[ n < 5 and p == 1 for n, p in zip(*rows)] for rows in zip(calc_neighbors(grid), grid)]
        grid = [[1 if x and not valid else 0 for x, valid in zip(*rows)] for rows in zip(grid, valid_positions)]
        r = sum([sum(row) for row in valid_positions])
        if r == 0:
            break
        removed += r

    output = removed


    print("Answer Part 2:")
    print(output)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
