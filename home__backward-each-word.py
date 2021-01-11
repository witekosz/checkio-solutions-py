# TODO solve it using regexp

def backward_string_by_word(text: str) -> str:
    reversed_text = []

    temp_word = []
    for c in text:
        if c.isspace():
            if temp_word:
                reversed_text.extend(reversed(temp_word))
                temp_word = []
            reversed_text.append(c)
        else:
            temp_word.append(c)
    else:
        if temp_word:
            reversed_text.extend(reversed(temp_word))

    return "".join(reversed_text)


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
