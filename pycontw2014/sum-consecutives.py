def sum_consecutives(lst: list[int]) -> list[int]:
    if not lst:
        return []

    current_num = next(iter(lst))
    local_lst = []
    return_lst = []
    for e in lst:
        if e == current_num:
            local_lst.append(e)
        else:
            current_num = e
            return_lst.append(sum(local_lst))
            local_lst = [e]

    return_lst.append(sum(local_lst))
    return return_lst


# fmt: off
if __name__ == '__main__':
    print("Example:")
    print(list(sum_consecutives([1, 1, 1, 1])))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(sum_consecutives([1, 1, 1, 1])) == [4]
    assert list(sum_consecutives([1, 1, 2, 2])) == [2, 4]
    assert list(sum_consecutives([1, 1, 2, 1])) == [2, 2, 1]
    assert list(sum_consecutives([3, 3, 3, 4, 4, 5, 6, 6])) == [9, 8, 5, 12]
    assert list(sum_consecutives([1])) == [1]
    assert list(sum_consecutives([])) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
