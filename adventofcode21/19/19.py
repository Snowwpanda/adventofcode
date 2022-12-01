import queue
import numpy as np
from collections import deque
import collections

set_of_rotations = [[sign_x, sign_y, sign_z, rotate]
                    for sign_x in [1, -1]
                    for sign_y in [1, -1]
                    for sign_z in [1, -1]
                    for rotate in [0, 1, 2]
                    ]


def write_sol(out, num):
    f = open(f'output_{num}.txt', 'w')
    f.write(f'{out}\n')
    f.close()


def read_input():
    f = open("input.txt", "r")
    data = f.read().splitlines()
    f.close()
    return data


def read_input(string):
    f = open(string, "r")
    data = f.read().splitlines()
    f.close()
    return data


def flip_beacon(beacon, shift, rot):
    tmp_list = beacon[:rot[3]].copy()
    for i in range(rot[3]):
        beacon[i] = beacon[(i + rot[3]) % 3]
    for i in range(3, rot[3], -1):
        beacon[i] = beacon[(i + rot[3]) % 3]
    for i in range(rot[3]):
        beacon[(i +3-rot[3] )%3] = tmp_list
    for i in range(3):
        beacon[i] = rot[i] * beacon[i] + shift[i]
    return beacon


def recoordinate_scanner(scanner, shift, rot):
    for i in range(len(scanner)):
        scanner[i] = flip_beacon(scanner[i], shift, rot)


def try_overlap(scanner, new_scanner):
    pass


def task19():
    data = read_input("example.txt")
    print(data)
    scanners = []
    scanner = []
    for line in data:
        if line == '':
            scanners.append(np.array(scanner))
            scanner = []
        elif line[-1] == '-':
            pass
        else:
            scanner.append([int(s) for s in line.split(',')])
    reviewed = []
    bfs_queue = queue.Queue()
    vis = set()
    not_vis = set(scanners)
    while not bfs_queue.empty():
        scanner = bfs_queue.get()
        for new_scanner in scanners:
            overlap, shift, rot = try_overlap(scanner, new_scanner)
            if overlap:
                recoordinate_scanner(new_scanner, shift, rot)
                bfs_queue.put(new_scanner)
        reviewed.append(scanner)

    set_of_beacons = set([beacon for scanner in reviewed for beacon in scanner])
    print(len(set_of_beacons))
    # write_sol(len(set_of_beacons), 1)

    return


task19()
