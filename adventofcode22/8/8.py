import numpy as np
import re
import numpy as np


def solveA(file_name):
    with open(file_name) as my_file:
        grid = []
        for line in my_file:
            grid.append(line.strip())


        n = len(grid)
        m = len(grid[0])
        visible = np.zeros((n,m))

        for i in range(n):
            sight = -1
            for j in range(m):
                if int(grid[i][j]) > sight:
                    visible[i,j] = 1
                    sight = int(grid[i][j])
            sight = -1
            for j in range(m-1, 0, -1):
                if int(grid[i][j]) > sight:
                    visible[i,j] = 1
                    sight = int(grid[i][j])

        for j in range(m):
            sight = -1
            for i in range(n):
                if int(grid[i][j]) > sight:
                    visible[i, j] = 1
                    sight = int(grid[i][j])
            sight = -1
            for i in range(n - 1, 0, -1):
                if int(grid[i][j]) > sight:
                    visible[i, j] = 1
                    sight = int(grid[i][j])





        print(sum(sum(visible)))





def solveB(file_name):

    with open(file_name) as my_file:
        grid = []
        for line in my_file:
            grid.append([int(i) for i in line.strip()])


        n = len(grid)
        m = len(grid[0])
        scenicscore = np.ones((n,m))

        for i in range(n):
            pos_of_last_tree_of_height = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for j in range(m):
                scenicscore[i][j] *= j - pos_of_last_tree_of_height[grid[i][j]]
                for idx in range(grid[i][j]+1):
                    pos_of_last_tree_of_height[idx] = j

        for i in range(n):
            pos_of_last_tree_of_height = [m-1] * 10
            for j in range(m-1, 0, -1):
                scenicscore[i][j] *= pos_of_last_tree_of_height[grid[i][j]] - j
                for idx in range(grid[i][j]+1):
                    pos_of_last_tree_of_height[idx] = j

        for j in range(m):
            pos_of_last_tree_of_height = [0,0,0,0,0,0,0,0,0,0]
            for i in range(n):
                scenicscore[i][j] *= i - pos_of_last_tree_of_height[grid[i][j]]
                for idx in range(grid[i][j]+1):
                    pos_of_last_tree_of_height[idx] = i

        for j in range(m):
            pos_of_last_tree_of_height = [n - 1] * 10
            for i in range(n-1,0,-1):
                scenicscore[i][j] *= pos_of_last_tree_of_height[grid[i][j]] - i
                for idx in range(grid[i][j]+1):
                    pos_of_last_tree_of_height[idx] = i


        max_score = 0
        max_position = [0,0]
        for i in range(n):
            for j in range(m):
                if max_score < scenicscore[i,j]:
                    max_score = scenicscore[i,j]
                    max_position = [i,j]
        print('Max scenic score is:')
        print(max_score)
        print('at position:')
        print(max_position)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
