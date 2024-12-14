import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt

def prod(lst):
    res = 1
    for l in lst:
        res *= l
    return res


def move_robot(robot, t, bounds):
    p = np.array(robot[:2])
    v = np.array(robot[2:])
    new_pos = p + t*v
    while not (0 <= new_pos[0] < bounds[0] and 0 <= new_pos[1] < bounds[1]):
        new_pos[0] = ( new_pos[0] + bounds[0] ) % bounds[0]
        new_pos[1] = ( new_pos[1] + bounds[1] ) % bounds[1]
    return new_pos

def get_quadrant(pos, bounds):
    x = pos[0]
    y = pos[1]
    boundx = bounds[0]
    boundy = bounds[1]

    # check on the line:
    if x == boundx//2 or y == boundy//2:
        return -1

    quadrant = 0
    if x > boundx//2:
        quadrant += 1
    if y > boundy//2:
        quadrant += 2
    
    return quadrant



def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # input: 
    # p=0,4 v=3,-3
    # p=6,3 v=-1,-3

    robots = [[int(x) for x in re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line.strip()).groups()] for line in lines]

    boundx = 101
    boundy = 103
    # boundx = 11
    # boundy = 7

    robots_end = [move_robot(robot, 100, (boundx, boundy)) for robot in robots]

    quadrants = [0,0,0,0]
    for robot_pos in robots_end:
        quadrant = get_quadrant(robot_pos, (boundx, boundy))
        if quadrant != -1:
            quadrants[quadrant] += 1
    

    # product of quadrants
    res = prod(quadrants)
    
    # Print result
    print("Answer Part 1:")
    print(res)

def display_grid(robots, time, bounds):
    robots_end = [move_robot(robot, time, bounds) for robot in robots]
    grid = np.zeros((bounds[1], bounds[0]))
    for robot_pos in robots_end:
        grid[robot_pos[1], robot_pos[0]] = 1
        
    # find anomolies
    if np.sum(grid[:bounds[1]//5, :]) <= 40:
        print(f"Vertical anomolie: {time}")
    elif np.sum(grid[:, :bounds[0]//5]) <= 40:
        print(f"Horizontal anomolie: {time}")
    else:
        return
    plt.ion()
    plt.imshow(grid)
    plt.show()
    plt.pause(0.01)
    plt.clf()
    # Vertical: 30
    # Horizontal: 81
    # Vertical: 133
    # Horizontal: 182
    # Vertical: 236
    # Horizontal: 283


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    robots = [[int(x) for x in re.match(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', line.strip()).groups()] for line in lines]

    boundx = 101
    boundy = 103
    # boundx = 11
    # boundy = 7


    plt.figure()

    # for time in range(10000):
    #     display_grid(robots, time, (boundx, boundy))
    #     # print(time)
    
    # calculate overlap: 30 + x*103 and 81 + y*101
    time = ( 101 + (81-30) ) // 2 * 103 + 30

    display_grid(robots, time, (boundx, boundy))

    # product of quadrants
    res = 0


    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')