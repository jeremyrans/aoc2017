input = [l.strip('\n') for l in open('input.txt').readlines()][0]

in_garbage = False
ignore_next = False
depth = 0
score = 0
for i, c in enumerate(input):
    if ignore_next:
        ignore_next = False
        continue

    if in_garbage and c == '!':
        ignore_next = True
        continue

    if c == '<' and not in_garbage:
        in_garbage = True
        continue
    if c == '>' and in_garbage:
        in_garbage = False
        continue
    if in_garbage:
        score += 1

print score
