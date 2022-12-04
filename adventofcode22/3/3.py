import numpy as np
import re


def priority(letter):
    if re.match('[a-z]', letter):
        return ord(letter) - ord('a') + 1
    if re.match('[A-Z]', letter):
        return ord(letter) - ord('A') + 27
    print('Not a letter')
    return 0

def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        
        total_score = 0
        for line in my_file:
            line = line.strip()
            if re.match('[a-zA-Z]*', line):
                first_half = line[:len(line)//2]
                second_half = line[len(line)//2:]
                intersection_letter = set(first_half).intersection(second_half).pop()
                total_score += priority(intersection_letter)
        print('Total priorities sums up to:')
        print(total_score)


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        total_score = 0
        group_member = 0
        common_items = {}
        badge = 'a'
        for line in my_file:
            line = line.strip()
            if re.match('[a-zA-Z]*', line):
                if group_member == 0:
                    common_items = set(line)
                    group_member = 1
                elif group_member == 1:
                    common_items = common_items.intersection(line)
                    group_member = 2
                elif group_member == 2:
                    badge = common_items.intersection(line).pop()
                    total_score += priority(badge)
                    group_member =0

        print('Total badge priorities sums up to:')
        print(total_score)

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
