import numpy as np
import re
import pathlib as pl
from pathlib import Path

def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    lines = [[int(x) for x in line.split()] for line in lines]
    # reports are safe if increasing or decreasing, differing by 1-3
    safe_records = 0
    
    for line in lines:
        inc_dec = 1 if line[0] < line[-1] else -1
        last = line[0] - inc_dec
        for number in line:
            if (number - last) * inc_dec not in [1, 2, 3]:
                break
            last = number
        else:
            safe_records += 1
        
    res = safe_records

    # return sum
    print("Answer Part 1:")
    print(res)



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    

    lines = [[int(x) for x in line.split()] for line in lines]
    # reports are safe if increasing or decreasing, differing by 1-3
    safe_records = 0
    
    for line in lines:
        if len(line) < 4:
            safe_records += 1
            continue
        # testing both increasing and decreasing because easier and sequence is at least 4 long
        for inc_dec in [1, -1]:
            bad_levels = -1
            for i in range(1, len(line)):
                if (line[i] - line[i-1]) * inc_dec not in [1, 2, 3]:
                    if bad_levels not in [-1, i-1]:
                        break
                    bad_levels = i
                    if i == len(line) - 1 or (line[i+1] - line[i-1]) * inc_dec in [1, 2, 3]:
                        continue
                    if (i == 1 or (line[i] - line[i-2]) * inc_dec in [1, 2, 3]) and (line[i+1] - line[i]) * inc_dec in [1, 2, 3] :
                        continue
                    break
            else:
                safe_records += 1
        
        
        
    res = safe_records

    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')