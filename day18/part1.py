lines = [l.strip('\n') for l in open('input.txt').readlines()]

registers = {}
sounds = []
pos = 0

def snd(x):
    try:
        sounds.append(registers[x])
    except KeyError:
        sounds.append(int(x))

def set(x, y):
    try:
        registers[x] = registers[y]
    except KeyError:
        registers[x] = int(y)

def add(x, y):
    try:
        registers[x] += registers[y]
    except KeyError:
        registers[x] += int(y)

def mul(x, y):
    try:
        registers[x] *= registers[y]
    except KeyError:
        registers[x] *= int(y)

def mod(x, y):
    try:
        registers[x] %= registers[y]
    except KeyError:
        registers[x] %= int(y)

def rcv(x):
    if registers.get(x, -1) != 0:
        print sounds[-1]
        exit()
        registers[x] = sounds[-1]

def jgz(x, y):
    global pos
    if registers.get(x, 0) > 0:
        try:
            pos += registers[y]
        except KeyError:
            pos += int(y)
        return True
    return False

def part1(lines):
    global pos
    while pos >= 0 and pos < len(lines):
        parts = lines[pos].split()
        if parts[1] not in registers:
            registers[parts[1]] = 0
        if parts[0] == 'snd':
            snd(*parts[1:])
        elif parts[0] == 'set':
            set(*parts[1:])
        elif parts[0] == 'add':
            add(*parts[1:])
        elif parts[0] == 'mul':
            mul(*parts[1:])
        elif parts[0] == 'mod':
            mod(*parts[1:])
        elif parts[0] == 'rcv':
            rcv(*parts[1:])
        elif parts[0] == 'jgz':
            if jgz(*parts[1:]):
                continue
        pos += 1


print part1(lines)
