def safe_pawns(pawns: set) -> int:
    rows = "abcdefgh"
    colums = "12345678"
    positions_deltas = [(-1, -1), (1, -1)]

    safe_pawns = set()
    for pawn in pawns:
        for delta_row, delta_column in positions_deltas:
            try:
                row_idx = rows.index(pawn[0]) + delta_row
                column_idx = colums.index(pawn[1]) + delta_column
                if row_idx < 0 or column_idx < 0:
                    raise IndexError

                pawn_position = rows[row_idx] + colums[column_idx]
            except IndexError:
                continue

            if pawn_position in pawns:
                safe_pawns.add(pawn)
                continue

    return len(safe_pawns)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
