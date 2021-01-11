from itertools import product


ROWS = "abcdefgh"
COLUMS = "12345678"
chessboard = list("".join(e) for e in product(COLUMS, ROWS))

def safe_pawns(pawns: set) -> int:
    safe_pawns = 0
    pawns = {"{1}{0}".format(*pawn) for pawn in pawns}

    for pawn in pawns:
        idx = chessboard.index(pawn)
        try:
            safe_pawn_one = chessboard[idx-7]
            safe_pawn_two = chessboard[idx-9]

            if safe_pawn_one in pawns or safe_pawn_two in pawns:
                safe_pawns += 1
        except IndexError:
            pass
    return safe_pawns


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print(safe_pawns(["a2","b2","c2","d2","e2","f2","g2","h2"]))
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
