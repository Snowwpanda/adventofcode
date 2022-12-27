import re
import numpy as np
from functools import cmp_to_key
import sys


def parse_line(line):
    robots = []
    for type in ['ore', 'clay', 'obsidian', 'geode']:
        robot = re.search(f'Each {type} robot costs ((\d+) ore)?( and )?((\d+) clay)?( and )?((\d+) obsidian)?', line).groups()
        rVector = []
        for i in [1,4,7]:
            if robot[i] is None:
                rVector.append(0)
            else:
                rVector.append(int(robot[i]))
        robots.append(np.array([0,0,0,0] + rVector + [0]))
    return robots


def calculate_geodes(robot_costs):
    start = [np.array([1,0,0,0,0,0,0,0])]
    for i in range(23):
        set = []
        for vector in start:
            if vector[0] < np.max(robot_costs[1:], axis= 0)[4] or vector[4] < robot_costs[1][4]:
                robot = robot_costs[0]
                if robot[4] <= vector[4]:
                    next = vector.copy()
                    next[4:] += vector[:4]
                    next = next - robot
                    next[0] += 1
                    set = set + [next]
                else:
                    next = vector.copy()
                    next[4:] += vector[:4]
                    set = set + [next]
            else:
                for j in range(1,4):
                    robot = robot_costs[j]
                    if robot[4] <= vector[4] and robot[5] <= vector[5] and robot[6] <= vector[6]:
                        next = vector.copy()
                        next[4:] += vector[:4]
                        next = next - robot
                        next[j] += 1
                        set = set + [next]
        start = set
    geodes = np.max(start, axis= 0)[7]
    return geodes




def solveA(file_name):

    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    max_geodes = 0
    for i in range(1,len(lines)+1):
        line = lines[i-1]
        robot_costs = parse_line(line)
        max_geodes += i * calculate_geodes(robot_costs)
        print(f'{i} {calculate_geodes(robot_costs)}')
    print('max possivle geodes:')
    print(max_geodes)



def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        print('free sides')


if __name__ == '__main__':
    solveA('test.txt')

    solveB('input.txt')
