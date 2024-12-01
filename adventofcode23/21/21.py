import math

import numpy as np
import re
import time
from collections import Counter
# import priority queue
import heapq


# import plt function


def inbounds(next, grid):
    return next[0] >= 0 and next[0] < len(grid) and next[1] >= 0 and next[1] < len(grid[0])


def bfs(grid, queue, max_distance, dist_map, start):
    dist_map[start] = 0
    while queue:
        current = queue.pop(0)
        if dist_map[current] == max_distance:
            continue
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if inbounds(next, grid) and grid[next[0]][next[1]] == '.':
                if next not in dist_map:
                    dist_map[next] = dist_map[current] + 1
                    queue.append(next)


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # transform lines to grid, '.' is empty, '#' is rock (blocked)
    grid = []
    for line in lines:
        grid.append(list(line))

    # find 'S' the starting point
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = '.'
                break

    queue = [start]
    max_distance = 64
    dist_map = {}
    # bfs with max distance
    bfs(grid, queue, max_distance, dist_map, start)

    # count all locations with even distance
    counter = 0
    for key in dist_map:
        if dist_map[key] % 2 == 0:
            counter += 1

    print(f"Amount of locations with even distance: {counter}")

    return


def is_empty(next, grid):
    x = next[0] % len(grid)
    y = next[1] % len(grid[0])
    return grid[x][y] == '.'


def bfs_create_distancemap(grid, dist_map, start):
    dist_map[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if inbounds(next, grid) and grid[next[0]][next[1]] == '.' and dist_map[next] == -1:
                dist_map[next] = dist_map[current] + 1
                queue.append(next)


def calculate_reachable(distance_map_top_right, i, j, steps_left):
    return 0


def steps_used_f(x, y, start, grid):  # build in s map
    # calculate steps used until corner of grid extract
    if x > 0:
        travel_x = grid.__len__() * x - start[0]
    elif x < 0:
        travel_x = grid.__len__() * abs(x + 1) + start[0] + 1
    else:
        travel_x = 0
    if y > 0:
        travel_y = grid[0].__len__() * y - start[1]
    elif y < 0:
        travel_y = grid[0].__len__() * abs(y + 1) + start[1] + 1
    else:
        travel_y = 0
    return travel_x + travel_y


def max_y_for_x(x, max_distance, start, grid):
    steps_used = steps_used_f(x, 0, start, grid)
    if steps_used > max_distance:
        return -1
    else:
        return (max_distance - steps_used + start[1]) // grid[0].__len__()


def min_y_for_x(x, max_distance, start, grid):
    steps_used = steps_used_f(x, 0, start, grid)
    if steps_used > max_distance:
        return -1
    else:
        return (max_distance - steps_used - start[1] - 1) // grid[0].__len__() + 1


def bfs_create_large_distancemap(grid, param, start):
    param[start] = 0
    queue = [start]
    while queue:
        current = queue.pop(0)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            next = (current[0] + direction[0], current[1] + direction[1])
            if inbounds(next, param) and param[next] == -1:
                if grid[next[0] % len(grid)][next[1] % len(grid[0])] == '.':
                    param[next] = param[current] + 1
                    queue.append(next)


def add_reachable(distance_maps, grid, start, x, y, max_distance, total, memory_map, map_patches):

    large_start = (start[0] + len(grid) * abs(x), start[1] + len(grid[0]) * abs(y))

    if (x,y) not in distance_maps:
        distance_maps[ (x,y)] = np.ones((len(grid) * ( 2 *abs(x) +1), len(grid[0]) * (2*abs(y)+1)), dtype=int) * -1

        bfs_create_large_distancemap(grid, distance_maps[ (x,y)], large_start)

    d_map = distance_maps[(x,y) ]

    # sum([ sum([ dist != -1 and dist % 2 == 0 for dist in row] ) for row in d_map])
    # if (entry_x, entry_y, steps_left) in map_patches:
    #     map_patches[(entry_x, entry_y, steps_left)] += 1
    # else:
    #     map_patches[(entry_x, entry_y, steps_left)] = 1
    if (x , y , max_distance) in memory_map:
        return memory_map[(x , y , max_distance) ]
    # go through d_map
    total_reachable = 0
    for i in range(-start[0], len(grid) - start[0]):
        for j in range(-start[1], len(grid[0]) - start[1]):
            dist = d_map[large_start[0] + i + len(grid) *( x)][large_start[1] + j + len(grid[0]) * (y)]
            if dist != -1 and dist <= max_distance and (dist - max_distance) % 2 == 0:
                total_reachable += 1
    memory_map[(x , y , max_distance) ] = total_reachable
    # sum([ sum([ dist != -1 and dist % 2 == 0 for dist in row] ) for row in distance_maps[(0,0)]])
    # sum([ sum([ dist != -1 and dist % 2 == 0 for dist in row[262:] ]) for row in distance_maps[(0,1)]])
    return total_reachable


def add_reachable_old(distance_maps, grid, start, x, y, max_distance, total, memory_map, map_patches):
    if x > 0:
        entry_x = 0
    elif x < 0:
        entry_x = len(grid) - 1
    else:
        entry_x = start[0]
    if y > 0:
        entry_y = 0
    elif y < 0:
        entry_y = len(grid[0]) - 1
    else:
        entry_y = start[1]

    if (entry_x, entry_y) not in distance_maps:
        distance_maps[(entry_x, entry_y)] = np.ones((len(grid), len(grid[0])), dtype=int) * -1
        bfs_create_distancemap(grid, distance_maps[(entry_x, entry_y)], (entry_x, entry_y))

    d_map = distance_maps[(entry_x, entry_y)]
    steps_left = max_distance - steps_used_f(x, y, start, grid)
    if (entry_x, entry_y, steps_left) in map_patches:
        map_patches[(entry_x, entry_y, steps_left)] += 1
    else:
        map_patches[(entry_x, entry_y, steps_left)] = 1
    if (entry_x, entry_y, steps_left) in memory_map:
        return memory_map[(entry_x, entry_y, steps_left)]
    # go through d_map
    total_reachable = 0
    for i in range(len(d_map)):
        for j in range(len(d_map[0])):
            dist = d_map[i][j]
            if dist != -1 and dist <= steps_left and (dist - steps_left) % 2 == 0:
                total_reachable += 1
    memory_map[(entry_x, entry_y, steps_left)] = total_reachable
    return total_reachable
    # sum([ sum([ (dist+1) % 2 for dist in row] ) for row in distance_maps[(0,0)]])


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # transform lines to grid, '.' is empty, '#' is rock (blocked)
    grid = []
    for line in lines:
        grid.append(list(line))

    # assuming grid is a square
    if not all([len(grid[i]) == len(grid) for i in range(len(grid))]):
        print("Error: grid is not a square")
        return

    # find 'S' the starting point
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
                grid[i][j] = '.'
                break

    # check if axis is free:
    print(f"x-axis free {all([ele == '.' for ele in grid[start[0]]])}")
    print(f"y-axis free {all([ele == '.' for ele in [grid[i][start[1]] for i in range(len(grid))]])}")

    distance_maps = {}
    memory_map = {}

    queue = [start]

    max_distance = 26501365

    dist_map = {}
    # bfs with max distance

    # count '.' in grid
    total_freespaces_s = add_reachable(distance_maps, grid, start, 0, 0, max_distance, 0, memory_map, {})
    total_freespaces_ns = add_reachable(distance_maps, grid, start, 0, 1, max_distance, 0, memory_map, {})
    # Count '.' free spaces in grid
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                count += 1
    print(f"Total free spaces in grid: {count}")

    total = 0
    # go around:
    map_patches = {}
    map_patches[(start[0], start[1], 400)] = 0
    map_patches[(start[0], start[1] + 1, 400)] = 0

    # while x >= -max_horizontal:
    #     min_y = min_y_for_x(x, max_distance, start, grid)
    #     max_y = max_y_for_x(x, max_distance, start, grid)
    #     if min_y == -1 or max_y == -1:
    #         x -= 1
    #         continue
    #     if max_y + min_y + 1 <= 3:
    #         for y in range(-min_y, max_y + 1):
    #             total += add_reachable(distance_maps, grid, start, x, y, max_distance, total, memory_map, map_patches)
    #     else:
    #         total += add_reachable(distance_maps, grid, start, x, -min_y, max_distance, total, memory_map, map_patches)
    #         total += add_reachable(distance_maps, grid, start, x, -min_y + 1, max_distance, total, memory_map,
    #                                map_patches)
    #         total += add_reachable(distance_maps, grid, start, x, max_y - 1, max_distance, total, memory_map,
    #                                map_patches)
    #         total += add_reachable(distance_maps, grid, start, x, max_y, max_distance, total, memory_map, map_patches)
    #         total += (((abs(x + max_y) % 2) + max_y + min_y - 3) // 2) * total_freespaces_ns + \
    #                  (((abs(x + max_y + 1) % 2) + max_y + min_y - 3) // 2) * total_freespaces_s
    #         map_patches[(start[0], start[1] + 1, 200)] += ((abs(x + max_y) % 2) + max_y + min_y - 3) // 2
    #         map_patches[(start[0], start[1], 200)] += ((abs(x + max_y + 1) % 2) + max_y + min_y - 3) // 2
    #         # print(f"map_patches[(start[0], start[1]+1, 200)] = {map_patches[(start[0], start[1]+1, 200)]}, this time plus {((abs(x + max_y ) % 2) + max_y + min_y - 3) // 2}")
    #
    #     x -= 1

    print(f"Amount of locations with even distance: {total}")
    # Amount of locations with even distance: 608606028661513 is too high
    # Amount of locations with even distance: 608603022093775
    # Amount of locations with even distance: 608603022093762
    # Amount of locations with even distance: 608193770812170

    max_patches_dir = (max_distance-start[0]-1) // len(grid) + 1
    # SECOND CALCULATION ATTEMPT:
    # top
    top = add_reachable(distance_maps, grid, start, 0, 1, 66+130, 0, memory_map, map_patches)
    # right
    right = add_reachable(distance_maps, grid, start, 1, 0, 66+130, 0, memory_map, map_patches)
    # bottom
    bottom = add_reachable(distance_maps, grid, start, 0, -1, 66+130, 0, memory_map, map_patches)
    # left
    left = add_reachable(distance_maps, grid, start, -1, 0, 66+130, 0, memory_map, map_patches)
    # right slope
    right_slope_small = add_reachable(distance_maps, grid, start, 1, 1, 66+66+64, 0, memory_map, map_patches)
    right_slope_large = add_reachable(distance_maps, grid, start, 1, 1, 66+66+65 + 130, 0, memory_map, map_patches)
    # left slope
    left_slope_small = add_reachable(distance_maps, grid, start, -1, 1, 66+66+64, 0, memory_map, map_patches)
    left_slope_large = add_reachable(distance_maps, grid, start, -1, 1, 66+66+65 + 130, 0, memory_map, map_patches)
    # right incline
    right_incline_small = add_reachable(distance_maps, grid, start, 1, -1, 66+66+64, 0, memory_map, map_patches)
    right_incline_large = add_reachable(distance_maps, grid, start, 1, -1, 66+66+65 + 130, 0, memory_map, map_patches)
    # left incline
    left_incline_small = add_reachable(distance_maps, grid, start, -1, -1, 66+66+64, 0, memory_map, map_patches)
    left_incline_large = add_reachable(distance_maps, grid, start, -1, -1, 66+66+65 + 130, 0, memory_map, map_patches)
    m = max_patches_dir
    full_ns_spaces = ((m //2) * 2) * ((m //2) * 2)
    full_s_spaces = (((m-1) //2) * 2 + 1) * (((m-1) //2) * 2 + 1)

    new_total = top + right + bottom + left + \
                right_slope_small * max_patches_dir + right_slope_large * (max_patches_dir-1) + \
                left_slope_small * max_patches_dir + left_slope_large * (max_patches_dir-1) + \
                right_incline_small * max_patches_dir + right_incline_large * (max_patches_dir-1) + \
                left_incline_small * max_patches_dir + left_incline_large * (max_patches_dir-1) + \
                total_freespaces_s * full_s_spaces + total_freespaces_ns * full_ns_spaces

    print(f"top: {top}")
    print(f"right: {right}")
    print(f"bottom: {bottom}")
    print(f"left: {left}")
    print(f"right_slope_small: {right_slope_small}")
    print(f"right_slope_large: {right_slope_large}")
    print(f"left_slope_small: {left_slope_small}")
    print(f"left_slope_large: {left_slope_large}")
    print(f"right_incline_small: {right_incline_small}")
    print(f"right_incline_large: {right_incline_large}")
    print(f"left_incline_small: {left_incline_small}")
    print(f"left_incline_large: {left_incline_large}")
    print(f"total_freespaces_s: {total_freespaces_s}")
    print(f"total_freespaces_ns: {total_freespaces_ns}")


    print(f"new_total: {new_total}")

    # new 608193770819618 not correct
    # top: 5628
    # right: 5626
    # bottom: 5597
    # left: 5599
    # right_slope_small: 951
    # right_slope_large: 6537
    # left_slope_small: 933
    # left_slope_large: 6525
    # right_incline_small: 947
    # right_incline_large: 6523
    # left_incline_small: 938
    # left_incline_large: 6508
    # total_freespaces_s: 7427
    # total_freespaces_ns: 7434
    # new_total: 608193770819618

    # top: 5628
    # right: 5626
    # bottom: 5597
    # left: 5599
    # right_slope_small: 951
    # right_slope_large: 6537
    # left_slope_small: 933
    # left_slope_large: 6525
    # right_incline_small: 947
    # right_incline_large: 6523
    # left_incline_small: 938
    # left_incline_large: 6508
    # total_freespaces_s: 7434
    # total_freespaces_ns: 7427
    # new_total: 608193767987418
    # top: 5628
    # right: 5626
    # bottom: 5597
    # left: 5599
    # right_slope_small: 951
    # right_slope_large: 6537
    # left_slope_small: 933
    # left_slope_large: 6525
    # right_incline_small: 947
    # right_incline_large: 6523
    # left_incline_small: 938
    # left_incline_large: 6508
    # total_freespaces_s: 7434
    # total_freespaces_ns: 7427
    # new_total: 608193767979991

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
