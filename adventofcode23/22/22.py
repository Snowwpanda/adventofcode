import math

import numpy as np
import re
import time
from collections import Counter
# import priority queue
import heapq

# import plt function


def brick_fall(b_n, bricks, grid):
    brick = bricks[b_n]
    # vertical brick (z start != z end)
    if brick[0][2] != brick[1][2]:
        # find lowest point
        bottom = (brick[0][0], brick[0][1], min(brick[0][2], brick[1][2]))
        below = bottom
        while below[2] > 1 and grid[below[0]][below[1]][below[2]-1] == -1:
            below = (below[0], below[1], below[2]-1)
        # update grid
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    grid[i][j][k] = -1
        if below != bottom:
            # move brick to lowest point
            brick[1][2] = below[2] + abs(brick[1][2] - brick[0][2])
            brick[0][2] = below[2]
        # update grid
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    grid[i][j][k] = b_n
        above = bottom - brick[0] + brick[1] + np.array((0, 0, 1))
        # check if brick was supporting another brick
        if grid[above[0]][above[1]][above[2]] != -1:
            brick_fall(grid[above[0]][above[1]][above[2]], bricks, grid)
    else: # horizontal brick (z start == z end)
        if brick[0][2]  == 1:
            return
        # check if free
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                if grid[i][j][brick[0][2]-1] != -1:
                    return

        # check if brick was supporting another brick
        set_above = set()
        for i in range(brick[0][0], brick[1][0] + 1):
            for j in range(brick[0][1], brick[1][1] + 1):
                if grid[i][j][brick[0][2] + 1] != -1:
                    set_above.add(grid[i][j][brick[0][2] + 1])
        # update grid
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    grid[i][j][k] = -1
        # move brick down
        brick[0] = np.array((brick[0][0], brick[0][1], brick[0][2]-1))
        brick[1] = np.array((brick[1][0], brick[1][1], brick[1][2]-1))
        # update grid
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    grid[i][j][k] = b_n
        # fall again if needed
        brick_fall(b_n, bricks, grid)
        # fall all supported bricks
        for sup_b_n in set_above:
            brick_fall(sup_b_n, bricks, grid)


def support_of(b_n, bricks, grid):
    support = set()
    brick = bricks[b_n]
    # vertical brick (z start != z end)
    if brick[0][2] != brick[1][2]:
        if grid[brick[0][0]][brick[0][1]][min(brick[0][2], brick[1][2])-1] != -1:
            support.add(grid[brick[0][0]][brick[0][1]][min(brick[0][2], brick[1][2])-1])
    else: # horizontal brick (z start == z end)
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                if grid[i][j][brick[0][2]-1] != -1:
                    support.add(grid[i][j][brick[0][2]-1])
    return support


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # each line is a brick, number of brick is number of line
    # bricks are given in the form x,y,z~x,y,z forming start and end points
    # simultaneousls get max x, y, z
    max_xyz = [0, 0, 0]
    bricks = []
    for line in lines:
        brick = []
        for point in line.split('~'):
            brick.append(np.array([int(x) for x in point.split(',')]))
        bricks.append(brick)
        max_xyz = [max(max_xyz[i], max(brick[0][i], brick[1][i]))  for i in range(3)]



    # create 3d grid of bricks (np array)
    grid = np.zeros((max_xyz[0]+2, max_xyz[1]+2, max_xyz[2]+2), dtype=int) -1
    # fill grid with bricks
    for b_n in range(len(bricks)):
        brick = bricks[b_n]
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    grid[i][j][k] = b_n

    # let bricks fall
    for b_n in range(len(bricks)):
        brick_fall(b_n, bricks, grid)

    # map out supported bricks
    supported_by = []
    for b_n in range(len(bricks)):
        supported_by.append(support_of(b_n, bricks, grid))

    # start with set of all bricks
    disintegrateable = set(range(len(bricks)))
    # remove bricks that are solo supportive
    for b_n in range(len(bricks)):
        if len(supported_by[b_n]) == 1:
            # remove if still contained in disintegrateable
            support = list(supported_by[b_n])[0]
            if support in disintegrateable:
                disintegrateable.remove(support)

    # we can disintegrate bricks that are supported by only one brick
    print(f"Amount of bricks that can be disintegrated: {len(disintegrateable)}")

    # 467 too low

    return


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # each line is a brick, number of brick is number of line
    # bricks are given in the form x,y,z~x,y,z forming start and end points
    # simultaneousls get max x, y, z
    max_xyz = [0, 0, 0]
    bricks = []
    for line in lines:
        brick = []
        for point in line.split('~'):
            brick.append(np.array([int(x) for x in point.split(',')]))
        bricks.append(brick)
        max_xyz = [max(max_xyz[i], max(brick[0][i], brick[1][i]))  for i in range(3)]



    # create 3d grid of bricks (np array)
    grid = np.zeros((max_xyz[0]+2, max_xyz[1]+2, max_xyz[2]+2), dtype=int) -1
    # fill grid with bricks
    for b_n in range(len(bricks)):
        brick = bricks[b_n]
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                for k in range(brick[0][2], brick[1][2]+1):
                    grid[i][j][k] = b_n

    # let bricks fall
    for b_n in range(len(bricks)):
        brick_fall(b_n, bricks, grid)

    # map out supported bricks
    supported_by = []
    for b_n in range(len(bricks)):
        supported_by.append(support_of(b_n, bricks, grid))

    # start with set of all bricks
    disintegrateable = set(range(len(bricks)))
    # remove bricks that are solo supportive
    for b_n in range(len(bricks)):
        if len(supported_by[b_n]) == 1:
            # remove if still contained in disintegrateable
            support = list(supported_by[b_n])[0]
            if support in disintegrateable:
                disintegrateable.remove(support)


    # n**2 algorithm to find the root of disintegratable tree und count the subtree
    reverse_supported_by = [set() for b_n in range(len(bricks))]
    for b_n in range(len(bricks)):
        for support in supported_by[b_n]:
            reverse_supported_by[support].add(b_n)

    chain_reaction = [set([b_n]) for b_n in range(len(bricks))]
    for b_n in range(len(bricks)):
        # calculate chain reaction for brick b_n
        changed = True
        while changed:
            changed = False
            for above_brick in range(len(bricks)):
                if above_brick not in chain_reaction[b_n] and all([sup in chain_reaction[b_n] for sup in supported_by[above_brick]]) and supported_by[above_brick].__len__() >= 1:
                    chain_reaction[b_n].add(above_brick)
                    changed = True

    # get max chain reaction
    sum_chain_reaction = 0
    for b_n in range(len(bricks)):
        sum_chain_reaction += chain_reaction[b_n].__len__() -1
    print(f"Sum chain reaction: {sum_chain_reaction}")
    return


if __name__ == '__main__':
    # time the solution:
    start_time = time.time()
    solveA('test.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
