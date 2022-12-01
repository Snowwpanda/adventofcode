import queue

import numpy as np
from collections import deque


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    f.close()
    return data


def is_lowpoint(data, i, j):
    at_loc = data[i][j]
    if i != 0 and data[i-1][j] <= at_loc:
        return False
    elif j != 0 and data[i][j-1] <= at_loc:
        return False
    elif i != len(data)-1  and data[i+1][j] <= at_loc:
        return False
    elif j != len(data[0])-1 and data[i][j+1] <= at_loc:
        return False
    else:
        data[i][j] = -data[i][j]
        return True


def is_in(data, param):
    i = param[0]
    j = param[1]
    if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]) or data[i][j] >= 9:
        return False
    else:
        return True


def bfs_basin_size(data, i, j):
    size = 1
    bfs_queue = queue.Queue()
    bfs_queue.put(np.array([i, j]))
    directions = np.array([[1,0], [-1,0], [0,1], [0,-1]])
    data[i][j] = 10
    while True:
        if bfs_queue.empty():
            break
        p = bfs_queue.get()
        for d_r in directions:
            if is_in(data, p+d_r):
                data[(p+d_r)[0]][(p+d_r)[1]] = 10
                bfs_queue.put(p+d_r)
                size += 1
    return size

def task9():
    data = read_input()
    ## data = ['2199943210','3987894921','9856789892','8767896789','9899965678']
    data = np.array([[int(char)for char in line] for line in data ])
    print(data, len(data),len(data[0]))
    total_risk_level = 0
    basin_sizes = []
    for i in range(len(data)):
        for j in range(len(data[0])):
            if is_lowpoint(data, i, j):
                total_risk_level += -data[i][j] + 1

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != 9 and is_lowpoint(data, i, j):
                basin_sizes.append(bfs_basin_size(data, i, j))
    basin_sizes.sort(reverse=True)

    print(total_risk_level)
    write_sol(total_risk_level, 1)

    prod = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]
    print(prod)
    write_sol(prod, 2)


task9()