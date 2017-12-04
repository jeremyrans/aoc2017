lines = [l.strip() for l in open('input.txt').readlines()]

count = 0
for line in lines:
    incr = True
    for w in line.split():
        if line.split().count(w) > 1:
            incr = False
            break
    if incr:
        count += 1

print count

