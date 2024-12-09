import numpy as np
import re
import pathlib as pl



def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    id = 0
    files = True
    real_system = []
    for char in lines[0]:
        if files:  
            real_system += [id for i in range(int(char))]
            id += 1
        else:
            real_system += ['.' for i in range(int(char))]
        files = not files
    
    real_system_copy = real_system.copy()

    # compress
    checksum = 0
    index = 0
    while index < len(real_system):
        if real_system[index] != '.':
            checksum += index * real_system[index]
        else:
            end = real_system.pop()
            while end == '.':
                end = real_system.pop()
            if index >= len(real_system):
                break
            checksum += index * end
        index += 1
    

    res = checksum

    # Print result
    print("Answer Part 1:")
    print(res)


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()
        
        



    res = 0

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    # solveB('input.txt')