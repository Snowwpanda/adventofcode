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


def add_edge(edge, adj_list):
    u = edge[0]
    v = edge[1]
    if u in adj_list:
        adj_list[u].append(v)
    else:
        adj_list[u] = [v]
    if v in adj_list:
        adj_list[v].append(u)
    else:
        adj_list[v] = [u]


def count_dfs(start, adj_list, vis):
    count = 0
    if start.islower():
        vis[start] = True
    for neighbor in adj_list[start]:
        if neighbor == 'end':
            count += 1
            continue
        if not vis[neighbor]:
            count += count_dfs(neighbor, adj_list, vis)
    vis[start] = False
    return count

def count_dfs_twice(start, adj_list, vis):
    count = 0
    if start.islower():
        vis[start] = True
    for neighbor in adj_list[start]:
        if neighbor == 'end':
            count += 1
        elif not vis[neighbor]:
            count += count_dfs_twice(neighbor, adj_list, vis)
        elif vis[neighbor] and neighbor.islower() and neighbor != 'start':
            count += count_dfs(neighbor, adj_list, vis)
            vis[neighbor] = True

    vis[start] = False
    return count



def task12():
    data = read_input()
    data = [line.split('-') for line in data]
    print(data)

    adj_list = dict()
    for edge in data:
        add_edge(edge, adj_list)

    vis = dict()
    for i in adj_list:
        vis[i] = False

    ways = count_dfs('start', adj_list, vis)
    print(ways)
    write_sol(ways, 1)

    ways = count_dfs_twice('start', adj_list, vis)
    print(ways)
    write_sol(ways, 2)


task12()