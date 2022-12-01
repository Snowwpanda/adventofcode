import queue
import numpy as np
from collections import deque


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    f.close()
    return data


def get_split(snail_str):
    counter = 0
    for i in range(len(snail_str)):
        char = snail_str[i]
        if char == '[':
            counter += 1
        elif char == ']':
            counter -= 1
        elif counter == 1 and char == ',':
            return i
        else:
            continue


def make_numeric(snail_str):
    if snail_str.isnumeric():
        return int(snail_str)
    else:
        split = get_split(snail_str)
        return [make_numeric(snail_str[1:split]), make_numeric(snail_str[split + 1:-1])]


# def try_split(snail_num):
#     snail1 = snail_num[0]
#     snail2 = snail_num[1]
#     if type(snail1) == int:
#         if snail1 >= 10:
#             snail_num[0] = [snail1 // 2, (snail1+1)//2]
#             return True
#     else:
#         if try_split(snail_num[0]):
#             return True
#     if type(snail2) == int:
#         if snail2 >= 10:
#             snail_num[1] = [snail2 // 2, (snail2 + 1) // 2]
#             return True
#     else:
#         if try_split(snail_num[1]):
#             return True
#     return False


# def try_explode(snail_num, param):
#     if param == 0:
#         return True
#     if type(snail_num[0]) != int:
#         if try_explode(snail_num[0], param - 1):
#             return True
#     if type(snail_num[1]) != int:
#         if try_explode(snail_num[1], param - 1):
#             return True
#     return False


def add_left_num(snail_num, pos, param):
    for i in range(pos - 1, -1, -1):
        if type(snail_num[i]) == int:
            snail_num[i] += param
            return


def add_right_num(snail_num, pos, param):
    for i in range(pos, len(snail_num)):
        if type(snail_num[i]) == int:
            snail_num[i] += param
            return

def explode(snail_num, pos):
    add_left_num(snail_num, pos, snail_num[pos + 1])
    add_right_num(snail_num, pos + 4, snail_num[pos + 3])
    snail_num.pop(pos)
    snail_num.pop(pos)
    snail_num.pop(pos)
    snail_num.pop(pos)
    snail_num.pop(pos)
    snail_num.insert(pos, 0)
    return


def try_explode(snail_num):
    tick_tock = 0
    for i in range(len(snail_num)):
        char = snail_num[i]
        if char == '[':
            tick_tock += 1
            if tick_tock == 5:
                explode(snail_num, i)
                return True
        elif char == ']':
            tick_tock -= 1
    return False


def try_split(snail_num):
    for i in range(len(snail_num)):
        if type(snail_num[i]) == int and snail_num[i] >= 10:
            big = snail_num.pop(i)
            snail_num.insert(i, ']')
            snail_num.insert(i, (big+1)//2)
            snail_num.insert(i, ',')
            snail_num.insert(i, big //2)
            snail_num.insert(i, '[')
            return True

    return False


def snail_reduce(snail_num):
    while True:
        if try_explode(snail_num):
            continue
        if try_split(snail_num):
            continue
        break
    return 0


def pull_apart(line):
    list = [char for char in line]
    for i in range(len(list)):
        if list[i].isnumeric():
            list[i] = int(list[i])
    return list


def magnitude(snail_num):
    if type(snail_num) == int:
        return snail_num
    else:
        return (magnitude(snail_num[0]) * 3) + (magnitude(snail_num[1]) * 2)


def task18():
    data = read_input()
    snail_num = pull_apart(data[0])
    for line in data[1:]:
        snail_num = ['['] + snail_num +[ ',' ]+ pull_apart(line) + [']']
        snail_reduce(snail_num)

    snail_num = ''.join([str(ele) for ele in snail_num])
    snail_num = make_numeric(snail_num)

    print(snail_num)


    final_sum = magnitude(snail_num)
    print(final_sum)
    write_sol(final_sum, 1)

    highest_mag = (-1,-1, 0)
    for i in range(len(data)):
        for j in range(len(data)):
            sum_snail =  ['['] + pull_apart(data[i]) +[ ',' ]+ pull_apart(data[j]) + [']']
            snail_reduce(sum_snail)
            sum_snail = ''.join([str(ele) for ele in sum_snail])
            sum_snail = make_numeric(sum_snail)
            sum_snail = magnitude(sum_snail)
            if magnitude(sum_snail) > highest_mag[2]:
                highest_mag = (i, j, magnitude(sum_snail))

    print(highest_mag)
    write_sol(highest_mag[2], 2)


task18()
