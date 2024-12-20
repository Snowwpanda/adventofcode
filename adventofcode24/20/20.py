import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue

def in_bounds(i, j, grid):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

def cheat_bfs(grid, start, end, max_dist):
    q = queue.Queue()
    q.put((*start, False))
    dist = {(*start, False): 0}
    while not q.empty():
        i, j, cheated = q.get()
        if dist[(i, j, cheated)] > max_dist:
            continue
        if (i, j) == end:
            print(dist[(i, j, cheated)], cheated)
            if cheated == False:
                return dist
            continue
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if grid[ni][nj] == 0:
                if (ni, nj, cheated) not in dist:
                    dist[(ni, nj, cheated)] = dist[(i, j, cheated)] + 1
                    q.put((ni, nj, cheated))
        
        if not cheated:
            #check dist for cheats:
            if i > 1 and grid[i-1][j] == 1:
                for di, dj in [(-1, 1), (-1, -1), (-2, 0)]:
                    ni, nj = i + di, j + dj
                    if grid[ni][nj] == 0 and (ni, nj, (i, j, ni, nj)) not in dist:
                        dist[(ni, nj, (i, j, ni, nj))] = dist[(i, j, False)] + 2
                        q.put((ni, nj, (i, j, ni, nj)))
            if i < len(grid) - 2 and grid[i+1][j] == 1:
                for di, dj in [(1, 1), (1, -1), (2, 0)]:
                    ni, nj = i + di, j + dj
                    if grid[ni][nj] == 0 and (ni, nj, (i, j, ni, nj)) not in dist:
                        dist[(ni, nj, (i, j, ni, nj))] = dist[(i, j, False)] + 2
                        q.put((ni, nj, (i, j, ni, nj)))
            if j > 1 and grid[i][j-1] == 1:
                for di, dj in [(0, -2)]:
                    ni, nj = i + di, j + dj
                    if grid[ni][nj] == 0 and (ni, nj, (i, j, ni, nj)) not in dist:
                        dist[(ni, nj, (i, j, ni, nj))] = dist[(i, j, False)] + 2
                        q.put((ni, nj, (i, j, ni, nj)))
            if j < len(grid[0]) - 2 and grid[i][j+1] == 1:
                for di, dj in [(0, 2)]:
                    ni, nj = i + di, j + dj
                    if grid[ni][nj] == 0 and (ni, nj, (i, j, ni, nj)) not in dist:
                        dist[(ni, nj, (i, j, ni, nj))] = dist[(i, j, False)] + 2
                        q.put((ni, nj, (i, j, ni, nj)))
                        
                        

def bfs_map(grid, start, max_dist):
    q = queue.Queue()
    q.put(start)
    dist = {start: 0}
    while not q.empty():
        i, j = q.get()
        if dist[(i, j)] > max_dist - 100:
            return dist
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if grid[ni][nj] == 0:
                if (ni, nj) not in dist:
                    dist[(ni, nj)] = dist[(i, j)] + 1
                    q.put((ni, nj))




def bfs(grid, start, end):
    q = queue.Queue()
    q.put(start)
    dist = {start: 0}
    while not q.empty():
        i, j = q.get()
        if (i, j) == end:
            return dist[(i, j)]
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i + di, j + dj
            if grid[ni][nj] == 0:
                if (ni, nj) not in dist:
                    dist[(ni, nj)] = dist[(i, j)] + 1
                    q.put((ni, nj))

def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    grid = [[1 if x == '#' else 0 for x in line.strip()] for line in lines]


    # find s and e
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
            if c == 'E':
                end = (i, j)

    # BFS from s

    no_cheat = bfs(grid, start, end)

    all_dist_from_start = bfs_map(grid, start, end)
    
    all_dist_from_end = bfs_map(grid, end, start)

    # visualize


    count = 0
    for key, value in all_dist_from_start.items():
        for dir in [(2, 0), (1,1), (0, 2), (-1, 1), (-2, 0), (-1, -1), (0, -2), (1, -1)]:
            new_key = (key[0] + dir[0], key[1] + dir[1])
            if new_key in all_dist_from_end and all_dist_from_end[new_key] + value + 2 <= no_cheat - 100 :
                count += 1
            

    
    res = count

    
    # Print result
    print("Answer Part 1:")
    print(res)





def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()



    grid = [[1 if x == '#' else 0 for x in line.strip()] for line in lines]


    # find s and e
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == 'S':
                start = (i, j)
            if c == 'E':
                end = (i, j)

    # BFS from s

    no_cheat = bfs(grid, start, end)

    all_dist_from_start = bfs_map(grid, start, no_cheat)
    
    all_dist_from_end = bfs_map(grid, end, no_cheat)

    # visualize

    dist_20 = [((dx, dy), (abs(dx) + abs(dy))) for dx in range(-20, 21) for dy in range(-20, 21) if abs(dx) + abs(dy) <= 20]

    count = 0
    for key_s, value_s in all_dist_from_start.items():
        for cheat, len in dist_20:
            key_e = (key_s[0] + cheat[0], key_s[1] + cheat[1])
            if key_e in all_dist_from_end and all_dist_from_end[key_e] + value_s + len <= no_cheat - 100:
                count += 1
            

    
    res = count

    # Print result
    print("Answer Part 1:")
    print(res)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')