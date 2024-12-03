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

    # lines = [[int(x) for x in line.split()] for line in lines]
    # # reports are safe if increasing or decreasing, differing by 1-3
    # safe_records = 0
    
    # for line in lines:
    #     inc_dec = 1 if line[0] < line[-1] else -1
    #     last = line[0] - inc_dec
    #     for number in line:
    #         if (number - last) * inc_dec not in [1, 2, 3]:
    #             break
    #         last = number
    #     else:
    #         safe_records += 1
        
    # res = safe_records

    # # return sum
    # print("Answer Part 1:")
    # print(res)



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        # lines = my_file.readlines()
        instructions = re.findall(r"(don't|do|mul)\((\d*)(,?)(\d*)\)", my_file.read())
    
    sum = 0
    do = True
    for instruction in instructions:
        if instruction[0] == 'do':
            do = True
        elif instruction[0] == 'don\'t':
            do = False
        else:
            if not do or '' in instruction[1:]:
                continue
            first = int(instruction[1])
            second = int(instruction[3])
            sum += first * second
        
        
    res = sum

    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')