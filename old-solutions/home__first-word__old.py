def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    text2 = text.replace(',', ' ')
    text3 = text2.replace('.',' ')
    text4 = text3.strip()
    if text4.startswith('.') and text.find(' '):
        word = text4[1:text4.find(' ')]
        return word
    elif text4.find(' ') != -1:
        word = text4[0:text4.find(' ')]
        return word
    else:
        return text4


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
