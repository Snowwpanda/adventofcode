# import numpy as np
# import re
import pathlib as pl
from pathlib import Path

# from PIL import Image


def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    ranges, ingredients = input_data.split('\n\n')
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges.split()]
    ranges = sorted(ranges, key=lambda x: x[0])
    ingredients = [int(x) for x in ingredients.split()]
    ingredients = sorted(ingredients)

    fresh = 0
    range_index = 0
    ingredient_index = 0
    while ingredient_index < len(ingredients) and range_index < len(ranges):
        i = ingredients[ingredient_index]
        r = ranges[range_index]
        if i < r[0]:
            ingredient_index += 1
        elif i <= r[1]:
            fresh += 1
            ingredient_index += 1
        else:
            range_index += 1

    output = fresh

    print("Answer Part 1:")
    print(output)

    
def solveB(file_name):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()
    
    
    ranges, _ = input_data.split('\n\n')
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges.split()]
    ranges = sorted(ranges, key=lambda x: x[0])

    total_fresh = 0
    index = ranges[0][0]
    for r in ranges:
        total_fresh += max(r[1], index -1 ) - max(r[0], index) + 1
        index = max(r[1] + 1, index) 
    output = total_fresh

    print("Answer Part 2:")
    print(output)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
