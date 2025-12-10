# import numpy as np
# import re
import pathlib as pl
from pathlib import Path



def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    red_tiles = [tuple([int(num) for num in line.split(',')]) for line in input_data.splitlines()]

    max = (0, (0,0), (0,0))
    for tile1 in red_tiles:
        for tile2 in red_tiles:
            x_dist = abs(tile1[0] - tile2[0]) + 1
            y_dist = abs(tile1[1] - tile2[1]) + 1
            area = x_dist * y_dist
            if area > max[0]:
                max = (area, tile1, tile2)
    
    output = max[0]


    print("Answer Part 1:")
    print(output)



def solveB(file_name):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    red_tiles = [tuple([int(num) for num in line.split(',')]) for line in input_data.splitlines()]
    

    for index, tile in enumerate(red_tiles):
        x_dir = True
        y_dir = True
        before_tile = red_tiles[index -1]
        after_tile = red_tiles[(index +1) % len(red_tiles)]
        for other in (before_tile, after_tile):
            if tile[0] != other[0]:
                x_dir = tile[0] < other[0]
            if tile[1] != other[1]:
                y_dir = tile[1] < other[1]
        max_x = tile[0]
        
        while True:


    
    


    print("Answer Part 2:")
    # print(output)
    

if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')
