class Person:
    def __init__(self):
        self._age = 0  # начальное значение

    def set_age(self, age):
        if age < 0:
            print("Ошибка: возраст не может быть отрицательным!")
        else:
            self._age = age

    def get_age(self):
        return self._age


# Пример использования
p = Person()
p.set_age(25)
print(p.get_age())  # Вывод: 25

p.set_age(-5)  # Ошибка



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am {name}  an animal"

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return "Woof"

class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)

    def speak(self):
        return "Meow"

# Пример использования:
dog = Dog("Buddy")
cat = Cat("Kitty")

print(dog.name, dog.speak())  # Вывод: Buddy Woof
print(cat.name, cat.speak())  # Вывод: Kitty Meow


class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is driving"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is pedaling"


# Полиморфная функция
def move(vehicle):
    return vehicle.move()


# Пример использования:
car = Car()
bike = Bicycle()

print(move(car))   # Car is driving
print(move(bike))  # Bicycle is pedaling

import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Пример использования:
rect = Rectangle(10, 5)
circle = Circle(7)

print(rect.area())  # Вывод: 50
print(circle.area())  # Вывод: ~153.94