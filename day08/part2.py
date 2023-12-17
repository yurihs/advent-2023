import itertools
import math


def parse_instructions(line):
    return (0 if x == "L" else 1 for x in line.strip())


def parse_path(line):
    source, destinations = line.strip().split(" = ")
    destinations = destinations.replace("(", "").replace(")", "").split(", ")
    return source, destinations


def count_steps(*, network, instructions):
    insts = itertools.cycle(instructions)
    starting_nodes = tuple(x for x in network if x.endswith("A"))
    nodes = tuple(starting_nodes)
    steps = 0
    distances = [None for _ in starting_nodes]
    while any(x is None for x in distances):
        for i, node in enumerate(nodes):
            if node.endswith("Z") and distances[i] is None:
                distances[i] = steps
        inst = next(insts)
        nodes = tuple(network[x][inst] for x in nodes)
        steps += 1
    return math.lcm(*distances)


with open("input.txt") as f:
    instructions = parse_instructions(f.readline())
    f.readline()
    network = dict(map(parse_path, f.readlines()))
    print(count_steps(network=network, instructions=instructions))
