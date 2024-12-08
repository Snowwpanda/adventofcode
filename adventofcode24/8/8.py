import numpy as np
import re
import pathlib as pl



def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()
    
    grid = [[char for char in line.strip()] for line in lines]

    antenna_types = {}
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != '.':
                if char in antenna_types:
                    antenna_types[char].append((x, y))
                else:
                    antenna_types[char] = [(x, y)]
    
    antinodes = set()
    for antenna_list in antenna_types.values():
        if antenna_list.__len__() == 1:
            continue
        # run over pairs of distinct antennas
        for first_antenna in antenna_list:
            for second_antenna in antenna_list:
                if first_antenna == second_antenna:
                    continue
                # add the antinode to the set if in grid
                antinode = (2 * second_antenna[0] - first_antenna[0], 2 * second_antenna[1] - first_antenna[1])
                if 0 <= antinode[0] < grid.__len__() and 0 <= antinode[1] < grid[0].__len__():
                    antinodes.add(antinode)


    res = len(antinodes)

    # Print result
    print("Answer Part 1:")
    print(res)


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()
        
        
    grid = [[char for char in line.strip()] for line in lines]

    antenna_types = {}
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char != '.':
                if char in antenna_types:
                    antenna_types[char].append((x, y))
                else:
                    antenna_types[char] = [(x, y)]
    
    antinodes = set()
    for antenna_list in antenna_types.values():
        if antenna_list.__len__() == 1:
            continue
        # run over pairs of distinct antennas
        for first_antenna in antenna_list:
            for second_antenna in antenna_list:
                if first_antenna == second_antenna:
                    continue
                # add the ray of antinodes unti lout of bounds
                antinode = (second_antenna[0], second_antenna[1])
                antinodes.add(antinode)
                while True:
                    antinode = (antinode[0] + second_antenna[0] - first_antenna[0], antinode[1] + second_antenna[1] - first_antenna[1])
                    if not (0 <= antinode[0] < grid.__len__() and 0 <= antinode[1] < grid[0].__len__()):
                        break
                    antinodes.add(antinode)




    res = len(antinodes)

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')