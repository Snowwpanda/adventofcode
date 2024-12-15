import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    grid = [[1 if x == '#' else 0 for x in line.strip()] for line in lines if line[0] == '#']

    directions_map = {'^': np.array([-1, 0]), 'v': np.array([1, 0]), '>': np.array([0, 1]), '<': np.array([0, -1])}

    instructions_chars =[[c for c in line.strip()] for line in lines if line[0] in ['<', 'v', '>', '^']]
    instructions = [directions_map[move] for move in sum(instructions_chars, [])]
    
    boxes = set()
    robot = np.array([1, 1])
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            if val == 'O':
                boxes.add((x, y))
            elif val == '@':
                robot = np.array([x, y])
            

    for move in instructions:
        # move forward
        robot += move
        # check grid
        if grid[robot[0]][robot[1]] == 1:
            robot -= move
            continue
        
        # check boxes
        if (robot[0], robot[1]) in boxes:
            boxes.remove((robot[0], robot[1]))
            box = robot + move
            # continue along boxrow
            while (box[0], box[1]) in boxes:
                box += move
            
            # check grid for box
            if grid[box[0]][box[1]] == 0:
                boxes.add((box[0], box[1]))
            else:
                boxes.add((robot[0], robot[1]))
                robot -= move
            
    
            
    def gps(box):
        return box[0] * 100 + box[1]
    
    res = sum([gps(box) for box in boxes])
    
    # Print result
    print("Answer Part 1:")
    print(res)


def box_isfree(box, move, boxes, grid):
    # move forward
    is_free = True
    boxes.remove(box)
    new_box = box + move
    # check grid
    if grid[new_box[0]][new_box[1]] == 1 or grid[new_box[0]][new_box[1] + 1] == 1:
        is_free = False
    # check boxes
    for b in [(new_box[0], new_box[1] - 1), (new_box[0], new_box[1]), (new_box[0], new_box[1] + 1)]:
        if b in boxes:
            is_free = box_isfree(b, move, boxes, grid) and is_free
    
    boxes.add(box)
    return is_free

def move_box(box, move, boxes, grid):
    boxes.remove(box)
    new_box = box + move
    # check grid

    # check boxes
    for b in [(new_box[0], new_box[1] - 1), (new_box[0], new_box[1]), (new_box[0], new_box[1] + 1)]:
        if b in boxes:
            move_box(b, move, boxes, grid)
    
    boxes.add(tuple(new_box))
    return

def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    grid = [[1 if line[i // 2] == '#' else 0 for i in range(2* len(line.strip()))] for line in lines if line[0] == '#']

    directions_map = {'^': np.array([-1, 0]), 'v': np.array([1, 0]), '>': np.array([0, 1]), '<': np.array([0, -1])}

    instructions_chars =[[c for c in line.strip()] for line in lines if line[0] in ['<', 'v', '>', '^']]
    instructions = [directions_map[move] for move in sum(instructions_chars, [])]
    
    boxes = set()
    robot = np.array([1, 1])
    for x, line in enumerate(lines):
        for y, val in enumerate(line):
            if val == 'O':
                boxes.add((x, 2 * y))
            elif val == '@':
                robot = np.array([x, 2 * y])
                
    plt.figure()
    
    def display_grid(grid, robot, boxes):
        display_grid = np.copy(grid)
        for box in boxes:
            display_grid[box[0]][box[1]] += 5
            display_grid[box[0]][box[1] + 1] = 7

        display_grid[robot[0]][robot[1]] = 9

        # plot grid
        plt.clf()
        plt.ion()
        plt.imshow(display_grid)
        plt.show()
        plt.pause(0.01)

    # display_grid(grid, robot, boxes)
    for move in instructions:
        # move forward
        robot += move
        # check grid
        if grid[robot[0]][robot[1]] == 1:
            robot -= move
            continue
        
        # check boxes
        for pos in [(robot[0], robot[1]), (robot[0], robot[1] - 1)]:
            if pos in boxes and not box_isfree(pos, move, boxes, grid):
                robot -= move
                break
        else:
            # if all are free move
            for pos in [(robot[0], robot[1]), (robot[0], robot[1] - 1)]:
                if pos in boxes:
                    move_box(pos, move, boxes, grid)

        
        # display_grid(grid, robot, boxes)
        continue
        
            
    
            
    def gps(box):
        return box[0] * 100 + box[1]
    
    

    display_grid(grid, robot, boxes)

    res = sum([gps(box) for box in boxes])
    
    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')