import math

import numpy as np
import re
import time
from collections import Counter
# import plt function
import matplotlib.pyplot as plt

def map_notes_to_pipedirections(letter):
    # possible pipes are |-LFJ7 and .
    # give back directions in the form (1,1,0,0) where the ones stand for the connections, in the order up, right, down, left
    map = {
        '|': (1,0,1,0),
        '-': (0,1,0,1),
        'L': (1,1,0,0),
        'F': (0,1,1,0),
        'J': (1,0,0,1),
        '7': (0,0,1,1),
        '.': (0,0,0,0)
    }
    return map[letter]

def inbounds(x,y, bounds):
    return not (x < 0 or y < 0 or x >= bounds[0] or y >= bounds[1])


def next_position(right, next_right, lines, bounds):

    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    # check in bounds
    if not inbounds(right[0] + directions[next_right][0], right[1] + directions[next_right][1], bounds):
        print("out of bounds")
        return None, None
    # get next direction
    next_pos = (right[0] + directions[next_right][0], right[1] + directions[next_right][1])
    next_pos_pipe = lines[bounds[1] - next_pos[1] -1][next_pos[0]]
    for i in range(4):
        if map_notes_to_pipedirections(next_pos_pipe)[i] == 1 and i != (next_right + 2) % 4:
            return next_pos, i



def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    bounds = ( lines[0].__len__()-1, lines.__len__())     # because of the \n


    # find coordinates of 'S'
    for i in range(lines.__len__()):
        if "S" in lines[i]:
            start = (lines[i].index('S'), lines.__len__() - i - 1)
            break

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    starting_pipe = [0,0,0,0]
    for direction in directions:
        # check in bounds
        if not inbounds(start[0] + direction[0], start[1] + direction[1], bounds):
            continue

        adjacent_pipe = lines[bounds[1] - start[1] - direction[1] -1][start[0] + direction[0]]
        pipe = map_notes_to_pipedirections(adjacent_pipe)
        back_index = (directions.index(direction) + 2) % 4
        if pipe[back_index] == 1:
            starting_pipe[directions.index(direction)] = 1

    # now we have the starting pipe, we can start the search
    # Lets assume that the loop has even length
    right = start
    left = start
    next_right = 0
    next_left = 3
    # right is the first one in starting_pipe and left is the last one
    for i in range(4):
        if starting_pipe[i] == 1:
            next_right = i
            break
    for i in range(4):
        if starting_pipe[i] == 1:
            next_left = i

    right, next_right = next_position(right, next_right, lines, bounds)
    left, next_left = next_position(left, next_left, lines, bounds)

    coutner = 1
    while right != left:
        print(f"right: {right}, left: {left}")
        right, next_right = next_position(right, next_right, lines, bounds)
        left, next_left = next_position(left, next_left, lines, bounds)
        coutner += 1
        if right == None or left == None:
            print("No solution")
            return

    # print solution and counter of solution
    print(f"Farthest square {right} is at distance {coutner}")



    return




def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    bounds = ( lines[0].__len__()-1, lines.__len__())     # because of the \n


    # find coordinates of 'S'
    for y in range(lines.__len__()):
        if "S" in lines[y]:
            start = (lines[y].index('S'), lines.__len__() - y - 1)
            break

    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    starting_pipe = [0,0,0,0]
    for direction in directions:
        # check in bounds
        if not inbounds(start[0] + direction[0], start[1] + direction[1], bounds):
            continue

        adjacent_pipe = lines[bounds[1] - start[1] - direction[1] -1][start[0] + direction[0]]
        pipe = map_notes_to_pipedirections(adjacent_pipe)
        back_index = (directions.index(direction) + 2) % 4
        if pipe[back_index] == 1:
            starting_pipe[directions.index(direction)] = 1

    # now we have the starting pipe, we can start the search
    # Lets assume that the loop has even length
    right = start
    left = start
    next_right = 0
    next_left = 3
    # right is the first one in starting_pipe and left is the last one
    for y in range(4):
        if starting_pipe[y] == 1:
            next_right = y
            break
    for y in range(4):
        if starting_pipe[y] == 1:
            next_left = y

    right, next_right = next_position(right, next_right, lines, bounds)
    left, next_left = next_position(left, next_left, lines, bounds)

    # create a grid with the loop
    grid = [[0 for i in range(bounds[0])] for j in range(bounds[1])]
    grid[bounds[1] - right[1] - 1][right[0]] = 1
    grid[bounds[1] - left[1] - 1][left[0]] = 1
    grid[bounds[1] - start[1] - 1][start[0]] = 1

    while right != left:
        print(f"right: {right}, left: {left}")
        right, next_right = next_position(right, next_right, lines, bounds)
        left, next_left = next_position(left, next_left, lines, bounds)
        grid[bounds[1] - right[1] - 1][right[0]] = 1
        grid[bounds[1] - left[1] - 1][left[0]] = 1

    # now check for each position if inside the loop or outside the loop
    inside_counter = 0
    for y in range(bounds[1]):
        # default outside the loop
        inside = False
        for x in range(bounds[0]):
            if grid[bounds[1] - y - 1][x] == 1:
                # if we cross then we switch from outside to inside or vice versa, assuming we are in the bottom left of a field
                if lines[bounds[1] - y - 1][x] in ['|', 'F', '7']:
                    inside = not inside
                continue
            else:
                if inside:
                    grid[bounds[1] - y - 1][x] = 2
                    inside_counter += 1
                    continue

    print(f"Inside the loop there are {inside_counter} squares")




    return



if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
