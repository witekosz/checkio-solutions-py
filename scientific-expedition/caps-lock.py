def caps_lock(text: str) -> str:
    caps = False
    text_lst = []

    for c in text:
        if c == "a":
            caps = not caps
        else:
            if caps:
                letter = c.upper()
            else:
                letter = c
            text_lst.append(letter)

    return "".join(text_lst)


if __name__ == '__main__':
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    print("Coding complete? Click 'Check' to earn cool rewards!")
