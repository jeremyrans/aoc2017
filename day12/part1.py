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

find_links('0')

print len(linked_programs)
