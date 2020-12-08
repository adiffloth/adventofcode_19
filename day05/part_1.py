def opcodes():
    ptr = 0
    while ptr < len(prog):
        opstr = str(prog[ptr]).zfill(5)
        opcode, modes = int(opstr[-2:]), [int(x) for x in opstr[:3]]
        if opcode == 99:  # Halt
            break
        elif opcode == 1:  # Add
            v1, v2, v3 = get_3vals(ptr, modes)
            prog[v3] = v1 + v2
            ptr += 4
        elif opcode == 2:  # Multiply
            v1, v2, v3 = get_3vals(ptr, modes)
            prog[v3] = v1 * v2
            ptr += 4
        elif opcode == 3:  # Input
            prog[prog[ptr + 1]] = input('Enter system id: ')
            ptr += 2
        elif opcode == 4:  # Output
            v1 = prog[ptr + 1] if modes[-1] else prog[prog[ptr + 1]]
            print(v1)
            ptr += 2
        elif opcode == 5:  # Jump if true
            v1 = prog[ptr + 1] if modes[2] else prog[prog[ptr + 1]]
            v2 = prog[ptr + 2] if modes[1] else prog[prog[ptr + 2]]
            if v1 != 0:
                ptr = v2
            else:
                ptr += 3
        elif opcode == 6:  # Jump if false
            v1 = prog[ptr + 1] if modes[2] else prog[prog[ptr + 1]]
            v2 = prog[ptr + 2] if modes[1] else prog[prog[ptr + 2]]
            if v1 == 0:
                ptr = v2
            else:
                ptr += 3
        elif opcode == 7:  # Less than
            v1, v2, v3 = get_3vals(ptr, modes)
            prog[v3] = 1 if v1 < v2 else 0
            ptr += 4
        elif opcode == 8:  # Equals
            v1, v2, v3 = get_3vals(ptr, modes)
            prog[v3] = 1 if v1 == v2 else 0
            ptr += 4
        else:
            raise RuntimeError(f'Invalid opcode: {opcode}')

    return prog


def get_3vals(ptr, modes):
    vals = []
    for i, mode in enumerate(modes[-1::-1][:-1]):
        vals.append(int(prog[ptr + i + 1] if mode else prog[prog[ptr + i + 1]]))
    vals.append(prog[ptr + 3])
    return vals


prog = [int(i) for i in open('day05/1.in').read().split(',')]
opcodes()
