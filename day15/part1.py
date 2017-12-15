af = 16807
bf = 48271
denom = 2147483647


def part1(a, b):
    match_count = 0

    for i in xrange(40000000):
        a = (a * af) % denom
        b = (b * bf) % denom

        a_bits = bin(a)[2:][-16:]
        b_bits = bin(b)[2:][-16:]

        if a_bits == b_bits:
            match_count += 1

    return match_count

print part1(634, 301)
