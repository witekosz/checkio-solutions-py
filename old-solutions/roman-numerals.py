roman_dict = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M"
}

ROMANS = (('M',  1000),
          ('CM', 900),
          ('D',  500),
          ('CD', 400),
          ('C',  100),
          ('XC', 90),
          ('L',  50),
          ('XL', 40),
          ('X',  10),
          ('IX', 9),
          ('V',  5),
          ('IV', 4),
          ('I',  1))

def checkio(data):

    data_len = len(str(data))
    data_str = str(data)

    data_str_reversed = ''.join(reversed(data_str))
    # print(data_str_reversed)

    data_list = list()

    for i, e in enumerate(data_str_reversed):
        # print(i, e)
        # print(data_str[i:])
        data_list.append(str(e) + i * '0')

    print(data_list)
    new_data_list = list()

    for i, e in enumerate(data_list):

        print(i, e)

        print(int(e) % int("1" + ("0" * i)))
        if e >= 5:

        new_data_list.insert(0, e)

    print(new_data_list)


    return ""


# checkio(6)
# checkio(76)
checkio(499)
# checkio(3888)