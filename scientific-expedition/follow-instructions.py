def follow(instructions: str) -> tuple:
    position = [0, 0]
    position_mapping = {
        "r": ("x", 1),
        "l": ("x", -1),
        "f": ("y", 1),
        "b": ("y", -1)
    }

    for c in instructions:
        axis_name = position_mapping[c][0]
        diff = position_mapping[c][1]
        if axis_name == "x":
            position[0] += diff
        else:
            position[1] += diff
    return tuple(position)


if __name__ == '__main__':
    print("Example:")
    print(follow("fflff"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert follow("fflff") == (-1, 4)
    assert follow("ffrff") == (1, 4)
    assert follow("fblr") == (0, 0)
    print("Coding complete? Click 'Check' to earn cool rewards!")
