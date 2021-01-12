import math

from itertools import combinations
from typing import List, Tuple


def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    chains = 0

    for circle1, circle2 in combinations(circles, 2):
        # print(circle1, circle2)
        # for Python 3.8 and above
        # dist = math.dist((circle1[0], circle1[1]), (circle2[0], circle2[1]))
        dist = math.hypot(circle1[0] - circle2[0], circle1[1] - circle2[1])
        radius_sum = circle1[2] + circle2[2]

        # print(dist, radius_sum)
        if dist >= radius_sum:
            chains += 1

    return chains


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
