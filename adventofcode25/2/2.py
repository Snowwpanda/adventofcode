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
    
    while (dnumb := double(numb)) <= max:
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


def clean_range(r: tuple[str, str]) -> list:
    if len(r[0]) != len(r[1]):
        bound = 10 ** len(r[0]) - 1
        return [(int(r[0]), bound, len(r[0]))] + clean_range((str(bound+1), r[1]))
    return [(int(r[0]), int(r[1]), len(r[0]))]

def explicit_sol_A(file_name: str):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()
    
    ranges = [(r.split('-')) for r in input_data.split(',')]
    ranges = sum([clean_range(r) for r in ranges], [])

    total_invalid = 0
    for start, end, digit_len in ranges:
        if digit_len %2 !=0:
            continue
        divisor = 10 ** (digit_len//2) + 1
        smallest = ((start-1) // divisor) + 1
        largest = (end // divisor)
        # sumation of arithmetic series, using formula n/2 * (a + l)
        total_invalid += (largest - smallest + 1) * (smallest + largest) * divisor // 2

    print("Explicit Answer Part 1:")
    print(total_invalid)


    


if __name__ == '__main__':
    # solveA('input.txt')

    # solveB('input.txt')

    explicit_sol_A('input.txt')