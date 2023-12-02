def parse_set(x):
    red, green, blue = 0, 0, 0
    for cube in x.split(", "):
        value, name = cube.split(" ")
        if name == "red":
            red += int(value)
        elif name == "green":
            green += int(value)
        elif name == "blue":
            blue += int(value)
    return (red, green, blue)


def validate_game(x):
    name, sets = x.strip().split(": ")
    game_id = int(name.removeprefix("Game "))
    cubes = map(parse_set, sets.split("; "))
    shown_red, shown_green, shown_blue = map(max, zip(*cubes))
    is_valid = shown_red <= 12 and shown_green <= 13 and shown_blue <= 14
    return game_id if is_valid else 0


with open("input.txt") as f:
    print(sum(map(validate_game, f)))
