'''
https://adventofcode.com/2019/day/2
Trying to find the combination of starting noun and verb that produces a specific output.
Brute force it!
'''

from day02.intcode import opcodes


def replace_instructions(noun, verb):
    with open('2/input.txt') as f:
        input = [int(i) for i in f.read().split(',')]
        input[1] = noun
        input[2] = verb
    return input


def brute_force(target):
    for noun in range(0, 100):
        for verb in range(0, 100):
            ret_val = opcodes(replace_instructions(noun, verb))[0]
            if ret_val == target:
                return 100 * noun + verb


if __name__ == '__main__':
    TARGET = 19690720
    print(brute_force(TARGET))
