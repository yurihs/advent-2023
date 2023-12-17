import itertools


def parse_instructions(line):
    return (0 if x == "L" else 1 for x in line.strip())


def parse_path(line):
    source, destinations = line.strip().split(" = ")
    destinations = destinations.replace("(", "").replace(")", "").split(", ")
    return source, destinations


def count_steps(*, network, instructions):
    insts = itertools.cycle(instructions)
    node = "AAA"
    steps = 0
    while node != "ZZZ":
        inst = next(insts)
        node = network[node][inst]
        steps += 1
    return steps


with open("input.txt") as f:
    instructions = parse_instructions(f.readline())
    f.readline()
    network = dict(map(parse_path, f.readlines()))
    print(count_steps(network=network, instructions=instructions))
