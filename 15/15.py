import queue
import numpy as np
from collections import deque


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    f.close()
    return data


def get_neighbors(point):
    x = point[0]
    y = point[1]
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]


def level(point, data):
    return data[point[0]][point[1]]


def in_grid(point, width, height):
    if 0 <= point[0] < height and 0 <= point[1] < width:
        return True
    else:
        return False

def dikstra(data):
    q = queue.PriorityQueue()
    q.put((0, (0, 0)))

    width = len(data[0])
    height = len(data)
    vis = set()
    dist = 0
    while not q.empty():
        (dist, point) = q.get()
        if point in vis:
            continue
        if point == (height - 1, width - 1):
            break
        vis.add(point)
        neigh_list = get_neighbors(point)
        if dist == 448:
            pass
        for neighbor in neigh_list:
            if (neighbor not in vis) and in_grid(neighbor, width, height):
                q.put((dist + level(neighbor, data), neighbor))
    return dist

def task15():
    data = read_input()
    data = np.array([[int(char) for char in line] for line in data])
    dist = dikstra(data)
    print(dist)
    write_sol(dist, 1)

    data = np.array([[n + i  for i in range(5) for n in line ]for line in data])
    data = np.array([line for i in range(5) for line in data + i* np.ones((100,500), dtype=int) ])
    data = np.array([[((i-1 )% 9) + 1 for i in line] for line in data])


    dist = dikstra(data)
    print(dist)
    write_sol(dist, 2)


task15()
