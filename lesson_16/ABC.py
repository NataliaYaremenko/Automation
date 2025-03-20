from abc import ABC, abstractmethod

# Абстрактний клас
class Figure(ABC):
    @abstractmethod
    def area(self):
        """Метод для обчислення площі"""
        pass

    @abstractmethod
    def perimeter(self):
        """Метод для обчислення периметру"""
        pass

# Конкретні реалізації (наслідування від абстрактного класу)
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

rectangle = Rectangle(5, 10)