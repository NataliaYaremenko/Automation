#Завдання 1
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
class Manager(Employee):
        def __init__(self, name, salary, department):
            super().__init__(name, salary)
            self. department = department

class Developer(Employee):
        def __init__(self, name, salary, programming_language):
            super().__init__(name, salary)
            self.programming_language = programming_language
        
class TeamLead(Employee):
            def __init__(self, name, salary, department, team_size, programming_language):
                # Manager.__init__(self, name, salary, department)
                # Developer.__init__(self, name, salary, programming_language)
                super().__init__(name, salary)              
                self.department = department
                self.team_size = team_size
                self.programming_language = programming_language

import unittest

class TestTeamLead(unittest.TestCase):
      def test_attributes(self):
            teamlead = TeamLead("Nata", 100000, "IT", 10, "Python")
            self.assertEqual(teamlead.name, "Nata")
            self.assertEqual(teamlead.salary, 100000)
            self.assertEqual(teamlead.department, "IT")
            self.assertEqual(teamlead.team_size, 10)
            self.assertEqual(teamlead.programming_language, "Python")

if __name__ == "__main__":
    unittest.main()

#Завдання 2
from abc import ABC, abstractmethod

class Shape(ABC):
      @abstractmethod
      def area(self):
            pass
      
      @abstractmethod
      def perimeter(self):
            pass
      
class Square(Shape):
    def __init__(self, side):
            self.__side = side

    def area(self):
            return self.__side * self.__side
         
    def perimeter(self):
            return self.__side * 4


class Rectangle(Shape):
    def __init__(self, height, width):
            self.__height = height
            self.__width = width

    def area(self):
            return self.__height * self.__width
         
    def perimeter(self):
            return (self.__height + self.__width) * 2
      
shapes = [Square(10), Rectangle(2, 5)]

for shape in shapes:
    print(f"Perimeter of the {shape.__class__.__name__}: {shape.perimeter()}")
    print(f"Area of the {shape.__class__.__name__}: {shape.area()}")