import re
import numpy as np
from functools import cmp_to_key
import sys
import operator

replace_map = {
    '#' : 16,
    '.' : 0,
    '<' : 1,
    '>' : 2,
    '^' : 4,
    'v' : 8,
}

def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    directions = np.array([[1,0],[0,1],[-1,0],[0,-1]])
    grid = []
    for line in lines:
        grid.append([replace_map[char] for char in line.strip()])
    grid = np.array(grid)
    time = 0
    (n,m) = grid.shape
    possible_pos = np.zeros((n,m))
    possible_pos[0,1] = 1

    while possible_pos[n-1, m-2] == 0:
        possible_pos[n-1, m-2] += possible_pos[n-2, m-2]
        possible_pos[1:-1,1:-1] += possible_pos[2:,1:-1] + possible_pos[1:-1,2:] + possible_pos[:-2,1:-1] + possible_pos[1:-1,:-2]
        # '<' : 1,
        # '>' : 2,
        # '^' : 4,
        # 'v' : 8,
        # blizzards never leave the grid
        left = grid[1:-1, 1:-1] % 2 == 1
        left = np.concatenate((left[:, 1:], left[:, 0].reshape(n-2, 1)), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        right = grid[1:-1, 1:-1] % 2 == 1
        right = np.concatenate((right[:, m-3].reshape(n-2,1), right[:, :m-3]), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        up = grid[1:-1, 1:-1] % 2 == 1
        up = np.concatenate((up[1:, :], up[0, :].reshape(1,m-2)), axis=0)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        down = grid[1:-1, 1:-1] % 2 == 1
        down = np.concatenate((down[n-3, :].reshape(1,m-2), down[:n-3, :]), axis=0)

        grid[1:-1, 1:-1] = left + right*2 + up*4 + down*8
        possible_pos = (possible_pos != 0) * (grid == 0) * 1
        time += 1


    print('shortest time')
    print(time)



def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    directions = np.array([[1,0],[0,1],[-1,0],[0,-1]])
    grid = []
    for line in lines:
        grid.append([replace_map[char] for char in line.strip()])
    grid = np.array(grid)
    time = 0
    (n,m) = grid.shape

    possible_pos = np.zeros((n,m))
    possible_pos[0,1] = 1

    while possible_pos[n-1, m-2] == 0:
        possible_pos[n-1, m-2] += possible_pos[n-2, m-2]
        possible_pos[1:-1,1:-1] += possible_pos[2:,1:-1] + possible_pos[1:-1,2:] + possible_pos[:-2,1:-1] + possible_pos[1:-1,:-2]
        # '<' : 1,
        # '>' : 2,
        # '^' : 4,
        # 'v' : 8,
        # blizzards never leave the grid
        left = grid[1:-1, 1:-1] % 2 == 1
        left = np.concatenate((left[:, 1:], left[:, 0].reshape(n-2, 1)), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        right = grid[1:-1, 1:-1] % 2 == 1
        right = np.concatenate((right[:, m-3].reshape(n-2,1), right[:, :m-3]), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        up = grid[1:-1, 1:-1] % 2 == 1
        up = np.concatenate((up[1:, :], up[0, :].reshape(1,m-2)), axis=0)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        down = grid[1:-1, 1:-1] % 2 == 1
        down = np.concatenate((down[n-3, :].reshape(1,m-2), down[:n-3, :]), axis=0)

        grid[1:-1, 1:-1] = left + right*2 + up*4 + down*8
        possible_pos = (possible_pos != 0) * (grid == 0) * 1
        time += 1

    possible_pos = np.zeros((n,m))
    possible_pos[n-1,m-2] = 1
    while possible_pos[0, 1] == 0:
        possible_pos[0, 1] += possible_pos[1, 1]
        possible_pos[1:-1,1:-1] += possible_pos[2:,1:-1] + possible_pos[1:-1,2:] + possible_pos[:-2,1:-1] + possible_pos[1:-1,:-2]
        # '<' : 1,
        # '>' : 2,
        # '^' : 4,
        # 'v' : 8,
        # blizzards never leave the grid
        left = grid[1:-1, 1:-1] % 2 == 1
        left = np.concatenate((left[:, 1:], left[:, 0].reshape(n-2, 1)), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        right = grid[1:-1, 1:-1] % 2 == 1
        right = np.concatenate((right[:, m-3].reshape(n-2,1), right[:, :m-3]), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        up = grid[1:-1, 1:-1] % 2 == 1
        up = np.concatenate((up[1:, :], up[0, :].reshape(1,m-2)), axis=0)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        down = grid[1:-1, 1:-1] % 2 == 1
        down = np.concatenate((down[n-3, :].reshape(1,m-2), down[:n-3, :]), axis=0)

        grid[1:-1, 1:-1] = left + right*2 + up*4 + down*8
        possible_pos = (possible_pos != 0) * (grid == 0) * 1
        time += 1
    possible_pos = np.zeros((n,m))
    possible_pos[0,1] = 1

    while possible_pos[n-1, m-2] == 0:
        possible_pos[n-1, m-2] += possible_pos[n-2, m-2]
        possible_pos[1:-1,1:-1] += possible_pos[2:,1:-1] + possible_pos[1:-1,2:] + possible_pos[:-2,1:-1] + possible_pos[1:-1,:-2]
        # '<' : 1,
        # '>' : 2,
        # '^' : 4,
        # 'v' : 8,
        # blizzards never leave the grid
        left = grid[1:-1, 1:-1] % 2 == 1
        left = np.concatenate((left[:, 1:], left[:, 0].reshape(n-2, 1)), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        right = grid[1:-1, 1:-1] % 2 == 1
        right = np.concatenate((right[:, m-3].reshape(n-2,1), right[:, :m-3]), axis=1)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        up = grid[1:-1, 1:-1] % 2 == 1
        up = np.concatenate((up[1:, :], up[0, :].reshape(1,m-2)), axis=0)
        grid[1:-1, 1:-1] = grid[1:-1, 1:-1] / 2
        down = grid[1:-1, 1:-1] % 2 == 1
        down = np.concatenate((down[n-3, :].reshape(1,m-2), down[:n-3, :]), axis=0)

        grid[1:-1, 1:-1] = left + right*2 + up*4 + down*8
        possible_pos = (possible_pos != 0) * (grid == 0) * 1
        time += 1

    print('shortest time')
    print(time)








if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
