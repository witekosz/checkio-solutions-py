VOWELS = "aeiouy"

def translate(phrase: str) -> str:
    translated_lst = []
    iterator = enumerate(phrase)

    for i, letter in iterator:
        try:
            if letter in VOWELS:
                next_letter = phrase[i+1]
                if next_letter in VOWELS and letter == next_letter:
                    translated_lst.append(letter)
                    next(iterator), next(iterator)
            else:
                translated_lst.append(letter)
        except IndexError:
            pass

    return "".join(translated_lst)


if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
