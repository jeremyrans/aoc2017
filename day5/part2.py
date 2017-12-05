lines = [int(l.strip()) for l in open('input.txt').readlines()]

tot = len(lines)
pos = 0

count = 0

while True:
    count += 1
    oldPos = pos
    pos += lines[pos]

    if lines[oldPos] >= 3:
        lines[oldPos] -= 1
    else:
        lines[oldPos] += 1

    if pos >= tot:
        print count
        break
