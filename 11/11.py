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


def flash(data, i, j):
    flashes = 1
    data[i][j] = 0
    for x in range(max(i - 1, 0), min(i + 2, 10)):
        for y in range(max(j - 1, 0), min(j + 2, 10)):
            if data[x][y] != 0:
                data[x][y] += 1
                if data[x][y] > 9:
                    flashes += flash(data, x, y)
    return flashes


def check_flashes(data):
    flashes = 0
    for i in range(10):
        for j in range(10):
            if data[i][j] > 9:
                flashes += flash(data, i, j)
    return flashes


def task11():
    data = read_input()

    data = np.array([[int(char) for char in line] for line in data])

    increase = np.ones((10, 10))
    flashes = 0
    for step in range(100):
        data = data + increase
        flashes += check_flashes(data)
    
    for step in range(1000):
        data = data + increase
        if check_flashes(data) == 100:
            end_step = step + 101
            break

    print(flashes)
    write_sol(flashes, 1)
    
    
    print(end_step)
    write_sol(end_step, 2)

task11()
