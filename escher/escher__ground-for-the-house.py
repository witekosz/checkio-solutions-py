def house(plan: str) -> int:
    rows = plan.strip().splitlines()
    colums = list(map("".join, zip(*rows)))

    rows_idx = [i+1 for i, row in enumerate(rows) if "#" in row]
    if rows_idx:
        rows_len = len(list(range(rows_idx[0], rows_idx[-1] + 1)))
    else:
        rows_len = 0

    colums_idx = [i+1 for i, colum in enumerate(colums) if "#" in colum]
    if colums_idx:
        columns_len = len(list(range(colums_idx[0], colums_idx[-1] + 1)))
    else:
        columns_len = 0

    return rows_len * columns_len


if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")
