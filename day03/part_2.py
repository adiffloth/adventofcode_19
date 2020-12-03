def trace_wire(wire):
    x = y = 0
    trace = {}
    steps = 0
    for pt in wire.split(','):
        dir = pt[0]
        cnt = int(pt[1:])
        for _ in range(cnt):
            x += dx[dir]
            y += dy[dir]
            steps += 1
            trace[(x, y)] = steps
    return trace


dx = {'D': 0, 'U': 0, 'R': 1, 'L': -1}
dy = {'D': -1, 'U': 1, 'R': 0, 'L': 0}

w1, w2 = [x for x in open('day03/1.in').read().splitlines()]

t1 = trace_wire(w1)
t2 = trace_wire(w2)
intersections = t1.keys() & t2.keys()
print(min(t1[pt] + t2[pt] for pt in intersections))
