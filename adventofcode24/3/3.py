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

    sum = 0
    
    for line in lines:
        # search for all with re
        for match in re.finditer(r'mul\((\d+),(\d+)\)', line):

            sum += int(match.group(1)) * int(match.group(2))


    res = sum

    # Print result
    print("Answer Part 1:")
    print(res)





    
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
    solveA('input.txt')

    solveB('input.txt')