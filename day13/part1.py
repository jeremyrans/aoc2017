input = [l.strip('\n') for l in open('input.txt').readlines()]
print input

layers = {}
scanners = {}

scanner_loc = 0
severity = 0

for l in input:
    parts = l.split()
    layers[int(parts[0].strip(':'))] = int(parts[1])
    scanners[int(parts[0].strip(':'))] = 0

for pos in xrange(max(layers.keys()) + 1):
    range = layers.get(pos, 0)
    if range > 0 and pos % (2 * range - 2) == 0:
        severity += pos * range

print severity
