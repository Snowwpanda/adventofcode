import re
import numpy as np
from functools import cmp_to_key
import sys



def solveA(file_name):

    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        list = []
        for i in range(len(lines)):
            list.append((int(lines[i].strip()), i))
            if lines[i] == '0\n':
                tuple0 = (int(lines[i].strip()), i)
        N = len(list)
        decryptedList = list.copy()
        for number in list:
            index = decryptedList.index(number)
            decryptedList.pop(index)
            decryptedList.insert((index + number[0]) % (N-1), number)

    index0 = decryptedList.index(tuple0)
    numbers = [decryptedList[(index0 + 1000) % N][0],decryptedList[(index0 + 2000) % N][0],decryptedList[(index0 + 3000) % N][0]]
    print('after decryption 1000,2000,3000:')
    print(decryptedList)
    print(numbers)
    print(sum(numbers))



def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()
        list = []
        for i in range(len(lines)):
            list.append((int(lines[i].strip()) * 811589153, i))
            if lines[i] == '0\n':
                tuple0 = (int(lines[i].strip()), i)
        N = len(list)
        decryptedList = list.copy()
        for c in range(10):
            for number in list:
                index = decryptedList.index(number)
                decryptedList.pop(index)
                decryptedList.insert((index + number[0]) % (N-1), number)

    index0 = decryptedList.index(tuple0)
    numbers = [decryptedList[(index0 + 1000) % N][0],decryptedList[(index0 + 2000) % N][0],decryptedList[(index0 + 3000) % N][0]]
    print('after decryption 1000,2000,3000:')
    print(decryptedList)
    print(numbers)
    print(sum(numbers))


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
