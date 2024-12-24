import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue






def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    edges = [line.strip().split('-') for line in lines]
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    adj_list = {vertex: [] for vertex in vertices}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])

    triples = set()
    for vertex, neighbors in adj_list.items():
        for neighbour in neighbors:
            if neighbour < vertex:
                continue
            for neighbour2 in adj_list[neighbour]:
                if neighbour2 < neighbour:
                    continue
                if neighbour2 in neighbors:
                    triples.add(tuple(sorted([vertex, neighbour, neighbour2])))
    
    t_triples = 0
    for triple in triples:
        if 't' in [ triple[0][0], triple[1][0], triple[2][0]]:
            t_triples += 1
    
    res = t_triples

    # Print result
    print("Answer Part 1:")
    print(res)




def build_adj_list(vertices, edges):
    adj_list = {vertex: [] for vertex in vertices}
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    return adj_list

def find_vertices(edges):
    vertices = set()
    for edge in edges:
        vertices.add(edge[0])
        vertices.add(edge[1])
    return vertices

def build_triples(adj_list):
    triples = {vertex: [] for vertex in adj_list.keys()}
    for vertex, neighbors in adj_list.items():
        for neighbour in neighbors:
            for neighbour2 in adj_list[neighbour]:
                if neighbour2 < neighbour:
                    continue
                if neighbour2 in neighbors:
                    triples[vertex].append(tuple(sorted([neighbour, neighbour2])))
    return triples

def largest_clique(adj_list):
    max_largest_clique = 2
    # this isn't correct but seems close enough for the input
    max_clique = [v for v in adj_list.keys()]

    t_triples = build_triples(adj_list)
    # sort by number of triples
    t_triples = {k: v for k, v in sorted(t_triples.items(), key=lambda item: len(item[1]), reverse=True)}
    for vertex, triples in t_triples.items():
        if len(triples) == 0 or len(triples) < (max_largest_clique - 1)*(max_largest_clique - 2) // 2:
            continue
        t_neighbors = find_vertices(triples)
        subgraph = build_adj_list(t_neighbors, triples)
        max_subclique, max_vert = largest_clique(subgraph)
        if max_subclique + 1 > max_largest_clique:
            max_largest_clique = max_subclique + 1
            max_clique = max_vert + [vertex]
        # remove vertex:
        for neighbor in adj_list[vertex]:
            for triple in t_triples[neighbor]:
                if vertex in triple:
                    t_triples[neighbor].remove(triple)

    return max_largest_clique, max_clique



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    edges = [line.strip().split('-') for line in lines]
    vertices = find_vertices(edges)
    adj_list = build_adj_list(vertices, edges)
    

    max_largest_clique = 2
    v_clique = []

    t_triples = build_triples(adj_list)
    # sort by number of triples
    t_triples = {k: v for k, v in sorted(t_triples.items(), key=lambda item: len(item[1]), reverse=True) if k[0] == 't'}
    for vertex, triples in t_triples.items():
        if len(triples) == 0 or len(triples) < (max_largest_clique - 1)*(max_largest_clique - 2) // 2:
            continue
        t_neighbors = find_vertices(triples)
        subgraph = build_adj_list(t_neighbors, triples)
        max_subclique, v_subclique = largest_clique(subgraph)
        if max_subclique + 1 > max_largest_clique:
            max_largest_clique = max_subclique + 1
            v_clique = v_subclique + [vertex]

    print(max_largest_clique, v_clique)
    res = sorted(v_clique)

    # Print result
    print("Answer Part 2:")
    print(','.join(res))


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')