import math

import numpy as np
import re
import time
from collections import Counter
# import priority queue
import heapq

# import plt function

def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # calculate max right and max down
    curr = [0,0]
    max_sides = [0,0]
    min_sides = [0,0]
    for line in lines:
        if re.search('([LDRU]) (\d+)', line):
            direction, num = re.search('([LDRU]) (\d+)', line).groups()
            num = int(num)
            if direction == 'L':
                curr[0] -= num
            elif direction == 'R':
                curr[0] += num
            elif direction == 'U':
                curr[1] -= num
            elif direction == 'D':
                curr[1] += num
        max_sides[0] = max(max_sides[0], curr[0])
        max_sides[1] = max(max_sides[1], curr[1])
        min_sides[0] = min(min_sides[0], curr[0])
        min_sides[1] = min(min_sides[1], curr[1])
        # check below 0

    # create grid
    grid = np.zeros((max_sides[0]-min_sides[0]+1, max_sides[1]-min_sides[1]+1))

    # draw the dig plan
    curr = [-min_sides[0], -min_sides[1]]
    grid[curr[0], curr[1]] = 1
    for line in lines:
        if re.search('([LDRU]) (\d+)', line):
            direction, num = re.search('([LDRU]) (\d+)', line).groups()
            num = int(num)
            if direction == 'L':
                grid[curr[0]-num:curr[0], curr[1]] = 1
                curr[0] -= num
            elif direction == 'R':
                grid[curr[0]+1:curr[0]+num+1, curr[1]] = 1
                curr[0] += num
            elif direction == 'U':
                grid[curr[0], curr[1]-num:curr[1]] = 1
                curr[1] -= num
            elif direction == 'D':
                grid[curr[0], curr[1]+1:curr[1]+num+1] = 1
                curr[1] += num

    print(f"grid is:")
    print(grid)

    # calculate area of grid
    area = 0
    for i in range(grid.shape[0]):
        inside = False
        for j in range(grid.shape[1]):
            if grid[i,j] == 1 or inside:
                area += 1
            if grid[i,j] == 1 and i < grid.shape[0]-1 and grid[i+1,j] == 1:
                inside = not inside

    print(f"area is {area}")






    return



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # calculate max right and max down
    curr = [0,0]
    max_sides = [0,0]
    min_sides = [0,0]
    for line in lines:
        if re.search('#(.{5})([0-3])', line):
            num, dir = re.search('#(.{5})([0-3])', line).groups()
            # convert num and direction
            # num is in hexadecimal
            num = int(num, 16)
            # direction in [R, D, L, U]
            dir_map = {0:'R', 1:'D', 2:'L', 3:'U'}
            direction = dir_map[int(dir)]

            if direction == 'L':
                curr[0] -= num
            elif direction == 'R':
                curr[0] += num
            elif direction == 'U':
                curr[1] -= num
            elif direction == 'D':
                curr[1] += num
        max_sides[0] = max(max_sides[0], curr[0])
        max_sides[1] = max(max_sides[1], curr[1])
        min_sides[0] = min(min_sides[0], curr[0])
        min_sides[1] = min(min_sides[1], curr[1])
        # check below 0

    # create array with points
    grid = []
    for i in range(max_sides[1]-min_sides[1]+3):
        grid.append(set())

    # draw the dig plan
    curr = [-min_sides[0]+2, -min_sides[1]+1]
    grid[curr[1]].add(curr[0])
    for line in lines:
        if re.search('#(.{5})([0-3])', line):
            num, dir = re.search('#(.{5})([0-3])', line).groups()
            # convert num and direction
            # num is in hexadecimal
            num = int(num, 16)
            # direction in [R, D, L, U]
            dir_map = {0:'R', 1:'D', 2:'L', 3:'U'}
            direction = dir_map[int(dir)]


            if direction == 'L':
                curr[0] -= num
                grid[curr[1]].add(curr[0])
            elif direction == 'R':
                curr[0] += num
                grid[curr[1]].add(curr[0])
            elif direction == 'U':
                curr[1] -= num
                for row in grid[curr[1]:curr[1]+num]:
                    row.add(curr[0])
            elif direction == 'D':
                curr[1] += num
                for row in grid[curr[1]-num+1:curr[1]+1]:
                    row.add(curr[0])

    print(f"grid is:")
    # print(grid)

    # calculate area of grid
    area = 0
    for i in range(1,grid.__len__()):
        inside = False
        online = False
        row = sorted(grid[i])
        curr_point = 0
        for point in row:
            if inside or online:
                area += point - curr_point
            else:
                area += 1
            if not point in grid[i-1] or not point in grid[i+1]:
                online = not online
            if point in grid[i+1]:
                inside = not inside
            curr_point = point

    print(f"area is {area}")
    #
    # area is 147839570293376
    # B: --- 738.1280493736267 seconds ---

    return


if __name__ == '__main__':
    # time the solution:
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
