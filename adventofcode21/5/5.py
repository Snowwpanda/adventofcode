import numpy as np


def check_line(line):
    if line[0][0] == line[1][0]:
        return 1
    elif line[0][1] == line[1][1]:
        return 0
    elif line[0][0] - line[0][1] == line[1][0] - line[1][1]:
        return 2
    elif line[0][0] + line[0][1] == line[1][0] + line[1][1]:
        return 3
    else:
        return -1


def add_line(line, field):
    [a, b] = line[0]
    [c, d] = line[1]
    x_dir = 1 if c > a else 0 if c == a else -1
    y_dir = 1 if d > b else 0 if d == b else -1
    dist = max([a-c, b-d, c-a, d-b])
    for add in range(dist+1):
        field[a + (add * x_dir)][b + (add * y_dir)] += 1
    return 0


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def task5():
    f = open("input.txt", "r")
    lines = f.read().splitlines()
    f.close()
    field = np.zeros((1000, 1000))
    lines = np.array([[[int(x) for x in point.split(",")] for point in line.split(" -> ")] for line in lines])

    for line in lines:
        if check_line(line) == 0 or check_line(line) == 1:
            add_line(line, field)

    write_sol((field > 1).sum(), 1)
    print((field > 1).sum())

    for line in lines:
        if check_line(line) >= 2:
            add_line(line, field)

    write_sol((field > 1).sum(), 2)
    print((field > 1).sum())


task5()
