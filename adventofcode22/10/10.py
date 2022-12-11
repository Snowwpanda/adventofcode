import re
import numpy as np



def solveA(file_name):
    with open(file_name) as my_file:
        instructions = []
        for line in my_file:
            if re.match('(noop|addx -?\d*)\n?', line):
                instructions.append(line.split())


        current_cycle = 0
        current_signal = 1
        total = 0
        for instr in instructions:
            if instr[0] == 'noop':
                current_cycle += 1
                if current_cycle % 40 == 20:
                    total += current_signal*current_cycle
            elif instr[0] == 'addx':
                current_cycle += 2
                if current_cycle % 40 == 20:
                    total += current_signal*current_cycle
                if current_cycle % 40 == 21:
                    total += current_signal*(current_cycle-1)
                current_signal += int(instr[1])
            if current_cycle > 220:
                break
        print("total:")
        print(total)






def solveB(file_name):
    with open(file_name) as my_file:
        instructions = []
        for line in my_file:
            if re.match('(noop|addx -?\d*)\n?', line):
                instructions.append(line.split())

        display = ''
        current_cycle = 0
        current_signal = 1
        total = 0
        for instr in instructions:
            if instr[0] == 'noop':
                dist = abs(current_cycle - current_signal)
                if dist <= 1:
                    display += '#'
                else:
                    display += '.'
                current_cycle += 1
                if current_cycle== 40:
                    current_cycle = 0
                    display += '\n'
            elif instr[0] == 'addx':
                dist = abs(current_cycle - current_signal)
                if dist <= 1:
                    display += '#'
                else:
                    display += '.'
                current_cycle += 1
                if current_cycle== 40:
                    current_cycle = 0
                    display += '\n'
                dist = abs(current_cycle - current_signal)
                if dist <= 1:
                    display += '#'
                else:
                    display += '.'
                current_cycle += 1
                if current_cycle== 40:
                    current_cycle = 0
                    display += '\n'
                current_signal += int(instr[1])

        print("Display:")
        print(display)









if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
