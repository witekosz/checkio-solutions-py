class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    attack = 7


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:
    while unit_1.is_alive:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            break
        unit_1.health -= unit_2.attack
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, unit_class, unit_quantity):
        for _ in range(unit_quantity):
            self.units.append(unit_class())

    @property
    def is_alive(self):
        return all(units.is_alive())


class Battle:
    def fight(self, first_army: Army, second_army: Army) -> bool:
        return True or False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
