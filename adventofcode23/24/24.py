import math

import numpy as np
import re
from collections import Counter
# import priority queue
import heapq
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import threading
import time

# import plt function


def parallel(vel1, vel2):
    x1, y1 = vel1[0], vel1[1]
    x2, y2 = vel2[0], vel2[1]
    return x1 * y2 == x2 * y1


def calcluate_intersection(pos1, vel1, pos2, vel2):
    t1 = ((pos2[0]-pos1[0] ) * vel2[1] - (pos2[1]-pos1[1]) * vel2[0] ) /  (vel1[0] * vel2[1] - vel1[1] * vel2[0])
    t2 = ((pos2[0]-pos1[0] ) * vel1[1] - (pos2[1]-pos1[1]) * vel1[0] ) /  (vel1[0] * vel2[1] - vel1[1] * vel2[0])
    intersection = [pos1[0] + t1 * vel1[0], pos1[1] + t1 * vel1[1]]
    return intersection, t1, t2


def check_if_intersect(hailstrom1, hailstrom2, min_max_x, min_max_y, max_time):
    pos1, vel1 = hailstrom1
    pos2, vel2 = hailstrom2
    # check if vel1 and vel2 are parallel (actually not covering case where they are opposite directions)
    if parallel(vel1, vel2):
        return False
    # check if they intersect
    dist_12 = [pos2[0] - pos1[0], pos2[1] - pos1[1]]
    # if not parallel(dist_12, vel_21):
    #     return False
    intersection, t1, t2 = calcluate_intersection(pos1, vel1, pos2, vel2)
    if t1 < 0 or t2 < 0:
        return False

    # check if intersection is in the test area
    if intersection[0] < min_max_x[0] or intersection[0] > min_max_x[1]:
        return False
    if intersection[1] < min_max_y[0] or intersection[1] > min_max_y[1]:
        return False

    return True

def intersection_in_testarea(hailstormes, min_max_x, min_max_y, max_time):
    count = 0
    n_hailstormes = len(hailstormes)
    for i in range(n_hailstormes):
        for j in range(i+1, n_hailstormes):
            # check if they intersect
            hailstrom1 = hailstormes[i]
            hailstrom2 = hailstormes[j]
            # check if they intersect
            do_intersect = check_if_intersect(hailstrom1, hailstrom2, min_max_x, min_max_y, max_time)
            if do_intersect:
                count += 1
    return count



def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    hailstormes = []
    for line in lines:
        # hailstorm is of the form 19, 13, 30 @ -2,  1, -2 where these are position and velocity
        pos, vel = line.split('@')
        pos = [int(x.strip()) for x in pos.split(',')]
        vel = [int(x.strip()) for x in vel.split(',')]
        hailstormes.append([pos, vel])

    # min_max_x = (7, 27)
    # min_max_y = (7, 27)
    min_max_x = (200000000000000, 400000000000000)
    min_max_y = (200000000000000, 400000000000000)
    max_time = 1000
    collisions = intersection_in_testarea(hailstormes, min_max_x, min_max_y, max_time)

    print(f"collisions: {collisions}")

    return


def scalarproduct(v1, v2):
    # 3d scalar product
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2]*v2[2]


def crossproduct(v1, v2):
    # 3d cross product
    return [v1[1] * v2[2] - v1[2] * v2[1],
            v1[2] * v2[0] - v1[0] * v2[2],
            v1[0] * v2[1] - v1[1] * v2[0]]

def difference(v1, v2):
    return [v1[0]-v2[0], v1[1]-v2[1], v1[2]-v2[2]]

def norm(v):
    return math.sqrt(scalarproduct(v, v))


def distance_between_2(hailstrom1, hailstrom2):
    pos1, vel1 = hailstrom1
    pos2, vel2 = hailstrom2
    dist = abs(scalarproduct(crossproduct(vel1, vel2), difference(pos1,pos2))  / (norm(crossproduct(vel1, vel2))))
    # distance_between_2([[19,13, 30], [18,19,22]], [[20,25,34],[-2,-2,-4]])
    return dist


def get_point(hailstrom2, t2):
    return [hailstrom2[0][0] + t2 * hailstrom2[1][0], hailstrom2[0][1] + t2 * hailstrom2[1][1], hailstrom2[0][2] + t2 * hailstrom2[1][2]]


def estimate_t2_log(start, hailstrom2, hailstrom3):
    step = 1
    t2 = 0
    next_hail = get_point(hailstrom2, t2)
    dist = distance_between_2([start, next_hail], [hailstrom3[0], hailstrom3[1]])
    while dist > 4:
        t2 += step
        next_hail2 = get_point(hailstrom2, t2)
        dist2 = distance_between_2([start, next_hail2], [hailstrom3[0], hailstrom3[1]])
        if dist2 < dist:
            dist = dist2
            next_hail = next_hail2
            step *= 2
        elif dist2 > dist:
            t2 -= step
            step /= 2
        elif dist2 == dist:
            return -1

    return t2


def triangulate_with_3(hailstormes):
    # look at hailstormes 0, 1, 2, 3
    hailstrom1 = hailstormes[0]
    hailstrom2 = hailstormes[1]
    hailstrom3 = hailstormes[2]
    hailstrom4 = hailstormes[3]
    # start with first hailstorm and take any starting point (1000 intervals)
    # then try to estimate the second velocity to get to the second hailstorm
    for t1 in range(0,100000, 1000):
        start = [hailstrom1[0][0] + t1 * hailstrom1[1][0], hailstrom1[0][1] + t1 * hailstrom1[1][1], hailstrom1[0][2] + t1 * hailstrom1[1][2]]
        t2 = estimate_t2_log(start, hailstrom2, hailstrom3)
        if t2 < 0:
            continue
        



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    hailstormes = []
    for line in lines:
        # hailstorm is of the form 19, 13, 30 @ -2,  1, -2 where these are position and velocity
        pos, vel = line.split('@')
        pos = [int(x.strip()) for x in pos.split(',')]
        vel = [int(x.strip()) for x in vel.split(',')]
        hailstormes.append([pos, vel])

    # try to triangulate with 3
    triangulate_with_3(hailstormes)



    print(f"Find rock trajectory")

    # longest path: 6542
    # B: --- 1279.6866073608398 seconds ---

    return


if __name__ == '__main__':
    # time the solution:
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('test.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
