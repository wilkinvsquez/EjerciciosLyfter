import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_perimeter():
        pass 

    @abstractmethod
    def calculate_area():
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        
    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def calculate_area(self):
        return self.side ** 2
    
    def calculate_perimeter(self):
        return 4 * self.side

class Rectangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def calculate_area(self):
            return self.base * self.height
        
    def calculate_perimeter(self):
        return 2 * (self.base * self.height)

