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


def insert_step(template, inserts):
    insert_out = template[0]
    for char in template[1:]:
        if insert_out[-1] + char in inserts:
            insert_out += inserts[insert_out[-1] + char]
        insert_out += char
    return insert_out


def apply_step(inserts, list_of_inserts):
    new_list_of_inserts = dict()
    for pair in list_of_inserts:
        res1 = pair[0] + inserts[pair]
        res2 = inserts[pair] + pair[1]
        if res1 in inserts and res2 in inserts:
            new_list_of_inserts[pair] = list_of_inserts[res1].copy() + list_of_inserts[res2].copy()
        elif res1 in inserts:
            new_list_of_inserts[pair] = list_of_inserts[res1].copy()
        elif res2 in inserts:
            new_list_of_inserts[pair] = list_of_inserts[res2].copy()
        else:
            new_list_of_inserts[pair] = np.zeros(26, dtype=np.ulonglong)
        new_list_of_inserts[pair][ord(inserts[pair]) - ord('A')] += 1

    for pair in list_of_inserts:
        list_of_inserts[pair] = new_list_of_inserts[pair]


def task14():
    data = read_input()
    template = data[0]

    inserts = dict([line.split(' -> ') for line in data[2:]])

    fresh_template = template
    for step in range(10):
        fresh_template = insert_step(fresh_template, inserts)

    occ = [fresh_template.count(char) for char in fresh_template]
    occ.sort()
    diff = occ[-1] - occ[0]
    print(occ)
    print(diff)
    write_sol(diff, 1)

    list_of_inserts = [pair for pair in inserts]

    count = np.zeros((len(inserts), 26), dtype=np.ulonglong)
    for i in range(len(list_of_inserts)):
        count[i][ord(inserts[list_of_inserts[i]]) - ord('A')] += 1
    list_of_inserts = dict(zip(list_of_inserts, count))

    starting_pairs = [''.join(pair) for pair in zip(template[:-1], template[1:])]
    for step in range(39):
        apply_step(inserts, list_of_inserts)

    end_res_letters = np.zeros(26, dtype=np.ulonglong)
    for pair in starting_pairs:
        end_res_letters += list_of_inserts[pair]
    for char in template:
        end_res_letters[ord(char) - ord('A')] += 1

    high = np.amax(end_res_letters)
    nonzero = [num for num in end_res_letters if num != 0]
    low = min(nonzero)
    print(high - low)
    write_sol(high - low, 2)


print(ord('A'))
task14()
