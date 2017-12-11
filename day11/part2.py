import math

input = [l.strip('\n') for l in open('input.txt').readlines()][0]
path = input.split(',')

x, y = 0.0, 0.0

furthest = 0

for p in path:
    if p == 'nw':
        x -= 1
        y -= 0.5
    elif p == 'n':
        y -= 0.5
    elif p == 'ne':
        y -= 0.5
        x += 1
    elif p == 'se':
        x += 1
        y += 0.5
    elif p == 's':
        y += 0.5
    elif p == 'sw':
        y += 0.5
        x -= 1

    furthest = max(furthest, max(abs(math.floor(x)), abs(math.floor(y))))

print furthest
