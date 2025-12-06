# import numpy as np
# import re
import pathlib as pl
from pathlib import Path

# from PIL import Image

def pord(x: list):
    result = 1
    for i in x:
        result *= i
    return result

def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    stacks = [[int(x) for x in line.split()] for line in input_data.splitlines()[:-1]]
    operations =  input_data.splitlines()[-1].split()

    lines = list(zip(*stacks))

    total = 0
    for i in range(len(operations)):
        op = operations[i]
        line = lines[i]
        if op == '+':
            total += sum(line)
        elif op == '*':
            total += pord(line)

    output = total
        
    print("Answer Part 1:")
    print(output)

    
def solveB(file_name):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()


    lines = list(zip(*(input_data+ ' '*10).splitlines()))

    total = 0
    running_total = 0
    current_op = '+'
    for line in lines:
        if not line:
            continu
        n = ''.join(line[:-1]).strip()
        if n == '':
            total += running_total
            running_total = 0
            continue
        else:
            n = int(n)
        if line[-1] in ['+', '*']:
            current_op = line[-1]
            running_total = n
        else:
            if current_op == '+':
                running_total += n
            elif current_op == '*':
                running_total *= n

    total += running_total
    output = total

    print("Answer Part 2:")
    print(output)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
