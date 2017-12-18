import itertools

lines = [l.strip('\n') for l in open('input.txt').readlines()]

regs = [{}, {}]
queues = {0: [], 1: []}
waiting = [False, False]
sent = [0, 0]
done = [False, False]

def snd(registers, p, x):
    sent[p] += 1
    try:
        to_send = registers[x]
    except KeyError:
        to_send = int(x)
    queues[p].append(to_send)
    print sent


def set(registers, x, y):
    try:
        registers[x] = registers[y]
    except KeyError:
        registers[x] = int(y)


def add(registers, x, y):
    try:
        registers[x] += registers[y]
    except KeyError:
        registers[x] += int(y)


def mul(registers, x, y):
    try:
        registers[x] *= registers[y]
    except KeyError:
        registers[x] *= int(y)


def mod(registers, x, y):
    try:
        registers[x] %= registers[y]
    except KeyError:
        registers[x] %= int(y)


def rcv(registers, p, x):
    other_program = 1 - p
    if len(queues[other_program]) == 0:
        waiting[p] = True
        if waiting[other_program] or done[other_program]:
            deadlock()
    else:
        registers[x] = queues[other_program].pop(0)
        waiting[p] = False
    return not waiting[p]


def jgz(registers, p, x, y):
    if registers.get(x, x) > 0:
        try:
            d = registers[y]
        except KeyError:
            d = int(y)
        return d
    return 1


def deadlock():
    print "Sent: %s" % sent[1]
    exit()


def is_int(x):
    try:
        int(x)
        return True
    except Exception:
        return False


def part2(lines):
    positions = [0, 0]
    for pid in itertools.cycle([0, 1]):
        pos = positions[pid]
        registers = regs[pid]
        if 0 <= pos < len(lines):
            parts = lines[pos].split()
            if parts[1] not in registers and not is_int(parts[1]):
                registers[parts[1]] = pid
            if parts[0] == 'snd':
                snd(registers, pid, *parts[1:])
            elif parts[0] == 'set':
                set(registers, *parts[1:])
            elif parts[0] == 'add':
                add(registers, *parts[1:])
            elif parts[0] == 'mul':
                mul(registers, *parts[1:])
            elif parts[0] == 'mod':
                mod(registers, *parts[1:])
            elif parts[0] == 'rcv':
                if not rcv(registers, pid, *parts[1:]):
                    continue
            elif parts[0] == 'jgz':
                positions[pid] += jgz(registers, pid, *parts[1:])
                continue
        else:
            done[pid] = True
            continue
        regs[pid] = registers
        positions[pid] += 1
    return sent


part2(lines)
