import collections

lines = [l for l in open('input.txt').readlines()]

registers = collections.defaultdict(int)

for line in lines:
    exec("%s else 0" % line.replace("dec", "-=").replace("inc", "+=")[:-1], globals(), registers)

print max(v for k, v in registers.iteritems())
