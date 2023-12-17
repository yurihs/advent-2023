from collections import Counter

cards_map = (
    {k: i + 10 for i, k in enumerate("TQKA")}
    | {str(i): i for i in range(10)}
    | {"J": 0}
)
hand_types_map = {
    k: i + 1
    for i, k in enumerate(
        [
            "high-card",
            "one-pair",
            "two-pair",
            "three-of-a-kind",
            "full-house",
            "four-of-a-kind",
            "five-of-a-kind",
        ]
    )
}


def recognize_cards(cards):
    common_cards = [card for card, _ in Counter(cards).most_common() if card != 0]
    if common_cards:
        most_common_card = common_cards[0]
        cards = [most_common_card if card == 0 else card for card in cards]
    counts = Counter(cards).most_common()
    highest_count = counts[0][1]
    n_distinct = len(counts)
    if n_distinct == 1:
        return "five-of-a-kind"
    elif n_distinct == 2:
        if highest_count == 4:
            return "four-of-a-kind"
        return "full-house"
    elif n_distinct == 3:
        if highest_count == 3:
            return "three-of-a-kind"
        return "two-pair"
    elif highest_count == 2:
        return "one-pair"
    return "high-card"


def parse_hand(hand):
    cards = tuple(cards_map[x] for x in hand)
    hand_type = recognize_cards(cards)
    return (hand_types_map[hand_type],) + cards


def parse_line(line):
    first, second = line.split(" ")
    return parse_hand(first), int(second)


with open("input.txt") as f:
    lines = list(sorted(map(parse_line, f)))
    print(sum(x[1] * (i + 1) for i, x in enumerate(lines)))
