import numpy as np

def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        heaviest_load = 0;
        heaviest_elf = 0;
        current_elf = 1;
        current_load = 0;
        for line in my_file:
            if line == '\n' or line == '\r\n':
                current_elf += 1;
                current_load = 0;
            elif line[:-1].isnumeric():
                current_load += float(line[:-1])
                if current_load > heaviest_load:
                    heaviest_load = current_load
                    heaviest_elf = current_elf
            else:
                print('error, recieved non number input!!')

        print("The heaviest elf is:")
        print(heaviest_elf)
        print("He has a total load of:")
        print(heaviest_load)

def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        elf_list = [];
        current_elf = 1;
        current_load = 0;
        for line in my_file:
            if line == '\n' or line == '\r\n':
                elf_list.append(current_load)
                current_elf += 1;
                current_load = 0;
            elif line[:-1].isnumeric():
                current_load += float(line[:-1])
            else:
                print('error, recieved non number input!!')
        elf_list.sort(reverse=True)
        while len(elf_list) < 3:
            elf_list.append(0)
        # print(elf_list)
        print("The three most heavily loaded elves have a load of:")
        print(f"{elf_list[0]} + {elf_list[1]} + {elf_list[2]}")
        print(sum(elf_list[0:3]))





if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')