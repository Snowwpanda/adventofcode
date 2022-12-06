import numpy as np
import re




def solveA(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())
        
        signal = my_file.read()
        if not re.match('[a-z]+', signal):
            print("wrong format")
            return
        start = 4
        while(start <= len(signal) and len(set(signal[start-4:start])) != 4):
            start += 1
        print("Marker ends at position:")
        if start > len(signal):
            print(f"no marker found until the end {start -1}")
        else:
            print(f"{start} with the marker being \'{signal[start-4:start]}\'")


def solveB(file_name):
    with open(file_name) as my_file:
        # print(my_file.read())

        signal = my_file.read()
        if not re.match('[a-z]+', signal):
            print("wrong format")
            return
        start = 14
        while(start <= len(signal) and len(set(signal[start-14:start])) != 14):
            start += 1
        print("Marker ends at position:")
        if start > len(signal):
            print(f"no marker found until the end {start -1}")
        else:
            print(f"{start} with the marker being \'{signal[start-14:start]}\'")

if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
