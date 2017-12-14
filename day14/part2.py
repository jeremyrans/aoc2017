key = "jzgqcdpd"


def compute_hash(s):
    knot_bytes = [ord(x) for x in s] + [17, 31, 73, 47, 23]
    numbers = range(0, 256)
    size = len(numbers)
    cur_pos = 0
    skip_size = 0

    for _ in xrange(64):
        for i in knot_bytes:
            if (cur_pos + i) > size:
                end = numbers[cur_pos:]
                start = numbers[:i - len(end)]
                sub_list = list(reversed(end + start))
                numbers = sub_list[-len(start):] + numbers[len(start):cur_pos] + sub_list[:len(end)]
            else:
                sub_list = list(reversed(numbers[cur_pos:cur_pos + i]))
                numbers = numbers[:cur_pos] + sub_list + numbers[cur_pos + i:]
            cur_pos += (i + skip_size)
            cur_pos = cur_pos % size
            skip_size += 1

    hash = ''
    for x in xrange(0, 256, 16):
        output = 0
        for i in numbers[x:x + 16]:
            output = output ^ i

        hash += hex(output)[2:].zfill(2)

    return hash


grid = []
for i in xrange(128):
    x = "%s-%d" % (key, i)
    bs = "".join(bin(int(c, 16))[2:].zfill(4) for c in compute_hash(x))
    grid.append(bs)

print '\n'.join(grid)


def claim(y, x):  # claim all 1s touching i, j
    if (y, x) in seen:
        return
    elif grid[y][x] == "1":
        seen.append((y, x))
    else:
        return
    if y > 0:
        claim(y - 1, x)
    if y < 127:
        claim(y + 1, x)
    if x > 0:
        claim(y, x - 1)
    if x < 127:
        claim(y, x + 1)

groups = 0
seen = []
for i in xrange(128):
    for j in xrange(128):
        if grid[i][j] == "0":
            continue
        if (i, j) in seen:
            continue
        groups += 1
        claim(i, j)

print groups
