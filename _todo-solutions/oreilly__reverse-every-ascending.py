def reverse_ascending(items: list) -> list:
    ascending_sub_items = []

    temp_sub_lst = []
    for i, e in enumerate(items):
        print(e, items[i+1])
        next_e = items[i+1]
        if next_e > e:
            temp_sub_lst.append(next_e)
        else:
            ascending_sub_items.extend(sorted(temp_sub_lst, reverse=True))
            temp_sub_lst.clear()
            ascending_sub_items.append(e)
        print("temp_sub_lst", temp_sub_lst)
        print("ascending_sub_items", ascending_sub_items)
    print(items)
    return items


if __name__ == '__main__':
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
