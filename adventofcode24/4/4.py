import numpy as np
import re
import pathlib as pl
from pathlib import Path


def count_subarray(arr, search_string):
    # arr to string
    full_str = ''.join(arr)
    return full_str.count(search_string)

def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # tranform into numpy matrix for rotatoin:
    lines = np.array([[x for x in line.strip()] for line in lines])

    xmas_count = 0
    # forward and backward:
    for line in lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
        
    # mirror along diagonal (for vertical):
    lines = np.rot90(np.fliplr(lines))
    # forward and backward:
    for line in lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
    
    # create matrix but every line shifted by 1 more to the right (for diagonal /)
    shifted_lines = np.array([[' ' for x in range(len(lines) -y -1)] + list(lines[y]) + [' ' for x in range(y)]   for y in range(len(lines))]) 
    shifted_lines = np.rot90(np.fliplr(shifted_lines))
    # forward and backward:
    for line in shifted_lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')
    
    # create matrix but every line shifted by 1 more to the left (for diagonal \)
    shifted_lines = np.array([[' ' for x in range(y)] + list(lines[y]) + [' ' for x in range(len(lines) -y -1)]   for y in range(len(lines))]) 
    shifted_lines = np.rot90(np.fliplr(shifted_lines))
    # forward and backward:
    for line in shifted_lines:
        xmas_count += count_subarray(line, 'XMAS')
        xmas_count += count_subarray(line, 'SAMX')

    res = xmas_count

    # Print result
    print("Answer Part 1:")
    print(res)

def transform1(pos, index, n):
    # turn diagonal coordinates into matrix coordinates
    x = pos
    y = index + pos - (n -1)
    return (x, y)

    
def transform2(pos, index, n):
    # turn diagonal coordinates into matrix coordinates
    x = pos
    y = index - pos
    return (x, y)



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    
    # tranform into numpy matrix:
    lines = np.array([[x for x in line.strip()] for line in lines])

    n = len(lines)

    
    # create matrix but every line shifted by 1 more to the right (for diagonal \)
    shifted_lines = np.array([[' ' for x in range(len(lines) -y -1)] + list(lines[y]) + [' ' for x in range(y)]   for y in range(len(lines))]) 
    shifted_lines = np.rot90(np.fliplr(shifted_lines))

    # Keeping track of all the 'A's with MAS or SAM in the vicinity
    found_mas = set()

    # forward and backward:
    for index, line in enumerate(shifted_lines):
        found_mas.update([transform1(match.start() +1, index, n) for match in re.finditer('MAS', ''.join(line))])
        found_mas.update([transform1(match.start() +1, index, n) for match in re.finditer('SAM', ''.join(line))])

    
    count_x_mas = 0
    # create matrix but every line shifted by 1 more to the left (for diagonal /)
    shifted_lines = np.array([[' ' for x in range(y)] + list(lines[y]) + [' ' for x in range(len(lines) -y -1)]   for y in range(len(lines))]) 
    shifted_lines = np.rot90(np.fliplr(shifted_lines))
    # forward and backward:
    for index, line in enumerate(shifted_lines):
        for match in [transform2(match.start() +1, index, n) for match in re.finditer('MAS', ''.join(line))] :
            if match in found_mas:
                count_x_mas += 1
        for match in [transform2(match.start() +1, index, n) for match in re.finditer('SAM', ''.join(line))] :
            if match in found_mas:
                count_x_mas += 1

    

        
        
    res = count_x_mas

    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')