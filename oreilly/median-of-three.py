from typing import Iterable
from statistics import median


def median_three(els: Iterable[int]) -> Iterable[int]:
    els_median = []
    for i, e in enumerate(els):
        if i >= 2:
            els_median.append(median(els[i-2:i+1]))
        else:
            els_median.append(e)
    return els_median


if __name__ == '__main__':
    print("Example:")
    print(list(median_three([1, 2, 3, 4, 5, 6, 7])))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(median_three([1, 2, 3, 4, 5, 6, 7])) == [1, 2, 2, 3, 4, 5, 6]
    assert list(median_three([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
