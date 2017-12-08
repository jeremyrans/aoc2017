import collections

lines = [l for l in open('input.txt').readlines()]

registers = collections.defaultdict(int)

for line in lines:
    l = line.split()
    l[0] = "registers['%s']" % l[0]
    l[1] = l[1].replace("dec", "-=")
    l[1] = l[1].replace("inc", "+=")
    l[4] = "registers['%s']" % l[4]
    l.append("else 0")
    exec(" ".join(l))

print max(v for k, v in registers.iteritems())
