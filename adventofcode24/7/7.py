import numpy as np
import re
import pathlib as pl


def possibly_valid(result, nums):
    if len(nums) == 1:
        return nums[0] == result
    last = nums[-1]
    return (possibly_valid(result - last, nums[:-1]) or 
            (result % last == 0 and possibly_valid(result // last, nums[:-1])))


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    eqs = []
    for line in lines:
        eq = line.split(':')
        result = int(eq[0])
        nums = [int(num) for num in eq[1].strip().split(' ')]
        eqs.append((result, nums))

    sum = 0
    for eq in eqs:
        result, nums = eq
        if possibly_valid(result, nums):
            sum += result
    
    res = sum

    # Print result
    print("Answer Part 1:")
    print(res)



def possibly_valid_withconcat(result, nums):
    if len(nums) == 1:
        return nums[0] == result
    last = nums[-1]
    digits = len(str(last))
    return (possibly_valid_withconcat(result - last, nums[:-1]) or 
            (result % last == 0 and possibly_valid_withconcat(result // last, nums[:-1])) or
            (result % (10 ** digits) == last and possibly_valid_withconcat(result // (10 ** digits), nums[:-1])))



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()
        
    eqs = []
    for line in lines:
        eq = line.split(':')
        result = int(eq[0])
        nums = [int(num) for num in eq[1].strip().split(' ')]
        eqs.append((result, nums))

    sum = 0
    for eq in eqs:
        result, nums = eq
        if possibly_valid_withconcat(result, nums):
            sum += result


    res = sum

    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')