FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"
FIRST_NINETEEN = [*FIRST_TEN, *SECOND_TEN]


def checkio(number: int) -> str:

    str_repr: str = str()
    words: list = list()

    hun_div: int = number // 100
    if hun_div:
        words.append(FIRST_TEN[hun_div - 1])
        words.append(HUNDRED)
    number -= hun_div * 100

    if number < 20 and number != 0:
        words.append(FIRST_NINETEEN[number - 1])

    else:
        ten_div: int = number // 10
        if ten_div:
            words.append(OTHER_TENS[ten_div - 2])
        number -= ten_div * 10

        div: int = number // 1
        if div:
            words.append(FIRST_TEN[div - 1])

    str_repr: str = " ".join(words)

    return str_repr


# print(checkio(9))
print(checkio(133))
print(checkio(20))
print(checkio(100))

# if __name__ == '__main__':
#     assert checkio(4) == 'four', "1st example"
#     assert checkio(133) == 'one hundred thirty three', "2nd example"
#     assert checkio(12) == 'twelve', "3rd example"
#     assert checkio(101) == 'one hundred one', "4th example"
#     assert checkio(212) == 'two hundred twelve', "5th example"
#     assert checkio(40) == 'forty', "6th example"
#     assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
