import numpy as np
import re
import pathlib as pl

def calculate_stones(stone, time, memo):
    if time == 0:
        return 1
    if (stone, time) in memo:
        return memo[(stone, time)]
    digits = len(str(stone))
    if stone == 0:
        result = calculate_stones(1, time - 1, memo)
    elif digits % 2 == 1:
        result = calculate_stones(stone * 2024, time - 1, memo)
    elif digits % 2 == 0:
        first_half = int(str(stone)[:digits//2])
        second_half = int(str(stone)[digits//2:])
        result = calculate_stones(first_half, time - 1, memo) + calculate_stones(second_half, time - 1, memo)
    
    memo[(stone, time)] = result
    return result
        



def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    stones = [int(x) for x in lines[0].split()]
    time = 25
    memo = {}
    stone_line = [calculate_stones(stone, time, memo) for stone in stones]

    res = sum(stone_line)

    # Print result
    print("Answer Part 1:")
    print(res)




def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    stones = [int(x) for x in lines[0].split()]
    time = 75
    memo = {}
    stone_line = [calculate_stones(stone, time, memo) for stone in stones]

    res = sum(stone_line)

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')