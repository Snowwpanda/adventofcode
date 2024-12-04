import numpy as np
import re
import pathlib as pl
from pathlib import Path


def count_subarray(arr, search_string):
    count = 0
    # arr to string
    full_str = ''.join(arr)
    return full_str.count(search_string)

def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # tranform into numpy matrix:
    lines = np.array([[x for x in line.strip()] for line in lines])

    xmas_count = 0
    # forward and backward:
    for line in lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
        
    # create matrix but every line shifted by 1 more to the right
    shifted_lines = np.array([[' ' for x in range(y)] + list(lines[y]) + [' ' for x in range(len(lines) -y -1)]   for y in range(len(lines))]) 
    shifted_lines = np.rot90(np.fliplr(shifted_lines))
    # forward and backward:
    for line in shifted_lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
    
    # mirror along diagonal:
    lines = np.rot90(np.fliplr(lines))
    # forward and backward:
    for line in lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
    
    # create matrix but every line shifted by 1 more to the right
    shifted_lines = np.array([[' ' for x in range(len(lines) -y -1)] + list(lines[y]) + [' ' for x in range(y)]   for y in range(len(lines))]) 
    shifted_lines = np.rot90(np.fliplr(shifted_lines))
    # forward and backward:
    for line in shifted_lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
    

    res = xmas_count

    # Print result
    print("Answer Part 1:")
    print(res)



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    

        
        
    res = safe_records

    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    # solveB('input.txt')