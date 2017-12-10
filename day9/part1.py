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

    if c == '<' and not in_garbage:
        in_garbage = True
    if c == '>' and in_garbage:
        in_garbage = False
    if not in_garbage:
        if c == '{':
            depth += 1
        if c == '}':
            score += depth
            depth -= 1

print score
