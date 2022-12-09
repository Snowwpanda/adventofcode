import numpy as np
import re


def DFS(dir, direct_files_map, adj_map, total_files_map):
    total = 0
    if dir in total_files_map:
        return total_files_map[dir]

    if dir in direct_files_map:
        total += direct_files_map[dir]
    if dir in adj_map:
        for subdir in adj_map[dir]:
            total += DFS(subdir, direct_files_map, adj_map, total_files_map)

    total_files_map[dir] = total
    return total


def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        adj_map = dict()
        direct_files_map = dict()
        current_dir_path = ['.']
        total_files_map = dict()

        for line in my_file:
            line = line.split()
            if len(line) < 2:
                print('error')
                return
            elif len(line) == 3 and line[0] == '$' and line[1] == 'cd':
                if line[2] == '.':
                    current_dir_path = ['.']
                elif line[2] == '..':
                    current_dir_path.pop()
                elif re.match('[a-z]+', line[2]):
                    current_dir_path.append(line[2])
            elif len(line) == 2 and line[0] == '$' and line[1] == 'ls':
                continue
            elif len(line) == 2 and line[0] == 'dir':
                curr_path = '/'.join(current_dir_path)
                if curr_path in adj_map:
                    adj_map[curr_path].append(curr_path + '/' + line[1])
                else:
                    adj_map[curr_path] = [curr_path + '/' + line[1]]
            elif len(line) == 2 and line[0].isnumeric():
                curr_path = '/'.join(current_dir_path)
                if curr_path in direct_files_map:
                    direct_files_map[curr_path] += int(line[0])
                else:
                    direct_files_map[curr_path] = int(line[0])

        total_files_map['.'] = DFS('.', direct_files_map, adj_map, total_files_map)
        sum_of_lessthan100000 = 0
        for dir in total_files_map:
            if total_files_map[dir] < 100000:
                sum_of_lessthan100000 += total_files_map[dir]
        print(sum_of_lessthan100000)

def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        adj_map = dict()
        direct_files_map = dict()
        current_dir_path = ['.']
        total_files_map = dict()

        for line in my_file:
            line = line.split()
            if len(line) < 2:
                print('error')
                return
            elif len(line) == 3 and line[0] == '$' and line[1] == 'cd':
                if line[2] == '.':
                    current_dir_path = ['.']
                elif line[2] == '..':
                    current_dir_path.pop()
                elif re.match('[a-z]+', line[2]):
                    current_dir_path.append(line[2])
            elif len(line) == 2 and line[0] == '$' and line[1] == 'ls':
                continue
            elif len(line) == 2 and line[0] == 'dir':
                curr_path = '/'.join(current_dir_path)
                if curr_path in adj_map:
                    adj_map[curr_path].append(curr_path + '/' + line[1])
                else:
                    adj_map[curr_path] = [curr_path + '/' + line[1]]
            elif len(line) == 2 and line[0].isnumeric():
                curr_path = '/'.join(current_dir_path)
                if curr_path in direct_files_map:
                    direct_files_map[curr_path] += int(line[0])
                else:
                    direct_files_map[curr_path] = int(line[0])

        total_files_map['.'] = DFS('.', direct_files_map, adj_map, total_files_map)
        min_dir_size = total_files_map['.']
        threshold = total_files_map['.']  - 40000000
        for dir in total_files_map:
            if min_dir_size > total_files_map[dir] >= threshold:
                min_dir_size = total_files_map[dir]
        print(min_dir_size)

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
