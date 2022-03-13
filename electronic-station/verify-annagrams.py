def verify_anagrams(a: str, b: str) -> bool:
    word_list = list(a.replace(" ", "").lower())

    for c in b.replace(" ", "").lower():
        try:
            word_list.remove(c)
        except ValueError:
            return False

    if word_list:
        return False
    else:
        return True


if __name__ == '__main__':
    print("Example:")
    print(verify_anagrams('Programming', 'Gram Ring Mop'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
