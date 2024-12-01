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


def inbounds(grid, neighbor):
    return neighbor[0] >= 0 and neighbor[0] < len(grid) and neighbor[1] >= 0 and neighbor[1] < len(grid[0])


def get_neighbors(grid, current):
    directions = {
        '>': (0, 1, '<'),
        '<': (0, -1, '>'),
        '^': (-1, 0, 'v'),
        'v': (1, 0, '^')
    }
    neighbors = []
    for direction in directions:
        if directions[direction][2] == current[2]:
            continue
        neighbor = (current[0] + directions[direction][0], current[1] + directions[direction][1], direction)
        if inbounds(grid, neighbor) and (grid[neighbor[0]][neighbor[1]] == '.' or grid[neighbor[0]][neighbor[1]] == direction):
            neighbors.append(neighbor)
    return neighbors


def bfs_longest_path(grid, start, end):
    longest_path = 0
    queue = [[start, 0]]
    visited = set(start)

    visual = np.zeros((len(grid), len(grid[0])), dtype=int)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                visual[i][j] = 1
    visual[start[0]][start[1]] =  2
    while queue:
        [current, distance] = queue.pop(0)
        visual[current[0]][current[1]] = 0
        for neighbor in get_neighbors(grid, current):
            if neighbor == end:
                longest_path = max(longest_path, distance+1)
            visited.add(neighbor)
            queue.append([neighbor, distance + 1])
            visual[neighbor[0]][neighbor[1]] = 2
    return longest_path





def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # read in grid:
    grid = [ list(line) for line in lines ]

    start = (0,1, 'v')
    end = (len(lines)-1, len(lines[0])-2, 'v')

    longest_path = bfs_longest_path(grid, start, end)

    print(f"longest path: {longest_path}")



    return


def calculate_dist(path, dist_map):
    dist = 0
    for i in range(len(path)-1):
        dist += dist_map[(path[i], path[i+1])]
    return dist


def visualize_grid(grid, plt):

    def update_grid(grid, step):
        update_plot(grid)

    current_step = 0
    # grid = np.zeros((200, 200))

    thread = threading.Thread(target=update_plot, args=(grid, plt))
    return thread


def dfs_longest_path(grid, start, end, crossings, dist_map):
    longest_path = 0
    adj_list = {}
    for crossing in crossings:
        adj_list[crossing] = []
    for crossing in crossings:
        for neighor in crossings:
            if (crossing, neighor) in dist_map:
                adj_list[crossing].append([neighor, dist_map[(crossing, neighor)]])

    path = [start]
    path_children = []
    next_child = 0
    path_children.append(next_child)
    visited = set()
    visited.add(start)
    dist = adj_list[start][0][1]
    visualize = np.zeros((len(grid), len(grid[0])), dtype=int)

    # open new window with visualization of with visualize


    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                visualize[i][j] = 1
    visualize[start[0]][start[1]] = 2


    while path:
        continue_path = False
        while not continue_path and path:
            children = adj_list[path[-1]]
            for i in range(next_child, len(children)):
                if children[i][0] not in visited:
                    visited.add(children[i][0])
                    path.append(children[i][0])
                    visualize[children[i][0][0]][children[i][0][1]] = 2
                    path_children.append(i)
                    next_child = 0
                    continue_path = True
                    break
            if not continue_path:
                if path[-1] == end:
                    longest_path = max(longest_path, calculate_dist(path, dist_map))
                visualize[path[-1][0]][path[-1][1]] = 0
                visited.remove(path.pop(-1))
                next_child = path_children.pop(-1) + 1

    return longest_path









def get_crossings(grid):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    crossings = []
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[0])-1):
            # empty neighbors
            sum = 0
            for dir in directions:
                if grid[i+dir[0]][j+dir[1]] != '#':
                    sum += 1
            if sum > 2:
                crossings.append((i,j))
    return crossings


def get_neighbors_b(grid, current):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dir in directions:
        neighbor = (current[0] + dir[0], current[1] + dir[1])
        if inbounds(grid, neighbor) and grid[neighbor[0]][neighbor[1]] != '#':
            neighbors.append(neighbor)
    return neighbors


def get_dist_map(grid, crossings):
    d_map = {}
    for crossing in crossings:
        queue = [[crossing, 0]]
        visited = set(crossing)
        while queue:
            current, distance = queue.pop(0)
            for neighbor in get_neighbors_b(grid, current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    if neighbor in crossings:
                        d_map[(crossing, neighbor)] = distance + 1
                    else:
                        queue.append([neighbor, distance + 1])
    return d_map



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

        # read in grid:
        grid = [list(line) for line in lines]

        start = (0, 1)
        end = (len(lines) - 1, len(lines[0]) - 2)
        crossings = get_crossings(grid)
        crossings.append(start)
        crossings.append(end)
        dist_map = get_dist_map(grid, crossings)

        longest_path = dfs_longest_path(grid, start, end, crossings, dist_map)


    print(f"longest path: {longest_path}")

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
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
