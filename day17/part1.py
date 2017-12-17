def part1(steps):
    pos = 0
    buffer = [0]

    for i in xrange(1, 2018):
        pos += steps
        pos %= len(buffer)
        buffer.insert(pos + 1, i)
        pos += 1

    return buffer[pos+1]


print part1(359)
