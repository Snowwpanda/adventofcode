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

    start = 50
    zerocounter = 0
    for line in lines:
        sign, value = line[0], int(line[1:].strip())
        if sign == "R":
            start = (start + value) % 100
        elif sign == "L":
            start = (start - value) % 100
        if start == 0:
            zerocounter += 1
    
    print("Answer Part 1:")
    print(zerocounter)



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    start = 50
    zerocounter = 0
    for line in lines:
        sign, value = line[0], int(line[1:].strip())
        if value == 0:
            continue
        if start == 0 and sign == "L":
            # careful for overcounting when stopping at 0
            zerocounter -= 1
        if sign == "R":
            start = (start + value)
        elif sign == "L":
            start = (start - value)
        if start >= 100:
            zerocounter += start // 100
            start = start % 100
        elif start <= 0:
            zerocounter += (-start) // 100 + 1
            start = start % 100


    
    print("Answer Part 2:")
    print(zerocounter)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')