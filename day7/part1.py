lines = [l for l in open('input.txt').readlines()]

nodes = {}

for line in lines:
    l = line.split()
    name = l[0]
    weight = int(l[1][1:-1])
    children = [x.strip(",") for x in l[3:]]

    nodes[name] = (weight, children)

possible_roots = []
all_children = []

for k, (weight, children) in nodes.iteritems():
    if len(children) != 0:
        possible_roots.append(k)
        all_children.extend(children)

print [pr for pr in possible_roots if pr not in all_children]
