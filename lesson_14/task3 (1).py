# Інкапсуляція означає приховування внутрішньої реалізації об'єкта та надання доступу до даних через публічний інтерфейс.
# Це дозволяє захистити дані від некоректного використання або прямого втручання.
#
# Дані (поля) і методи (функції) групуються всередині одного класу.
# Доступ до даних контролюється за допомогою модифікаторів доступу: private, protected, public.


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватна змінна

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів")

    def get_balance(self):
        return self.__balance  # Доступ через метод

# Наслідування дозволяє створювати нові класи на основі існуючих.
# Новий клас (похідний) успадковує властивості та методи батьківського класу.
#
# Це сприяє повторному використанню коду.
# Дозволяє розширювати або змінювати функціональність базового класу.


class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Гав!"

class Cat(Animal):
    def speak(self):
        return "Мяу!"

# Поліморфізм дозволяє використовувати один і той самий метод у різних класах із різною реалізацією.
# Це підвищує гнучкість та масштабованість коду.
#
# Методи з однаковими іменами в різних класах можуть поводитися по-різному.
# Поліморфізм реалізується за допомогою наслідування та перевизначення методів.

def animal_speak(animal):
    print(animal.speak())

dog = Dog()
cat = Cat()

animal_speak(dog)  # Гав!
animal_speak(cat)  # Мяу!


# Абстракція дозволяє приховувати складність системи, показуючи тільки суттєві деталі.
# В ООП це досягається за допомогою абстрактних класів та інтерфейсів.
#
# Абстрактний клас — це клас, у якому є методи без реалізації.
# Абстракція допомагає створювати шаблони для класів.



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

rect = Rectangle(5, 10)
print(rect.area())  # 50





# Super

class Parent:
    def greet(self):
        print("Привіт із батьківського класу!")

class Child(Parent):
    def greet(self):
        super().greet()  # Виклик методу greet() з батьківського класу
        print("Привіт із дочірнього класу!")

child = Child()
child.greet()




class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Виклик __init__ батьківського класу
        self.age = age

child = Child("Олександр", 25)
print(child.name)  # Олександр
print(child.age)   # 25
