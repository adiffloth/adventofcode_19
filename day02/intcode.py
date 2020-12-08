'''
https://adventofcode.com/2019/day/2

Playing with opcodes.

Test cases:
1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99
'''


def opcodes(input_ls):
    for i in range(0, len(input_ls), 4):
        opcode = int(input_ls[i])
        if opcode == 99:
            # print('opcode: exit')
            break
        elif opcode == 1:
            input_ls[input_ls[i + 3]] = input_ls[input_ls[i + 1]] + input_ls[input_ls[i + 2]]
        elif opcode == 2:
            input_ls[input_ls[i + 3]] = input_ls[input_ls[i + 1]] * input_ls[input_ls[i + 2]]
        else:
            raise RuntimeError(f'Invalid opcode: {opcode}')

    return input_ls


if __name__ == '__main__':

    assert opcodes([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert opcodes([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert opcodes([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert opcodes([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
    print('Tests passed.')

    # Get the input string and replace the two values to restore the "1202 program alarm state".
    with open('day02/input.txt') as f:
        input = [int(i) for i in f.read().split(',')]
        input[1] = 12
        input[2] = 2

    print(opcodes(input)[0])
