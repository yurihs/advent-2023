import itertools


def apply_map(v, ranges):
    for dst_start, src_start, length in ranges:
        src_end = src_start + length
        if src_start <= v < src_end:
            diff = v - src_start
            return dst_start + diff
    return v


def find_location_from_seed(value, *, almanac):
    sequence = [
        "seed",
        "soil",
        "fertilizer",
        "water",
        "light",
        "temperature",
        "humidity",
        "location",
    ]
    for src, dst in itertools.pairwise(sequence):
        value = apply_map(value, almanac[f"{src}-to-{dst}"])
    return value


def parse_numbers(line):
    return [int(x) for x in line.split(" ")]


def parse_map(line):
    label, content = line.strip().split(" map:\n")
    return label, [parse_numbers(x) for x in content.split("\n")]


def parse_almanac(text):
    parts = text.split("\n\n")
    seeds = parse_numbers(parts.pop(0).removeprefix("seeds: "))
    maps = dict(parse_map(part) for part in parts)
    maps["seeds"] = seeds
    return maps


with open("input.txt") as f:
    almanac = parse_almanac(f.read())
    locations = (
        find_location_from_seed(seed, almanac=almanac) for seed in almanac["seeds"]
    )
    print(min(locations))
