import re


def get_first_last_digits(x):
    matches = re.findall(r"\d", x)
    return int(matches[0] + matches[-1])


with open("input.txt") as f:
    print(sum(map(get_first_last_digits, f)))
