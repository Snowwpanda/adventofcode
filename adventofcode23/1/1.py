import numpy as np
import re

def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    calibration_values = []
    for line in lines:
        number = 0
        check = 0
        for pos in line:
            # check if it is a digit
            if pos.isdigit():
                number = number + int(pos) * 10
                check += 1
                break
        # for loop over line but in reverse
        for pos in line[::-1]:
            # check if it is a digit
            if pos.isdigit():
                number = number + int(pos)
                check += 1
                break
        if check != 2:
            print("ERROR")

        calibration_values.append(number)

    print(calibration_values)
    # print sum
    print(sum(calibration_values))

def solveB(file_name):

    # map digits to numbers
    digit_map = {"zero": 0,
                 "one" : 1,
                 "two" : 2,
                 "three": 3,
                 "four": 4,
                 "five": 5,
                 "six": 6,
                 "seven": 7,
                 "eight": 8,
                 "nine": 9,}

    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    calibration_values = []
    for line in lines:
        number = 0
        check = 0
        for i in range(0, len(line)):
            # get first digit in line
            if line[i].isdigit():
                number = number + int(line[i]) * 10
                check += 1
                break

            for digit in digit_map.keys():
                if re.match(f"({digit}).*", line[i:]):
                    number = number + digit_map[digit] * 10
                    check += 1
                    break
            if check == 1:
                break

        # for loop over line but in reverse
        for i in range(len(line)-1, 0-1, -1):
            # get first digit in line
            if line[i].isdigit():
                number = number + int(line[i])
                check += 1
                break

            for digit in digit_map.keys():
                if re.match(f"({digit}).*", line[i:]):
                    number = number + digit_map[digit]
                    check += 1
                    break
            if check == 2:
                break

        if check != 2:
            print("ERROR")
        calibration_values.append(number)

    print(calibration_values)
    # print sum
    print(sum(calibration_values))





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')