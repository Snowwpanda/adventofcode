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


def calc_path(prev, start, end):
    path = [end]
    while path[-1] != start:
        path.append(prev[path[-1]])
    path.reverse()
    return path


def bfs(start, end, nodes, adj_list, weights):

    queue = [start]
    prev = {}
    visited = set(start)
    while queue:
        current = queue.pop(0)
        for neighbor in adj_list[current]:
            if weights[(current, neighbor)] == 0:
                if neighbor == end:
                    prev[neighbor] = current
                    queue = []
                    break
                if neighbor not in visited:
                    visited.add(neighbor)
                    prev[neighbor] = current
                    queue.append(neighbor)

    if end not in prev:
        print("no path")
        return 0

    path = calc_path(prev, start, end)

    for i in range(len(path)-1):
        if weights[(path[i+1], path[i])] == 0:
            weights[(path[i], path[i+1])] = 1
        else:
            weights[(path[i+1], path[i])] = 0

    return 1


def find_compontent(start, weights, adj_list, nodes):
    queue = [start]
    visited = set([start])
    while queue:
        current = queue.pop(0)
        for neighbor in adj_list[current]:
            if weights[(current, neighbor)] == 0:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return visited


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # edges of the form node: node node node
    adj_list = {}
    for line in lines:
        node, neighbors = line.split(': ')
        neighbors = neighbors.split()
        for neighbor in neighbors:
            if node in adj_list:
                adj_list[node].append(neighbor)
            else:
                adj_list[node] = [neighbor]
            if neighbor in adj_list:
                adj_list[neighbor].append(node)
            else:
                adj_list[neighbor] = [node]

    nodes = list(adj_list.keys())
    nodes.sort()

    weights = {}
    for node in nodes:
        for neighbor in adj_list[node]:
            weights[(node, neighbor)] = 0

    # try a flow from nodes[0] to nodes[-1]
    start = nodes[0]
    end = nodes[-1]

    # find cut of size 3
    for node in nodes[1:]:
        end = node
        bfs(start, end, nodes, adj_list, weights)
        bfs(start, end, nodes, adj_list, weights)
        bfs(start, end, nodes, adj_list, weights)
        cut4 = bfs(start, end, nodes, adj_list, weights)
        if cut4 == 0:
            print(f"found cut of size 3 {start} to {end}")
            break
        else:
            # reset weights:
            for node in nodes:
                for neighbor in adj_list[node]:
                    weights[(node, neighbor)] = 0

    component = find_compontent(start, weights, adj_list, nodes)
    print(f"fround cut of size 3 with compontent {component}")
    print(f"compontent size: {len(component)}")
    print(f" product = {len(component) * (len(nodes) - len(component))}")






    return



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()



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
