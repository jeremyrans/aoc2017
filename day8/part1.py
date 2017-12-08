import collections

import operator

lines = [l for l in open('input.txt').readlines()]

registers = {}
instructions = []

ops = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne
}

for line in lines:
    l = line.split()
    reg = l[0]
    op = ops[l[-2]]
    cond_reg = l[-3]
    delta = int(l[2]) if l[1] == "inc" else -int(l[2])

    if reg not in registers:
        registers[reg] = 0

    if cond_reg not in registers:
        registers[cond_reg] = 0

    if op(registers[cond_reg], int(l[-1])):
        registers[reg] += delta


print max(v for k, v in registers.iteritems())
