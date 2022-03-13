import math


def simple_areas(*args) -> float:
    match args:
        case (x,):
            r = x / 2
            return math.pi * r * r
        case (x, y):
            return x * y
        case (x, y, z):
            p = (x + y + z) / 2
            return math.sqrt(p * (p - x) * (p - y) * (p - z))
        case _:
            return 0


# fmt: off
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
