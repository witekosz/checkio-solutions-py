class AbstractCook:
    food_name = None
    drink_name = None

    def __init__(self):
        self.foods_sum = 0
        self.drinks_sum = 0

    def add_food(self, quantity: int, price: int):
        self.foods_sum += quantity * price

    def add_drink(self, quantity: int, price: int):
        self.drinks_sum += quantity * price

    def total(self):
        return f"{self.food_name}: {self.foods_sum}, {self.drink_name}: {self.drinks_sum}, Total: {self.foods_sum + self.drinks_sum}"


class JapaneseCook(AbstractCook):
    food_name = "Sushi"
    drink_name = "Tea"


class RussianCook(AbstractCook):
    food_name = "Dumplings"
    drink_name = "Compote"


class ItalianCook(AbstractCook):
    food_name = "Pizza"
    drink_name = "Juice"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)
    print(client_1.total())

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
