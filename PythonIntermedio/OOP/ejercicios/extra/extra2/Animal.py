class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"


cat = Cat("Michi")
dog = Dog("Firulais")

print(cat.speak())
print(dog.speak())