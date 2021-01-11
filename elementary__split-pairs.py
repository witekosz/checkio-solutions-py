def split_pairs(a: str) -> list:
    if len(a) % 2 == 1:
        a += "_"

    pairs = []
    iterator = enumerate(a)
    for i, c in iterator:
        pairs.append(c + a[i + 1])
        next(iterator)
    return pairs


if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
