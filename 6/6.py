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


def task6():
    data = read_input()
    data = [int(i) for i in data[0].split(',')]
    reproduce_table = np.zeros(257)
    reproduce_table[0] = 1
    for i in range(1, 8):
        reproduce_table[i] = 2
    reproduce_table[8] = 3
    reproduce_table[9] = 3
    for i in range(10, 81):
        reproduce_table[i] = reproduce_table[i - 7] + reproduce_table[i - 9]

    total_pop = int(sum([reproduce_table[80 - i] * data.count(i) for i in range(8)]))

    print(total_pop)
    write_sol(total_pop, 1)


    for i in range(81, 257):
        reproduce_table[i] = reproduce_table[i - 7] + reproduce_table[i - 9]

    total_pop = int(sum([reproduce_table[256 - i] * data.count(i) for i in range(8)]))
    print(total_pop)
    write_sol(total_pop, 2)


task6()
