import operator

from functools import reduce


def parse_set(x):
    red, green, blue = 0, 0, 0
    for cube in x.split(", "):
        value, name = cube.split(" ")
        if name == "red":
            red += int(value)
        elif name == "green":
            green += int(value)
        elif name == "blue":
            blue += int(value)
    return (red, green, blue)


def get_game_power(x):
    _, sets = x.strip().split(": ")
    cubes = list(map(parse_set, sets.split("; ")))
    minimums = map(max, zip(*cubes))
    return reduce(operator.mul, minimums)


with open("input.txt") as f:
    print(sum(map(get_game_power, f)))
