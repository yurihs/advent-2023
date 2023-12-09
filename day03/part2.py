from collections import defaultdict
import re


def get_gear_coords(lines):
    gear_coords = set()
    for x, line in enumerate(lines):
        for y, char in enumerate(line.strip()):
            if char == '*':
                gear_coords.add((x, y))
    return gear_coords


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
    gear_coords = get_gear_coords(lines)
    gears = defaultdict(list)
    for x, line in enumerate(lines):
        for match in re.finditer(r"\d+", line.strip()):
            for neighbor_coords in get_neighbor_coords(x, match.start(), match.end()):
                if neighbor_coords in gear_coords:
                    gears[neighbor_coords].append(int(match[0]))
                    break
    return [v[0] * v[1] for v in gears.values() if len(v) == 2]


with open("input.txt") as f:
    print(sum(parse_schematic(f.readlines())))
