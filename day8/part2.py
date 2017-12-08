import collections

lines = [l for l in open('input.txt').readlines()]

registers = collections.defaultdict(int)
m = 0

for line in lines:
    exec("%s else 0" % line.replace("dec", "-=").replace("inc", "+=")[:-1], globals(), registers)
    m = max([v for v in registers.itervalues()] + [m])

print m
