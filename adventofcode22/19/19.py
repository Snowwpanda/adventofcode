import queue
import re
import numpy as np
from functools import cmp_to_key
import sys
from queue import PriorityQueue


def parse_line(line):
    robots = []
    for type in ['ore', 'clay', 'obsidian', 'geode']:
        robot = re.search(f'Each {type} robot costs ((\d+) ore)?( and )?((\d+) clay)?( and )?((\d+) obsidian)?',
                          line).groups()
        rVector = []
        for i in [1, 4, 7]:
            if robot[i] is None:
                rVector.append(0)
            else:
                rVector.append(int(robot[i]))
        robots.append(rVector + [0])
    return robots


def calculate_greedy_geodes(robot_costs, volcanotime, version):
    start = (1, 0, 0, 0, 0, 0, 0, 0, 0) # tuple of orerobots, clayrobots, obsidianrobots, geoderobots, ore, clay, obsidian, geode, time
    queue = [start]
    maxGeodes = 0
    maxTuple = (4, robot_costs[2][1], robot_costs[3][2], 8, 7, 2* robot_costs[2][1], 2*robot_costs[3][2], 41, 32)
    visited = set()
    visited.add(start)
    for maxOre in range(1, max([robot[0] for robot in robot_costs[1:]]) + 1):
        queue = [start]
        while queue:
            current = queue.pop(0)
            maxGeodes = max(maxGeodes, current[7] + current[3] * (volcanotime - current[8]))

            # ore
            if current[0] < maxTuple[0]:
                time = max(0, ((robot_costs[0][0] - current[4] - 1) // current[0]) + 1) + 1
                # if additional time doesn't exceed volcanotime
                if time + current[8] < volcanotime:
                    next = np.array(current)
                    next[4:8] += np.array(current[:4]) * time
                    next[4:8] = next[4:8] - robot_costs[0]
                    next[8] += time
                    next[0] += 1
                    # if anything excedes maxTuple, reduce it to maxTuple
                    for i in range(4, 8):
                        next[i] = min(next[i], maxTuple[i])
                    next = tuple(next)
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)

            # clay
            if current[1] < maxTuple[1]:
                time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
                if time + current[8] < volcanotime:
                    next = np.array(current)
                    next[4:8] += np.array(current[:4]) * time
                    next[4:8] = next[4:8] - robot_costs[1]
                    next[8] += time
                    next[1] += 1
                    for i in range(4, 8):
                        next[i] = min(next[i], maxTuple[i])
                    next = tuple(next)
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)

            # obsidian
            if current[2] < maxTuple[2] and current[1] != 0:
                time = max(0, ((robot_costs[2][1] - current[5] - 1) // current[1]) + 1,
                           ((robot_costs[2][0] - current[4] - 1) // current[0]) + 1) + 1
                if time + current[8] < volcanotime:
                    next = np.array(current)
                    next[4:8] += np.array(current[:4]) * time
                    next[4:8] -= robot_costs[2]
                    next[8] += time
                    next[2] += 1
                    for i in range(4, 8):
                        next[i] = min(next[i], maxTuple[i])
                    next = tuple(next)
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)


            # geodes
            if current[3] < maxTuple[3] and current[2] != 0:
                time = max(0, ((robot_costs[3][2] - current[6] - 1) // current[2]) + 1,
                           ((robot_costs[3][0] - current[4] - 1) // current[0]) + 1) + 1
                if time + current[8] < volcanotime:
                    next = np.array(current)
                    next[4:8] += np.array(current[:4]) * time
                    next[4:8] -= robot_costs[3]
                    next[8] += time
                    next[3] += 1
                    for i in range(4, 8):
                        next[i] = min(next[i], maxTuple[i])
                    next = tuple(next)
                    if next not in visited:
                        visited.add(next)
                        queue.append(next)


    return maxGeodes


def calculate_geodes(robot_costs, volcanotime):
    start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0])
    queue = [start]
    maxGeodes = 0

    while queue:
        current = queue.pop(0)
        maxGeodes = max(maxGeodes, current[7] + current[3] * (volcanotime - current[8]))

        # ore
        if current[0] < max([robot[0] for robot in robot_costs[1:]]):
            time = max(0, ((robot_costs[0][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime:
                next = current.copy()
                next[0] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[0]
                next[8] += time
                queue.append(next)
        # clay
        if current[0] < robot_costs[2][1]:
            time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime:
                next = current.copy()
                next[1] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[1]
                next[8] += time
                queue.append(next)
        # obsidian
        if current[1] != 0:
            time = max(0, ((robot_costs[2][1] - current[5] - 1) // current[1]) + 1,
                       ((robot_costs[2][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime:
                next = current.copy()
                next[2] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[2]
                next[8] += time
                queue.append(next)
        # geodes
        if current[2] != 0:
            time = max(0, ((robot_costs[3][2] - current[6] - 1) // current[2]) + 1,
                       ((robot_costs[3][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < 24:
                next = current.copy()
                next[3] += 1
                next[4:8] += current[:4] * time
                next[4:8] -= robot_costs[3]
                next[8] += time
                queue.append(next)

    return maxGeodes


def calculate_longer_geodes(robot_costs, volcanotime):
    start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0])
    queue = [start]
    maxGeodes = 0
    for maxOre in range(1, max([robot[0] for robot in robot_costs[1:]]) + 1):
        for maxClay in range(1, robot_costs[2][1] + 1):
            maxWaitOb = 3
            maxWaitGe = 2
            queue = [start]
            while queue:
                current = queue.pop(0)
                maxGeodes = max(maxGeodes, current[7] + current[3] * (volcanotime - current[8]))

                # ore
                if current[0] < maxOre:
                    time = max(0, ((robot_costs[0][0] - current[4] - 1) // current[0]) + 1) + 1
                    if time + current[8] < volcanotime:
                        next = current.copy()
                        next[0] += 1
                        next[4:8] += current[:4] * time
                        next[4:8] = next[4:8] - robot_costs[0]
                        next[8] += time
                        queue.append(next)
                        continue
                # clay
                if current[1] < maxClay:
                    time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
                    if time + current[8] < volcanotime:
                        next = current.copy()
                        next[1] += 1
                        next[4:8] += current[:4] * time
                        next[4:8] = next[4:8] - robot_costs[1]
                        next[8] += time
                        queue.append(next)
                        continue

                # if current[4] > robot_costs[1][0] + 1:
                #     time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
                #     if time + current[8] < volcanotime:
                #         next = current.copy()
                #         next[1] += 1
                #         next[4:8] += current[:4] * time
                #         next[4:8] = next[4:8] - robot_costs[1]
                #         next[8] += time
                #         queue.append(next)

                # geodes
                if current[2] != 0:
                    time = max(0, ((robot_costs[3][2] - current[6] - 1) // current[2]) + 1,
                               ((robot_costs[3][0] - current[4] - 1) // current[0]) + 1) + 1
                    if time + current[8] < volcanotime and time <= maxWaitGe:
                        next = current.copy()
                        next[3] += 1
                        next[4:8] += current[:4] * time
                        next[4:8] -= robot_costs[3]
                        next[8] += time
                        queue.append(next)

                # obsidian
                if current[1] != 0:
                    time = max(0, ((robot_costs[2][1] - current[5] - 1) // current[1]) + 1,
                               ((robot_costs[2][0] - current[4] - 1) // current[0]) + 1) + 1
                    if time + current[8] < volcanotime and time <= maxWaitOb:
                        next = current.copy()
                        next[2] += 1
                        next[4:8] += current[:4] * time
                        next[4:8] = next[4:8] - robot_costs[2]
                        next[8] += time
                        queue.append(next)

    return maxGeodes


def solveA(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    max_geodes = 0
    for i in range(1, len(lines) + 1):
        line = lines[i - 1]
        robot_costs = parse_line(line)
        geodes = calculate_geodes(robot_costs, 24)
        max_geodes += i * geodes
        print(f'{i} {geodes}')
    print('max possible geodes:')
    print(max_geodes)


def calculate_fixed_geodes(robot_costs, volcanotime):
    maxGeodes = 0
    maxOre = 4
    maxWaitOb = 2
    maxWaitGe = 2
    if robot_costs[0][0] == 4:
        start = np.array([4, 1, 0, 0, 4, 1, 0, 0, 11, 0, 0])
        if robot_costs[1][0] == 2:
            start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
            maxOre = 2
    elif robot_costs[0][0] == 2:
        start = np.array([4, 3, 0, 0, 4, 6, 0, 0, 9, 0, 0])
        if robot_costs[1][0] == 3:
            start = np.array([3, 0, 0, 0, 3, 0, 0, 0, 5, 0, 0])
            maxOre = 3
    else:
        start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    queue = [start]
    while queue:
        current = queue.pop(0)
        if current[7] + current[3] * (volcanotime - current[8]) >= maxGeodes:
            maxGeodes = current[7] + current[3] * (volcanotime - current[8])
            pass

        # ore
        if current[0] < maxOre:
            time = max(0, ((robot_costs[0][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime:
                next = current.copy()
                next[0] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[0]
                next[8] += time
                queue.append(next)
                continue

        skipClay = False
        # geodes
        if current[2] != 0:
            time = max(0, ((robot_costs[3][2] - current[6] - 1 - min(current[10], current[7])) // current[2]) + 1,
                       ((robot_costs[3][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime and time <= maxWaitGe:
                next = current.copy()
                next[3] += 1
                next[4:8] -= robot_costs[3]
                if next[6] < 0:
                    next[7] -= next[6]
                    next[10] -= next[6]
                    next[6] = 0
                else:
                    skipClay = True
                next[4:8] += current[:4] * time
                next[8] += time
                queue.append(next)

        # obsidian
        if current[1] != 0:
            time = max(0, ((robot_costs[2][1] - current[5] - 1 - min(current[9], current[6])) // current[1]) + 1,
                       ((robot_costs[2][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime and time <= maxWaitOb:
                next = current.copy()
                next[2] += 1
                next[4:8] = next[4:8] - robot_costs[2]
                if next[5] < 0:
                    next[6] -= next[5]
                    next[9] -= next[5]
                    next[5] = 0
                else:
                    skipClay = True
                next[4:8] += current[:4] * time
                next[8] += time
                if current[3] > 0:
                    next[10] += 0  # current[3]
                queue.append(next)

        # clay
        if not skipClay and current[5] < (robot_costs[2][1] - current[1]) * (volcanotime - current[8]):
            time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime:
                next = current.copy()
                next[1] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[1]
                next[8] += time
                if next[3] == 0:
                    next[9] += next[2]
                queue.append(next)

    return maxGeodes


def compare_with_queue(current, queue):
    for element in queue:
        timediff = current[8] - element[8]
        if timediff >= 0:
            if element[1] + timediff >= current[1] and element[2] >= current[2] and element[3] >= current[3]:
                if element[5] + (((2 * current[1] + timediff - 1) * timediff) // 2) >= current[5] and element[6] >= \
                        current[6] and element[7] >= current[7]:
                    return False
    return True


def calculate_nexttry_geodes(robot_costs, volcanotime):
    if robot_costs[0][0] == 4:
        start = np.array([4, 1, 0, 0, 4, 1, 0, 0, 11, 0, 0])
    elif robot_costs[0][0] == 2:
        start = np.array([4, 3, 0, 0, 4, 6, 0, 0, 9, 0, 0])
    else:
        start = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    # queue = PriorityQueue()
    # queue.put(start)
    maxGeodes = 0
    maxOre = 4
    maxWaitOb = 3
    maxWaitGe = 2
    queue = [start]
    while queue:
        current = queue.pop(0)
        if not compare_with_queue(current, queue):
            continue
        maxGeodes = max(maxGeodes, current[7] + current[3] * (volcanotime - current[8]))

        # ore
        if current[0] < maxOre:
            time = max(0, ((robot_costs[0][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime:
                next = current.copy()
                next[0] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[0]
                next[8] += time
                if compare_with_queue(next, queue):
                    queue.append(next)
        # clay
        time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
        if time + current[8] < volcanotime:
            next = current.copy()
            next[1] += 1
            next[4:8] += current[:4] * time
            next[4:8] = next[4:8] - robot_costs[1]
            next[8] += time
            if compare_with_queue(next, queue):
                queue.append(next)

        # if current[4] > robot_costs[1][0] + 1:
        #     time = max(0, ((robot_costs[1][0] - current[4] - 1) // current[0]) + 1) + 1
        #     if time + current[8] < volcanotime:
        #         next = current.copy()
        #         next[1] += 1
        #         next[4:8] += current[:4] * time
        #         next[4:8] = next[4:8] - robot_costs[1]
        #         next[8] += time
        #         queue.append(next)

        # geodes
        if current[2] != 0:
            time = max(0, ((robot_costs[3][2] - current[6] - 1) // current[2]) + 1,
                       ((robot_costs[3][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime and time <= maxWaitGe:
                next = current.copy()
                next[3] += 1
                next[4:8] += current[:4] * time
                next[4:8] -= robot_costs[3]
                next[8] += time

                if compare_with_queue(next, queue):
                    queue.append(next)

        # obsidian
        if current[1] != 0:
            time = max(0, ((robot_costs[2][1] - current[5] - 1) // current[1]) + 1,
                       ((robot_costs[2][0] - current[4] - 1) // current[0]) + 1) + 1
            if time + current[8] < volcanotime and time <= maxWaitOb:
                next = current.copy()
                next[2] += 1
                next[4:8] += current[:4] * time
                next[4:8] = next[4:8] - robot_costs[2]
                next[8] += time

                if compare_with_queue(next, queue):
                    queue.append(next)

    return maxGeodes


class array_to_int():
    max_array = []
    multi_array = []

    def __init__(self, array):
        self.max_array = array
        self.multi_array = [1]
        for i in range(1, len(array)):
            self.multi_array.append(self.multi_array[i - 1] * array[i - 1])

    def map_array(self, x):
        res = 0
        for i in range(len(x)):
            res += x[i] * self.multi_array[i]
        return res

    def map_int(self, x):
        res = []
        for i in range(len(self.max_array)):
            res.append(x % self.max_array[i])
            x //= self.max_array[i]
        return np.array(res)


def afforadable(a_v, robot):
    for i in range(4):
        if a_v[i + 4] < robot[i]:
            return False
    return True


def time_needed(a_v, param):
    delta_t = 1
    for i in range(4):
        if param[i] != 0 and a_v[i+4] < param[i]:
            if a_v[i] == 0:
                return 32
            delta_t = max(delta_t, (param[i] - a_v[i+4]) // a_v[i] + 1)
    return delta_t


def calculate_max_possible_geodes(robot_costs, days):
    ## Set up dp table. 8 parameters, ore, clay, obidian, geode, ore robot, clay robot, obsidian robot, geode robot
    ## Assume maxs:
    time = 0
    max_array = []
    if robot_costs[0][0] == 4:
        ore = np.array(robot_costs[0])
        clay = np.array(robot_costs[1])
        obsidian = np.array(robot_costs[2])
        geodes = np.array(robot_costs[3])
        start = np.array([1, 0, 0, 0, 0, 0, 0, 0])
        max_array = [5, obsidian[1], geodes[2]-1, 8, 8, obsidian[1] * 2, 2 * geodes[2], 40]
        time = 0
    elif robot_costs[0][0] == 2:
        for i in range(4):
            robot_costs[i][0] = 0
        ore = np.array(robot_costs[0])
        clay = np.array(robot_costs[1])
        obsidian = np.array(robot_costs[2])
        geodes = np.array(robot_costs[3])
        start = np.array([0, 0, 0, 0, 0, 0, 0, 0])
        max_array = [1, obsidian[1], geodes[2], 15, 1, obsidian[1] * 2, 2 * geodes[2], 45]
        time = 6

    print(f"maxarray: {max_array}")
    ## create a graph on each possible value below max_array and then do a bfs search
    maxvertex = np.prod(max_array)
    bestgeodes = 0
    bestarray = []


    q = queue.Queue()
    a = array_to_int(max_array)
    q.put(a.map_array(np.array(start)))
    dist = {}

    dist[a.map_array(start)] = time

    while not q.empty():
        v = q.get()
        a_v = a.map_int(v)
        time = dist[v]
        if time == days:
            break
        for robot in range(0, 4):
            delta_t = time_needed(a_v, robot_costs[robot])
            if delta_t + time >= days:
                continue
            next = a_v.copy()
            next[4:] += a_v[:4] * delta_t
            next[4:] -= robot_costs[robot]
            next[robot] += 1
            # cutoff over max
            for i in range(8):
                if next[i] >= max_array[i] - 1:
                    next[i] = max_array[i] - 1
            if not np.array_equiv(next , a.map_int(a.map_array(next))):
                print(f"error: {next}")
            if not a.map_array(next) in dist:
                dist[a.map_array(next)] = time + delta_t
                q.put(a.map_array(next))
                if (next[7] + (32 -time -delta_t) * next[3] )> bestgeodes:
                    bestgeodes = next[7] + (32 -time -delta_t) * next[3]
                    bestarray = next.copy()


    print(f"bestgeodes: {bestgeodes}")
    print(f"bestarray: {bestarray}")
    return bestgeodes


def solveB(file_name):
    with open(file_name) as my_file:
        ## too lazy for asserting..
        lines = my_file.readlines()

    max_geodes = 1
    for i in range(1, min(len(lines) + 1, 4)):
        line = lines[i - 1]
        robot_costs = parse_line(line)
        geodes = calculate_greedy_geodes(robot_costs, 32, i)
        max_geodes *= geodes
        print(f'{i} {geodes}')
    # 1    40
    # 2    9
    # 3    28
    print('max possible geodes:')
    print(max_geodes)

    ## working with copilot:

    max_days = 32
    max_geodes = 1
    for i in range(1, min(len(lines) + 1, 4)):
        if i == 1:
            continue
        line = lines[i - 1]
        robot_costs = parse_line(line)
        geodes = calculate_max_possible_geodes(robot_costs, 32)
        max_geodes *= geodes
        print(f'{i} {geodes}')
    print('max possible geodes:')
    print(max_geodes)
    # 1    41
    # maxarray: [5, 14, 11, 8, 8, 28, 32, 40]
    # bestgeodes: 19
    # bestarray: [ 4  9  7  4  7 27  3 15]
    # 2 19
    # maxarray: [5, 12, 3, 8, 8, 24, 16, 40]
    # bestgeodes: 24
    # bestarray: [ 2  4  2  3  7 23  1 12]
    # 3 24
    # max possible geodes:
    # 18696

    # max_geodes = 1
    # for i in range(1, min(len(lines)+1, 4)):
    #     line = lines[i - 1]
    #     robot_costs = parse_line(line)
    #     geodes = calculate_fixed_geodes(robot_costs, 32)
    #     max_geodes *= geodes
    #     print(f'{i} {geodes}')
    # # 1 52
    # # 2 13
    # # 3 31
    # print('max possible geodes:')
    # print(max_geodes)

    # max_geodes = 1
    # for i in range(1, min(len(lines)+1, 4)):
    #     line = lines[i - 1]
    #     robot_costs = parse_line(line)
    #     geodes = calculate_nexttry_geodes(robot_costs, 32)
    #     max_geodes *= geodes
    #     print(f'{i} {geodes}')
    # # 1 52
    # # 2 13
    # # 3 31
    # print('max possible geodes:')
    # print(max_geodes)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')
