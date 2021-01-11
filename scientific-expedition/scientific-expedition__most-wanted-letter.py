from collections import Counter


def checkio(text: str) -> str:
    text_cleared = (c for c in text.lower() if c.isalpha())
    letter_counter = Counter(text_cleared)

    max_letters = []
    max_count = None
    for letter, value in letter_counter.most_common():
        if max_count is None:
            max_count = value
            max_letters.append(letter)
        elif value == max_count:
            max_letters.append(letter)
        else:
            break
    return sorted(max_letters)[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
