import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue

def bfs(grid, start, end):
    dist = {start: 0}
    queue = [start]
    while queue:
        curr = queue.pop(0)
        if curr == end:
            return dist[end]
        for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
            next = (curr[0] + dir[0], curr[1] + dir[1])
            if grid[next[0]][next[1]] == 0 and next not in dist:
                dist[next] = dist[curr] + 1
                queue.append(next)



def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # initialize grid of size nxn
    n = 71
    number_of_bytes = 1024


    grid = np.zeros((n+2, n+2))
    start = (1,1)
    end = (n,n)
    grid[0] = np.ones(n+2)
    grid[n+1] = np.ones(n+2)
    for y in range(n+2):
        grid[y][0] = 1
        grid[y][n+1] = 1

    lines = [line.strip().split(',') for line in lines]
    falling_bytes = [(int(x), int(y)) for [x,y] in lines]

    for fall in falling_bytes[:number_of_bytes]:
        x, y = fall
        grid[x+1][y+1] = 1

    # start is top left, end is bottom right

    # bfs
    distance = bfs(grid, start, end)


    
    res = distance
    
    # Print result
    print("Answer Part 1:")
    print(res)



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    # initialize grid of size nxn
    n = 71
    number_of_bytes = 1024


    grid = np.zeros((n+2, n+2))
    start = (1,1)
    end = (n,n)
    grid[0] = np.ones(n+2)
    grid[n+1] = np.ones(n+2)
    for y in range(n+2):
        grid[y][0] = 1
        grid[y][n+1] = 1

    lines = [line.strip().split(',') for line in lines]
    falling_bytes = [(int(x), int(y)) for [x,y] in lines]

    for fall in falling_bytes[:number_of_bytes]:
        x, y = fall
        grid[x+1][y+1] = 1

    # start is top left, end is bottom right

    # bfs
    distance = bfs(grid, start, end)



    while distance != None:
        x, y = falling_bytes[number_of_bytes]
        grid[x+1][y+1] = 1
        distance = bfs(grid, start, end)
        number_of_bytes += 1

    


    
    res = falling_bytes[number_of_bytes-1]
    
    # Print result
    print("Answer Part 1:")
    print(res)
    print(f"{res[0]},{res[1]}")


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')