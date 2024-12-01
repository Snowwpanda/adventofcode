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

    # split lines into two lists
    lines = [line.split() for line in lines]
    list1 = [int(line[0]) for line in lines]
    list2 = [int(line[1]) for line in lines]

    # sort
    list1.sort()
    list2.sort()

    # calculate distance
    diff = np.subtract(list1, list2)

    res = sum(abs(diff))

    # return sum
    print("Answer Part 1:")
    print(res)



    
def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    
    # split lines into two lists
    lines = [line.split() for line in lines]
    list1 = [int(line[0]) for line in lines]
    list2 = [int(line[1]) for line in lines]

    # sort
    list1.sort()
    list2.sort()

    # Create counting dictionary from list1 (initializing with 0)
    count_dict = dict.fromkeys(list1, 0)

    for num in list2:
        if num in count_dict:
            count_dict[num] += 1
    

    # Sum the count_dict by multiplying key and value
    similarity_list = [num * count_dict[num] for num in list1]
    res = sum(similarity_list)

    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')