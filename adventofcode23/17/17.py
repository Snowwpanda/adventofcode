import math

import numpy as np
import re
import time
from collections import Counter
# import priority queue
import heapq

# import plt function


class visited_class():
    n = 0
    m = 0
    visited = dict()
    final_dist = -1

    def __init__(self, grid):
        self.n = grid.__len__()
        self.m = grid[0].__len__()
        self.visited = dict()

    def inbounds(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.m

    def visit_vector(self, x, y, dir, dist):
        if not self.inbounds(x, y):
            return False
        if (x, y, dir) in self.visited and self.visited[(x, y, dir)] <= dist:
            return False
        else:
            self.visited[(x, y, dir)] = dist
            if x == self.n-1 and y == self.m-1 and \
                    (self.final_dist == -1 or dist < self.final_dist):
                self.final_dist = dist
            return True


    def visit(self, next):
        if next.__len__() < 4:
            print('next must be a list of length 3')
            return
        return self.visit_vector(next[0], next[1], next[2], next[3])

class my_prio_queue():
    # building my own prio queue, with a simple balanced binary tree, minimum at the root
    queue = []

    def __init__(self):
        self.queue = []

    def push(self, item):
        # add item to the end of the queue and rebalance
        self.queue.append(item)
        self.rebalance(-1)

    def pop(self):
        # mimimum is always first element, replace with last element and rebalance
        minimum = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.queue.pop(-1)
        self.rebalance(0)
        return minimum

    def rebalance(self, index):
        # rebalance, starting at index
        # if index is -1, start at the end
        while index < 0:
            index = self.queue.__len__() + index
        # if it is smaller than the parent swap and rebalance
        if index > 0 and self.queue[index][3] < self.queue[(index-1)//2][3]:
            self.swap(index, (index-1)//2)
            self.rebalance((index-1)//2)
        # if it is larger than the children swap with the smallest child and rebalance
        if index < self.queue.__len__() and (index*2+1 < self.queue.__len__() and self.queue[index][3] > self.queue[index*2+1][3] or index*2+2 < self.queue.__len__() and self.queue[index][3] > self.queue[index*2+2][3]):
            if index*2+2 >= self.queue.__len__() or self.queue[index*2+1][3] < self.queue[index*2+2][3]:
                self.swap(index, index*2+1)
                self.rebalance(index*2+1)
            else:
                self.swap(index, index*2+2)
                self.rebalance(index*2+2)

    def swap(self, index1, index2):
        # swap two elements
        temp = self.queue[index1]
        self.queue[index1] = self.queue[index2]
        self.queue[index2] = temp




def dijkstra(grid, queue, visited, min_max_dist = (1,3)):
    min = min_max_dist[0]
    max = min_max_dist[1]
    while queue:
        curr = queue.pop()
        if curr[0] == visited.n-1 and curr[1] == visited.m-1:
            return
        dir = curr[2]
        directions = {
            'r': [1,0],
            'd': [0,1],
            'l': [-1,0],
            'u': [0,-1]
        }
        if dir in ['r', 'l']:
            next_dir = ['u', 'd']
        else:
            next_dir = ['r', 'l']
        for d in next_dir:
            for i in range(min,max+1):
                if not visited.inbounds(curr[0] + directions[d][0]*i, curr[1] + directions[d][1]*i):
                    continue
                next = [curr[0] + directions[d][0]*i, curr[1] + directions[d][1]*i, d, curr[3] + sum([grid[curr[1] + directions[d][1]*j][curr[0] + directions[d][0]*j] for j in range(1, i+1)])]
                if visited.visit(next):
                    queue.push(next)
    return



def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # create grid
    grid = [[int(num) for num in line] for line in lines]
    # make sure grid is rectangle
    if not all([len(line) == len(grid[0]) for line in grid]):
        print('Grid is not rectangular')
        return
    shortest_dist = math.inf

    # create visited which is 2 times the grid
    visited = visited_class(grid)
    # create a priority queue with the fourth element
    queue = my_prio_queue()
    queue.push([0,0,'r', 0])
    visited.visit( [0,0,'r', 0])
    # run dijkstra
    dijkstra(grid, queue, visited)
    shortest_dist = min(shortest_dist, visited.final_dist)

    # create visited which is 2 times the grid
    visited = visited_class(grid)
    # create a priority queue with the fourth element
    queue = my_prio_queue()
    queue.push([0,0,'d', 0])
    visited.visit([0,0,'d', 0])
    # run dijkstra
    dijkstra(grid, queue, visited)
    shortest_dist = min(shortest_dist, visited.final_dist)




    print(f"Shortest path is {shortest_dist}")

    return



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()


    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # create grid
    grid = [[int(num) for num in line] for line in lines]
    # make sure grid is rectangle
    if not all([len(line) == len(grid[0]) for line in grid]):
        print('Grid is not rectangular')
        return
    shortest_dist = math.inf

    # create visited which is 2 times the grid
    visited = visited_class(grid)
    # create a priority queue with the fourth element
    queue = my_prio_queue()
    queue.push([0,0,'r', 0])
    visited.visit( [0,0,'r', 0])
    # run dijkstra
    dijkstra(grid, queue, visited, (4,10))
    shortest_dist = min(shortest_dist, visited.final_dist)

    # create visited which is 2 times the grid
    visited = visited_class(grid)
    # create a priority queue with the fourth element
    queue = my_prio_queue()
    queue.push([0,0,'d', 0])
    visited.visit([0,0,'d', 0])
    # run dijkstra
    dijkstra(grid, queue, visited, (4,10))
    shortest_dist = min(shortest_dist, visited.final_dist)




    print(f"Shortest path is {shortest_dist}")



    return


if __name__ == '__main__':
    start_time = time.time()
    solveA('test.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
