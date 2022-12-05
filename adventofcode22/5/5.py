import numpy as np
import re



def move_stacks_9000(param_list, stacks):
    if len(param_list) != 3 or len(stacks) <= param_list[1] or len(stacks) <= param_list[2] or len(stacks[param_list[1]]) < param_list[0]:
        return
    [times, from_stack, to_stack] = param_list
    for i in range(times):
        crate = stacks[from_stack].pop()
        stacks[to_stack].append(crate)
    return


def move_stacks_9001(param_list, stacks):
    if len(param_list) != 3 or len(stacks) <= param_list[1] or len(stacks) <= param_list[2] or len(stacks[param_list[1]]) < param_list[0]:
        return
    [times, from_stack, to_stack] = param_list
    for crate in stacks[from_stack][-times:]:
        stacks[from_stack].pop()
        stacks[to_stack].append(crate)
    return



def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        
        stacks = [[], []]
        n_stacks = 1

        for line in my_file:
            if re.match('^(\[[A-Z]\] |    )*(\[[A-Z]\]|   )\n', line):
                for i in range((len(line)+1)//4):
                    if i >= len(stacks)-1:
                        stacks.append([])
                    if re.match('\[[A-Z]\]', line[i*4: (i*4+3)]):
                        stacks[i+1].append(line[i*4+1])
            elif re.match('^( \d  )*( \d  )\n?', line):
                break
            else:
                print("wrong format")
                break
        for stack in stacks:
            stack = stack.reverse()


        for line in my_file:
            parameters = re.match('move (\d+) from (\d+) to (\d+)', line.strip())
            if parameters and len(parameters.groups()) == 3:
               move_stacks_9000([int(i) for i in parameters.groups()], stacks)

        print("Top of the stacks:")
        for stack in stacks:
            if stack:
                print(stack.pop(), end = '')
        print('')

def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        stacks = [[], []]
        n_stacks = 1

        for line in my_file:
            if re.match('^(\[[A-Z]\] |    )*(\[[A-Z]\]|   )\n', line):
                for i in range((len(line)+1)//4):
                    if i >= len(stacks)-1:
                        stacks.append([])
                    if re.match('\[[A-Z]\]', line[i*4: (i*4+3)]):
                        stacks[i+1].append(line[i*4+1])
            elif re.match('^( \d  )*( \d  )\n?', line):
                break
            else:
                print("wrong format")
                break
        for stack in stacks:
            stack = stack.reverse()


        for line in my_file:
            parameters = re.match('move (\d+) from (\d+) to (\d+)', line.strip())
            if parameters and len(parameters.groups()) == 3:
               move_stacks_9001([int(i) for i in parameters.groups()], stacks)

        print("Top of the stacks:")
        for stack in stacks:
            if stack:
                print(stack.pop(), end = '')
        print('')

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
