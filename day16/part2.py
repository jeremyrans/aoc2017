lines = [l.strip('\n') for l in open('input.txt').readlines()]


def spin(p, x):
    return p[-x:] + p[:-x]


def exchange(p, a, b):
    t_a = p[a]
    t_b = p[b]
    p[a] = t_b
    p[b] = t_a
    return p


def partner(p, a, b):
    i_a = p.index(a)
    i_b = p.index(b)
    p[i_a] = b
    p[i_b] = a
    return p


def part2(moves):
    split_moves = moves.split(',')
    programs = [chr(97 + i) for i in xrange(16)]
    prev_positions = []

    for j in xrange(int(1e9)):
        for m in split_moves:
            if m[0] == 's':
                programs = spin(programs, int(m[1:]))
            elif m[0] == 'x':
                programs = exchange(programs, *[int(x) for x in m[1:].split('/')])
            elif m[0] == 'p':
                programs = partner(programs, *m[1:].split('/'))

        new_pos = ''.join(programs)
        if new_pos in prev_positions:
            # cycle detected, so just modulo for the final position
            final_pos = prev_positions[int(1e9) % j - 1]
            return final_pos
        prev_positions.append(new_pos)

print part2(lines[0])
