import numpy as np
import re
import time


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in times and distances:
    for line in lines:
        if re.search('Time:\s*(\d*\s+)*', line):
            times = [int(time) for time in line.split(':')[1].split()]
        if re.search('Distance:\s*(\d*\s+)*', line):
            distances = [int(distance) for distance in line.split(':')[1].split()]

    # pair up times and distances in races
    races = []
    for i in range(times.__len__()):
        races.append([times[i], distances[i]])

    for race in races:
        # binary search min times
        time = race[0]
        min_time = 0
        max_time = race[0]//2
        while min_time + 1 < max_time:
            mid = (min_time + max_time) // 2
            if mid * (time - mid) > race[1]:
                max_time = mid
            else:
                min_time = mid
        range_pos = time - 2 * min_time - 1
        race.append(range_pos)
        print(max_time)

    # take the product of the min times
    sol = 1
    for race in races:
        sol *= race[2]

    print(f'The minimum times product is {sol}')



    return



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in times and distances:
    for line in lines:
        if re.search('Time:\s*(\d*\s+)*', line):
            time = int(line.split(':')[1].replace(' ', '').strip())
        if re.search('Distance:\s*(\d*\s+)*', line):
            distance = int(line.split(':')[1].replace(' ', '').strip())

    # contact the numbers for the big race
    races = [[time, distance]]

    for race in races:
        # binary search min times
        time = race[0]
        min_time = 0
        max_time = race[0]//2
        while min_time + 1 < max_time:
            mid = (min_time + max_time) // 2
            if mid * (time - mid) > race[1]:
                max_time = mid
            else:
                min_time = mid
        range_pos = time - 2 * min_time - 1
        race.append(range_pos)
        print(max_time)

    # take the product of the min times
    sol = 1
    for race in races:
        sol *= race[2]

    print(f'The minimum times product is {sol}')


    return


if __name__ == '__main__':
    solveA('input.txt')

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("--- %s seconds ---" % (time.time() - start_time))
