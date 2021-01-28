from dataclasses import dataclass
from datetime import datetime


@dataclass
class Person:
    first_name: str
    last_name: str
    birth_date: str
    job: str
    working_years: float
    salary: int
    country: str
    city: str
    gender: str = "unknown"

    def name(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self):
        print()
        return self.age

    def work(self):
        return f"Is a {self.job}"

    def money(self):
        return f"{self.working_years * 12 * self.salary}"


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    p1 = Person("John", "Smith", "19.09.1979", "welder", 15, 3600, "Canada", "Vancouver", "male")
    print(p1)
    p2 = Person("Hanna Rose", "May", "05.12.1995", "designer", 2.2, 2150, "Austria", "Vienna")
    assert p1.name() == "John Smith", "Name"
    assert p1.age() == 38, "Age"
    assert p2.work() == "Is a designer", "Job"
    assert p1.money() == "648 000", "Money"
    assert p2.home() == "Lives in Vienna, Austria", "Home"
    print("Coding complete? Let's try tests!")
