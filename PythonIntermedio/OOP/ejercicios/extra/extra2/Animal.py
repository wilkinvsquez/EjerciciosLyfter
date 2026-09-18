class Animal:
    def __init__(self):
        pass

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"


cat = Cat()
dog = Dog()

print(cat.speak())
print(dog.speak())