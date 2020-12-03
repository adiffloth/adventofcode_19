'''
https://adventofcode.com/2019/day/1#part2
Add in the fuel required for the new fuel
'''


def fuel_needed(mass):
    if mass < 9:
        return 0
    return (mass // 3 - 2) + fuel_needed(mass // 3 - 2)


def test1():
    print('five')


if __name__ == '__main__':
    with open('1/input.txt') as f:
        masses = f.read().splitlines()

    fuel = 0

    for mass in masses:
        fuel += fuel_needed(int(mass))

    print(fuel)
