def long_repeat(line: str) -> int:
    """
        length the longest substring that consists of the same char
    """
    max_counter = 0

    temp_counter = 0
    for i, c in enumerate(line):
        try:
            temp_counter += 1
            next_char = line[i+1]
            if c != next_char:
                if temp_counter > max_counter:
                    max_counter = temp_counter
                temp_counter = 0
        except IndexError:
            pass
        finally:
            if temp_counter > max_counter:
                max_counter = temp_counter

    return max_counter


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(long_repeat("aaa"))
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
