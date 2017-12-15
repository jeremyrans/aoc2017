af = 16807
bf = 48271
denom = 2147483647


def next_a(a):
    a = (a * af) % denom
    while a % 4 != 0:
        a = (a * af) % denom
    return a


def next_b(b):
    b = (b * bf) % denom
    while b % 8 != 0:
        b = (b * bf) % denom
    return b


def part1(a, b):
    match_count = 0

    for i in xrange(5000000):
        a = next_a(a)
        b = next_b(b)

        a_bits = bin(a)[2:][-16:]
        b_bits = bin(b)[2:][-16:]

        if a_bits == b_bits:
            match_count += 1

    return match_count

print part1(634, 301)
