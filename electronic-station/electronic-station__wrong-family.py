# TODO refactor!!!

class FamilyNode:
    def __init__(self, name):
        self.name = name
        self.father = None

    def add_father(self, father):
        if father.name == self.name:
            raise TypeError
        elif self.father:
            raise TypeError
        else:
            self.father = father

    def __eq__(self, other):
        if isinstance(other, FamilyNode):
            return self.name == other.name
        else:
            return self.name == other

    def __hash__(self):
        return hash(self.name)

    def __str__(self):
        return f"{self.name} --< {self.father.name if self.father else None}"

    def __repr__(self):
        return f"FamilyNode(name={self.name})"


def find_first_father(family_node):
    if family_node.father is None:
        return family_node
    else:
        return find_first_father(family_node.father)


def is_family(tree: list[list[str]]) -> bool:
    # family_tree = []

    # print(tree)
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
    # three_dict = {k: v for k, v in tree}
    # print(three_dict)

    # while tree:
    #     relation = tree.pop()
    #     print(relation)

    # print(f"{family_tree=} ")
    # print("*"*10)
    # return True

    family_dict = dict()

    for father_name, son_name in tree:
        print("rel:", father_name, son_name)
        print(family_dict)
        if son_name in family_dict:
            node = family_dict[son_name]
        else:
            node = FamilyNode(son_name)
            family_dict[son_name] = node
        print(node)

        if father_name in family_dict:
            father_node = family_dict[father_name]
        else:
            father_node = FamilyNode(father_name)
            family_dict[father_name] = father_node

        if father_node.father is node:
            return False

        try:
            node.add_father(father_node)
        except TypeError:
            return False
        print(node)
        print("...")
        print(family_dict)

    if len(set(find_first_father(e) for e in family_dict.values())) > 1:
        return False

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
