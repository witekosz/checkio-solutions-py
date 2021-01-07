def count_consecutive_summers(num):
    list_numbers = list(range(1, num + 1))
    matched = int()

    for i, e in enumerate(list_numbers):
        summed = e
        next_num = i
        while summed <= num:
            if summed == num:
                matched += 1
                break
            next_num += 1
            summed += list_numbers[next_num]

    return matched


print(count_consecutive_summers(42))

if __name__ == '__main__':
    print(count_consecutive_summers(42))

    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
