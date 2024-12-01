import math

import numpy as np
import re
import time
from collections import Counter
# import priority queue
import heapq

# import plt function


class module_class:
    type = 0 # broadcaster, flipflop, conjunction
    map_type = {
        'broadcaster': 0,
        '%': 1,
        '&': 2,
    }

    def __init__(self, label, type, destinations, inputs):
        self.label = label
        self.type = self.map_type[type]
        self.destinations = destinations
        new_memory = {}
        for input in inputs:
            new_memory[input] = 0
        self.memory = new_memory.copy()
        if self.type == 1:
            self.add_input(label)
        self.history = set()
        self.log = []
        self.memory_snapshot = self.memory.copy()


    def get_pulse(self, source, pulse, iteration):
        self.log.append((source, pulse))
        output = []
        if self.type == 0: # broadcaster
            for destination in self.destinations:
                output.append((self.label, pulse, destination))
        elif self.type == 1:
            output =  self.get_pulse_filp_flop(source, pulse)
        elif self.type == 2:
            output =  self.get_pulse_conjunction(source, pulse, iteration)
        for pulse in output:
            if pulse not in self.history:
                self.history.add(pulse)
                print(pulse + (iteration,)  )
        return output

    def get_pulse_filp_flop(self, source, pulse):
        output = []
        if pulse == 1:
            return output
        self.memory[self.label] = 1 - self.memory[self.label]
        for destination in self.destinations:
            output.append((self.label, self.memory[self.label], destination))
        return output

    def get_pulse_conjunction(self, source, pulse, iteration):
        output = []
        self.memory[source] = pulse
        if all([self.memory[input] != 0 for input in self.memory]):
            pulse = 0
            if self.label in ['pr', 'qs', 'jv', 'jm']:
                print(f"pulse: {pulse} {self.label} {iteration}")
        else:
            pulse = 1
        for destination in self.destinations:
            output.append((self.label, pulse, destination))
        return output

    def add_input(self, input):
        self.memory[input] = 0

    def get_memory(self):
        return self.memory

    def take_snapshot(self):
        changes = []
        for key in self.memory:
            if key in self.memory_snapshot and self.memory[key] != self.memory_snapshot[key]:
                changes.append((key, self.memory[key]))
        if len(changes) >= 2:
            print(f"{self.label}: {self.memory}")
        self.memory_snapshot = self.memory.copy()
def push_button(param, modulesMap, memoryMap, counter_high, counter_low):

    queue = [f'button;0;{param}']
    counter_low += 1
    while len(queue) > 0:
        signal = queue.pop(0)
        # print(f"signal: {signal}")
        origin, value, target = signal.split(';')
        value = int(value)
        if target == 'rx' and value == 0:
            return 0, 0
        if target not in modulesMap:
            # if target != 'rx':
            #     print(f"Error: {signal} not in modulesMap")
            continue
        if target == 'broadcaster':
            for destination in modulesMap[target]:
                queue.append(f"{'broadcaster'};{value};{destination}")
                print(f"{'broadcaster'};{value};{destination}")
                if value == 1:
                    counter_high += 1
                else:
                    counter_low += 1
        elif modulesMap[target][0] == '&':
            memoryMap[target][origin] = value
            if all([memoryMap[target][input] != 0 for input in memoryMap[target]]):
                value = 0
            else:
                value = 1
            for destination in modulesMap[target][1:]:
                queue.append(f"{target};{value};{destination}")
                print(f"{target};{value};{destination}")
                if value == 1:
                    counter_high += 1
                else:
                    counter_low += 1
        elif modulesMap[target][0] == '%':
            if value != 1:
                memoryMap[target] = 1 - memoryMap[target]
                value = memoryMap[target]
                for destination in modulesMap[target][1:]:
                    queue.append(f"{target};{value};{destination}")
                    print(f"{target};{value};{destination}")
                    if value == 1:
                        counter_high += 1
                    else:
                        counter_low += 1
            else:
                for destination in modulesMap[target][1:]:
                    print(f"{target};null;{destination}")

        else:
            print(f"Error: should not reach here")
            continue

    return counter_high, counter_low

def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    modulesMap = {}
    modules = set()
    for line in lines:
        if re.search("(%\w+|&\w+|broadcaster) -> (.*)", line ):
            capture = re.search("(%\w+|&\w+|broadcaster) -> (.*)", line ).groups()
            print(capture)
            destinations = capture[1].split(', ')
            if capture[0][0] in ['&', '%']:
                modulesMap[capture[0][1:]] = [capture[0][0]] + destinations
            else:
                modulesMap[capture[0]] = destinations

    # memoryMap = {}
    # for key in modulesMap:
    #     value = modulesMap[key]
    #     if value[0] == '&':
    #         inputMap = {}
    #         for input in modulesMap:
    #             if key in modulesMap[input]:
    #                 inputMap[input] = 0
    #         memoryMap[key] = inputMap.copy()
    #     elif value[0] == '%':
    #         memoryMap[key] = 0

    # run simulation through all modules starting with broadcaster
    counter_high = 0
    counter_low = 0
    #loop 1000
    for i in range(1000):
        counter_high, counter_low = push_button('broadcaster', modulesMap, memoryMap, counter_high, counter_low)
    print(f"counter_high: {counter_high}")
    print(f"counter_low: {counter_low}")
    print(f"product: {counter_high * counter_low}")

    print(f"modulesMap: ")
    print(modulesMap)

    return

def push_button_b(param, modules, iteration):
    queue = [('button', 0, param)]
    # if iteration % 256 == 0:
    #     print(f"{queue[0]} {iteration}")
    while len(queue) > 0:
        signal = queue.pop(0)
        # print(f"signal: {signal}")
        origin, value, target = signal
        value = int(value)
        if target == 'rx' and value == 0:
            print(f"rx recieved low at iteration: {iteration}")
        if target not in modules:
            # if target != 'rx':
            #     print(f"Error: {signal} not in modulesMap")
            continue
        pulses = modules[target].get_pulse(origin, value, iteration)
        for pulse in pulses:
            queue.append(pulse)


    if iteration % 1024 == 0:
        print(f"iteration: {iteration}")
        for m in modules:
            module = modules[m]
            module.take_snapshot()
    return


def bfs(start, modules, dist_map):
    queue = [start]
    dist_map[start] = 0
    while len(queue) > 0:
        current = queue.pop(0)
        if current in modules:
            for destination in modules[current].destinations:
                if destination not in dist_map:
                    dist_map[destination] = dist_map[current] + 1
                    queue.append(destination)


def fully_caclulable_bfs(modules, start):
    fully_calc = set()
    fully_calc.add(start)
    queue = [start]
    while len(queue) > 0:
        current = queue.pop(0)
        if current in modules:
            for destination in modules[current].destinations:
                if destination in fully_calc:
                    continue
                inputs = list(modules[destination].memory.keys())
                if all([(input in fully_calc or input == destination) for input in inputs]):
                    fully_calc.add(destination)
                    queue.append(destination)
    return fully_calc

def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        lines = my_file.read().splitlines()
        # get rif of empty lines at the end
        while lines[-1] == '':
            lines.pop()

    # read in modules
    modulesMap = {}
    modules = {}
    for line in lines:
        if re.search("(%|&|broadcaster)(\w*) -> (.*)", line ):
            capture = re.search("(%|&|broadcaster)(\w*) -> (.*)", line ).groups()
            # print(capture)
            destinations = capture[2].split(', ')
            if capture[0][0] in ['&', '%']:
                modulesMap[capture[1]] = [capture[0][0]] + destinations
                modules[capture[1]] = (module_class(capture[1], capture[0][0], destinations, []))
            else:
                modulesMap[capture[0]] = destinations
                modules[capture[0]] = (module_class(capture[0], capture[0], destinations, []))



    for key in modulesMap:
        value = modulesMap[key]
        if value[0] in ['&', '%']:
            for input in modulesMap:
                if key in modulesMap[input]:
                    modules[key].add_input(input)



    for m in modules:
        module = modules[m]
        module.take_snapshot()
    counter = 0
    while counter < 8006:
        counter += 1
        push_button_b('broadcaster', modules, counter)

    # pulse: 0 qs 3863
    # pulse: 0 pr 3943
    # pulse: 0 jm 3989
    # pulse: 0 jv 4003

    # calculate kgV of 3863 3943 3989 4003
    print(f"kgV: {math.lcm(3863, 3943, 3989, 4003)}")
    print(f" or just assume they are prime numbers: {3863 * 3943 * 3989 * 4003}")


    # print(f"counter_high: {counter_high}")
    # print(f"counter_low: {counter_low}")
    # print(f"product: {counter_high * counter_low}")

    return


if __name__ == '__main__':
    # time the solution:
    start_time = time.time()
    # solveA('test.txt')
    print("A: --- %s seconds ---" % (time.time() - start_time))

    # time the solution:
    start_time = time.time()
    solveB('input.txt')
    print("B: --- %s seconds ---" % (time.time() - start_time))
