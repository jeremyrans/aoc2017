import collections

lines = [l for l in open('input.txt').readlines()]

registers = collections.defaultdict(int)
values = []

for line in lines:
    l = line.split()
    reg = l[0]
    l[0] = "registers['%s']" % reg
    l[1] = l[1].replace("dec", "-=")
    l[1] = l[1].replace("inc", "+=")
    l[4] = "registers['%s']" % l[4]
    l.append("else 0")
    exec(" ".join(l))
    values.append(registers[reg])

print max(values)
