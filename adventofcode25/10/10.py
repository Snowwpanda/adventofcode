# import numpy as np
# import re
import pathlib as pl
from pathlib import Path
from collections import deque


def bfs(machine):
    t = machine[0].strip('[]')
    l = len(t)
    t = t.replace('.', '0').replace('#', '1')[::-1]
    target = int(t, 2)
    s = 0
    buttons = [sum([2**int(i) for i in button.strip('()').split(',')]) for button in machine[1:-1]]

    visited = set()
    queue = [(s, 0)]  
    while queue:
        current, steps = queue.pop(0)
        for button in buttons:
            neighbor = current ^ button
            if neighbor not in visited:
                if neighbor == target:
                    return steps + 1
                visited.add(neighbor)
                queue.append((neighbor, steps + 1))

    return 0


def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    machines = [line.split() for line in input_data.splitlines()]

    fewest_buttons = 0
    for machine in machines:
        fewest_buttons += bfs(machine)

    output = fewest_buttons

    print("Answer Part 1:")
    print(output)

def joltage(machine):
    joltage_target = tuple(int(i) for i in  machine[-1].strip("{}").split(','))
    l = len(joltage_target)
    buttons = [button.strip('()').split(',') for button in machine[1:-1]]
    buttons = [tuple(1 if str(i) in button else 0 for i in range(l)) for button in buttons]

    queue = deque()
    queue.append((joltage_target, 0, 0)) 
    visited = set()
    
    while queue:
        joltage, button_index, presses = queue.popleft()
        if any(j < 0 for j in joltage):
            continue
        if joltage == tuple(0 for _ in range(l)):
            print(presses)
            return presses
        if joltage in visited:
            continue
        visited.add(joltage)    
        for index, button in enumerate(buttons[button_index:]):
            new_joltage = tuple(joltage[i] - button[i] for i in range(l))
            queue.append((new_joltage, button_index + index, presses + 1))
        
    return 0

                





def solveB(file_name):
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    machines = [line.split() for line in input_data.splitlines()]

    fewest_buttons = 0
    for machine in machines:
        fewest_buttons += joltage(machine)

    output = fewest_buttons

    print("Answer Part 2:")
    print(output)
    

if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')
