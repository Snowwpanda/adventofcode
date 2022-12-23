import re
import numpy as np
from functools import cmp_to_key


def floydWarshall(valveGraph, valveNames):
    N = len(valveNames)
    dist = np.ones([N,N,N]) * N

    for i in range(N):
        dist[0, i, i] = 0

    for k in range(1, N):
        for i in range(N):
            dist[k, i, i] = 0
        for i in range(k):
            for j in range(k):
                if i == j and valveNames[k] in valveGraph[i]:
                    dist[k, i, k] = 1
                    dist[k, k, i] = 1
                elif i != j and valveNames[k] in valveGraph[j]:
                    dist[k, i, k] = min(dist[k, i, k], dist[k-1, i, j] + 1)
                    dist[k, k, i] = min(dist[k, k, i], dist[k-1, j, i] + 1)
        for i in range(k):
            for j in range(k):
                dist[k, i, j] = min(dist[k-1, i, j], dist[ k, i, k] + dist[ k, k, j])
    return dist[N-1]


def calcluate_max_flow(start, nonzeroValvesFlow, submatrix, time):
    total = 0;
    endpath = []
    for i in np.where(nonzeroValvesFlow != 0)[0]:
        if time >= submatrix[start][i] + 1:
            tmp = nonzeroValvesFlow[i]
            nonzeroValvesFlow[i] = 0
            [subTotal, subPath] = calcluate_max_flow(i, nonzeroValvesFlow, submatrix, time - submatrix[start][i] - 1)
            if subTotal + (tmp * (time - submatrix[start][i] - 1)) > total:
                [total, endpath] = [subTotal + (tmp * (time - submatrix[start][i] - 1)), subPath.copy()]
            nonzeroValvesFlow[i] = tmp
    return [total, [start] + endpath]



def calcluate_elephant_max_flow(startme, startelephant, nonzeroValvesFlow, submatrix, timeme, timeelephant):
    ## assuming at least 1 person works till the end
    total = 0;
    endpath = []
    if len(np.where(nonzeroValvesFlow != 0)[0]) != 0 and timeme >= min(submatrix[startme][np.where(nonzeroValvesFlow != 0)[0]] + [0]):
        for i in np.where(nonzeroValvesFlow != 0)[0]:
            if timeme >= submatrix[startme][i] + 1:
                tmp = nonzeroValvesFlow[i]
                nonzeroValvesFlow[i] = 0
                [subTotal, subPath] = calcluate_elephant_max_flow(i, startelephant, nonzeroValvesFlow, submatrix, timeme - submatrix[startme][i] - 1, timeelephant)
                if subTotal + (tmp * (timeme - submatrix[startme][i] - 1)) > total:
                    [total, endpath] = [subTotal + (tmp * (timeme - submatrix[startme][i] - 1)), subPath.copy()]
                nonzeroValvesFlow[i] = tmp
    else:
        [subTotal, subPath] = calcluate_max_flow(startelephant, nonzeroValvesFlow, submatrix, timeelephant)
        if subTotal > total:
            [total, endpath] = [subTotal, subPath.copy()]
    return [total, [startme] + endpath]


def solveA(file_name):

    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        valveNames = []
        valveFlow = []
        valveGraph = []
        for line in lines:
            if re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]*\n?)', line):
                input = re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]*\n?)', line).groups()
            else:
                pass
            valveNames.append(input[0])
            valveFlow.append(int(input[1]))
            valveGraph.append(input[2].strip().split(', '))

        print(valveGraph)
        N = len(valveNames)
        nonzeroValves = np.array(valveNames.index('AA'))
        for i in range(N):
            if valveFlow[i] > 0:
                nonzeroValves = np.append(nonzeroValves , int(i))

        alltoallDist = floydWarshall(valveGraph, valveNames)

        submatrix = np.array([row[nonzeroValves] for row in  alltoallDist])[nonzeroValves]
        time = 30
        start = 0
        nonzeroValvesFlow = np.array(valveFlow)[nonzeroValves]
        print(nonzeroValvesFlow)

        [totalFlow, path] = calcluate_max_flow(start, nonzeroValvesFlow, submatrix, 30)



        print('total')
        print(totalFlow)
        print(path)


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        valveNames = []
        valveFlow = []
        valveGraph = []
        for line in lines:
            if re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]*\n?)', line):
                input = re.match('Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([\w, ]*\n?)', line).groups()
            else:
                pass
            valveNames.append(input[0])
            valveFlow.append(int(input[1]))
            valveGraph.append(input[2].strip().split(', '))

        print(valveGraph)
        N = len(valveNames)
        nonzeroValves = np.array(valveNames.index('AA'))
        for i in range(N):
            if valveFlow[i] > 0:
                nonzeroValves = np.append(nonzeroValves , int(i))

        alltoallDist = floydWarshall(valveGraph, valveNames)

        submatrix = np.array([row[nonzeroValves] for row in  alltoallDist])[nonzeroValves]

        nonzeroValvesFlow = np.array(valveFlow)[nonzeroValves]
        print(nonzeroValvesFlow)

        [totalFlow, path] = calcluate_elephant_max_flow(0, 0, nonzeroValvesFlow, submatrix, 26, 26)



        print('total')
        print(totalFlow)
        print(path)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
