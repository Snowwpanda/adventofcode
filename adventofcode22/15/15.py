import re
import numpy as np
from functools import cmp_to_key


def fill_grid(sensor, grid):
    row = 2000000
    xmax = grid.shape[0]
    dist = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
    distToRow = abs(sensor[1] - row)
    if distToRow <= dist:
        for i in range(-dist+distToRow, dist-distToRow+1):
            grid[i + sensor[0]] = 1
    return grid



def solveA(file_name):

    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        sensors = []
        for line in lines:
            sensors.append([int(i) for i in re.search('(\d+)[^\d]*(\d+)[^\d]*(\d+)[^\d]*(\d+)', line).groups()])
        xcors = max([i[0] for i in sensors] + [i[2] for i in sensors])
        grid = np.zeros(xcors*4)
        for sensor in sensors:
            gird = fill_grid(sensor, grid)

        for sensor in sensors:
            if sensor[3] == 2000000:
                grid[sensor[2]] = 0
        print(sum(grid == 1))


def check_line(xrow, sensors):
    ypos = 0
    for sensor in sensors:
        dist = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
        distToSensor = abs(sensor[0] - xrow) + abs(sensor[1] - ypos)
        if dist >= distToSensor:
            ypos = sensor[1] + dist - abs(sensor[0] - xrow) + 1

    return ypos


    row = 2000000
    xmax = grid.shape[0]
    dist = abs(sensor[0] - sensor[2]) + abs(sensor[1] - sensor[3])
    distToRow = abs(sensor[1] - row)
    if distToRow <= dist:
        for i in range(-dist+distToRow, dist-distToRow+1):
            grid[i + sensor[0]] = 1
    return grid


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        sensors = []
        for line in lines:
            sensors.append([int(i) for i in re.search('(-?\d+)[^\d-]*(-?\d+)[^\d-]*(-?\d+)[^\d-]*(-?\d+)', line).groups()])

        sensors.sort(key = lambda x: x[1])
        key = lambda x: x.modified
        for i in range(4000001):
            j = check_line(i, sensors)
            if j <= 4000000:
                x = i
                y = j
                break


        print([x,y])
        print(4000000*x + y)

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
