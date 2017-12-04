lines = [l.strip() for l in open('input.txt').readlines()]

count = 0
for line in lines:
    incr = True
    l = line.split()
    for i, w in enumerate(l):
        for j, w2 in enumerate(l):
            if i == j:
                continue
            if len(w) != len(w2):
                continue
            if sorted(w) == sorted(w2):
                incr = False
    if incr:
        count += 1

print count

