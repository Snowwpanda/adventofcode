import numpy as np
import re
import pathlib as pl
from pathlib import Path

def solveA(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    banks = [[int(x) for x in bank] for bank in input_data.split()]

    output = 0

    for bank in banks:
        first_battery = max(bank[:-1])
        index = bank.index(first_battery)
        second_battery = max(bank[index+1:])
        output += first_battery * 10 + second_battery

        


    print("Answer Part 1:")
    print(output)



    
def solveB(file_name):    
    # Read input
    with open(pl.Path(__file__).parent.absolute() / file_name) as f:
        input_data = f.read().strip()

    banks = input_data.split()

    output = 0

    for bank in banks:
        joltage = ''
        index = 0
        # choosing 12 batteries greedily
        for i in range(len(bank)-11, len(bank)+1):
            battery = max(bank[index:i])
            joltage += battery
            index = bank.index(battery, index) + 1
        output += int(joltage)
            
    
    print("Answer Part 2:")
    print(output)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')
