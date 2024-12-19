import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue

def design_possible(towels, design, max_towel_length):
    if design in towels:
        return 1
    for i in range(1, max_towel_length+1):
        if design[:i] in towels and design_possible(towels, design[i:], max_towel_length):
            return 1
    return 0


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    towels = set(lines[0].strip().split(', '))

    max_towel_length = max([len(towel) for towel in towels])

    designs = [design.strip() for design in lines[2:]]

    possible = [design_possible(towels, design, max_towel_length) for design in designs]

    n_possible = sum(possible)



    
    res = n_possible
    
    # Print result
    print("Answer Part 1:")
    print(res)



def count_design_possible(towels, design, max_towel_length, memo):
    if design in memo:
        return memo[design]
    count = 0
    for i in range(1, min(max_towel_length, len(design))+1):
        if design[:i] in towels:
            count += count_design_possible(towels, design[i:], max_towel_length, memo)

    memo[design] = count
    return count


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    towels = set(lines[0].strip().split(', '))

    max_towel_length = max([len(towel) for towel in towels])

    designs = [design.strip() for design in lines[2:]]
    memo = {'': 1}
    possible = [count_design_possible(towels, design, max_towel_length, memo) for design in designs]

    n_possible = sum(possible)

    
    res = n_possible

    # Print result
    print("Answer Part 1:")
    print(res)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')