def part2(steps):
    pos = 0
    second_value = 0
    for i in xrange(1, 50000000):
        pos += steps
        pos %= i
        if pos == 0:
            second_value = i
        pos += 1

    return second_value


print part2(359)
