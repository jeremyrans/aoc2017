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


def check_win(start_at):
    for pos in layers.iterkeys():
        range = layers.get(pos, 0)
        if (pos + start_at) % (2 * range - 2) == 0:
            return False
    return True


for i in xrange(100000000):
    if check_win(i):
        print i
        break
