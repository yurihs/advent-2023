import re


def get_symbol_coords(lines):
    symbol_coords = set()
    for x, line in enumerate(lines):
        for y, char in enumerate(line.strip()):
            if char != "." and not char.isdigit():
                symbol_coords.add((x, y))
    return symbol_coords


def get_neighbor_coords(x, min_y, max_y):
    neighbors = set()
    for y in range(min_y, max_y):
        neighbors.add((x, y - 1))
        neighbors.add((x, y + 1))
        neighbors.add((x - 1, y))
        neighbors.add((x + 1, y))
        neighbors.add((x - 1, y - 1))
        neighbors.add((x - 1, y + 1))
        neighbors.add((x + 1, y - 1))
        neighbors.add((x + 1, y + 1))
    return neighbors


def parse_schematic(lines):
    symbol_coords = get_symbol_coords(lines)
    numbers = []
    for x, line in enumerate(lines):
        for match in re.finditer(r"\d+", line.strip()):
            for neighbor_coords in get_neighbor_coords(x, match.start(), match.end()):
                if neighbor_coords in symbol_coords:
                    numbers.append(match[0])
                    break
    return map(int, numbers)


with open("input.txt") as f:
    print(sum(parse_schematic(f.readlines())))
