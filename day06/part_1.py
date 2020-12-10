from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter()

orbits = [i for i in open('day06/0.in').read().splitlines()]
child_map = defaultdict(list)
for orbit in orbits:
    child_map[orbit.split(')')[0]].append(orbit.split(')')[1])
# pp.pprint(child_map)

# Count direct and indirect orbits. Do DFS for every non-leaf node.
# At each step, store root and terminal nodes in a set to eliminate double counting.
all_orbits = set()
for root in [*child_map]:
    q = [root]
    while q:
        curr_node = q.pop()
        for n in child_map[curr_node]:
            q.append(n)
        if root != curr_node:
            all_orbits.add((root, curr_node))

print(len(all_orbits))
