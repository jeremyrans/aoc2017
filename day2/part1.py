lines = [l.strip() for l in open('input.txt').readlines()]

split_lines = [[int(l) for l in line.split()] for line in lines]

sum = 0
for l in split_lines:
    sum += max(l) - min(l)

print sum
