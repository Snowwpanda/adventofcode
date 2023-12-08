import math

import numpy as np
import re
import time
from collections import Counter




def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in lr and nodes of the form AAA = (BBB, CCC)
    nodes = dict()
    for line in lines:
        if re.search('^[LR]+$', line.strip()):
            directions = line.strip()
        if re.search('.*=.*\(.*\)', line):
            node = line.split('=')[0].strip()
            lr = [child.strip() for child in  re.match('.*\((.*)\)', line).group(1).split(',')]
            nodes[node] = lr

    # travel from AAA until we reach ZZZ
    current_node = 'AAA'
    pos = 0
    counter = 0
    while( True):
        if current_node == 'ZZZ':
            break
        if directions[pos] == 'L':
            current_node = nodes[current_node][0]
        elif directions[pos] == 'R':
            current_node = nodes[current_node][1]
        else:
            print('something went wrong')
            break
        pos = (pos + 1) % len(directions)
        counter += 1

    print(f'The total number of steps is {counter}')


def find_period(node, nodes, directions):
    final_node = ''
    prefix = 0
    period_len = 0
    pos = 0
    counter = 0
    curr_node = node
    visiting = dict()

    # find period starting point
    start = 0
    prefix_and_period = 0
    start_node = ''
    while( True):
        if pos in visiting.keys() and curr_node in visiting[pos]:
            start = pos
            prefix_and_period = counter
            start_node = curr_node
            break
        else:
            if pos not in visiting.keys():
                visiting[pos] = []
            visiting[pos].append(curr_node)
        if directions[pos] == 'L':
            curr_node = nodes[curr_node][0]
        elif directions[pos] == 'R':
            curr_node = nodes[curr_node][1]
        else:
            print('something went wrong')
            break
        pos = (pos + 1) % len(directions)
        counter += 1

    # find prefix

    pos = 0
    counter = 0
    curr_node = node
    period_len = 0
    record = False
    period_values = []
    while( True):
        if pos == start and curr_node == start_node:
            if counter == prefix_and_period:
                break
            prefix = counter
            period_len = prefix_and_period - prefix
            record = True
            # start with an array of false of length period_len
            period_values = [False] * period_len
        if record and curr_node[-1] == 'Z':
            period_values[counter % period_len] = curr_node
        if directions[pos] == 'L':
            curr_node = nodes[curr_node][0]
        elif directions[pos] == 'R':
            curr_node = nodes[curr_node][1]
        else:
            print('something went wrong')
            break
        pos = (pos + 1) % len(directions)
        counter += 1

    return [prefix , period_len, period_values]


class class_period:
    period_values = []
    prefix = 0
    period_len = 0
    multiple = 1
    has_single_sol = False
    sol_index = 0
    node = 'no_node'

    def __init__(self, node, nodes, directions):
        prefix, period_len, period_values = find_period(node, nodes, directions)
        self.node = node
        self.prefix = prefix
        self.period_len = period_len
        self.period_values = period_values
        self.multiple =  self.period_len // directions.__len__()

        if len([v for v in period_values if v != False]) == 1:
            self.has_single_sol = True
            filtered_vals = list(filter(lambda x: x != False, period_values))
            self.sol_index = filtered_vals.index(filtered_vals[0])

    def check(self, pos):
        return self.period_values[pos % self.period_len] != False

    def get_next(self, pos):
        if self.has_single_sol:
            return ((self.sol_index - pos + self.period_len -1) % self.period_len) +1
        else:
            for i in range(1, self.period_len):
                if self.check(pos + i):
                    return i % self.period_len








def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in lr and nodes of the form AAA = (BBB, CCC)
    nodes = dict()
    for line in lines:
        if re.search('^[LR]+$', line.strip()):
            directions = line.strip()
        if re.search('.*=.*\(.*\)', line):
            node = line.split('=')[0].strip()
            lr = [child.strip() for child in  re.match('.*\((.*)\)', line).group(1).split(',')]
            nodes[node] = lr

    curr_nodes = [node for node in nodes.keys() if node[-1] == 'A']
    periods = []
    for node in curr_nodes:
        periods.append(class_period(node, nodes, directions))

    # print all period_lengths
    for period in periods:
        print(period.period_len)

    for period in periods:
        print(period.multiple)

    # find the lowest common multiple of all period lengths
    lcm = np.lcm.reduce([period.period_len for period in periods])
    print(f'The lowest common multiple is {lcm}')
    print("not gonna work")

    print(f"The period {periods[0].node} has length {periods[0].period_len} and and a single sol at {periods[0].prefix}")

    print(f"We found out actually all periods have the same end points (at 0) so we can just take direction length times the smallest common multiple of all multipes.")

    # find smallest common multiple of all period.multiple
    lcm = 1
    for period in periods:
        lcm = math.lcm(lcm, period.multiple)
    print(f'The lowest common multiple is {lcm * directions.__len__()}..seems like a bit of a cheat though...')

    pos = 0
    single_period = periods[0]
    pos = single_period.get_next(pos)
    end = -1
    while(True):
        for period in periods[1:]:
            if not period.check(pos):
                pos = pos + single_period.get_next(pos)
                end = -1
                break
            end = pos
        if end != -1 or pos > 10000000000:
            break

    if pos > 10000000000:
        print('No solution found, try increasing the limit of 10000000000')
    else:
        print(f'The first solution is at {pos}')

    return



if __name__ == '__main__':
    solveA('input.txt')

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
