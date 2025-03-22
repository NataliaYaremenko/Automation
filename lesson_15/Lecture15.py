#SOLID

# S: Single Responsibility Principle (Принцип єдиної відповідальності)
# Кожен клас відповідає за одну дію: тварина має ім'я, клас для звуків відповідає за звуки,
# а клас для рухів відповідає за рухи.

class Animal:
    def __init__(self, name):
        self.name = name


class AnimalSound:
    def make_sound(self, animal):
        if isinstance(animal, Dog):
            return "Woof!"
        elif isinstance(animal, Cat):
            return "Meow!"


class AnimalMovement:
    def move(self, animal):
        if isinstance(animal, Dog):
            return f"{animal.name} is running!"
        elif isinstance(animal, Cat):
            return f"{animal.name} is jumping!"


class Dog(Animal):
    pass


class Cat(Animal):
    pass


# Використання
dog = Dog("Buddy")
cat = Cat("Whiskers")

sound = AnimalSound()
movement = AnimalMovement()

print(sound.make_sound(dog))  # Woof!
print(movement.move(cat))     # Whiskers is jumping!


# O: Open/Closed Principle (Принцип відкритості/закритості)
# Базовий клас Animal відкритий для розширення новими тваринами, але закритий для модифікацій.

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


class Cow(Animal):
    def make_sound(self):
        return "Moo!"


# Використання
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())


# L: Liskov Substitution Principle (Принцип підстановки Лісков)
# Підкласи повинні коректно заміняти базові класи.
# Наприклад, клас Птах поділяється на літаючих і нелітаючих птахів.

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass


class FlyingBird(Bird):
    def move(self):
        return "I can fly!"


class FlightlessBird(Bird):
    def move(self):
        return "I can walk!"


class Sparrow(FlyingBird):
    pass


class Ostrich(FlightlessBird):
    pass


# Використання
birds = [Sparrow(), Ostrich()]

for bird in birds:
    print(bird.move())


# I: Interface Segregation Principle (Принцип розділення інтерфейсу)
# Класи не повинні залежати від методів, які вони не використовують.
# Качка використовує і політ, і плавання, тоді як пінгвін - тільки плавання.

class CanFly(ABC):
    @abstractmethod
    def fly(self):
        pass


class CanSwim(ABC):
    @abstractmethod
    def swim(self):
        pass


class Duck(CanFly, CanSwim):
    def fly(self):
        return "The duck is flying!"

    def swim(self):
        return "The duck is swimming!"


class Penguin(CanSwim):
    def swim(self):
        return "The penguin is swimming!"


# Використання
duck = Duck()
penguin = Penguin()

print(duck.fly())    # The duck is flying!
print(duck.swim())   # The duck is swimming!
print(penguin.swim())  # The penguin is swimming!


# D: Dependency Inversion Principle (Принцип інверсії залежностей)
# Ми використовуємо абстракції (AnimalSound), щоб залежати від інтерфейсів, а не від конкретних реалізацій.

class AnimalSound(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class DogSound(AnimalSound):
    def make_sound(self):
        return "Woof!"


class CatSound(AnimalSound):
    def make_sound(self):
        return "Meow!"


class Animal:
    def __init__(self, sound: AnimalSound):
        self.sound = sound

    def make_sound(self):
        return self.sound.make_sound()


# Використання
dog = Animal(DogSound())
cat = Animal(CatSound())

print(dog.make_sound())  # Woof!
print(cat.make_sound())  # Meow!





# MRO (Method Resolution Order) - це порядок, у якому Python шукає методи в класах під час їх виклику.
# Це особливо важливо при роботі з множинним наслідуванням.

# Приклад 1: Класична ієрархія наслідування

class Animal:
    def speak(self):
        return "I am an animal."


class Mammal(Animal):
    def speak(self):
        return "I am a mammal."


class Dog(Mammal):
    def speak(self):
        return "I am a dog."


# Клас Dog наслідує Mammal, а Mammal - Animal.
# Якщо викликати метод speak(), Python знайде його спочатку в Dog, потім у Mammal, і лише потім в Animal.
dog = Dog()
print(dog.speak())  # Виведе: "I am a dog"

# MRO для класу Dog
print(Dog.mro())  # Виведе: [<class '__main__.Dog'>, <class '__main__.Mammal'>, <class '__main__.Animal'>, <class 'object'>]


# Приклад 2: Множинне наслідування

class Flyer:
    def action(self):
        return "I can fly."


class Swimmer:
    def action(self):
        return "I can swim."


class Duck(Flyer, Swimmer):
    pass


# Клас Duck наслідує Flyer і Swimmer.
# Python використовує MRO, щоб знайти метод action().
duck = Duck()
print(duck.action())  # Виведе: "I can fly" (береться з Flyer)

# MRO для класу Duck
print(Duck.mro())  # Виведе: [<class '__main__.Duck'>, <class '__main__.Flyer'>, <class '__main__.Swimmer'>, <class 'object'>]


# Приклад 3: Випадок "Діамант"

class A:
    def method(self):
        return "Method from A"


class B(A):
    def method(self):
        return "Method from B"


class C(A):
    def method(self):
        return "Method from C"


class D(B, C):
    pass




class LifeCycleDemo:
    # Етап створення об'єкта
    def __init__(self, name):
        self.name = name
        print(f"[__init__] Об'єкт {self.name} створений")

    # Метод демонстрації дій над об'єктом
    def do_something(self):
        print(f"[do_something] Об'єкт {self.name} виконує дію")

    # Метод завершення життєвого циклу об'єкта
    def __del__(self):
        print(f"[__del__] Об'єкт {self.name} знищений")



c1 = LifeCycleDemo()

# Створення об'єкта
obj = LifeCycleDemo("DemoObject")

# Виконання дій над об'єктом
obj.do_something()

# Примусове видалення об'єкта
del obj

# Додатковий приклад зі створенням нового об'єкта
obj2 = LifeCycleDemo("AnotherObject")
obj2.do_something()

# Кінець програми: всі об'єкти видаляються автоматично

#Double Under

import math

class UnaryExample:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"UnaryExample({self.value})"

    # __pos__ -> Додатний знак (+obj)
    # Викликається при додатному знаку перед об'єктом.
    def __pos__(self):
        return UnaryExample(+self.value)

    # __neg__ -> Від'ємний знак (-obj)
    # Викликається при від'ємному знаку перед об'єктом.
    def __neg__(self):
        return UnaryExample(-self.value)

    # __abs__ -> Абсолютне значення (abs(obj))
    # Викликається функцією abs() для отримання абсолютного значення.
    def __abs__(self):
        return UnaryExample(abs(self.value))

    # __invert__ -> Бітовий NOT (~obj)
    # Викликається при застосуванні бітової інверсії.
    def __invert__(self):
        return UnaryExample(~self.value)

    # __round__ -> Округлення (round(obj, n))
    # Викликається для округлення до n знаків після коми.
    def __round__(self, n=0):
        return UnaryExample(round(self.value, n))

    # __floor__ -> Підлога (math.floor(obj))
    # Викликається для отримання найбільшого цілого числа, яке не перевищує значення.
    def __floor__(self):
        return UnaryExample(math.floor(self.value))

    # __ceil__ -> Стеля (math.ceil(obj))
    # Викликається для отримання найменшого цілого числа, яке більше або дорівнює значенню.
    def __ceil__(self):
        return UnaryExample(math.ceil(self.value))


# Приклади використання
obj = UnaryExample(10.75)





class BinaryExample:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"BinaryExample({self.value})"

    # __add__ -> Додавання (obj1 + obj2)
    def __add__(self, other):
        return BinaryExample(self.value + other.value)

#1 + 2
#Class Integer
#1 - instance of Integer
#2 - instance of Integer
#+: int + int
#1.__add__(2)

# "1" and "2"
# 1 - instance of str
# 2 - instance of str
#+: str + str


    # __sub__ -> Віднімання (obj1 - obj2)
    def __sub__(self, other):
        return BinaryExample(self.value - other.value)

    # __mul__ -> Множення (obj1 * obj2)
    def __mul__(self, other):
        return BinaryExample(self.value * other.value)

    # __truediv__ -> Ділення (obj1 / obj2)
    def __truediv__(self, other):
        return BinaryExample(self.value / other.value)

    # __floordiv__ -> Цілочисельне ділення (obj1 // obj2)
    def __floordiv__(self, other):
        return BinaryExample(self.value // other.value)

    # __mod__ -> Залишок від ділення (obj1 % obj2)
    def __mod__(self, other):
        return BinaryExample(self.value % other.value)

    # __pow__ -> Піднесення до степеня (obj1 ** obj2)
    def __pow__(self, other):
        return BinaryExample(self.value ** other.value)

    # __eq__ -> Порівняння на рівність (obj1 == obj2)
    def __eq__(self, other):
        return self.value == other.value

    # __lt__ -> Менше (obj1 < obj2)
    def __lt__(self, other):
        return self.value < other.value

    # __le__ -> Менше або дорівнює (obj1 <= obj2)
    def __le__(self, other):
        return self.value <= other.value

    # __gt__ -> Більше (obj1 > obj2)
    def __gt__(self, other):
        return self.value > other.value

    # __ge__ -> Більше або дорівнює (obj1 >= obj2)
    def __ge__(self, other):
        return self.value >= other.value








class Vector:
    def __init__(self, x, y,z):
        self.x = x
        self.y = y
        self.z = z


    def __add__(self, other):
        # Перевіряємо, чи інший об'єкт також є вектором
        if isinstance(other, Vector):
            # Додаємо відповідні координати
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return NotImplemented  # Якщо інший об'єкт не вектор, повертаємо стандартне значення

    def __repr__(self):
        # Представлення об'єкта у вигляді рядка
        return f"Vector({self.x}, {self.y})"


# Створюємо два об'єкти класу Vector
v1 = Vector(2, 3, 5)
v2 = Vector(5, 7, 6)

# Додаємо два вектори
result = v1 + v2








# Виводимо результат
print(result)




class PublicExample:
    def __init__(self):
        self.public_var = "Я публічний"

    def public_method(self):
        return "Це публічний метод"

# Використання
obj = PublicExample()
print(obj.public_var)  # Прямий доступ до змінної
print(obj.public_method())  # Виклик публічного методу



class ProtectedExample:
    def __init__(self):
        self._protected_var = "Я захищений"

    def _get_request(self):
        return "Це захищений метод"

p1 = ProtectedExample()

p1._get_request()

class Child(ProtectedExample):
    def access_protected(self):
        return self._protected_method()

# Використання
obj = ProtectedExample()
print(obj._protected_var)  # Можна отримати доступ, але Python натякає, що це "внутрішнє"
print(obj._protected_method())  # Можна викликати

child = Child()
print(child.access_protected())  # Доступ із дочірнього класу




class PrivateExample:
    def __init__(self):
        self.__private_var = "Я приватний"

    def __private_method(self):
        return "Це приватний метод"

    def access_private(self):
        # Доступ до приватних даних всередині класу
        return self.__private_var, self.__private_method()

    def __metod1(self):
        pass

    def __metod2(self):
        pass

    def common_method(self):
        return self.__metod1() + self.__metod2() + self.__private_method()

# Використання
obj = PrivateExample()

obj.common_method()



# print(obj.__private_var)  # Помилка: AttributeError
# print(obj.__private_method())  # Помилка: AttributeError

print(obj.access_private())  # Доступ через публічний метод





class Example:
    def __init__(self):
        self.name = "Андрій"
        self.age = 30

obj = Example()


# Отримуємо значення атрибутів
print(getattr(obj, 'name'))  # Виведе: Андрій
print(getattr(obj, 'age'))   # Виведе: 30

# Атрибуту "height" немає, але можна задати значення за замовчуванням
print(getattr(obj, 'height', 'Невідомо'))  # Виведе: Невідомо

#getattr(), #setattr(), #hasattr(), #delattr


def __setattr__(self, attr):
    print("Error")





class Example:
    def __init__(self):
        self.name = "Андрій"

obj = Example()

# Змінюємо значення існуючого атрибуту
setattr(obj, 'name', 'Олексій')
print(obj.name)  # Виведе: Олексій

# Додаємо новий атрибут
setattr(obj, 'age', 25)
print(obj.age)  # Виведе: 25



class Example:
    def __init__(self):
        self.name = "Андрій"

obj = Example()

# Перевіряємо наявність атрибутів
print(hasattr(obj, 'name'))   # Виведе: True
print(hasattr(obj, 'age'))    # Виведе: False



class Example:
    def __init__(self):
        self.name = "Андрій"
        self.age = 30

obj = Example()

# Видаляємо атрибут
delattr(obj, 'age')
print(hasattr(obj, 'age'))  # Виведе: False

# Спроба видалити неіснуючий атрибут викликає помилку
# delattr(obj, 'height')  # AttributeError: 'Example' object has no attribute 'height'





