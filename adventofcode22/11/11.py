import re
import numpy as np
import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}

def eval_binary_expr(monkeyOperation, item):

    op1, oper, op2 = monkeyOperation.split(' ')
    if op1 == 'old':
        op1 = item
    else:
        op1 = int(op1)
    if op2 == 'old':
        op2 = item
    else:
        op2 = int(op2)
    return ops[oper](op1, op2)

def solveA(file_name):
    monkeyItems = []
    monkeyOperation = []
    monkeyTest = []

    with open(file_name) as my_file:

        lines = my_file.readlines()

    N = (len(lines)+1)//7
    for i in range(N ):
        monkeyItems.append([int(n) for n in re.search('(\d+,? ?)+', lines[7*i+1]).group().split(', ')])
        monkeyOperation.append(re.search('new = (.*)\n', lines[7*i+2]).groups()[0])
        monkeyTest.append([int(re.search('\d+', lines[7*i+3+j]).group()) for j in range(3) ])

    ## round
    inspectionCount = np.zeros(N)
    rounds = 20
    for r in range(rounds):
        for m in range(N):
            inspectionCount[m] += len(monkeyItems[m])
            for item in monkeyItems[m]:
                item = eval_binary_expr(monkeyOperation[m], item)  // 3
                if item % monkeyTest[m][0] == 0:
                    monkeyItems[monkeyTest[m][1]].append(item)
                else:
                    monkeyItems[monkeyTest[m][2]].append(item)
            monkeyItems[m] = []


    total = 0
    print("inspectionCount:")
    print(inspectionCount)
    sorted = np.sort(inspectionCount)
    print(sorted[-1] * sorted[-2])






def solveB(file_name):
    monkeyItems = []
    monkeyOperation = []
    monkeyTest = []

    with open(file_name) as my_file:

        lines = my_file.readlines()

    N = (len(lines)+1)//7
    for i in range(N ):
        monkeyItems.append([int(n) for n in re.search('(\d+,? ?)+', lines[7*i+1]).group().split(', ')])
        monkeyOperation.append(re.search('new = (.*)\n', lines[7*i+2]).groups()[0])
        monkeyTest.append([int(re.search('\d+', lines[7*i+3+j]).group()) for j in range(3) ])

    ## round
    inspectionCount = np.zeros(N)
    prod = 1
    for test in monkeyTest:
        prod *= test[0]
    rounds = 10000
    for r in range(rounds):
        for m in range(N):
            inspectionCount[m] += len(monkeyItems[m])
            for item in monkeyItems[m]:
                item = eval_binary_expr(monkeyOperation[m], item) % prod
                if item % monkeyTest[m][0] == 0:
                    monkeyItems[monkeyTest[m][1]].append(item)
                else:
                    monkeyItems[monkeyTest[m][2]].append(item)
            monkeyItems[m] = []


    total = 0
    print("inspectionCount:")
    print(inspectionCount)
    sorted = np.sort(inspectionCount)
    print(sorted[-1] * sorted[-2])










if __name__ == '__main__':
    solveA('input.txt')

    solveB('input.txt')
