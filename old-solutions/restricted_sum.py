def checkio(data):
    total = int()
    print("test")

    def add(x):
        nonlocal total
        total += x

    list(map(add, data))

    return total

print(checkio([1, 2, 3]))
