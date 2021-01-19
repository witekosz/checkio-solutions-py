from itertools import chain

import numpy as np


# TODO refactor

digits = [str(d) * 4 for d in range(1, 10)]

def checkio(matrix: list[list[int]]) -> bool:
    rows = matrix
    columns = list(map(list, zip(*rows)))

    array = np.array(matrix)
    offsets = list(reversed([-e for e in range(len(rows[0]))])) + [e for e in range(1, len(rows[0]))]
    diagonals = []
    for e in offsets:
        diagonals.append(np.diagonal(array, e))

    array = np.rot90(array)
    for e in offsets:
        diagonals.append(np.diagonal(array, e))

    for e in chain(rows, columns, diagonals):
        e = "".join(str(c) for c in e)

        for seq in digits:
            if seq == e or seq in e:
                return True
    else:     
        return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        [1, 2, 1, 1],
        [1, 1, 4, 1],
        [1, 3, 1, 6],
        [1, 7, 2, 5]
    ]) == True
    assert checkio([
        [7, 1, 4, 1],
        [1, 2, 5, 2],
        [3, 4, 1, 3],
        [1, 1, 8, 1]
    ]) == False
    assert checkio([
        [2, 1, 1, 6, 1],
        [1, 3, 2, 1, 1],
        [4, 1, 1, 3, 1],
        [5, 5, 5, 5, 5],
        [1, 1, 3, 1, 1]
    ]) == True
    assert checkio([
        [7, 1, 1, 8, 1, 1],
        [1, 1, 7, 3, 1, 5],
        [2, 3, 1, 2, 5, 1],
        [1, 1, 1, 5, 1, 4],
        [4, 6, 5, 1, 3, 1],
        [1, 1, 9, 1, 2, 1]
    ]) == True
    print('All Done! Time to check!')
