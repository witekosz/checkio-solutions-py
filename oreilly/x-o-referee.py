from typing import List
from itertools import chain


def checkio(game_result: List[str]) -> str:
    results_dict = {
        "XXX": "X",
        "OOO": "O"
    }
    rows = game_result
    columns = list(map("".join, zip(*rows)))
    diagonal = [
        "".join([rows[0][0], rows[1][1], rows[2][2]]),
        "".join([rows[2][0], rows[1][1], rows[0][2]])
    ]

    for e in chain(rows, columns, diagonal):
        if e in results_dict:
            return results_dict[e]
    else:
        return "D"


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
