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
    # Order should be < v  ^ > unless blocked, then '>', '^' and 'v' first.

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
        while pos[1] < button_pos[1]:
            instr += '^'
            pos[1] += 1
        while pos[0] < button_pos[0]:
            instr += '>'
            pos[0] += 1
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





pos_seq = [
    '>A',
    '^A',
    'vA',
    '<A',
    '<vA',
    '<^A',
    '>vA',
    '>^A',
    'v<A',
    'v>A',
    '^<A',
    '^>A',
]




map_movement = {
    (0,0): [''],
    (-1,0): ['<'],
    (1,0): ['>'],
    (0,1): ['^'],
    (0,-1): ['v'],
    (1,1) : ['>^','^>'],
    (-1,-1): ['<v','v<'],
    (1,-1): ['>v','v>'],
    (-1,1): ['<^','^<'],
}

def max_seq_duration(seq, seq_duration):
    pos = [0,0] 
    cost = 0
    for index in range(len(seq)):
        next_symbol = seq[index]
        next_button = button_pos[next_symbol]
        
        diff = (next_button[0] - pos[0], next_button[1] - pos[1])
        # reduce diff to 1:
        cost += max(abs(diff[0]) -1 , 0)
        cost += max(abs(diff[1]) -1 , 0)
        movement = (np.sign(diff[0]), np.sign(diff[1]))
            
        if (next_button[1] == 0 and pos[0] == -2) or (next_button[0] == -2 and pos[1] == 0): 
            if movement == (1,-1):
                cost += seq_duration['>vA']
                pos = [next_button[0], next_button[1]]
                continue
            elif movement == (-1,-1):
                cost += seq_duration['v<A']
                pos = [next_button[0], next_button[1]]
                continue
            elif movement == (-1,1):
                cost += seq_duration['^<A']
                pos = [next_button[0], next_button[1]]
                continue
            elif movement == (1,1):
                cost += seq_duration['>^A']
                pos = [next_button[0], next_button[1]]
                continue
        else:
            cost += min([seq_duration[seq + 'A'] for seq in map_movement[movement]])
            pos = [next_button[0], next_button[1]]

    return cost


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    # leave away the 'A'
    codes = [line.strip() for line in lines]

    # first for me
    seq_duration = {}
    for seq in pos_seq:
        seq_duration[seq] = len(seq)

    for robot_n in range(25):
        next_seq_duration = {}
        for next_seq in pos_seq:
            next_seq_duration[next_seq] = max_seq_duration(next_seq, seq_duration)
        seq_duration = next_seq_duration

        
        # < before v and ^, ^, v before >    
        if seq_duration['<vA'] > seq_duration['v<A']:
            print('heuristic was wrong at robot ', robot_n)
        if seq_duration['<^A'] > seq_duration['^<A']:
            print('heuristic was wrong at robot ', robot_n)
        if seq_duration['>^A'] < seq_duration['^>A']:
            print('heuristic was wrong at robot ', robot_n)
        if seq_duration['>vA'] < seq_duration['v>A']:
            print('heuristic was wrong at robot ', robot_n)

    
    complexity = [max_seq_duration(code, seq_duration) * int(code[:-1]) for code in codes]
    
    res = sum(complexity)

    # wrong 319566753494332
    # wrong     32889876332

    # Print result
    print("Answer Part 2:")
    print(res)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')