import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue

def dijkstra(grid, start, end):
    # priority queue
    pq = queue.PriorityQueue()
    visited = {}
    # start with east:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    pq.put((0, start, (0, 1)))
    visited[(start, (0, 1))] = 0
    pre_vis = {}

    
    while not pq.empty():
        cost, pos, dir = pq.get()
        # if pos == end:
        #     return cost
        # straight
        new_pos = ((pos[0] + dir[0], pos[1] + dir[1]), dir)
        if new_pos not in visited and grid[new_pos[0][0]][new_pos[0][1]] == 0:
            visited[new_pos] = cost + 1
            pq.put((cost + 1, new_pos[0], dir))
            pre_vis[new_pos] = [(pos, dir)]
        elif new_pos in visited and visited[new_pos] == cost + 1:
            pre_vis[new_pos] += [(pos, dir)]
        
        for change_dir in directions:
            if dir == change_dir or dir == (-change_dir[0], -change_dir[1]):
                continue
            new_pos = (pos, change_dir)
            if new_pos not in visited:
                visited[new_pos] = cost + 1000
                pq.put((cost + 1000, new_pos[0], change_dir))
                
                pre_vis[new_pos] = [(pos, dir)]
            elif visited[new_pos] == cost + 1000:
                pre_vis[new_pos] += [(pos, dir)]
    

    dist = min([visited.get((end, dir), math.inf) for dir in directions])
    # get end direction
    end_dirs = [dir for dir in directions if visited.get((end, dir), math.inf) == dist]

    # reconstruct paths, bfs backwards
    fields = set()
    q = queue.Queue()
    for end_dir in end_dirs:
        q.put((end, end_dir))
    while not q.empty():
        pos = q.get()
        fields.add(pos[0])
        if pos[0] == start:
            continue
        for pre_pos in pre_vis[pos]:
            q.put(pre_pos)
    
    print(f"Number of fields on shortest paths: {len(fields)}")

    return dist
        
    


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    grid = [[1 if x == '#' else 0  for x in line.strip()] for line in lines]

    # find E and S
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            if val == 'E':
                E = (i, j)
            if val == 'S':
                S = (i, j)

    # dijkstra
    distance = dijkstra(grid, S, E)


    
    res = distance
    
    # Print result
    print("Answer Part 1:")
    print(res)



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    grid = [[1 if x == '#' else 0  for x in line.strip()] for line in lines]

    # find E and S
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            if val == 'E':
                E = (i, j)
            if val == 'S':
                S = (i, j)

    # dijkstra
    distance = dijkstra(grid, S, E)


    
    res = distance
    
    # Print result
    print("Answer Part 1:")
    print(res)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')