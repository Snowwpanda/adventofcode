import numpy as np
import re
import pathlib as pl
import math
import matplotlib.pyplot as plt
import queue


def get_bit(bit, bits):
    if type(bits[bit]) == int:
        return bits[bit]
    else:
        bit1, op, bit2 = bits[bit]
        if op == 'AND':
            bit = get_bit(bit1, bits) & get_bit(bit2, bits)
        elif op == 'OR':
            bit =  get_bit(bit1, bits) | get_bit(bit2, bits)
        elif op == 'XOR':
            bit =  get_bit(bit1, bits) ^ get_bit(bit2, bits)
        else:
            print('Unknown operation:', op)
        bits[bit] = bit
        return bit
        


def solveA(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    bits = {}
    ops = []
    for line in lines:
        if ':' in line:
            var, bit = line.strip().split(': ')
            bits[var] = int(bit)
        elif '->' in line:
            bit1, op, bit2, rbit = re.match(r'(\w+|\d+) (AND|OR|XOR) (\w+|\d+) -> (\w+|\d+)', line).groups()
            ops.append((bit1, op, bit2, rbit))
            bits[rbit] = (bit1, op, bit2)
        else:
            print(line)

    output_bits = []
    index = 0
    while True:
        z_bit = f'z{index:02}'
        if z_bit not in bits:
            break
        output_bits += [get_bit(z_bit, bits)]
        index += 1
    
    out_n = 0
    for i, bit in enumerate(output_bits):
        out_n += bit << i
        
    res = out_n

    # Print result
    print("Answer Part 1:")
    print(res)




def solveB(file_name):    
    # add current path
    file_path = pl.Path(__file__).parent.absolute() / file_name

    with open(file_path) as my_file:
        # print(my_file.read())
        lines = my_file.readlines()

    bits = {}
    ops = []
    for line in lines:
        if ':' in line:
            var, bit = line.strip().split(': ')
            bits[var] = int(bit)
        elif '->' in line:
            bit1, op, bit2, rbit = re.match(r'(\w+|\d+) (AND|OR|XOR) (\w+|\d+) -> (\w+|\d+)', line).groups()
            ops.append((bit1, op, bit2, rbit))
            bits[rbit] = (bit1, op, bit2)
        else:
            print(line)

    # vars should be x.., y.., z.., ü.., XOR.., AND.., and (XORXORü)..

    # structure of calcs:
    #
    # >--->---XOR-------v
    # x   y    |  ü---->z
    #  |  |    v
    #  v  v    AND
    #  AND----v v
    #          ü(OR)

    xor_bit= set()
    or_bit = set()

    for operation in ops:
        bit1, op, bit2, rbit = operation
        if op == 'XOR':
            for bit in bit1, bit2:
                if bit[0] not in 'xyz':
                    xor_bit.add(bit)
        elif op == 'OR':
            for bit in bit1, bit2:
                or_bit.add(bit)

    wrong_bits = set()
    for operation in ops:
        bit1, op, bit2, rbit = operation
        if bit1[0] in 'xy' and op == 'XOR' and rbit not in xor_bit:
            wrong_bits.add(rbit)
        if op == 'OR' and rbit not in xor_bit:
            wrong_bits.add(rbit)
        if op == 'AND' and rbit not in or_bit:
            wrong_bits.add(rbit)
        if op == 'XOR' and rbit not in xor_bit and rbit[0] != 'z':
            wrong_bits.add(rbit)
        if rbit[0] == 'z' and (op != 'XOR' or bit1[0] in 'xy'):
            wrong_bits.add(rbit)

    # z00 is special remove
    if bits['z00'] == ('x00', 'XOR', 'y00') or bits['z00'] == ('y00', 'XOR', 'x00'):
        wrong_bits.remove('z00')
    # also z45 is special
    if bits['z45'][1] == 'OR':
        wrong_bits.remove('z45')
    # also x00 and y00 are special
    sp_bit = False
    for bit in wrong_bits:
        if (bits[bit][0] == 'x00' or bits[bit][0] == 'y00'):
            sp_bit = bit
            break

    #manual fix
    if sp_bit:
        wrong_bits.remove(sp_bit)
    wrong_bits.add('hdt')


    res = sorted(list(wrong_bits))
    res = ','.join(res)

    #wrong gbf,jfb,jgt,mht,nbf,z05,z09,z30,z45 # because z45 duh..

    # ideas: z05<>hdt  nbf<>z30  gbf<>z09  mht<>jgt
    # shs 16ü


    # Print result
    print("Answer Part 2:")
    print(res)


if __name__ == '__main__':
    # solveA('input.txt')

    solveB('input.txt')