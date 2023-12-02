import re

words = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def find_digit(x, *, last=False):
    if last:
        x = x[::-1]
    number_digit = re.search(r"\d", x)
    words_regex = "|".join(word[::-1] if last else word for word in words)
    word_digit = re.search(words_regex, x)
    if word_digit is None and number_digit is None:
        return None
    if word_digit is None:
        return number_digit[0]
    if number_digit is None or word_digit.start() < number_digit.start():
        return words[word_digit[0][::-1] if last else word_digit[0]]
    return number_digit[0]


def sum_digits(x):
    first = find_digit(x)
    last = find_digit(x, last=True)
    return int(first + (last or first))


with open("input.txt") as f:
    print(sum(map(sum_digits, f)))
