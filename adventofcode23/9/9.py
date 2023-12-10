import math

import numpy as np
import re
import time
from collections import Counter
# import plt function
import matplotlib.pyplot as plt


# def polyfit_with_fixed_points(n, x, y, xf, yf) :
#     mat = np.empty((n + 1 + len(xf),) * 2)
#     vec = np.empty((n + 1 + len(xf),))
#     x_n = x**np.arange(2 * n + 1)[:, None]
#     yx_n = np.sum(x_n[:n + 1] * y, axis=1)
#     x_n = np.sum(x_n, axis=1)
#     idx = np.arange(n + 1) + np.arange(n + 1)[:, None]
#     mat[:n + 1, :n + 1] = np.take(x_n, idx)
#     xf_n = xf**np.arange(n + 1)[:, None]
#     mat[:n + 1, n + 1:] = xf_n / 2
#     mat[n + 1:, :n + 1] = xf_n.T
#     mat[n + 1:, n + 1:] = 0
#     vec[:n + 1] = yx_n
#     vec[n + 1:] = yf
#     params = np.linalg.solve(mat, vec)
#     return params[:n + 1]


# n, d, f = 50, 8, 3
# x = np.random.rand(n)
# xf = np.random.rand(f)
# poly = np.polynomial.Polynomial(np.random.rand(d + 1))
# y = poly(x) + np.random.rand(n) - 0.5
# yf = np.random.uniform(np.min(y), np.max(y), size=(f,))
# params = polyfit_with_fixed_points(d, x, y, xf, yf)
# poly = np.polynomial.Polynomial(params)
# xx = np.linspace(0, 1, 1000)
# plt.plot(x, y, 'bo')
# plt.plot(xf, yf, 'ro')
# plt.plot(xx, poly(xx), '-')
# plt.show()


def poly_fit(sequence):
    length = sequence.__len__()
    curr_seq = np.array(sequence)
    next_value = sequence[-1]
    # loop while curr_seq is not empty and is not all zeros
    while curr_seq.__len__() > 0 and not np.all(curr_seq == 0):
        curr_seq = curr_seq[1:] - curr_seq[:-1]
        next_value += curr_seq[-1]

    return next_value


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read lines into a list of ints
    sequences = [[int(num) for num in line.strip().split()] for line in lines]

    # for each sequence try to match with a polynomial and calculate the next number
    sum_endvalues = 0
    for sequence in sequences:
        next_value = poly_fit(sequence)
        print(sequence)
        print(next_value)
        sum_endvalues += next_value

    print(f'The sum of the end values is {sum_endvalues}')

    return


def poly_prefit(sequence):
    curr_seq = np.array(sequence)
    pre_value = sequence[0]
    multiplier = -1
    # loop while curr_seq is not empty and is not all zeros
    while curr_seq.__len__() > 0 and not np.all(curr_seq == 0):
        curr_seq = curr_seq[1:] - curr_seq[:-1]
        pre_value += curr_seq[0] * multiplier
        multiplier *= -1

    return pre_value



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()


    # read lines into a list of ints
    sequences = [[int(num) for num in line.strip().split()] for line in lines]

    # for each sequence try to match with a polynomial and calculate the next number
    sum_prevalues = 0
    for sequence in sequences:
        pre_value = poly_prefit(sequence)
        print(sequence)
        print(pre_value)
        sum_prevalues += pre_value

    print(f'The sum of the end values is {sum_prevalues}')

    return



if __name__ == '__main__':
    solveA('input.txt')

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
