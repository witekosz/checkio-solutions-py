def can_pass(matrix: tuple, first: tuple, second: tuple):
    matrix = [list(m) for m in matrix]

    x_val = matrix[first[1]][first[0]]
    y_val = matrix[second[1]][second[0]]
    print(x_val, y_val)
    if x_val != y_val:
        return False

    val = x_val
    yx = first[0], first[1]
    new_coord = [yx]
    while new_coord:
        y, x = new_coord.pop()
        matrix[y][x] = "x"
        print((y, x))
        if (y, x) == second:
            return True

        if matrix[y][x+1] == val:
            print("E", matrix[y][x+1])
            matrix[y][x+1] = "E"
            new_coord.append((y, x+1))
        elif matrix[y][x-1] == val:
            print("W", matrix[y][x-1])
            matrix[y][x-1] = "W"
            new_coord.append((y, x-1))
        elif matrix[y+1][x] == val:
            print("S", matrix[y+1][x])
            matrix[y+1][x] = "S"
            new_coord.append((y+1, x))
        elif matrix[y-1][x] == val:
            print("N", matrix[y-1][x])
            matrix[y-1][x] = "N"
            new_coord.append((y-1, x))

        print("new_coord", new_coord)
        for m in matrix:
            print(m)
        print("-"*18)

    print(first)
    print(second)

    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) == False, 'First example'
