import numpy as np


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    f.close()
    return data


def count_number_in_output(data, num):
    if num == 1:
        lines = 2
    elif num == 4:
        lines = 4
    elif num == 7:
        lines = 3
    elif num == 8:
        lines = 7

    count = 0
    for line in data:
        for o in range(10, 15):
            if len(line[o]) == lines:
                count += 1
    return count


def output_value(line):
    numconcat = ''.join(
        line[0:10] + [num for num in line[0:10] if len(num) < 6] + [num for num in line[0:10] if len(num) < 4] + [num
                                                                                                                  for
                                                                                                                  num in
                                                                                                                  line[
                                                                                                                  0:10]
                                                                                                                  if
                                                                                                                  len(num) < 5])
    a = numconcat.count('a')
    b = numconcat.count('b')
    c = numconcat.count('c')
    d = numconcat.count('d')
    e = numconcat.count('e')
    f = numconcat.count('f')
    g = numconcat.count('g')
    ## unscrambled should be a =
    numer_dict = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
    }
    numer_dict = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
    }
    num_to_digit = {
        75: 0,
        37: 1,
        59: 2,
        73: 3,
        58: 4,
        64: 5,
        69: 6,
        51: 7,
        87: 8,
        82: 9,
    }
    out_num = 0
    for i in range(4):
        letter_num = sum([numer_dict[char] for char in line[-i-1]])
        out_num += num_to_digit[letter_num] * (10**i)

    return out_num

def task8():
    data = read_input()
    data = [line.split() for line in data]
    ones = count_number_in_output(data, 1)
    fours = count_number_in_output(data, 4)
    sevens = count_number_in_output(data, 7)
    eights = count_number_in_output(data, 8)

    write_sol(ones + fours + sevens + eights, 1)
    print(ones + fours + sevens + eights)

    ## unscrambled = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abdcefg', 'abdcfg']
    answer = sum([output_value(line) for line in data])
    write_sol(answer, 2)
    print(answer)


task8()
