import operator
import re

from functools import reduce


def parse_numbers(number_list):
    return map(int, re.findall(r"\d+", number_list))


def parse_document(lines):
    times = parse_numbers(lines[0])
    distances = parse_numbers(lines[1])
    return list(zip(times, distances))


def get_wins(duration, record):
    wins = 0
    for speed in range(0, duration + 1):
        distance = speed * (duration - speed)
        if distance > record:
            wins += 1
    return wins


with open("input.txt") as f:
    document = parse_document(f.readlines())
    print(reduce(operator.mul, (get_wins(*x) for x in document)))
