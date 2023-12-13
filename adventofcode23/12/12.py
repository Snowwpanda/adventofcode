import math

import numpy as np
import re
import time
from collections import Counter
# import plt function


def possibilities(springs, arrangement):
    if arrangement.__len__() == 0:
        return 1

    possible_prefix = springs.__len__() - (arrangement.__len__() - 1) - sum(arrangement)
    if possible_prefix < 0:
        return 0
    count = 0
    if arrangement.__len__() == 1:
        for i in range(possible_prefix+1):
            if re.match(rf'[.?]{{{i}}}[?#]{{{arrangement[0]}}}[.?]*$', springs):
                count += 1
        return count
    else:
        for i in range(possible_prefix+1):
            if re.match(rf'[.?]{{{i}}}[?#]{{{arrangement[0]}}}[.?]', springs):
                count += possibilities(springs[i+arrangement[0]+1:], arrangement[1:])


    return count


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    count_possibilities = 0
    for line in lines:
        if re.search(r'[.?#]+ (\d,)*\d', line):
            print(line + f"{ ' ' * (40 - line.__len__()) }", end='')
            springs, arrangement = line.split()
            arrangement = [int(number) for number in arrangement.split(',')]
            increment = possibilities(springs, arrangement)
            count_possibilities += increment
            print(f'{increment} possibilities, total count now {count_possibilities}')

    print(f'The number of possibilities is {count_possibilities}')


    return


def possibilities_singleblock(springs, arrangement):
    if arrangement.__len__() == 0:
        return 1
    if springs.__len__() < sum(arrangement[0]) + arrangement[0].__len__() - 1:
        return 0
    if arrangement.__len__() == 1:
        return possibilities(springs, arrangement[0])

    if springs[0] == '#':
        if springs[arrangement[0]] != '?':
            return 0
        return possibilities_singleblock(springs[arrangement[0]+1:], arrangement[1:])


    pass


def possibilities_binary(springs, arrangement):
    if arrangement.__len__() == 0:
        return 1

    possible_prefix = springs.__len__() - (arrangement.__len__() - 1) - sum(arrangement)
    if possible_prefix < 0:
        return 0
    count = 0
    if arrangement.__len__() <= 2:
        return possibilities(springs, arrangement)

    mid_a = arrangement.__len__() // 2

    pre_springs = sum(arrangement[:mid_a])
    post_springs = sum(arrangement[mid_a+1:])
    prefix = re.match(rf'([.]*[?#][.]*){{{pre_springs}}}', springs).end()
    postfix = re.search(rf'[.]*([.]*[?#][.]*){{{post_springs}}}$', springs).start()

    for i in range( prefix-1, postfix+1 - arrangement[mid_a]-2 +1):
        if re.match(rf'[.?][?#]{{{arrangement[mid_a]}}}[.?]', springs[i:i+arrangement[mid_a]+2]):
            count += possibilities_binary(springs[i+arrangement[mid_a]+2:], arrangement[mid_a+1:])  * possibilities_binary(springs[:i], arrangement[:mid_a])

    return count


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    count_possibilities = 0
    for line in lines:
        if re.search(r'[.?#]+ (\d,)*\d', line):
            print(line + f"{ ' ' * (40 - line.__len__()) }", end='')
            springs, arrangement = line.split()
            # multiply springs and arrangements by 5
            arrangement = [int(number) for number in arrangement.split(',')]  * 5
            springs = '?'.join([springs] * 5)
            increment = possibilities_binary(springs, arrangement)
            count_possibilities += increment
            print(f'{increment} possibilities, total count now {count_possibilities}')

    print(f'The number of possibilities is {count_possibilities}')

    # .?.??.?.?? 1,1                          34940426 possibilities, total count now 1088006519007
    # The number of possibilities is 1088006519007
    # B: --- 619.3437280654907 seconds ---


    return





if __name__ == '__main__':
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
