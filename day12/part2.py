input = [l.strip('\n') for l in open('input.txt').readlines()]

programs = {}

for l in input:
    data = [x.strip(',') for x in l.split()]
    programs[data[0]] = data[2:]

linked_programs = set()


def find_links(o):
    for x in programs[o]:
        if x not in linked_programs:
            linked_programs.add(x)
            find_links(x)


group_count = 0
while True:
    x = next((i for i in programs.keys() if i not in linked_programs), None)
    if x is None:
        break
    group_count += 1
    find_links(x)

print group_count
