class Employee:
    """Базовий клас, що містить ім'я та зарплату співробітника."""
    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary


class Manager(Employee):
    """Клас менеджера з додатковим атрибутом department."""
    def __init__(self, name: str, salary: float, department: str):
        super().__init__(name, salary)
        self.department = department


class Developer(Employee):
    """Клас розробника з додатковим атрибутом programming_language."""
    def __init__(self, name: str, salary: float, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language


class TeamLead(Employee):
    def __init__(self, name: str, salary: float, department: str, programming_language: str, team_size: int):
        super().__init__(name, salary)
        # Окремо ініціалізуємо Manager та Developer
        self.department = department
        self.programming_language = programming_language
        self.team_size = team_size


# Тест для TeamLead
import unittest


class TestTeamLead(unittest.TestCase):
    def test_attributes(self):
        lead = TeamLead("Ivan", 5000, "Development", "Python", 5)
        self.assertEqual(lead.name, "Ivan")
        self.assertEqual(lead.salary, 5000)
        self.assertEqual(lead.department, "Development")
        self.assertEqual(lead.programming_language, "Python")
        self.assertEqual(lead.team_size, 5)


if __name__ == "__main__":
    unittest.main()




# Завдання 2
from abc import ABC, abstractmethod
class Figure(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__width + self.__height)


class Circle(Figure):
    def __init__(self, radius: float):
        self.__radius = radius

    def area(self):
        return 3.14 * self.__radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.__radius

class Square(Figure):
    def __init__(self, side: float):
        self.__side = side

    def area(self):
        return (self.__side)**2

    def perimeter(self):
        return 4 * self.__side


class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        self.__a = a
        self.__b = b
        self.__c = c

    def area(self):
        s = (self.__a + self.__b + self.__c) / 2
        return (s * (s - self.__a) * (s - self.__b) * (s - self.__c)) ** 0.5

    def perimeter(self):
        return self.__a + self.__b + self.__c



# Створюємо об'єкти фігур
shapes = [
    Rectangle(5, 10),
    Circle(7),
    Triangle(3, 4, 5),
    Square(10)
]

# Виведення площі та периметра кожної фігури
for shape in shapes:
    print(f"Фігура: {shape.__class__.__name__}, Площа: {shape.area():.2f}, Периметр: {shape.perimeter():.2f}")


