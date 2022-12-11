import copy
import operator
import math
import numpy as np

f = open(
    'C:\\Users\\Bob Dang\\Desktop\\Uni Winter 2021\\side project\\Advant of code\\q11\\input.txt', "r")
data = f.read()
data = data.split("\n\n")
monkeys = []

ops = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}

for i in data:
    order = i.split("\n")
    temp = {}

    temp['items'] = order[1].split(":")[1].split(",")
    temp['operation'] = order[2].split("=")[1].split()
    temp['test'] = order[3].split()[-1]
    temp['True'] = order[4].split()[-1]
    temp['False'] = order[5].split()[-1]
    temp['count'] = 0
    monkeys.append(temp)


def dosimulate(time, divide=0):
    for k in range(time):
        for i in range(len(monkeys)):
            while len(monkeys[i]['items']) > 0:
                remove = monkeys[i]['items'].pop(0)

                operation = ops[monkeys[i]['operation'][1]](
                    int(remove), int(monkeys[i]['operation'][2] if monkeys[i]['operation'][2] != "old" else remove))

                # cal = math.floor(operation/divide)
                cal = operation % 9699690

                if cal % int(monkeys[i]['test']) == 0:
                    monkeys[int(monkeys[i]['True'])]['items'].append(cal)
                else:
                    monkeys[int(monkeys[i]['False'])]['items'].append(cal)
                monkeys[i]['count']+=1


monkeysTemp = copy.deepcopy(monkeys)

dosimulate(10000)
total = []
for i in range(len(monkeys)):
    # print(monkeys[i]['count'])
    total.append(monkeys[i]['count'])
total.sort()
print(total)
print(total[-1]*total[-2])
