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


def cal_x(start, steps):
    slowest = max(start - steps, 0)
    return ((start * (start + 1)) - (slowest * (slowest + 1))) // 2


def cal_y(start, steps):
    velo_dist = steps * start
    gravity = (steps * (steps - 1)) // 2
    return velo_dist - gravity


def binsearch_xmin(param, steps):
    left = 0
    right = param
    while left != right:
        start = (left + right) // 2
        if cal_x(start, steps) < param:
            left = start + 1
        else:
            right = start
    return left


def binsearch_ymin(param, steps):
    # assuming param negative
    left = param
    right = steps
    while left != right:
        start = (left + right) // 2
        if cal_y(start, steps) < param:
            left = start + 1
        else:
            right = start
    return left


def binsearch_xmax(param, steps):
    left = 0
    right = param
    while left != right:
        start = (left + right + 1) // 2
        if cal_x(start, steps) > param:
            right = start - 1
        else:
            left = start
    return left


def binsearch_ymax(param, steps):
    # assuming param negative
    left = param
    right = steps
    while left != right:
        start = (left + right + 1) // 2
        if cal_y(start, steps) > param:
            right = start - 1
        else:
            left = start
    return left


def psbl_for_steps(steps, target_area):
    x_min = binsearch_xmin(target_area[0][0], steps)
    x_max = binsearch_xmax(target_area[0][1], steps)
    y_min = binsearch_ymin(target_area[1][0], steps)
    y_max = binsearch_ymax(target_area[1][1], steps)
    if cal_y(y_max+1, steps) <= target_area[1][1] or cal_y(y_min-1, steps) >= target_area[1][0] \
            or cal_x(x_max+1, steps) <= target_area[0][1] or cal_x(x_min-1, steps) >= target_area[0][0]:
        pass
    if cal_y(y_max, steps) > target_area[1][1] or cal_y(y_min, steps) < target_area[1][0] \
            or cal_x(x_max, steps) > target_area[0][1] or cal_x(x_min, steps) < target_area[0][0]:
        pass
    if x_min <= x_max and y_min <= y_max:
        return [(i, j) for i in range(x_min, x_max+1) for j in range(y_min, y_max+ 1)]
    else:
        return []


def task17():
    data = read_input()[0]
    ## data = 'target area: x=20..30, y=-10..-5'
    data = data[15:].split(', y=')
    target_area = [[int(s) for s in line.split('..')] for line in data]
    print(target_area)

    max_y = 109
    max_up = 109 * 110 // 2
    print(max_up)
    write_sol(max_up, 1)

    psbl_starts = []
    for steps in range(1, 250):
        psbl_starts += psbl_for_steps(steps, target_area)

    psbl_starts = set(psbl_starts)
    print(len(psbl_starts))
    write_sol(len(psbl_starts), 2)


task17()
