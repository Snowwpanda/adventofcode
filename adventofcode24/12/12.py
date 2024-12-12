import numpy as np
import re
import pathlib as pl


def calculate_garden(grid, i, j, visited):
    visited.add((i, j))
    queue = [(i, j)]
    garden_type = grid[i][j]
    area = 1
    perimeter = 0
    while queue:
        i, j = queue.pop(0)
        for i_, j_ in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if grid[i_][j_] != garden_type:
                perimeter += 1
            elif (i_, j_) not in visited:
                area += 1
                visited.add((i_, j_))
                queue.append((i_, j_))
    return area, perimeter

def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    grid = [[x for x in line.strip()] for line in lines]

    # add edges of grid
    grid = [['.'] + line + ['.'] for line in grid]
    grid = [['.' for _ in range(len(grid[0]))]] + grid + [['.' for _ in range(len(grid[0]))]]

    fence_cost = 0
    visited = set()
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if (i, j) not in visited:
                area, perimeter = calculate_garden(grid, i, j, visited)
                fence_cost += area * perimeter
    
    res = fence_cost
    
    # Print result
    print("Answer Part 1:")
    print(res)

def calculate_garden_bulk(grid, i, j, visited):
    visited.add((i, j))
    queue = [(i, j)]
    garden_type = grid[i][j]
    area = 1
    sides = 0
    sides_set = set()
    while queue:
        i, j = queue.pop(0)
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i_, j_ = i + direction[0], j + direction[1]
            if grid[i_][j_] != garden_type:
                # check if neighbor in sides
                if (i_ + direction[1], j_+direction[0], direction) not in sides_set and (i_ - direction[1], j_ - direction[0], direction) not in sides_set:
                    sides += 1
                if (i_ + direction[1], j_+direction[0], direction) in sides_set and (i_ - direction[1], j_ - direction[0], direction) in sides_set:
                    sides -= 1
                sides_set.add((i_, j_, direction))
            elif (i_, j_) not in visited:
                area += 1
                visited.add((i_, j_))
                queue.append((i_, j_))
    return area, sides


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    
    grid = [[x for x in line.strip()] for line in lines]

    # add edges of grid
    grid = [['.'] + line + ['.'] for line in grid]
    grid = [['.' for _ in range(len(grid[0]))]] + grid + [['.' for _ in range(len(grid[0]))]]


    fence_cost = 0
    visited = set()
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[0])-1):
            if (i, j) not in visited:
                area, sides = calculate_garden_bulk(grid, i, j, visited)
                fence_cost += area * sides
    
    res = fence_cost

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')