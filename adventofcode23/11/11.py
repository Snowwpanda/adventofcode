import math

import numpy as np
import re
import time
from collections import Counter
# import plt function
import matplotlib.pyplot as plt


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()

    # find all galaxy coorinates. Galaxies are '#' in the map

    galaxies = []
    for y in range(lines.__len__()):
        for x in range(lines[0].__len__()):
            if lines[y][x] == '#':
                galaxies.append((x,y))
    n_galaxies = galaxies.__len__()

    # sum of all distances
    sum_distances = 0
    for galaxy in galaxies:
        sum_distances += sum([abs(galaxy[0] - x) + abs(galaxy[1] - y) for x,y in galaxies])
    sum_distances = sum_distances // 2

    # include expansion
    galaxies = sorted(galaxies, key=lambda x: x[1])
    for i in range(lines.__len__()):
        # if line is empty
        if not '#' in lines[i]:
            # count how many are above and how many below
            above = Counter([1 for x,y in galaxies if y > i])
            sum_distances += above[1] * (n_galaxies - above[1])
    # now do the same for the x axis
    galaxies = sorted(galaxies, key=lambda x: x[0])
    for i in range(lines[0].__len__()):
        # if line is empty
        if not '#' in [lines[y][i] for y in range(lines.__len__())]:
            # count how many are above and how many below
            above = Counter([1 for x,y in galaxies if x > i])
            sum_distances += above[1] * (n_galaxies - above[1])

    print(sum_distances)
    return




def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()

    # find all galaxy coorinates. Galaxies are '#' in the map

    galaxies = []
    for y in range(lines.__len__()):
        for x in range(lines[y].__len__()):
            if lines[y][x] == '#':
                galaxies.append((x,y))
    n_galaxies = galaxies.__len__()

    # sum of all distances
    sum_distances = 0
    for galaxy in galaxies:
        sum_distances += sum([abs(galaxy[0] - x) + abs(galaxy[1] - y) for x,y in galaxies])
    sum_distances = sum_distances // 2

    # include expansion
    galaxies = sorted(galaxies, key=lambda x: x[1])
    for i in range(lines.__len__()):
        # if line is empty
        if not '#' in lines[i]:
            # count how many are above and how many below
            above = Counter([1 for x,y in galaxies if y > i])
            sum_distances += above[1] * (n_galaxies - above[1]) * 999999
    # now do the same for the x axis
    galaxies = sorted(galaxies, key=lambda x: x[0])
    for i in range(lines[0].__len__()):
        # if line is empty
        if not '#' in [lines[y][i] for y in range(lines.__len__())]:
            # count how many are above and how many below
            above = Counter([1 for x,y in galaxies if x > i])
            sum_distances += (above[1] * (n_galaxies - above[1])) * 999999

    print(sum_distances)
    return





if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
