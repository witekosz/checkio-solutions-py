from collections import namedtuple


FatherNode = namedtuple("FatherNode", "father_name children_names")

def is_family(tree: list[list[str]]) -> bool:
    family_tree = []

    print(tree)
    # for father, son in tree:
    #     print(father, "=>", son)
    #     father_in_family = list(filter(lambda x: x.father_name == father, family_tree))
    #     print("len =", len(father_in_family))
    #     if not father_in_family:
    #         family_tree.append(FatherNode(father, [son]))
    #     elif len(father_in_family) == 1:
    #         father_in_family[0].children_names.append(son)
    #     elif len(father_in_family) > 1:
    #         print("Error? ", father_in_family)
    three_dict = {k: v for k, v in tree}
    print(three_dict)

    while tree:
        relation = tree.pop()
        print(relation)

    print(f"{family_tree=} ")
    print("*"*10)
    return True


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_family([
      ['Logan', 'Mike']
    ]) == True, 'One father, one son'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack']
    ]) == True, 'Two sons'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == True, 'Grandfather'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Logan']
    ]) == False, 'Can you be a father to your father?'
    assert is_family([
      ['Logan', 'Mike'],
      ['Logan', 'Jack'],
      ['Mike', 'Jack']
    ]) == False, 'Can you be a father to your brother?'
    assert is_family([
      ['Logan', 'William'],
      ['Logan', 'Jack'],
      ['Mike', 'Alexander']
    ]) == False, 'Looks like Mike is stranger in Logan\'s family'
    assert is_family([
      ['Jack', 'Mike'],
      ['Logan',  'Mike'],
      ['Logan', 'Jack'],
    ]) == False, 'Two fathers'
    print("Looks like you know everything. It is time for 'Check'!")
