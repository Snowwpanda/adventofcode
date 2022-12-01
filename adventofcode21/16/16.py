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


hex_trans = {
    '0': [0, 0, 0, 0],
    '1': [0, 0, 0, 1],
    '2': [0, 0, 1, 0],
    '3': [0, 0, 1, 1],
    '4': [0, 1, 0, 0],
    '5': [0, 1, 0, 1],
    '6': [0, 1, 1, 0],
    '7': [0, 1, 1, 1],
    '8': [1, 0, 0, 0],
    '9': [1, 0, 0, 1],
    'A': [1, 0, 1, 0],
    'B': [1, 0, 1, 1],
    'C': [1, 1, 0, 0],
    'D': [1, 1, 0, 1],
    'E': [1, 1, 1, 0],
    'F': [1, 1, 1, 1]
}


def translate_hex(param):
    bits = []
    for char in param:
        bits += hex_trans[char]
    return bits


def next_bits(num, data, pos):
    p = pos[0]
    pos[0] = p + num
    return data[p: p + num]


def bin_to_dec(bit_list):
    return sum([bit_list[-i - 1] * 2 ** i for i in range(len(bit_list))])


def read_next_package(data, pos):
    version = bin_to_dec(next_bits(3, data, pos))
    type = bin_to_dec(next_bits(3, data, pos))
    content = []
    if type == 4:
        literal = []
        while True:
            bit = next_bits(1, data, pos)[0]
            literal += next_bits(4, data, pos)
            if bit == 0:
                break
        content = literal
    else:
        len_id = next_bits(1, data, pos)[0]
        if len_id == 1:
            num_packs = bin_to_dec(next_bits(11, data, pos))
            for pack in range(num_packs):
                content.append(read_next_package(data, pos))
        else:
            bit_len = bin_to_dec(next_bits(15, data, pos))
            p = pos[0]
            while pos[0] < p + bit_len:
                content.append(read_next_package(data, pos))

    return (version, type, content)


def get_sum_vers(packages):
    vers_sum = 0
    for package in packages:
        vers_sum += package[0]
        if package[1] != 4:
            vers_sum += get_sum_vers(package[2])
    return vers_sum


def apply_function(type, content):
    if type == 0:
        return sum(content)
    elif type == 1:
        prod = 1
        for num in content:
            prod *= num
        return prod
    elif type == 2:
        return min(content)
    elif type == 3:
        return max(content)
    elif type == 5:
        if content[0] > content[1]:
            return 1
        else:
            return 0
    elif type == 6:
        if content[0] < content[1]:
            return 1
        else:
            return 0
    elif type == 7:
        if content[0] == content[1]:
            return 1
        else:
            return 0


def read_next_package_value(data, pos):
    version = bin_to_dec(next_bits(3, data, pos))
    type = bin_to_dec(next_bits(3, data, pos))
    content = []
    if type == 4:
        literal = []
        while True:
            bit = next_bits(1, data, pos)[0]
            literal += next_bits(4, data, pos)
            if bit == 0:
                break
        return bin_to_dec(literal)
    else:
        len_id = next_bits(1, data, pos)[0]
        if len_id == 1:
            num_packs = bin_to_dec(next_bits(11, data, pos))
            for pack in range(num_packs):
                content.append(read_next_package_value(data, pos))
        else:
            bit_len = bin_to_dec(next_bits(15, data, pos))
            p = pos[0]
            while pos[0] < p + bit_len:
                content.append(read_next_package_value(data, pos))
        return apply_function(type, content)



    return 0


def task16():
    data = read_input()[0]

    print(translate_hex('8A004A801A8002F478'))
    print(translate_hex(data))
    data = translate_hex(data)
    # data = translate_hex('D2FE28')
    pos = [0]
    packages = []
    packages.append(read_next_package(data, pos))
    vers_sum = get_sum_vers(packages)

    print(packages[0][0])
    print(vers_sum)
    write_sol(vers_sum, 1)

    pos = [0]
    result = read_next_package_value(data, pos)
    print(result)
    write_sol(result, 2)


print(ord('0'))
task16()
