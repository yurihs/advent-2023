import operator
import re

from functools import reduce


def parse_number(x):
    return int(x.split(":")[1].replace(" ", ""))


def get_wins(duration, record):
    wins = 0
    for speed in range(0, duration + 1):
        distance = speed * (duration - speed)
        if distance > record:
            wins += 1
    return wins


with open("input.txt") as f:
    time = parse_number(f.readline())
    distance = parse_number(f.readline())
    print(get_wins(time, distance))
