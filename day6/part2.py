lines = [l.split() for l in open('input.txt').readlines()][0]
lines = [int(i) for i in lines]

prev_configs = []

count = 0
while lines not in prev_configs:
    prev_configs.append(lines[:])
    maxV = max(lines)
    maxI = lines.index(maxV)

    lines[maxI] = 0
    for x in xrange(1, maxV+1):
        t = (maxI + x) % len(lines)
        lines[t] += 1

    count += 1

print count - prev_configs.index(lines)
