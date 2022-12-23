import re
import numpy as np
from functools import cmp_to_key


def compareLists(left, right):

    for i in range(max(len(left), len(right))+1):
        if i == len(left) and i == len(right):
            return 0
        elif i == len(left):
            return 1
        elif i == len(right):
            return -1
        elif not type(left[i]) is int and not type(right[i]) is int:
            result = compareLists(left[i], right[i])
            if result != 0:
                return result
        elif type(left[i]) is int and not type(right[i]) is int:
            result = compareLists([left[i]], right[i])
            if result != 0:
                return result
        elif not type(left[i]) is int and type(right[i]) is int:
            result = compareLists(left[i], [right[i]])
            if result != 0:
                return result
        elif type(left[i]) is int and type(right[i]) is int:
            if (left[i]) < (right[i]):
                return 1
            elif (left[i]) > (right[i]):
                return -1
        else:
            print('error')


def replaceGroup(restList, groupList, counter):
    for i in range(len(restList)):
        if type(restList[i]) is list:
            restList[i] = replaceGroup(restList[i], groupList, counter)
        elif restList[i] == f'group{counter}':
            restList[i] = groupList
    return restList

def convert(i):
    if type(i) is str and i.isnumeric():
        return int(i)
    return i

def toList(string, counter):
    match = re.search('\[[^\[\]]*\]', string)
    list = [convert(i) for i in match.group()[1:-1].split(',')]
    if list == ['']:
        list = []
    if match.group() == string:
        return list
    restList = toList(f'{string[:match.start()]}group{counter}{string[match.end():]}', counter+1)
    restList = replaceGroup(restList, list, counter)
    return restList




def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..

        lines = my_file.readlines()
        sumOfIndices = 0
        for i in range((len(lines) +1 )//3):
            left = lines[i*3].strip()
            right = lines[i*3 +1].strip()
            left = toList(left, 0)
            right = toList(right, 0)
            if compareLists(left, right) >= 0:
                sumOfIndices += i + 1
            else:
                pass

        print('Sum of Pairs:')
        print(sumOfIndices)


def mergesort(packages):
    if len(packages) <= 1:
        return packages
    middle = len(packages)// 2
    firstHalf = mergesort(packages[:middle])
    secondHalf = mergesort(packages[middle:])

    sortedList = []
    i = 0
    j = 0
    while i + j < len(packages):
        if i >= middle:
            sortedList.append(secondHalf[j])
            j += 1
        elif j >= len(secondHalf):
            sortedList.append(firstHalf[i])
            i += 1
        elif compareLists(firstHalf[i], secondHalf[j]) >= 0:
            sortedList.append(firstHalf[i])
            i += 1
        else:
            sortedList.append(secondHalf[j])
            j += 1

    return sortedList





def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..

        lines = my_file.readlines()
        packages = ['[[6]]', '[[2]]']
        for line in lines:
            if line != '\n':
                packages.append(line.strip())
        for i in range(len(packages)):
            packages[i] = toList(packages[i], 0)

        packages = mergesort(packages)
        multiply = 1
        for i in range(len(packages)):
            pack = packages[i]
            if len(pack) == 1 and len(pack[0]) == 1 and pack[0][0] in [2,6]:
                multiply *= (i +1)
    print('Prod:')
    print(multiply)


if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
