# import numpy as np
# import re
import pathlib as pl
from pathlib import Path

# from PIL import Image


def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    junctions = [tuple([int(num) for num in line.split(',')]) for line in input_data.splitlines()]


    square_distances = []
    for i in range(len(junctions)):
        for j in range(i+1, len(junctions)):
            a = junctions[i]
            b = junctions[j]
            dist = (a[0] - b[0])    **2 + (a[1] - b[1])**2  + (a[2] - b[2])**2
            square_distances.append((dist, i, j))
    
    # Choose how many edges
    edges = 1000
    # testfile 10
    if len(junctions) <= 20:
        edges = 10
    top_edges = sorted(square_distances)[:edges]


    # Merge_strucutre should for every node contain the parent node and the size of the tree
    partents = list(range(len(junctions)))
    components = { i: 1 for i in range(len(junctions)) }
    def find_root(node):
        root = partents[node]
        while partents[root] != root:
            root = partents[root]
        return root
    for _, i, j in top_edges:
        root_i = find_root(i)
        root_j = find_root(j)
        if root_i == root_j:
            continue
        else:
            partents[root_i] = root_j
            components[root_j] = components[root_j] + components[root_i]
            components.pop(root_i)
        

  
    # Top 3 largest components
    top_3 = sorted(components.values(), reverse=True)[:3]

    output = top_3[0] * top_3[1] * top_3[2]
    print("Answer Part 1:")
    print(output)



def solveB(file_name):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()
    junctions = [tuple([int(num) for num in line.split(',')]) for line in input_data.splitlines()]


    square_distances = []
    for i in range(len(junctions)):
        for j in range(i+1, len(junctions)):
            a = junctions[i]
            b = junctions[j]
            dist = (a[0] - b[0])    **2 + (a[1] - b[1])**2  + (a[2] - b[2])**2
            square_distances.append((dist, i, j))
    
    # # Choose how many edges
    # edges = 1000
    # # testfile 10
    # if len(junctions) <= 20:
    #     edges = 10
    # top_edges = sorted(square_distances)[:edges]


    # Merge_strucutre should for every node contain the parent node and the size of the tree
    last_edge = None
    partents = list(range(len(junctions)))
    components = { i: 1 for i in range(len(junctions)) }
    def find_root(node):
        root = partents[node]
        while partents[root] != root:
            root = partents[root]
        return root
    for _, i, j in sorted(square_distances):
        root_i = find_root(i)
        root_j = find_root(j)
        if root_i == root_j:
            continue
        else:
            partents[root_i] = root_j
            components[root_j] = components[root_j] + components[root_i]
            components.pop(root_i)
        if len(components) == 1:
            last_edge = (i, j)
            break


    output = junctions[last_edge[0]][0] * junctions[last_edge[1]][0]
    print("Answer Part 2:")
    print(output)
    

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
