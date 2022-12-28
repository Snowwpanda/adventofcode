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








if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
