import numpy as np
import re


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        map_win = {0: 3, 1: 6, 2: 0} # 0 = draw, 1 = win, 2 = lose
        total_score = 0
        for line in my_file:
            if re.match('[A-C] [X-Z]\n?', line):
                opponent, me = line.split()
                opponent = ord(opponent) - ord('A')
                me = ord(me) - ord('X')
                winscore = map_win[((me - opponent + 3) % 3)]
                myscore = me + 1
                total_score += (winscore + myscore)
        print('Total score sums up to:')
        print(total_score)


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        map_win = {0: 3, 1: 6, 2: 0} # 0 = draw, 1 = win, 2 = lose
        total_score = 0
        for line in my_file:
            if re.match('[A-C] [X-Z]\n?', line):
                opponent, result = line.split()
                opponent = ord(opponent) - ord('A')
                result = (ord(result) - ord('X') + 2) % 3
                winscore = map_win[result]
                myscore = ((opponent + result) % 3) + 1
                total_score += (winscore + myscore)
        print('Total score sums up to:')
        print(total_score)

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
