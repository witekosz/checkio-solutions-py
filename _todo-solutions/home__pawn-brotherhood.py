ROWS = "abcdefgh"
COLUMNS = "12345678"

def safe_pawns(pawns: set) -> int:
    safe_pawns = 0
    print(pawns)
    for pawn in pawns:
        if COLUMNS[COLUMNS.find(pawn[1])] != "1":
            try:
                diagonal_left = ROWS[ROWS.index(pawn[0])-1] + COLUMNS[COLUMNS.index(pawn[1])-1]
                print("d-l ", diagonal_left)
            except IndexError:
                diagonal_left = "unsafe"

            try:
                diagonal_right = ROWS[ROWS.index(pawn[0])+1] + COLUMNS[COLUMNS.index(pawn[1])-1]
                print("d-r ", diagonal_right)
            except IndexError:
                diagonal_right = "unsafe"

            if diagonal_left in pawns or diagonal_right in pawns:
                print("safe")
                safe_pawns += 1

    print(safe_pawns)
    return safe_pawns


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"])
    # print(safe_pawns(["a2","b2","c2","d2","e2","f2","g2","h2"]))
    # assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    # assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
