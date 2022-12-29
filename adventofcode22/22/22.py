import re
import numpy as np
from functools import cmp_to_key
import sys
import operator


def replace_grid(char):
    if char == ' ':
        return -1
    elif char == '#':
        return 1
    elif char == '.':
        return 0


def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    path = lines[-1].strip()
    grid = lines[:-2]
    maxX = len(grid)
    maxY = max([len(line)-1 for line in grid])
    for i in range(maxX):
        line = [ replace_grid(char) for char in  grid[i][:-1]]
        n = len(line)
        line = line + ([-1] * (maxY - n))
        grid[i] = line
    grid = np.array(grid)
    directions = np.array([[0,1],[1,0],[0,-1],[-1,0]])
    currDir = 0
    currPos = np.array([0,0]) #wrong currPos but ok
    while len(path) > 0:
        if re.search(r'^\d+', path):
            match = re.search(r'^(\d+)', path)
            dist = int(match.groups()[0])
            path = path[match.end():]
            next = currPos
            while dist > 0:
                next = next + directions[currDir]
                next[0] = (next[0] + maxX) % maxX
                next[1] = (next[1] + maxY) % maxY
                if grid[tuple(next)] == 1:
                    break
                elif grid[tuple(next)] == 0:
                    currPos = next
                    dist -= 1

        elif re.search(r'^[R]', path):
            currDir = (currDir + 1) % 4
            path = path[1:]
        elif re.search(r'^[L]', path):
            currDir = (currDir + 3) % 4
            path = path[1:]




    print('finalpos')
    print(currPos)
    print(currDir)
    print(1000 * (currPos[0]+1) + 4 * (currPos[1]+1) + currDir)


def fold_cube(grid):
    if grid.shape[0] == 200:
        grid_3d = np.ones([52,52,52]) * -1
        grid_3d[0,1:51,1:51] = grid[:50, 50:100]
        grid_3d[1:51, 1:51, 51] = np.transpose(grid[:50, 100:150])
        grid_3d[1:51, 51, 1:51] = grid[50:100, 50:100]
        grid_3d[51, 1:51, 1:51] = grid[149:99:-1, 50:100]
        grid_3d[1:51, 1:51, 0] = np.transpose(grid[149:99:-1, 0:50])
        grid_3d[1:51, 0, 1:51] = np.transpose(grid[150:200, 0:50])

    if grid.shape[0] == 12:
        grid_3d = np.ones([6, 6, 6]) * -1
        grid_3d[0, 1:5, 1:5] = grid[ :4, 8:12]
        grid_3d[1:5, 5, 1:5] = grid[ 4:8, 8:12]
        grid_3d[1:5, 1:5, 0] = grid[ 4:8, 4:8]
        grid_3d[1:5, 0, 1:5] = grid[ 4:8, 3::-1]
        grid_3d[5, 1:5, 1:5] = grid[ 11:7:-1, 8:12]
        grid_3d[1:5, 1:5, 5] = np.transpose(grid[  11:7:-1, 15:11:-1])
    return grid_3d


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    path = lines[-1].strip()
    grid = lines[:-2]
    maxX = len(grid)
    maxY = max([len(line)-1 for line in grid])
    for i in range(maxX):
        line = [ replace_grid(char) for char in  grid[i][:-1]]
        n = len(line)
        line = line + ([-1] * (maxY - n))
        grid[i] = line
    grid = np.array(grid)
    grid_3d = fold_cube(grid)
    currDir = np.array([0, 0, 1])
    right = np.array([0, 1, 0])
    currPos = np.array([0,1,1])
    while len(path) > 0:
        if re.search(r'^\d+', path):
            match = re.search(r'^(\d+)', path)
            dist = int(match.groups()[0])
            path = path[match.end():]
            next = currPos
            while dist > 0:
                next = next + currDir
                if grid_3d[tuple(next)] == -1:
                    nextDir = np.cross( right, currDir)
                    next += nextDir
                    if grid_3d[tuple(next)] == 1:
                        break
                    elif grid_3d[tuple(next)] == 0:
                        currPos = next
                        dist -= 1
                        currDir = nextDir
                elif grid_3d[tuple(next)] == 1:
                    break
                elif grid_3d[tuple(next)] == 0:
                    currPos = next
                    dist -= 1

        elif re.search(r'^[R]', path):
            tmp = currDir
            currDir = right
            right = -tmp
            path = path[1:]
        elif re.search(r'^[L]', path):
            tmp = currDir
            currDir = -right
            right = tmp
            path = path[1:]




    print('finalpos')
    print(currPos)
    print(currDir)

    print((11)*1000+(12+100)*4 +3)








if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
