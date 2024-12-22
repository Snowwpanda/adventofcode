import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue


def new_secret_num(num, it):
    for i in range(it):
        new_num = num << 6
        new_num = new_num ^ num
        new_num = new_num % 16777216
        new_num = new_num ^ (new_num >> 5)
        new_num = new_num % 16777216
        new_num = new_num ^ (new_num << 11)
        new_num = new_num % 16777216
        num = new_num

    return num




def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    secret_nums = [int(line.strip()) for line in lines]

    regeneration_per_day = 2000

    new_secrets = [new_secret_num(num, regeneration_per_day) for num in secret_nums]
        


    res = sum(new_secrets)
    
    # Print result
    print("Answer Part 1:")
    print(res)



def add_gain_for_seq(num, values, sellingpoints):

    fiveprice = (num% 10, new_secret_num(num, 1)% 10, new_secret_num(num, 2)% 10, 
                 new_secret_num(num, 3)% 10, new_secret_num(num, 4)% 10)
    fourchange = (fiveprice[1] - fiveprice[0], fiveprice[2] - fiveprice[1], 
                  fiveprice[3] - fiveprice[2], fiveprice[4] - fiveprice[3])

    secret_num = new_secret_num(num, 4)
    price = secret_num % 10

    values[fourchange].append(price)
    sellingpoints[fourchange].append(4)
    visited = {fourchange}

    for i in range(4, 2000):
        next_secret_num = new_secret_num(secret_num, 1)
        next_price = next_secret_num % 10
        change = next_price - price
        fourchange = (fourchange[1], fourchange[2], fourchange[3], change)
        if fourchange not in visited:
            values[fourchange].append(next_price)
            sellingpoints[fourchange].append(i)
            visited.add(fourchange)
        secret_num = next_secret_num
        price = next_price
    
    for key, value in values.items():
        if key not in visited:
            values[key].append(0)
            sellingpoints[key].append(-1)




def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    secret_nums = [int(line.strip()) for line in lines]

    values = {}
    sellingpoints = {}
    for i in range(-9, 10):
        for j in range(-9, 10):
            for k in range(-9, 10):
                for m in range(-9, 10):
                    values[(i, j, k, m)] = []
                    sellingpoints[(i, j, k, m)] = []
    

    for index, num in enumerate(secret_nums):
        add_gain_for_seq(num, values, sellingpoints)

    # find max
    max = 0
    seq = ()
    for key, value in values.items():
        if sum(value) > max:
            max = sum(value)
            seq = key

    print(f"max seq: {seq}")
    res = max

    # wrong: 1944

    # Print result
    print("Answer Part 2:")
    print(res)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')