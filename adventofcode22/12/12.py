import re
import numpy as np


def BFS(grid, dist, start, end):
    if np.array_equal(start, end):
        return True
    queue = [start]
    directions = [np.array([-1,0]),
                  np.array([0,1]),
                  np.array([0,-1]),
                  np.array([1,0])]
    while queue:
        current = queue.pop(0)
        curr_distance = dist[current[0], current[1]]
        curr_height = grid[current[0], current[1]]

        for dir in directions:
            next = current + dir
            if np.array_equal(next, end) and curr_height + 1 >= ord('z') - ord('a'):
                dist[next[0], next[1]] = curr_distance + 1
                return True
            if 0 <= next[0] < len(grid) and 0 <= next[1] < len(grid[0]):
                if dist[next[0], next[1]] == 0 and not np.array_equal(next, start) and curr_height + 1 >= grid[next[0], next[1]]:
                    dist[next[0], next[1]] = curr_distance + 1
                    queue.append(next)

    return False


def BFSdown(grid, dist, end):

    queue = [end]
    directions = [np.array([-1,0]),
                  np.array([0,1]),
                  np.array([0,-1]),
                  np.array([1,0])]
    while queue:
        current = queue.pop(0)
        curr_distance = dist[current[0], current[1]]
        curr_height = grid[current[0], current[1]]

        for dir in directions:
            next = current + dir
            if 0 <= next[0] < len(grid) and 0 <= next[1] < len(grid[0]):
                if grid[next[0], next[1]] == 0 and curr_height <= 1:
                    dist[next[0], next[1]] = curr_distance + 1
                    return True
                if dist[next[0], next[1]] == 0 and not np.array_equal(next, end) and curr_height - 1 <= grid[next[0], next[1]]:
                    dist[next[0], next[1]] = curr_distance + 1
                    queue.append(next)

    return False




def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        grid = [[ord(letter) - ord('a') for letter in line.strip()] for line in my_file.readlines()]
        grid = np.array(grid)
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == ord('S') - ord('a'):
                    start = (i,j)
                    grid[i,j] = 0
                if grid[i][j] == ord('E') - ord('a'):
                    end =  np.array([i,j])


        dist = np.zeros([n,m])
        foundEnd = BFS(grid, dist, start, end)

    print("Distance:")
    if foundEnd:
        print(dist[end[0],end[1]])
    else:
        print('End not reachable')






def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        grid = [[ord(letter) - ord('a') for letter in line.strip()] for line in my_file.readlines()]
        grid = np.array(grid)
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == ord('S') - ord('a'):
                    start = (i,j)
                    grid[i,j] = 0
                if grid[i][j] == ord('E') - ord('a'):
                    end =  np.array([i,j])


        dist = np.zeros([n,m])
        foundEnd = BFSdown(grid, dist, end)

    print("Distance:")
    if foundEnd:
        print(np.max(dist))
    else:
        print('End not reachable')












if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
