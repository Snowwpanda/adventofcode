import numpy as np
import re
import pathlib as pl



def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    id = 0
    files = True
    real_system = []
    for char in lines[0]:
        if files:  
            real_system += [id for i in range(int(char))]
            id += 1
        else:
            real_system += ['.' for i in range(int(char))]
        files = not files
    
    real_system_copy = real_system.copy()

    # compress
    checksum = 0
    index = 0
    while index < len(real_system):
        if real_system[index] != '.':
            checksum += index * real_system[index]
        else:
            end = real_system.pop()
            while end == '.':
                end = real_system.pop()
            if index >= len(real_system):
                break
            checksum += index * end
        index += 1
    

    res = checksum

    # Print result
    print("Answer Part 1:")
    print(res)


def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    system = [int(char) for char in lines[0].strip()]
    # mark start of block as accumulated sums
    start_of_blocks = [ sum(system[:i]) for i in range(len(system)) ]
    files = [(start_of_blocks[i], system[i]) for i in range(0, len(system), 2)]
    space = [(start_of_blocks[i], system[i]) for i in range(1, len(system), 2)]
    original_checksum = sum([(( 2 * files[i][0] + files[i][1] - 1) * files[i][1] * i) // 2 for i in range(len(files))])

    reverse_files = files[::-1]

    new_checksum = original_checksum
    # from front to back try to fill spaces
    for start, length in space:
        # go through files blocks, see if they fit
        for index, (file_start, file_length) in enumerate(reverse_files):
            # check if the block starts late enough and fits
            if file_length == 0:
                continue
            if start < file_start and length >= file_length:
                # moving block changes checksum
                id = len(reverse_files) - index - 1
                new_checksum += (start - file_start) * file_length * id
                # remove block
                reverse_files[index] = (file_start, 0)
                length -= file_length
                start += file_length
            
            # check if block is empty 
            if length == 0 or start >= file_start:
                break
        

    res = new_checksum 

    # Print result
    print("Answer Part 2:")
    print(res)



if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')