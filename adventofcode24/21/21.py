import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue


button_pos = {
    'A': (0, 0),
    '0': (-1, 0),
    '1': (-2, 1),
    '2': (-1, 1),
    '3': (0, 1),
    '4': (-2, 2),
    '5': (-1, 2),
    '6': (0, 2),
    '7': (-2, 3),
    '8': (-1, 3),
    '9': (0, 3),
    '<': (-2, -1),
    '>': (0, -1),
    '^': (-1, 0),
    'v': (-1, -1)
}


def translate_code(code):
    return [button_pos[button] for button in code]

def indirect_input(code, pos):
    if len(code) == 0:
        return ''
    button_pos = code.pop(0)
    instr = ''

    # while a sequence of move and press buttons may have the same number of inputs, somehow the order is important.
    # because the '<' is the most annoying key, we want to press it first and generally want to do '<v>' moves first. But we cannot cross the empty field ad (-2,0)
    # and making a zigzag would be worse. So manual fix. 
    # Order should be < v > ^  unless blocked, then '>', '^' and 'v' first.

    if (button_pos[1] == 0 and pos[0] == -2) or (button_pos[0] == -2 and pos[1] == 0):        
        while pos[0] < button_pos[0]:
            instr += '>'
            pos[0] += 1
        while pos[1] < button_pos[1]:
            instr += '^'
            pos[1] += 1
        while pos[1] > button_pos[1]:
            instr += 'v'
            pos[1] -= 1
        while pos[0] > button_pos[0]:
            instr += '<'
            pos[0] -= 1
    else:
        while pos[0] > button_pos[0]:
            instr += '<'
            pos[0] -= 1
        while pos[1] > button_pos[1]:
            instr += 'v'
            pos[1] -= 1
        while pos[0] < button_pos[0]:
            instr += '>'
            pos[0] += 1
        while pos[1] < button_pos[1]:
            instr += '^'
            pos[1] += 1
    instr += 'A'
    return instr + indirect_input(code, pos)





def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # leave away the 'A'
    codes = [line.strip() for line in lines]

    # translate to positions:
    translated_codes = [translate_code(code) for code in codes]


    code_complexity = {}
    for code in codes:
        robot0 = code
        robot1 = indirect_input(translate_code(robot0), [0, 0])
        robot2 = indirect_input(translate_code(robot1), [0, 0])
        me = indirect_input(translate_code(robot2), [0, 0])
        code_complexity[code] = len(me) * int(code[:-1])
    
    res = sum(code_complexity.values())

    
    # Print result
    print("Answer Part 1:")
    print(res)


def add_seq(seqences, amount, table = {}):
    for seq in seqences:
        if seq in table:
            table[seq] += amount
        else:
            table[seq] = amount
    return table



def indirect_input_seq(code, memo, robots = 25):

    seqences = code[:-1].split('A')

    robot = add_seq(seqences, 1, {})

    for i in range(robots +1):
        next_robot = {}
        for seq in robot:
            seq_list = []
            if seq in memo:
                seq_list = memo[seq]
            else:
                seq_inst = indirect_input(translate_code(seq + 'A'), [0,0])
                seq_list = seq_inst[:-1].split('A')
                memo[seq] = seq_list
            add_seq(seq_list, robot[seq], next_robot)
        robot = next_robot
        # me is robot 26

    inst_len = 0
    for seq, value in robot.items():
        inst_len += (len(seq) + 1 ) * value

    
    return inst_len




def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    # leave away the 'A'
    codes = [line.strip() for line in lines]

    # # test
    # codes = ['^A']

    # translate to positions:
    translated_codes = [translate_code(code) for code in codes]

    memo = {}
    code_complexity = {}
    for code in codes:
        robot = code
        inst_len = indirect_input_seq(robot, memo, robots = 25)
        code_complexity[code] = inst_len * int(code[:-1])
    
    res = sum(code_complexity.values())

    # Print result
    print("Answer Part 2:")
    print(res)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')