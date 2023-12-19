import math

import numpy as np
import re
import time
from collections import Counter


# import plt function


class visited_class():
    n = 0
    m = 0
    visited = set()

    def __init__(self, grid):
        self.n = grid.__len__()
        self.m = grid[0].__len__()
        self.visited = set()

    def inbounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m

    def visit_vector(self, x, y, dir):
        if not self.inbounds(x, y):
            return True
        if (x, y, dir) in self.visited:
            return True
        else:
            self.visited.add((x, y, dir))
            return False


    def visit(self, next):
        if next.__len__() != 3:
            print('next must be a list of length 3')
            return
        return self.visit_vector(next[0], next[1], next[2])

    def energized(self):
        # return all visited points (without counting directions)
        coordinates = [(x,y) for x,y,dir in self.visited]
        set_coordinates = set(coordinates)
        # print(set_coordinates) in a rectangular grid of size n,m
        # grid = [[0 for i in range(self.m)] for j in range(self.n)]
        # for x,y in set_coordinates:
        #     grid[x][y] = 1
        # for line in grid:
        #     print(line)

        return set_coordinates.__len__()


def bfs(grid, queue, visited):

    while queue:
        curr = queue.pop(0)
        dir = curr[2]
        directions = {
            'r': [1,0],
            'd': [0,1],
            'l': [-1,0],
            'u': [0,-1]
        }
        # get current mirror sign
        mirror = grid[curr[1]][curr[0]]

        # handle mirrors:
        if mirror == '/':
            mirror_slash = {  # '/' mirrors
                'r': 'u',
                'd': 'l',
                'l': 'd',
                'u': 'r'
            }
            dir = mirror_slash[dir]
        elif mirror == '\\':
            mirror_backslash = {  # '\' mirrors
                'r': 'd',
                'd': 'r',
                'l': 'u',
                'u': 'l'
            }
            dir = mirror_backslash[dir]

        # handle splitter:
        if mirror == '|' and dir in ['l','r']:
            dir = 'u'
            next_u = [curr[0] + directions[dir][0], curr[1] + directions[dir][1], dir]
            if not visited.visit(next_u):
                queue.append(next_u)
            dir = 'd'
            next_d = [curr[0] + directions[dir][0], curr[1] + directions[dir][1], dir]
            if not visited.visit(next_d):
                queue.append(next_d)
        elif mirror == '-' and dir in ['u','d']:
            dir = 'r'
            next_r = [curr[0] + directions[dir][0], curr[1] + directions[dir][1], dir]
            if not visited.visit(next_r):
                queue.append(next_r)
            dir = 'l'
            next_l = [curr[0] + directions[dir][0], curr[1] + directions[dir][1], dir]
            if not visited.visit(next_l):
                queue.append(next_l)
        else:
            next = [curr[0] + directions[dir][0], curr[1] + directions[dir][1], dir]
            if not visited.visit(next):
                queue.append(next)

    pass


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # create grid
    grid = [[char for char in line] for line in lines]
    # make sure grid is rectangle
    if not all([len(line) == len(grid[0]) for line in grid]):
        print('Grid is not rectangular')
        return

    # create visited which is 2 times the grid
    visited = visited_class(grid)

    queue = [[0,0,'r']]
    visited.visit(queue[0])

    # run bfs
    bfs(grid, queue, visited)


    print(visited.energized())


    return



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()



    # create grid
    grid = [[char for char in line] for line in lines]
    # make sure grid is recatanble
    if not all([len(line) == len(grid[0]) for line in grid]):
        print('Grid is not rectangular')
        return

    # create visited which is 2 times the grid
    max_energized = 0
    for i in range(grid[0].__len__()):
        visited = visited_class(grid)
        queue = [[i,0,'d']]
        visited.visit(queue[0])

        # run bfs
        bfs(grid, queue, visited)
        max_energized = max(max_energized, visited.energized())
    for i in range(grid[0].__len__()):
        visited = visited_class(grid)
        queue = [[i,grid.__len__()-1,'u']]
        visited.visit(queue[0])

        # run bfs
        bfs(grid, queue, visited)
        max_energized = max(max_energized, visited.energized())
    for i in range(grid.__len__()):
        visited = visited_class(grid)
        queue = [[0,i,'r']]
        visited.visit(queue[0])

        # run bfs
        bfs(grid, queue, visited)
        max_energized = max(max_energized, visited.energized())
    for i in range(grid.__len__()):
        visited = visited_class(grid)
        queue = [[grid[0].__len__()-1,i,'l']]
        visited.visit(queue[0])

        # run bfs
        bfs(grid, queue, visited)
        max_energized = max(max_energized, visited.energized())

    print(max_energized)


    return


if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
