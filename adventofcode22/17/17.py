import re
import numpy as np
from functools import cmp_to_key
import sys


def add_rows(chimney, nrows):
    if nrows <= 0:
        return chimney
    for i in range(nrows):
        chimney = np.append(chimney, np.array([[1, 0, 0, 0, 0, 0, 0, 0, 1]]), axis=0)
    return chimney


# ####
#
# .#.
# ###
# .#.
#
# ..#
# ..#
# ###
#
# #
# #
# #
# #
#
# ##
# ##

def drop_shape(chimney, count, height, jetstreams, jetpos):
    if count % 5 == 0:
        rockShape = np.array([[1, 1, 1, 1]])
    elif count % 5 == 1:
        rockShape = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
    elif count % 5 == 2:
        rockShape = np.array([[1, 1, 1], [0, 0, 1], [0, 0, 1]])
    elif count % 5 == 3:
        rockShape = np.array([[1], [1], [1], [1]])
    elif count % 5 == 4:
        rockShape = np.array([[1, 1], [1, 1]])
    position = np.array([height + 4, 3])
    while position[0] > 0:
        ## jetstream
        direction = jetstreams[jetpos]
        jetpos = (jetpos + 1) % (len(jetstreams))
        if direction == '<':
            direction = np.array([0, -1])
        elif direction == '>':
            direction = np.array([0, 1])
        else:
            print('no direction')
            direction = np.array([0, 0])
        for i in range(rockShape.shape[0]):
            for j in range(rockShape.shape[1]):
                if rockShape[i, j] == 1 and chimney[i + position[0], j + position[1] + direction[1]] == 1:
                    direction = np.array([0, 0])
                    break
        position += direction

        ## drop
        rest = False
        for i in range(rockShape.shape[0]):
            for j in range(rockShape.shape[1]):
                if rockShape[i, j] == 1 and chimney[i + position[0] - 1, j + position[1]] == 1:
                    rest = True
        if rest == True:
            for i in range(rockShape.shape[0]):
                for j in range(rockShape.shape[1]):
                    if rockShape[i, j] == 1:
                        chimney[i + position[0], j + position[1]] = 1
            return int(max(position[0] + (rockShape.shape[0] - 1), height)), jetpos
        else:
            position += np.array([-1, 0])


def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        jetstreams = my_file.readline().strip()
        height = 0
        chimney = np.ones([1, 9])
        chimney = add_rows(chimney, 7)

        jetpos = 0
        heights = []
        # np.set_printoptions(threshold=sys.maxsize)
        for count in range(2022):
            height, jetpos = drop_shape(chimney, count, height, jetstreams, jetpos)
            heights += [height]
            chimney = add_rows(chimney, height - chimney.shape[0] + 8)

        print('final height')
        print(height)


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        jetstreams = my_file.readline().strip()
        height = 0
        chimney = np.ones([1, 9])
        chimney = add_rows(chimney, 7)

        jetpos = 0
        heights = []
        # np.set_printoptions(threshold=sys.maxsize)
        height_1739 = 0
        height_plus1745 = 0
        for count in range(1000000000000):
            height, jetpos = drop_shape(chimney, count, height, jetstreams, jetpos)

            heights += [height]
            chimney = add_rows(chimney, height - chimney.shape[0] + 8)

            if count == 1739-1:
                height_1739 = height
            if count == 1739 + 1745-1:
                height_plus1745 = height - height_1739
            if count == ((1000000000000 - 1739) % 1745) + 1739 + 1745 -1:
                break

        height = height + ((1000000000000 - count - 1) // 1745 * height_plus1745 )
        print('final height')
        print(height)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
