import re
import numpy as np
from functools import cmp_to_key
import sys
import operator

replace_char = {
    '.': 0,
    '#': 1,
    '\n': 0,
}


def fill_directions(directions_NSWE, grid):
    directions_NSWE[0][1:, :] += grid[:-1, :]
    directions_NSWE[0][1:, 1:] += grid[:-1, :-1]
    directions_NSWE[0][1:, :-1] += grid[:-1, 1:]

    directions_NSWE[1][:-1, :] += grid[1:, :]
    directions_NSWE[1][:-1, 1:] += grid[1:, :-1]
    directions_NSWE[1][:-1, :-1] += grid[1:, 1:]

    directions_NSWE[2][:, 1:] += grid[:, :-1]
    directions_NSWE[2][1:, 1:] += grid[:-1, :-1]
    directions_NSWE[2][:-1, 1:] += grid[1:, :-1]

    directions_NSWE[3][:, :-1] += grid[:, 1:]
    directions_NSWE[3][1:, :-1] += grid[:-1, 1:]
    directions_NSWE[3][:-1, :-1] += grid[1:, 1:]

    pass


def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    n = len(lines)
    m = len(lines[0]) - 1
    for i in range(n):
        lines[i] = [replace_char[char] for char in lines[i].strip()]
    lines = np.array(lines)
    
    space = 20
    grid = np.zeros([n + space, m + space])
    grid[space//2:-space//2, space//2:-space//2] = lines
    elves = np.sum(grid)
    starting_direction = 0
    directions = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
    for time in range(10):
        directions_NSWE = [np.zeros([n + space, m + space]), np.zeros([n + space, m + space]), np.zeros([n + space, m + space]),
                           np.zeros([n + space, m + space])]
        fill_directions(directions_NSWE, grid)

        plan_grid = np.zeros([n + space, m + space])
        for i in range(n + space):
            for j in range(m + space):
                if grid[i,j] == 1:
                    if directions_NSWE[0][i, j] == 0 and directions_NSWE[1][i, j] == 0 and directions_NSWE[2][i, j] == 0 and directions_NSWE[3][i, j] == 0:
                        plan_grid[i, j] = 1
                        continue
                    for d in range(5):
                        if d == 4:
                            plan_grid[i,j] += 1
                        elif directions_NSWE[(d+starting_direction)%4][i,j] == 0:
                            plan_grid[tuple(np.array([i,j]) + directions[(d+starting_direction)%4])] += 1
                            break

        next_grid = np.zeros([n + space, m + space])
        for i in range(n + space):
            for j in range(m + space):
                if grid[i,j] == 1:
                    if directions_NSWE[0][i, j] == 0 and directions_NSWE[1][i, j] == 0 and directions_NSWE[2][i, j] == 0 and directions_NSWE[3][i, j] == 0:
                        next_grid[i, j] = 1
                        continue
                    for d in range(5):
                        if d == 4:
                            next_grid[i, j] = 1
                        elif directions_NSWE[(d+starting_direction)%4][i,j] == 0:
                            if plan_grid[tuple(np.array([i,j]) + directions[(d+starting_direction)%4])] > 1:
                                next_grid[i, j] = 1
                            else:
                                next_grid[tuple(np.array([i,j]) + directions[(d+starting_direction)%4])] = 1
                            break
        grid = next_grid
        starting_direction = (starting_direction+1)%4

    sx = 0
    ex = n + space -1
    sy = 0
    ey = m + space -1
    while np.sum(grid[sx]) == 0:
        sx += 1
    while np.sum(grid[ex]) == 0:
        ex -= 1
    while np.sum(grid[:,sy]) == 0:
        sy += 1
    while np.sum(grid[:,ey]) == 0:
        ey -= 1

    print('size:')
    print([sx,ex,sy,ey])
    print((ex-sx+1) * (ey - sy+1))
    print((ex-sx+1) * (ey - sy+1) - elves)





def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    n = len(lines)
    m = len(lines[0]) - 1
    for i in range(n):
        lines[i] = [replace_char[char] for char in lines[i].strip()]
    lines = np.array(lines)

    space = 320
    grid = np.zeros([n + space, m + space])
    grid[space//2:-space//2, space//2:-space//2] = lines
    elves = np.sum(grid)
    starting_direction = 0
    directions = np.array([[-1, 0], [1, 0], [0, -1], [0, 1]])
    allseparated = False
    round = 0
    while allseparated == False:

        allseparated = True
        directions_NSWE = [np.zeros([n + space, m + space]), np.zeros([n + space, m + space]), np.zeros([n + space, m + space]),
                           np.zeros([n + space, m + space])]
        fill_directions(directions_NSWE, grid)
        plan_grid = np.zeros([n + space, m + space])
        for i in range(n + space):
            for j in range(m + space):
                if grid[i,j] == 1:
                    if directions_NSWE[0][i, j] == 0 and directions_NSWE[1][i, j] == 0 and directions_NSWE[2][i, j] == 0 and directions_NSWE[3][i, j] == 0:
                        plan_grid[i, j] = 1
                        continue
                    allseparated = False
                    for d in range(5):
                        if d == 4:
                            plan_grid[i,j] += 1
                        elif directions_NSWE[(d+starting_direction)%4][i,j] == 0:
                            plan_grid[tuple(np.array([i,j]) + directions[(d+starting_direction)%4])] += 1
                            break

        next_grid = np.zeros([n + space, m + space])
        for i in range(n + space):
            for j in range(m + space):
                if grid[i,j] == 1:
                    if directions_NSWE[0][i, j] == 0 and directions_NSWE[1][i, j] == 0 and directions_NSWE[2][i, j] == 0 and directions_NSWE[3][i, j] == 0:
                        next_grid[i, j] = 1
                        continue
                    for d in range(5):
                        if d == 4:
                            next_grid[i, j] = 1
                        elif directions_NSWE[(d+starting_direction)%4][i,j] == 0:
                            if plan_grid[tuple(np.array([i,j]) + directions[(d+starting_direction)%4])] > 1:
                                next_grid[i, j] = 1
                            else:
                                next_grid[tuple(np.array([i,j]) + directions[(d+starting_direction)%4])] = 1
                            break
        grid = next_grid
        starting_direction = (starting_direction+1)%4
        round += 1

    sx = 0
    ex = n + space -1
    sy = 0
    ey = m + space -1
    while np.sum(grid[sx]) == 0:
        sx += 1
    while np.sum(grid[ex]) == 0:
        ex -= 1
    while np.sum(grid[:,sy]) == 0:
        sy += 1
    while np.sum(grid[:,ey]) == 0:
        ey -= 1

    print('size:')
    print([sx,ex,sy,ey])
    print((ex-sx+1) * (ey - sy+1))
    print((ex-sx+1) * (ey - sy+1) - elves)
    print('round:')
    print(round)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
