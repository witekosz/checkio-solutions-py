def house(plan: str) -> int:
    print(plan)
    rows = plan.strip().splitlines()

    min_x, max_x = 0, 0
    for row in rows:
        row_left_idx = row.find("#")
        row_right_idx = row.rfind("#")
        if row_left_idx != -1:
            if row_left_idx < min_x:
                min_x = row_left_idx + 1
            if row_right_idx > max_x:
                max_x = row_right_idx + 1
            print(min_x, max_x)
    print("end rows")
    print("\n")

    colums = list(zip(*rows))
    min_y, max_y = 0, 0
    for column in colums:
        column = "".join(column)

        column_left_idx = column.find("#")
        column_right_idx = column.rfind("#")
        if column_left_idx != -1:
            if column_left_idx < min_y:
                min_y = column_left_idx
            if column_right_idx > max_y:
                max_y = column_right_idx
        print(min_y, max_y)
    print("end columns")
    print("\n")

    print(max_x, min_x, max_y, min_y)
    ret = (max_x - min_x) * (max_y - min_y)
    print("ret", ret)
    print("\n")
    return ret


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
