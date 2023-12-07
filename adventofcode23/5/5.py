import numpy as np
import re
import time

def mapping_step(seed, map):
    for array in map:
        if seed >= array[1] and seed < array[1] + array[2]:
            output = array[0] + seed - array[1]
            return output
    return seed


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in seeds and maps, there are 7 maps, each map is followed by a number of lines with three numbers and then an empty line
    # e.g. seeds: 79 14 55 13
    #
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48
    #
    # soil-to-fertilizer map:
    # ...
    # fertilizer-to-water map:
    # ...
    # water-to-light map:
    # ...
    # light-to-temperature map:
    # ...
    # temperature-to-humidity map:
    # ...
    # humidity-to-location map:

    if re.search('seeds: ?(\d* )*', lines[0]):
        seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
    else:
        print('ERROR: seeds not found')
        return

    maps = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [],
            "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []}

    # read in maps
    current_map = ""
    for line in lines[1:]:
        # check if it is a new map
        if re.search('map:', line):
            current_map = line.split()[0].strip()
            if current_map not in maps.keys():
                print(f'ERROR: map {current_map} not recognized')
                return
            continue
        # check if it is an empty line
        if re.search('^\s*$', line):
            current_map = ""
            continue
        # check if it is a line with three numbers
        if re.search('^\d+ \d+ \d+$', line):
            maps[current_map].append([int(number) for number in line.split()])
            continue
        # if it is none of the above, it is an error
        print('ERROR: line not recognized')
        return

    # for each seed search for location
    min_location = -1
    for seed in seeds:
        soil = mapping_step(seed, maps["seed-to-soil"])
        fertilizer = mapping_step(soil, maps["soil-to-fertilizer"])
        water = mapping_step(fertilizer, maps["fertilizer-to-water"])
        light = mapping_step(water, maps["water-to-light"])
        temperature = mapping_step(light, maps["light-to-temperature"])
        humidity = mapping_step(temperature, maps["temperature-to-humidity"])
        location = mapping_step(humidity, maps["humidity-to-location"])
        if min_location == -1 or location < min_location:
            min_location = location

    print(f'The minimum location is {min_location}')


    return


def clean_intervals(seed_intervals):
    # if intervals overlap then merge them
    # sort intervals
    seed_intervals.sort(key=lambda x: x[0])
    # merge intervals
    merged_intervals = []
    next_interval = seed_intervals[0]
    for interval in seed_intervals[1:]:
        if interval[0] <= next_interval[1] :
            next_interval[1] = max(interval[1]  , next_interval[1])
        else:
            merged_intervals.append(next_interval)
            next_interval = interval
    merged_intervals.append(next_interval)
    return merged_intervals


def in_array(point, array):
    return point >= array[0] and point < array[0] + array[1]


def contains_array(interval, array):
    return interval[0] >= array[0] and interval[1] < array[0] + array[1]


def map_interval(interval, map):
    output_intervals = []
    # sort map by second column
    map.sort(key=lambda x: x[1])
    # find interval that contains the start of the interval
    first_interval = [mapping_step(interval[0], map)]
    for array in map:
        if in_array(interval[0], array[1:]):
            if contains_array( interval, array[1:] ):
                first_interval.append(first_interval[0] + interval[1] - interval[0])
                return [first_interval]
            else:
                first_interval.append(mapping_step(array[1] + array[2] -1, map))
                output_intervals = [first_interval] + map_interval([array[1] + array[2], interval[1]], map)
                return output_intervals

    # otherwise find interval which is the next highest:
    min_above = -1
    for array in map:
        if interval[0] < array[1]:
            min_above = array[1]
            break
    if interval[1] < min_above or min_above == -1:
        return [interval]
    else:
        output_intervals = [[interval[0], min_above-1]] + map_interval([min_above, interval[1]], map)
        return output_intervals



def map_intervals(intervals, map):
    mapped_intervals = []
    for interval in intervals:
        mapped_intervals += map_interval(interval, map)
    clean_intervals(mapped_intervals)
    return mapped_intervals



def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # read in seeds and maps, there are 7 maps, each map is followed by a number of lines with three numbers and then an empty line
    # e.g. seeds: 79 14 55 13
    #
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48
    #
    # soil-to-fertilizer map:
    # ...
    # fertilizer-to-water map:
    # ...
    # water-to-light map:
    # ...
    # light-to-temperature map:
    # ...
    # temperature-to-humidity map:
    # ...
    # humidity-to-location map:

    if re.search('seeds: ?(\d* )*', lines[0]):
        seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
    else:
        print('ERROR: seeds not found')
        return

    maps = {"seed-to-soil": [], "soil-to-fertilizer": [], "fertilizer-to-water": [], "water-to-light": [],
            "light-to-temperature": [], "temperature-to-humidity": [], "humidity-to-location": []}

    # read in maps
    current_map = ""
    for line in lines[1:]:
        # check if it is a new map
        if re.search('map:', line):
            current_map = line.split()[0].strip()
            if current_map not in maps.keys():
                print(f'ERROR: map {current_map} not recognized')
                return
            continue
        # check if it is an empty line
        if re.search('^\s*$', line):
            current_map = ""
            continue
        # check if it is a line with three numbers
        if re.search('^\d+ \d+ \d+$', line):
            maps[current_map].append([int(number) for number in line.split()])
            continue
        # if it is none of the above, it is an error
        print('ERROR: line not recognized')
        return

    # for each seed search for location
    min_location = -1
    # pair up seed numbers to get intervals
    seed_intervals = []
    for i in range(0, len(seeds), 2):
        seed_intervals.append([seeds[i], seeds[i+1] + seeds[i]])
    seed_intervals = clean_intervals(seed_intervals)

    soil_intervals = map_intervals(seed_intervals, maps["seed-to-soil"])
    fertilizer_intervals = map_intervals(soil_intervals, maps["soil-to-fertilizer"])
    water_intervals = map_intervals(fertilizer_intervals, maps["fertilizer-to-water"])
    light_intervals = map_intervals(water_intervals, maps["water-to-light"])
    temperature_intervals = map_intervals(light_intervals, maps["light-to-temperature"])
    humidity_intervals = map_intervals(temperature_intervals, maps["temperature-to-humidity"])
    location_intervals = map_intervals(humidity_intervals, maps["humidity-to-location"])
    location_intervals = clean_intervals(location_intervals)
    min_location = location_intervals[0][0]

    print(f'The minimum location is {min_location}')


    return


if __name__ == '__main__':
    solveA('input.txt')

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("--- %s seconds ---" % (time.time() - start_time))
