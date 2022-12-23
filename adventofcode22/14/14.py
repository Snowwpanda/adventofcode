import re
import numpy as np
from functools import cmp_to_key


def solveA(file_name):

    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        lines = [[[int(number) for number in pair.split(',')] for pair in line.strip().split(' -> ')] for line in lines]
        maxN = max([max([max(pair) for pair in line]) for line in lines])

        grid = np.zeros([2*maxN+3,maxN+3])

        for line in lines:
            start = line[0]
            for next in line[1:]:
                if start[0] != next[0]:
                    for i in np.arange(start[0], next[0]+np.sign(next[0]-start[0]), np.sign(next[0]-start[0])):
                        grid[i,start[1]] = 2
                elif start[1] != next[1]:
                    for j in np.arange(start[1], next[1]+np.sign(next[1]-start[1]), np.sign(next[1]-start[1])):
                        grid[start[0],j] = 2
                start = next

        total_sand = drop_sand(grid, [500,0])

        print(total_sand)
        print(np.count_nonzero(grid == 1))
                    







def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..

        with open(file_name) as my_file:
            ## too lazy for asserting..
            lines = my_file.readlines()
            lines = [[[int(number) for number in pair.split(',')] for pair in line.strip().split(' -> ')] for line in
                     lines]
            maxY = max([max([pair[1] for pair in line]) for line in lines])

            grid = np.zeros([maxY + 502, maxY + 2])

            for line in lines:
                start = line[0]
                for next in line[1:]:
                    if start[0] != next[0]:
                        for i in np.arange(start[0], next[0] + np.sign(next[0] - start[0]),
                                           np.sign(next[0] - start[0])):
                            grid[i, start[1]] = 2
                    elif start[1] != next[1]:
                        for j in np.arange(start[1], next[1] + np.sign(next[1] - start[1]),
                                           np.sign(next[1] - start[1])):
                            grid[start[0], j] = 2
                    start = next

            total_sand = drop_sand_bottom(grid, [500, 0])

            print(total_sand)
            print(np.count_nonzero(grid == 1))


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
