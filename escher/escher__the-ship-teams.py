def two_teams(sailors: dict) -> list:
    list_20_40 = []
    list_other = []

    for k, v in sailors.items():
        if v < 20 or v > 40:
            list_20_40.append(k)
        else:
            list_other.append(k)

    list_20_40_sort = sorted(list_20_40)
    list_other_sort = sorted(list_other)
    list_of_lists = []
    list_of_lists.append(list_20_40_sort)
    list_of_lists.append(list_other_sort)
    return list_of_lists


if __name__ == '__main__':
    print("Example:")
    print(two_teams({'Smith': 34, 'Wesson': 22, 'Coleman': 45, 'Abrahams': 19}))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert two_teams({
        'Smith': 34, 
        'Wesson': 22, 
        'Coleman': 45, 
        'Abrahams': 19}) == [
            ['Abrahams', 'Coleman'], 
            ['Smith', 'Wesson']
            ]

    assert two_teams({
        'Fernandes': 18,
        'Johnson': 22,
        'Kale': 41,
        'McCortney': 54}) == [
            ['Fernandes', 'Kale', 'McCortney'], 
            ['Johnson']
            ]
    print("Coding complete? Click 'Check' to earn cool rewards!")
