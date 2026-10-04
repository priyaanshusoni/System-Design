# defining a class is python


from turtle import mode


class Dog:

    species = "German"

    def __init__(self, name) -> None:
        self.species = name


dog = Dog("Indian")


print(dog.species)


# Four pillars of OOPs are
"""
1. Abstraction
2. Encapsulation --> A class is an example of Encapsulation
3. Polymorphism
4. Inheritence




"""


class Car:
    # constructor
    def __init__(self, brand, model) -> None:
        # Attributes(private by convention , with underscore)
        self.brand = brand
        self.model = model
        self._speed = 0

    def accelerate(self, increment):
        self._speed += increment

    def display_status(self):
        print(f"{self.brand} is running at {self._speed}")


corolla = Car(brand="Toyota", model="Corolla")

corolla.accelerate(20)

corolla.display_status()
