import itertools
import multiprocessing

from concurrent.futures import ProcessPoolExecutor
from functools import partial


def apply_reverse_map(v, ranges):
    for dst_start, src_start, length in ranges:
        dst_end = dst_start + length
        if dst_start <= v < dst_end:
            diff = v - dst_start
            return src_start + diff
    return v


def find_seed_from_location(value, *, almanac):
    sequence = [
        "location",
        "humidity",
        "temperature",
        "light",
        "water",
        "fertilizer",
        "soil",
        "seed",
    ]
    for src, dst in itertools.pairwise(sequence):
        value = apply_reverse_map(value, almanac[f"{dst}-to-{src}"])
    return value


def parse_numbers(line):
    return [int(x) for x in line.split(" ")]


def parse_map(line):
    label, content = line.strip().split(" map:\n")
    return label, [parse_numbers(x) for x in content.split("\n")]


def parse_seeds(seeds):
    for i in range(0, len(seeds), 2):
        start = seeds[i]
        length = seeds[i + 1]
        yield (start, start + length)


def parse_almanac(text):
    parts = text.split("\n\n")
    seeds = parse_numbers(parts.pop(0).removeprefix("seeds: "))
    maps = dict(parse_map(part) for part in parts)
    maps["seeds"] = list(parse_seeds(seeds))
    return maps


def is_valid_seed(value, *, almanac):
    return any(start <= value < stop for start, stop in almanac["seeds"])


def brute_force_seed_from_locations(start, *, almanac, step):
    for i in range(start, start + step):
        seed = find_seed_from_location(i, almanac=almanac)
        if is_valid_seed(seed, almanac=almanac):
            return i


with open("input.txt") as f:
    almanac = parse_almanac(f.read())
    n_workers = multiprocessing.cpu_count()
    start = 0
    step = 100000
    while True:
        with ProcessPoolExecutor(max_workers=n_workers) as executor:
            results = executor.map(
                partial(brute_force_seed_from_locations, almanac=almanac, step=step),
                (start + (step * i) for i in range(n_workers)),
            )
            results = [x for x in results if x is not None]
            if results:
                print(results[0])
                break
        start += step * n_workers
