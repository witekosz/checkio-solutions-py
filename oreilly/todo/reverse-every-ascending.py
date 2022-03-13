def reverse_ascending(items: list) -> list:
    ascending_sub_items = []

    temp_sub_lst = []
    iterator = enumerate(items)
    for i, e in iterator:
        try:
            next_e = next(iterator)[1]
            temp_sub_lst.append(e)
            temp_sub_lst.append(next_e)
            if temp_sub_lst == sorted(temp_sub_lst):
                print(temp_sub_lst)
            else:
                ascending_sub_items.extend(sorted(temp_sub_lst, reverse=True))
                temp_sub_lst.clear()
        except StopIteration:
            pass
    print(ascending_sub_items)
    return ascending_sub_items


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
