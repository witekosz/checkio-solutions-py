import math

from typing import List, Tuple
from collections import namedtuple


Triangle = namedtuple("triangle", "a b c")

Coords = List[Tuple[int, int]]

def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    triangle_1, triangle_1 = Triangle(*coords_1), Triangle(*coords_2)
    print(triangle_1, " | ", triangle_1)

    dist_coords_1 = (
        math.dist(coords_1[0], coords_1[1]),
        math.dist(coords_1[1], coords_1[2]),
        math.dist(coords_1[2], coords_1[0])
    )
    dist_coords_2 = (
        math.dist(coords_2[0], coords_2[1]),
        math.dist(coords_2[1], coords_2[2]),
        math.dist(coords_2[2], coords_2[0])
    )
    scale = tuple(map(lambda x: x[0] / x[1], zip(dist_coords_2, dist_coords_1)))

    print(dist_coords_1)
    print(dist_coords_2)
    print(scale)

    if dist_coords_1 == dist_coords_2:
        return True
    elif set(dist_coords_1) == set(dist_coords_2):
        return True
    elif scale[0] == scale[1] == scale[2]:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
