import numpy as np


def calculate_oxy(lines):
    oxygen = lines.copy()
    pos = 0
    while len(oxygen) > 1:
        mcb = np.sign(sum([line[pos] for line in oxygen]))
        if mcb == 0:
            mcb = 1
        size = len(oxygen)
        for j in range(size):
            if j == 998:
                pass
            if oxygen[size - j - 1][pos] != mcb:
                oxygen.pop(size - 1 - j)
        pos = pos + 1
        if pos >= len(oxygen[0]):
            print("error pos")
            break
    return oxygen[0]


def calculate_co2(lines):
    co2 = lines.copy()
    pos = 0
    while len(co2) > 1:
        mcb = np.sign(sum([line[pos] for line in co2]))
        if mcb == 0:
            mcb = -1
        elif sum([line[pos] for line in co2]) * mcb < len(co2):
            mcb = mcb * -1

        size = len(co2)
        for j in range(size):
            if j == 998:
                pass
            if co2[size - j - 1][pos] != mcb:
                co2.pop(size - 1 - j)
        pos = pos + 1
        if pos >= len(co2[0]):
            print("error pos")
            break
    return co2[0]

def task3():
    f = open("input.txt", "r")
    diagnostics = f.read()
    f.close()
    lines = diagnostics.splitlines()
    print(len(lines))
    lines = [np.array([int(char) * 2 - 1 for char in line]) for line in lines]
    print(lines)
    print(sum(lines))
    most_common_bit = np.sign(sum(lines))
    most_common_bit = (most_common_bit + 1) // 2
    print(most_common_bit)
    gamma = int(''.join(str(digit) for digit in most_common_bit), 2)
    epsilon = int(''.join(str(digit) for digit in -most_common_bit + 1), 2)
    if gamma + epsilon != 2 ** 12 - 1:
        print("something went wrong, gamma+eps != 2**12-1")
    power_cons = gamma * epsilon

    f = open(f'output_1.txt', 'w')
    f.write(f'{power_cons}\n')
    print(power_cons, epsilon, gamma, int(''.join(str(digit) for digit in -most_common_bit + 1), 2))
    f.close()

    oxygen = (calculate_oxy(lines) + 1) // 2
    co2 = (calculate_co2(lines) + 1) // 2
    oxygen = int(''.join(str(digit) for digit in oxygen), 2)
    co2 = int(''.join(str(digit) for digit in co2), 2)
    ls_rating = oxygen * co2
    print(ls_rating)
    f = open(f'output_2.txt', 'w')
    f.write(f'{ls_rating}\n')
    f.close()


task3()
