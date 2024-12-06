import numpy as np
import re
import pathlib as pl


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()
    
    # parse input, search for guard
    patrol = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    for index, line in enumerate(lines):
        for direction in patrol:
            if direction in line:
                guard_pos = np.array([index, line.index(direction)])
                facing = np.array(patrol[direction])
                break
        else:
            continue
        break
    else:
        print('No starting point found')
        return 0

    # write to 0, 1 grid
    grid = np.array([[1 if char == '#' else 0 for char in line.strip()] for line in lines])
    visited = set()
    visited.add(tuple(guard_pos))

    # rotation matrix to the right
    rotation_mat = np.array([[0, 1], [-1, 0]])

    while True: # this is actually risky since there may be a loop, for now assume no loops
        # check out of bounds
        x, y = tuple(guard_pos + facing)
        if x < 0 or y < 0 or x >= grid.shape[0] or y >= grid.shape[1]:
            break
        if grid[tuple(guard_pos + facing)] == 1:
            facing = np.dot(rotation_mat, facing)
        else:
            guard_pos += facing
            visited.add(tuple(guard_pos))
    
    res = len(visited)

    # Print result
    print("Answer Part 1:")
    print(res)


def outside_bounds(x, y, grid):
    return x < 0 or y < 0 or x >= grid.shape[0] or y >= grid.shape[1]

def calculate_movement(x, y, dir_x, dir_y, grid):
    dir = np.array([dir_x, dir_y])
    rotation_mat = np.array([[0, 1], [-1, 0]])
    pos = np.array([x, y]) - dir
    if outside_bounds(*pos, grid):
        return "exit"
    
    dir = np.dot(rotation_mat, dir)
    while not outside_bounds(*(pos + dir), grid):
        if grid[tuple(pos + dir)] == 1:
            return tuple(np.concatenate((pos+dir, dir)))
        else:
            pos += dir

    return "exit"
    
def inbetween(blockade, facing, start, next):
    if next != 'ex':
        if blockade[0] == start[0] and 0 == facing[0]:
            return start[1] < blockade[1] < next[1] or start[1] > blockade[1] > next[1]
        if blockade[1] == start[1] and 0 == facing[1]:
            return start[0] < blockade[0] < next[0] or start[0] > blockade[0] > next[0]
    else:
        if blockade[0] == start[0] and 0 == facing[0]:
            return (blockade[1] - start[1]) * facing[1] > 0
        if blockade[1] == start[1] and 0 == facing[1]:
            return (blockade[0] - start[0]) * facing[0] > 0
    return False


def has_loop(guard_pos, facing, blockade, movement_dict, grid):
    visited = set()
    # ugly fix for initial facing
    rotation_mat = np.array([[0, 1], [-1, 0]])

    pos_facing = (*guard_pos, *facing)
    while True:
        if pos_facing not in movement_dict:
            next_pos_facing = calculate_movement( *pos_facing , grid)
        else:
            next_pos_facing = movement_dict[pos_facing]
        # Check if blockade is inbetween
        if inbetween(blockade, np.dot(rotation_mat, np.array(pos_facing[2:]) ),(pos_facing[0] - pos_facing[2], pos_facing[1] - pos_facing[3]), next_pos_facing[:2]):
            next_pos_facing = (*blockade, *np.dot(rotation_mat, np.array(pos_facing[2:])))
        

        if next_pos_facing == "exit":
            return False
        if next_pos_facing in visited:
            return True
        visited.add(next_pos_facing)
        pos_facing = next_pos_facing
        
        



def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    # parse input, search for guard
    patrol = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    for index, line in enumerate(lines):
        for direction in patrol:
            if direction in line:
                init_guard_pos = np.array([index, line.index(direction)])
                init_facing = np.array(patrol[direction])
                break
        else:
            continue
        break
    else:
        print('No starting point found')
        return 0

    # write to 0, 1 grid
    grid = np.array([[1 if char == '#' else 0 for char in line.strip()] for line in lines])
    possible = set()
    guard_pos = init_guard_pos.copy()
    facing = init_facing.copy()
    possible.add(tuple(guard_pos))



    # Calculating quickreference for every direction and obstacle:
    movement_dict = {}
    for x, row in enumerate(grid):
        for y, pos in enumerate(row):
            for dir in patrol.values():
                movement_dict[(x, y, *dir)] = calculate_movement(x, y, *dir, grid)


    # add starting movement ugly fix
    # rotate other way around
    counter_rotation_mat = np.array([[0, -1], [1, 0]])
    fake_start = (*(init_guard_pos + np.dot(counter_rotation_mat, init_facing)), *np.dot(counter_rotation_mat, init_facing))

    guard_pos = init_guard_pos.copy()
    facing = init_facing.copy()
    while True:
        guard_pos += facing
        if grid[tuple(guard_pos)] == 1:
            movement_dict[fake_start] = (*guard_pos, *facing)
            break 
        # assuming we don't exit first step (part1)

    
    loop_blockades = set()
    # for blockade in possible:
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            blockade = (x, y)
            if has_loop(fake_start[:2], fake_start[2:], blockade, movement_dict, grid):
                loop_blockades.add(blockade)

    # remove starting point is present
    loop_blockades.discard(tuple(init_guard_pos))


    # for test should get (9, 7), (8, 3), (8, 1), (7, 7), (7, 6), (6, 3)
    res = len(loop_blockades)


    # Print result
    print("Answer Part 2:")
    print(res)





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')