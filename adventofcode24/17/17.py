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

    A_upper = 10
    while True:
        out = run_program(A_upper, B, C, program.copy())
        if len(out) <= len(program):
            A_upper *= 2
            A_upper -= 1
        else:
            break

    def code_to_int(code):
        c = code.copy()
        c.reverse()
        return int(str(''.join([str(x) for x in c])), 8)    
    
    program_val = code_to_int(program)
    # try like a binary search:
    low = 0
    high = A_upper
    while low < high - 1:
        mid = (low + high) // 2
        out = run_program(mid, B, C, program.copy())
        if len(out) > len(program):
            high = mid            
        elif len(out) < len(program) or code_to_int(out) < program_val:
            low = mid + 1
        elif code_to_int(out) > program_val:
            high = mid
        else:
            low = mid
            break
    
    diff = code_to_int(out) - program_val
    print(diff)
    
    for i in range(low-10000, low+10000000):
        out = run_program(i, B, C, program.copy())
        diff = code_to_int(out) - program_val
        print(diff)
        if diff == 0:
            low = i
            break
      
    res = low
    
    # Print result
    print("Answer Part 2:")
    print(res)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')