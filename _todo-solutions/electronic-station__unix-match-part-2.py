import re


def unix_match(filename: str, pattern: str) -> bool:
    print(filename, pattern)

    if pattern == "*":
        return True
    if "[]" in pattern:
        print("dasf")
        print(pattern)
        pattern = pattern.replace("[]", "")
        print(pattern)

    if not "." in filename:
        return False
    if "[!]" in pattern:
        pattern = pattern.replace("[!]", "")
    if "[!" in pattern:
        pattern = pattern.replace("[!", "[^")
    if "*" in pattern:
        pattern = pattern.replace("*", "\S+")
    if "?" in pattern:
        pattern = pattern.replace("?", ".")

    print(filename, pattern)
    match = re.search(rf"{pattern}", filename)
    print("match", match)

    return bool(match)


if __name__ == '__main__':
    print("Example:")
    unix_match("checkio","[c[]heckio")
    unix_match("[!]check.txt","[!]check.txt")
    print(unix_match('somefile.txt', '*'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', 'somefile.txt') == True
    assert unix_match('1name.txt', '[!abc]name.txt') == True
    assert unix_match('log1.txt', 'log[!0].txt') == True
    assert unix_match('log1.txt', 'log[1234567890].txt') == True
    assert unix_match('log1.txt', 'log[!1].txt') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
