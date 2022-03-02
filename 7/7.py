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


def task7():
    data = read_input()
    data = [int(i) for i in data[0].split(',')]
    median = np.median(data)
    best_position = int(median)

    spent_fuel = sum([abs(pos - best_position) for pos in data])
    print(spent_fuel, len(data), sum(data), best_position, '\n', sum(data > median))
    write_sol(spent_fuel, 1)

    ## feel bad cause i cheated here, true answer shouldn't be the average, do binary search? must be between median and average probably.
    average = np.average(data)
    best_position = int(average)

    spent_fuel = min( [ sum([(abs(pos - bp) * (abs(pos - bp) + 1)) // 2 for pos in data]) for bp in [best_position, best_position +1]] )
    print(spent_fuel, best_position, np.average(data))
    write_sol(spent_fuel, 2)

task7()