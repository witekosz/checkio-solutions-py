import math

from collections import namedtuple
from itertools import combinations
from typing import List, Tuple


Circle = namedtuple("Circle", "x y r")

def count_chains(circles: List[Tuple[int, int, int]]) -> int:
    circles = [Circle(*c) for c in circles]
    chains = 0
    counted = set()
    print(circles)

    for circle1, circle2 in combinations(circles, 2):
        print(circle1, circle2)
        dist = math.dist((circle1.x, circle1.y), (circle2.x, circle2.y))
        radius_sum = circle1.r + circle2.r

        print(dist, radius_sum)
        if dist >= radius_sum:
            print("one")
            if f"{hash(circle1)}:f{hash(circle2)}" in counted or f"{hash(circle2)}:f{hash(circle1)}" in counted:
                pass
            else:
                chains += 1
                counted.add(f"{hash(circle1)}:f{hash(circle2)}")
                counted.add(f"{hash(circle2)}:f{hash(circle1)}")
            print(counted)
    print("chains: ", chains)
    print("*"*20)
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
