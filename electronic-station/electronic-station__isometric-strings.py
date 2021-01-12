def isometric_strings(str1: str, str2: str) -> bool:
    cipher_dict = {}
    for char, char2 in zip(str1, str2):
        cipher_letter = cipher_dict.setdefault(char, char2)
        if cipher_letter != char2:
            return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(isometric_strings('add', 'egg'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert isometric_strings('add', 'egg') == True
    assert isometric_strings('foo', 'bar') == False
    assert isometric_strings('', '') == True
    assert isometric_strings('all', 'all') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
