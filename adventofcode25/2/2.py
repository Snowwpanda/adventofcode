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

    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in lines[0].split(',')]

    ranges = sorted(ranges, key=lambda x: x[0])

    max = ranges[-1][1]
    numb = 0
    current_range = 0
    invalid_ids = set()
    def double(x: int) -> int:
        return int(str(x) +  str(x))
    
    while double(numb) <= max:
        dnumb = double(numb)
        if dnumb >= ranges[current_range][0] :
            if dnumb <= ranges[current_range][1]:
                invalid_ids.add(dnumb)
            else:
                current_range += 1
                continue
        numb += 1
            
    print("Answer Part 1:")
    print(sum(invalid_ids))



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in lines[0].split(',')]

    ranges = sorted(ranges, key=lambda x: x[0])

    max = ranges[-1][1]
    numb = 0
    factor = 2
    current_range = 0
    invalid_ids = set()
    def multi(x: int, factor: int) -> int:
        return int(str(x) * factor)
    
    
    while True:
        mnumb = multi(numb, factor)
        if mnumb >= ranges[current_range][0] :
            if mnumb <= ranges[current_range][1]:
                invalid_ids.add(mnumb)
            else:
                current_range += 1
                continue
        numb += 1
        if multi(numb, factor) > max:
            current_range = 0
            numb = 1
            factor += 1
        # still?
        if multi(numb, factor) > max:
            break
        
            
    
    print("Answer Part 2:")
    print(sum(invalid_ids))




if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')