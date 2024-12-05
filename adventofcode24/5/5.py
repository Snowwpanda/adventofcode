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

    

def rules_sort(manual, order_dict):
    manual_set = set(manual)
    ordered_manual = []
    # restrict dict to local variables
    local_ordering = {k: [num for num in order_dict.get(k, []) if num in manual_set] for k in manual_set}
    while local_ordering:
        for k, v in local_ordering.items():
            if not v:
                ordered_manual.insert(0, k)
                del local_ordering[k]
                for k2, v2 in local_ordering.items():
                    if k in v2:
                        v2.remove(k)
                break
        else:
            print('No ordering possible')
            return 0
    
    # return middle element
    return int(ordered_manual[len(ordered_manual)//2])

        
            

def solveB(file_name):    
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
            continue
        middle_sum += rules_sort(manual, order_dict)

    res = middle_sum


    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')