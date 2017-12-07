lines = [l for l in open('input.txt').readlines()]

nodes = {}

for line in lines:
    l = line.split()
    name = l[0]
    weight = int(l[1][1:-1])
    children = [x.strip(",") for x in l[3:]]

    nodes[name] = [weight, children]

root = "dgoocsw"


def get_weight(n):
    weight = nodes[n][0]
    children = nodes[n][1]

    if not children:
        return weight
    child_weights = [get_weight(x) for x in children]
    return sum(child_weights) + weight


def find_odd_node(n):
    all_weights = [x[1] for x in n]
    for name, weight in n:
        if all_weights.count(weight) == 1:
            return name, max(all_weights) - min(all_weights)
    return None, None


diff = 0
while True:
    weights = []
    for n in nodes[root][1]:
        weights.append((n, get_weight(n)))

    new_root, new_diff = find_odd_node(weights)
    if new_root is None:
        # current root is the culprit
        print root, nodes[root][0] - diff
        break
    elif len(nodes[new_root][1]) == 0:
        # new_root is the culprit
        print new_root, nodes[new_root][0] - new_diff
        break

    root = new_root
    diff = new_diff
