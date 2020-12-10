from collections import defaultdict
import pprint
pp = pprint.PrettyPrinter()


def dfs_san(root):
    q = [root]
    while q:
        curr_node = q.pop()
        for n in child_map[curr_node]:
            if n == 'SAN':
                return True, dist_up(curr_node, root)
            q.append(n)
    return False, 0


def dist_up(curr_node, target):
    d = 0
    while curr_node != target and curr_node != 'COM':
        curr_node = parent_map[curr_node]
        d += 1
    return d


orbits = [i for i in open('day06/0.in').read().splitlines()]
child_map = defaultdict(list)
parent_map = defaultdict()
for orbit in orbits:
    child_map[orbit.split(')')[0]].append(orbit.split(')')[1])
    parent_map[orbit.split(')')[1]] = orbit.split(')')[0]

start_node = parent_map['YOU']
found = False
steps_up = 0
steps_down = 0
while not found:
    start_node = parent_map[start_node]
    steps_up += 1
    found, steps_down = dfs_san(start_node)
print(steps_up + steps_down)