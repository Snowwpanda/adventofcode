import re
import numpy as np
from functools import cmp_to_key
import sys
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

def eval_binary_expr(op1, oper, op2):
    op1, op2 = int(op1), int(op2)
    return ops[oper](op1, op2)


def get_monkeynumber(name, monkeyNumber, monkeyNames):
    index = monkeyNames.index(name)
    monkey = monkeyNumber[index]
    if type(monkey) is int:
        return monkey
    elif type(monkey) is str and monkey.isnumeric():
        return int(monkey)
    else:
        while re.search(r'[a-z]{4}', monkey):
            pattern = re.search(r'[a-z]{4}', monkey).group()
            monkey = re.sub(pattern, str(get_monkeynumber(pattern, monkeyNumber, monkeyNames)), monkey)
    if type(monkey) is str and re.match(r'^(-?\d+) ([+\-*/]) (-?\d+)$', monkey ):
        operation = re.match(r'^(-?\d+) ([+\-*/]) (-?\d+)$', monkey).groups()
        left = int(operation[0])
        right = int(operation[2])
        return int(ops[operation[1]](left, right))
    return f'({monkey})'


def solveA(file_name):
    monkeys = []
    with open(file_name) as my_file:
        ## too lazy for asserting..
        monkeys = [line.strip().split(': ') for line in my_file.readlines()]

    monkeyNames = [monkey[0] for monkey in monkeys]
    monkeyNumber = [monkey[1] for monkey in monkeys]
    rootMonkey = get_monkeynumber('root', monkeyNumber, monkeyNames)



    print('result')
    print(rootMonkey)


def reverse_op(num, pos, operation, equals):
    if operation == '*':
        return equals / num
    elif operation == '/' and pos == 2:
        return equals * num
    elif operation == '/' and pos == 1:
        return num / equals
    elif operation == '-' and pos == 1:
        return num - equals
    elif operation == '-' and pos == 2:
        return num + equals
    elif operation == '+':
        return equals - num


def revert_humn(monkey, equals, monkeyNumber, monkeyNames):
    monkeynum = monkeyNumber[monkeyNames.index(monkey)]
    monkey1, operation, monkey2 = re.match(r'^([a-z]{4}) ([+\-*/]) ([a-z]{4})$', monkeynum).groups()
    # monkey */+- int = equals
    if type(get_monkeynumber(monkey2, monkeyNumber, monkeyNames)) is int:
        newequals = reverse_op(get_monkeynumber(monkey2, monkeyNumber, monkeyNames), 2, operation,equals)
    elif type(get_monkeynumber(monkey1, monkeyNumber, monkeyNames)) is int:
        newequals = reverse_op(get_monkeynumber(monkey1, monkeyNumber, monkeyNames), 1,operation,equals)
        monkey1 = monkey2
    if monkey1 == 'humn':
        return newequals
    else:
        return revert_humn(monkey1, newequals, monkeyNumber, monkeyNames)


def solveB(file_name):
    monkeys = []
    with open(file_name) as my_file:
        ## too lazy for asserting..
        monkeys = [line.strip().split(': ') for line in my_file.readlines()]

    monkeyNames = [monkey[0] for monkey in monkeys]
    monkeyNumber = [monkey[1] for monkey in monkeys]
    indexhumn = monkeyNames.index('humn')
    monkeyNumber[indexhumn] = 'x'
    # root: bsbd + fcgj
    print('root: bsbd + fcgj')
    bsbd = get_monkeynumber("bsbd", monkeyNumber, monkeyNames)
    fcgj = get_monkeynumber("fcgj", monkeyNumber, monkeyNames)
    humn = revert_humn("bsbd", get_monkeynumber("fcgj", monkeyNumber, monkeyNames), monkeyNumber, monkeyNames)
    print(f'{bsbd}  and  {fcgj}')
    print(f'humn')
    print(f'{humn}')
   




if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
