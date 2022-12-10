import re
import numpy as np


def move_and_record(move, head, tail, visited):
    direction_map = {
        'U': np.array([0,1]),
        'D': np.array([0, -1]),
        'L': np.array([-1, 0]),
        'R': np.array([1, 0]),
    }
    direction = direction_map[move[0]]

    for i in range(move[1]):
        head += direction
        dist = head - tail
        if abs(dist[0]) > 1 or abs(dist[1]) > 1:
            tail += np.sign(dist)
            visited.add(f'{tail[0]},{tail[1]}')


def move_rope_and_record(move, rope, visited):
    direction_map = {
        'U': np.array([0,1]),
        'D': np.array([0, -1]),
        'L': np.array([-1, 0]),
        'R': np.array([1, 0]),
    }
    direction = direction_map[move[0]]

    for i in range(move[1]):
        rope[0] += direction
        for j in range(len(rope)-1):
            dist = rope[j] - rope[j+1]
            if abs(dist[0]) > 1 or abs(dist[1]) > 1:
                rope[j+1] += np.sign(dist)
        visited.add(f'{rope[-1][0]},{rope[-1][1]}')


def solveA(file_name):
    with open(file_name) as my_file:
        moves = []
        for line in my_file:
            if re.match('[LRUD] \d+\n?', line):
                line = line.split()
                moves.append([line[0], int(line[1])])


        visited = set(['0,0'])
        head = np.array([0,0])
        tail = np.array([0,0])
        for move in moves:
            move_and_record(move, head, tail, visited)
        print("Number of visited points:")
        print(len(visited))
        print("Points:")
        print(visited)






def solveB(file_name):
    with open(file_name) as my_file:
        moves = []
        for line in my_file:
            if re.match('[LRUD] \d+\n?', line):
                line = line.split()
                moves.append([line[0], int(line[1])])


        visited = set(['0,0'])
        rope = np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])
        for move in moves:
            move_rope_and_record(move, rope, visited)
        print("Number of visited points:")
        print(len(visited))
        print("Points:")
        print(visited)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
