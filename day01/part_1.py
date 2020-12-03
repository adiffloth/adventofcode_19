# https://adventofcode.com/2019/day/1

def fuel_needed(mass):
    return mass // 3 - 2


with open('1/input.txt') as f:
    masses = f.read().splitlines()

fuel = 0

for mass in masses:
    fuel += fuel_needed(int(mass))

print(fuel)
