import re


def parse_numbers(number_list):
    return set(x[0] for x in re.finditer(r"\d+", number_list))


def parse_card(n, line):
    _, contents = line.split(": ")
    winning, present = map(parse_numbers, contents.split(" | "))
    result = present.intersection(winning)
    return [i + 1 for i in range(n, n + len(result))]


def process_cards(card_definitions, card_instances):
    copies = []
    for instance in card_instances:
        copies.extend(card_definitions[instance])
    return copies


with open("input.txt") as f:
    card_definitions = {i + 1: parse_card(i + 1, x.strip()) for i, x in enumerate(f)}
    cards_instances = [k for k in card_definitions]
    n_cards = len(cards_instances)
    while cards_instances := process_cards(card_definitions, cards_instances):
        n_cards += len(cards_instances)
    print(n_cards)
