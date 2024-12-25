import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # parse input
    A, B, C = 0, 0, 0
    program = []
    for line in lines:
        # if starts with Register
        if line.startswith("Register"):
            letter, val = re.match(r"Register (\w): (\d+)", line).groups()
            if letter == 'A':
                A = int(val)
            elif letter == 'B':
                B = int(val)
            elif letter == 'C':
                C = int(val)
        elif line.startswith("Program"):
            seq = re.match(r"Program: ([\d,]+)", line).groups()[0]
            program = [int(x) for x in seq.split(",")]

    
    out = run_program(A, B, C, program)
        
    
    res = ','.join([str(x) for x in out])
    
    # Print result
    print("Answer Part 1:")
    print(res)


def run_program(A_orig, B, C, program):
    A = A_orig
    def combo(l_operand):
        if l_operand < 4:
            return l_operand
        elif l_operand == 4:
            return A
        elif l_operand == 5:
            return B
        elif l_operand == 6:
            return C
        else:
            print("Error")
            return -1

    out = []
    pointer = 0
    while pointer <= len(program)-2:
        instruction = program[pointer]
        l_operand = program[pointer+1]

        if instruction == 0:
            A = A // (2**combo(l_operand))
        elif instruction == 1:
            B = B ^ l_operand
        elif instruction == 2:
            B = combo(l_operand) % 8
        elif instruction == 3:
            if A != 0:
                pointer = l_operand
                continue
        elif instruction == 4:
            B = B ^ C
        elif instruction == 5:
            out.append(combo(l_operand) % 8)
        elif instruction == 6:
            B = A // (2**combo(l_operand))
        elif instruction == 7:
            C = A // (2**combo(l_operand))
        else:
            print("Unknown instruction")
        pointer += 2
    return out



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


        # parse input
    A, B, C = 0, 0, 0
    program = []
    for line in lines:
        # if starts with Register
        if line.startswith("Register"):
            letter, val = re.match(r"Register (\w): (\d+)", line).groups()
            if letter == 'A':
                A = int(val)
            elif letter == 'B':
                B = int(val)
            elif letter == 'C':
                C = int(val)
        elif line.startswith("Program"):
            seq = re.match(r"Program: ([\d,]+)", line).groups()[0]
            program = [int(x) for x in seq.split(",")]

    # A is processed in pieces of 3 bits, output is only dependend on the last 8 + 3 bits
    possible_outputs = [0] * (2 ** (8+3))
    for i in range(0, 2 ** (8+3)):
        possible_outputs[i] = run_program(i, B, C, program)

    # find A that gives the same output as the input
    A = []
    A = calc_A(A, possible_outputs, program)
        


    res = sum([ d * (8**(len(A)-i-1) ) for (i, d) in enumerate(A)])

    
    # Print result
    print("Answer Part 2:")
    print(res)

def calc_A(A, possible_outputs, program):
    if len(A) == len(program):
        return A
    index = len(A)
    next_out = program[-index - 1]
    # only dependent on last 8 bits, so last 3 groups of 3 bits
    prefix = sum([x * (8 ** (len(A[-3:])-i)) for i, x in enumerate(A[-3:])]) % (2**11) 
    for i in range(0, 8):
        if possible_outputs[i + prefix][0] == next_out:
            full_A = calc_A(A + [i], possible_outputs, program)
            if full_A:
                return full_A
    else:
        return False
if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')