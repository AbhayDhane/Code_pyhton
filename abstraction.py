from abc import ABC, abstractmethod

# Abstract class
class Shape(ABC):
    # Abstract method (no implementation here)
    @abstractmethod
    def area(self):
        pass

    # Abstract method
    @abstractmethod
    def perimeter(self):
        pass

# Concrete class inheriting from Shape
class Rectangle(Shape):
    # Constructor to initialize length and width
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Implementing abstract method area
    def area(self):
        return self.length * self.width

    # Implementing abstract method perimeter
    def perimeter(self):
        return 2 * (self.length + self.width)

# Another concrete class inheriting from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Creating objects
rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

circle = Circle(7)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())
