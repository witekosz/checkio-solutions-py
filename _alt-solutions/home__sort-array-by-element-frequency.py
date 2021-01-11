from collections import defaultdict


def frequency_sort(items: list) -> list:
    frequency_mapping = defaultdict(int)
    for e in items:
        frequency_mapping[e] += 1
    frequency_mapping = dict(sorted(frequency_mapping.items(), key=lambda x: x[1], reverse=True))

    ordered_items = []
    for k, v in frequency_mapping.items():
        for e in [k] * v:
            ordered_items.append(e)

    return ordered_items


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
