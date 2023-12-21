import math

import numpy as np
import re
import time
from collections import Counter
# import priority queue
import heapq

# import plt function

def run_workflow(curr_flow, workflows, part):
    ord_r = {
        'x': 0,
        'm': 1,
        'a': 2,
        's': 3
    }

    if curr_flow == 'A':
        return sum([int(rating) for rating in part])
    elif curr_flow == 'R':
        return 0

    if curr_flow not in workflows:
        print(f"Error: {curr_flow} not in workflows")
        return 0

    for step in workflows[curr_flow]:
        if ':' not in step:
            # just a step
            curr_flow = step
            return run_workflow(curr_flow, workflows, part)
        else:
            capture = re.search('^(\w)([<>])(\d+):(\w+)$', step).groups()
            rating_type, direction, rating, next_flow = capture
            if direction == '<':
                if int(part[ord_r[rating_type]]) < int(rating):
                    curr_flow = next_flow
                    return run_workflow(curr_flow, workflows, part)
            elif direction == '>':
                if int(part[ord_r[rating_type]]) > int(rating):
                    curr_flow = next_flow
                    return run_workflow(curr_flow, workflows, part)
            else:
                continue



def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    workflows = {}
    parts = []

    for line in lines:
        # read out workflows and parts where
        # workflows: in{s<1351:px,qqz}
        # {x=1679,m=44,a=2067,s=496} (always consist of the 4 ratings)
        if re.search('^(\w+)\{(((\w[<>]\d+:)?(\w+),?)+)\}$', line):
            # workflow
            capture = re.search('^(\w+)\{(((\w[<>]\d+:)?(\w+),?)+)\}$', line).groups()
            name = capture[0]
            steps = capture[1].split(',')
            workflows[name] = steps
        elif re.search('^\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$', line):
            part = re.search('^\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$', line).groups()
            parts.append(part)
        elif line == '':
            continue
        else:
            print(f"Error: line {line} not recognized")



    total_rating = 0
    for part in parts:
        curr_flow = 'in'
        total_rating += run_workflow(curr_flow, workflows, part)


    print(f"total rating is {total_rating}")


    return


def size_interval(interval):
    # interval has 4 tuples
    # return the size of the interval
    size = 1
    for i in range(4):
        if interval[i][0] > interval[i][1]:
            return 0
        else:
            size *= interval[i][1] - interval[i][0] + 1
    return size


def run_workflow_interval(curr_flow, index, workflows, interval):
    ord_r = {
        'x': 0,
        'm': 1,
        'a': 2,
        's': 3
    }


    if curr_flow == 'A':
        return size_interval(interval)
    elif curr_flow == 'R':
        return 0

    if curr_flow not in workflows:
        print(f"Error: {curr_flow} not in workflows")
        return 0

    step = workflows[curr_flow][index]
    if ':' not in step:
        # just a step
        curr_flow = step
        index = 0
        return run_workflow_interval(curr_flow, index, workflows, interval)
    else:
        capture = re.search('^(\w)([<>])(\d+):(\w+)$', step).groups()
        rating_type, direction, rating, next_flow = capture
        if direction == '<':
            if int(interval[ord_r[rating_type]][1]) < int(rating):
                curr_flow = next_flow
                index = 0
                return run_workflow_interval(curr_flow, index, workflows, interval)
            elif int(interval[ord_r[rating_type]][0]) >= int(rating):
                index += 1
                return run_workflow_interval(curr_flow, index, workflows, interval)
            else:
                # split the interval
                interval_1 = interval.copy()
                interval_1[ord_r[rating_type]] = (interval[ord_r[rating_type]][0], int(rating)-1)
                interval_2 = interval.copy()
                interval_2[ord_r[rating_type]] = (int(rating), interval[ord_r[rating_type]][1])
                sum = 0
                sum += run_workflow_interval(next_flow, 0, workflows, interval_1)
                sum += run_workflow_interval(curr_flow, index+1, workflows, interval_2)
                return sum
        elif direction == '>':
            if int(interval[ord_r[rating_type]][0]) > int(rating):
                curr_flow = next_flow
                index = 0
                return run_workflow_interval(curr_flow, index, workflows, interval)
            elif int(interval[ord_r[rating_type]][1]) <= int(rating):
                index += 1
                return run_workflow_interval(curr_flow, index, workflows, interval)
            else:
                # split the interval
                interval_1 = interval.copy()
                interval_1[ord_r[rating_type]] = (interval[ord_r[rating_type]][0], int(rating))
                interval_2 = interval.copy()
                interval_2[ord_r[rating_type]] = (int(rating)+1, interval[ord_r[rating_type]][1])
                sum = 0
                sum += run_workflow_interval(curr_flow, index+1, workflows, interval_1)
                sum += run_workflow_interval(next_flow, 0, workflows, interval_2)
                return sum
    print(f"Error: should not reach here")
    return 0


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    workflows = {}
    parts = []

    for line in lines:
        # read out workflows and parts where
        # workflows: in{s<1351:px,qqz}
        # {x=1679,m=44,a=2067,s=496} (always consist of the 4 ratings)
        if re.search('^(\w+)\{(((\w[<>]\d+:)?(\w+),?)+)\}$', line):
            # workflow
            capture = re.search('^(\w+)\{(((\w[<>]\d+:)?(\w+),?)+)\}$', line).groups()
            name = capture[0]
            steps = capture[1].split(',')
            workflows[name] = steps
        elif re.search('^\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$', line):
            part = re.search('^\{x=(\d+),m=(\d+),a=(\d+),s=(\d+)\}$', line).groups()
            parts.append(part)
        elif line == '':
            continue
        else:
            print(f"Error: line {line} not recognized")

    total_accepted = 0
    interval = [(1,4000), (1,4000), (1,4000), (1,4000)]
    # interval = [(787,787), (2655,2655), (1222,1222), (2876,2876)]
    total_accepted = run_workflow_interval("in", 0, workflows, interval)

    print(f"total accepted is {total_accepted}")


    return


if __name__ == '__main__':
    # time the solution:
    start_time = time.time()
    solveA('input.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
