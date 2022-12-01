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


close_dict = {
    '[': ']',
    '{': '}',
    '<': '>',
    '(': ')'
}
point_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
c_dict = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def illegal_p(line):
    s = []
    for char in line:
        if char in close_dict:
            s.append(close_dict[char])
        elif char == s.pop():
            pass
        else:
            return True, point_dict[char]

    c_points = 0
    s.reverse()
    for char in s:
        c_points = c_points * 5 + c_dict[char]
    return False, c_points


def task10():
    data = read_input()
    points = 0
    c_points = []
    for line in data:
        b, res_line = illegal_p(line)
        if b:
            points += res_line
        else:
            c_points.append(res_line)

    print(points)
    write_sol(points, 1)

    print(int(np.median(np.array(c_points))))
    write_sol(int(np.median(np.array(c_points))), 2)


task10()
