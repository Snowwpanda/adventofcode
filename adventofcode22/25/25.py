import re
import numpy as np
from functools import cmp_to_key
import sys

SNAFU_map = {
    '2' : 2,
    '1' : 1,
    '0' : 0,
    '-' : -1,
    '=' : -2,
}

SNAFU_inverse_map = {
    2 : '2',
    1 : '1',
    0 : '0',
    4 : '-',
    3 : '=',
}

def convert_SNAFU(SNAFU_string):
    SNAFU_num = [SNAFU_map[char] for char in SNAFU_string]
    n = len(SNAFU_string)
    power_of_5 = np.power(5*np.ones(n), np.arange(n-1,-1,-1))
    return sum(SNAFU_num * power_of_5)


def convert_back_SNAFU(total):
    string = ''
    while total != 0:
        rest = (total + 5) % 5
        string = SNAFU_inverse_map[rest]  + string
        total = (total + 2) // 5
    return string
    


def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        total = 0
        for line in my_file:
            num = convert_SNAFU(line.strip())
            total += num

        print('total')
        print(convert_back_SNAFU(total))


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        print('total')


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
