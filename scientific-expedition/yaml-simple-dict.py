def yaml(a: str) -> dict:
    date_gen = (data for data in a.split("\n") if data)

    data_dict = {}
    for e in date_gen:
        key, value = e.split(":")
        value = value.strip()

        if value.isdigit():
            data_dict[key] = int(value)
        else:
            data_dict[key] = value

    return data_dict


if __name__ == '__main__':
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
 'class': '12b',
 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")
