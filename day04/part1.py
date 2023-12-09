import re


def parse_numbers(number_list):
    return set(x[0] for x in re.finditer(r"\d+", number_list))


def score_card(line):
    _, contents = line.split(": ")
    winning, present = map(parse_numbers, contents.split(" | "))
    result = present.intersection(winning)
    if not result:
        return 0
    return 2 ** (len(result) - 1)


with open("input.txt") as f:
    print(sum(score_card(x.strip()) for x in f))
