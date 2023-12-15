import math

import numpy as np
import re
import time
from collections import Counter


# import plt function

def hash_value(seq):
    hash_value_seq = 0
    for char in seq:
        hash_value_seq += ord(char)
        hash_value_seq *= 17
        hash_value_seq %= 256
    return hash_value_seq


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    value = 0
    for line in lines:
        for seq in line.split(','):
            value += hash_value(seq)

    print(f'Hash value: {value}')

    return


class boxBox:
    contents = []
    focus = []

    def __init__(self):
        self.contents = []
        self.focus = []

    def contains(self, item):
        return item in self.contents

    def remove(self, item):
        index = self.contents.index(item)
        self.contents.remove(item)
        # remove focus at index
        self.focus.pop(index)

    def add(self, item, focus):
        self.contents.append(item)
        self.focus.append(int(focus))

    def replace(self, item, focus):
        index = self.contents.index(item)
        self.focus[index] = int(focus)

    def focus_power(self, box_nr):
        power = 0
        lenses = len(self.focus)
        for i in range(lenses):
            power += self.focus[i] * box_nr * (i+1)
        return power



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    boxes = []
    for i in range(256):
        # create 256 boxes from class box
        boxes.append(boxBox())

    init_seq = lines[0].split(',')
    for seq in init_seq:
        if '-' in seq:
            lb = seq.split('-')[0]
            box = boxes[hash_value(lb)]
            if box.contains(lb):
                box.remove(lb)
        elif '=' in seq:
            label, focus = seq.split('=')

            box = boxes[hash_value(label)]
            if box.contains(label):
                box.replace(label, focus)
            else:
                box.add(label, focus)

    focus_power = 0
    for i in range(256):
        focus_power += boxes[i].focus_power(i+1)

    print(f'Focus power: {focus_power}')



    return


if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
