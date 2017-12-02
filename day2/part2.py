import itertools

lines = [l.strip() for l in open('input.txt').readlines()]

split_lines = [[int(l) for l in line.split()] for line in lines]

sum = 0

for l in split_lines:
    for c in itertools.combinations(l, 2):
        if c[0] % c[1] == 0:
            sum += c[0] / c[1]
            break
        if c[1] % c[0] == 0:
            sum += c[1] / c[0]
            break

print sum
