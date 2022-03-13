def to_camel_case(name: str) -> str:
    name = name.title()

    camel_case_lst = []
    iterator = enumerate(name)
    for i, letter in iterator:
        if letter == "_":
            next_letter = next(iterator)[1]
            camel_case_lst.append(next_letter.upper())
        else:
            camel_case_lst.append(letter)

    return "".join(camel_case_lst)


if __name__ == '__main__':
    print("Example:")
    print(to_camel_case('name'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_camel_case("my_function_name") == "MyFunctionName"
    assert to_camel_case("i_phone") == "IPhone"
    assert to_camel_case("this_function_is_empty") == "ThisFunctionIsEmpty"
    assert to_camel_case("name") == "Name"
    print("Coding complete? Click 'Check' to earn cool rewards!")
