def checkio(data: list) -> str:
    crypt_dict = {}
    for e in data:
        l = list(zip((c for c in e), (ord(c) for c in e)))
        print(l)
        for c in e:
            crypt_dict[c] = ord(c)

    order = data
    print(crypt_dict)
    print(order)
    return order


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", \
        "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", \
        "Paste in"
    assert checkio(["a", "b", "c"]) == "abc", \
        "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", \
        "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", \
        "Concatenate and paste in"
