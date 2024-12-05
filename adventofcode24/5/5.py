import numpy as np
import re
import pathlib as pl


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()
    

    order_lines = [line.strip().split('|') for line in lines if re.search(r'(\d)+\|(\d+)', line)]
    manual_lines = [line.strip().split(',') for line in lines if re.search(r'\d+,(\d+,?)*', line)]

    order_dict = {}
    for pair in order_lines:
        if pair[0] not in order_dict:
            order_dict[pair[0]] = [pair[1]]
        else:
            order_dict[pair[0]] += [pair[1]]


    middle_sum = 0

    for manual in manual_lines:
        before = set()
        for num in manual:
            for after in order_dict.get(num, []):
                if after in before:
                    break
            else:
                before.add(num)
                continue
            break
        else:
            middle_sum += int(manual[len(manual)//2])

    res = middle_sum

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