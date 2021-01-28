class Army:

    def train_swordsman(self, name):
        return self._train_unit(Swordsman, name)

    def train_lancer(self, name):
        return self._train_unit(Archer, name)

    def train_archer(self, name):
        return self._train_unit(Archer, name)

    def _train_unit(self, klass, name):
        unit = klass()
        army_nation = type(self).__name__.strip("Army")
        unit.introduce = lambda : f"{klass} {name}, {army_nation} {lower(type(klass).__name__)}"
        return unit


class Swordsman:
    european = "Knight"
    asian = "Samurai"


class Lancer:
    european = "Raubritter"
    asian = "Ronin"


class Archer:
    european = "Ranger"
    asian = "Shinobi"


class AsianArmy(Army):
    pass


class EuropeanArmy(Army):
    pass


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    my_army = EuropeanArmy()
    enemy_army = AsianArmy()

    soldier_1 = my_army.train_swordsman("Jaks")
    soldier_2 = my_army.train_lancer("Harold")
    soldier_3 = my_army.train_archer("Robin")

    soldier_4 = enemy_army.train_swordsman("Kishimoto")
    soldier_5 = enemy_army.train_lancer("Ayabusa")
    soldier_6 = enemy_army.train_archer("Kirigae")

    assert soldier_1.introduce() == "Knight Jaks, European swordsman"
    assert soldier_2.introduce() == "Raubritter Harold, European lancer"
    assert soldier_3.introduce() == "Ranger Robin, European archer"

    assert soldier_4.introduce() == "Samurai Kishimoto, Asian swordsman"
    assert soldier_5.introduce() == "Ronin Ayabusa, Asian lancer"
    assert soldier_6.introduce() == "Shinobi Kirigae, Asian archer"

    print("Coding complete? Let's try tests!")
