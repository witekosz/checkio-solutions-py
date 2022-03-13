def popular_words(text: str, words: list) -> dict:
    text_low = text.lower()
    dict_words = dict()
    list_words = text_low.split()

    for word in words:
        dict_words[word] = 0

    for word in dict_words:
        if word in list_words:
            dict_words[word] = list_words.count(word)

    return dict_words


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
