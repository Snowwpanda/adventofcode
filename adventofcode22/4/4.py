import numpy as np
import re


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        
        total_score = 0
        for line in my_file:
            line = line.strip()
            if not re.match('\d+-\d+,\d+-\d+', line):
                print('wrong format')
                continue
            first_elf, second_elf = [[int(i) for i in interval.split('-')] for interval in line.split(',')]
            if (first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]) \
                or (first_elf[0] <= second_elf[0] and  first_elf[1] >= second_elf[1]):
                total_score += 1
        print('Number of pairs containing each other:')
        print(total_score)


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        total_score = 0
        for line in my_file:
            line = line.strip()
            if not re.match('\d+-\d+,\d+-\d+', line):
                print('wrong format')
                continue
            first_elf, second_elf = [[int(i) for i in interval.split('-')] for interval in line.split(',')]
            if (first_elf[0] <= second_elf[1] and first_elf[1] >= second_elf[0]) :
                total_score += 1
        print('Number of pairs containing each other:')
        print(total_score)

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
