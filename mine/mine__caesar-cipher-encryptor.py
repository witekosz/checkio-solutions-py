import string


def to_encrypt(text: str, delta: int) -> str:
    alphabet = string.ascii_lowercase + string.ascii_lowercase

    encrypted_text = []
    for c in text:
        if c.isspace():
            encrypted_text.append(c)
        else:
            idx = alphabet.index(c)
            encrypted_text.append(alphabet[idx + delta])

    return "".join(encrypted_text)


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
