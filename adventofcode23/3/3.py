import numpy as np
import re


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # for each line, get the numbers and record start and end position
    numbers = []
    for line_nr in range(lines.__len__()):
        line = lines[line_nr]
        number = 0
        start = 0
        started = False
        for i in range(line.__len__()):
            symbol = line[i]
            if symbol in '0123456789':
                if not started:
                    started = True
                    start = i
                    number += int(symbol)
                else:
                    number *= 10
                    number += int(symbol)
            else:
                if started:
                    started = False
                    numbers.append([number, line_nr, start, i - 1])
                    number = 0
                    start = 0
        if started:
            started = False
            numbers.append([number, line_nr, start, line.__len__() - 1])
            number = 0
            start = 0

    sum = 0
    # check for each number
    for number in numbers:
        # valid if there is a symbol not in [\.0-9] within start-1 and end+1 within 1 line distance
        first = max(0, number[2] - 1)
        last = min(lines[0].__len__() - 1, number[3] + 2)
        if (re.search('[^.0-9\n]', lines[number[1]][first:last])
                or re.search('[^.0-9\n]', lines[max(number[1] - 1, 0)][first:last])
                or re.search('[^.0-9\n]', lines[min(number[1] + 1, lines.__len__() - 1)][first:last])):
            # print(f'Number {number[0]} is valid')
            sum += number[0]

    print(f'The sum of all valid numbers is {sum}')

    # find the end of the number

    return


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # for each line, get the numbers and record start and end position
    numbers = []
    for line_nr in range(lines.__len__()):
        line = lines[line_nr]
        number = 0
        start = 0
        started = False
        for i in range(line.__len__()):
            symbol = line[i]
            if symbol in '0123456789':
                if not started:
                    started = True
                    start = i
                    number += int(symbol)
                else:
                    number *= 10
                    number += int(symbol)
            else:
                if started:
                    started = False
                    numbers.append([number, line_nr, start, i - 1])
                    number = 0
                    start = 0
        if started:
            started = False
            numbers.append([number, line_nr, start, line.__len__() - 1])
            number = 0
            start = 0

    # search line for gears, which are *, make a map of gears and their positions
    gears = []
    for line_nr in range(lines.__len__()):
        line = lines[line_nr]
        for i in range(line.__len__()):
            symbol = line[i]
            if symbol == '*':
                gears.append([line_nr, i])

    gearratios = 0
    # check for each number
    for gear in gears:
        adj_to_gear = 0
        product = 1
        for number in numbers:
            # if number is adjacent to gear, multiply product with number and increment adj_to_gear
            if (number[1] <= gear[0]+1 and number[1] >= gear[0]-1
                    and number[2] -1 <= gear[1] and number[3] +1 >= gear[1] ):
                product *= number[0]
                adj_to_gear += 1
                if adj_to_gear == 3:
                    break
        if adj_to_gear == 2:
            gearratios += product

    print(f'The sum of all valid gears is {gearratios}')

    return


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
