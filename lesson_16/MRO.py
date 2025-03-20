from abc import ABC, abstractmethod

# Абстрактний клас Animal
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        """Абстрактний метод для звуку"""
        pass

# Клас Mammal (Ссавець)
class Mammal(Animal):
    def __init__(self, name = "", num_legs = 2):
        # self.name = name
        super().__init__(name)  # Викликаємо батьківський __init__
        self.num_legs = num_legs

    def sound(self):
        print("Sound")

# Клас Bird (Птах)
class Bird(Animal):
    def __init__(self, name="", wingspan = 1.5):
        super().__init__(name)  # Викликаємо батьківський __init__
        self.wingspan = wingspan

    def sound(self):
        print("Sound Chirik")

# Клас Bat (Кажан) - комбінує Mammal і Bird
class Bat(Mammal, Bird):
    def __init__(self, name, num_legs, wingspan):
        # super().__init__(name, num_legs)  # Викликає Mammal.__init__(), а потім Bird.__init__()
        # self.wingspan = wingspan  # Оскільки super() викликає тільки один __init__, додаємо вручну
        Mammal().__init__(name, num_legs)
        Bird().__init__(name, wingspan)


    def sound(self):
        return "Squeak"  # Звук кажана

# Створення об'єкта Bat
bat = Bat("Nightwing", num_legs=2, wingspan=1.5)

# mammal = Mammal("Barsik", 2)

# Вивід атрибутів
# print(f"Назва: {bat.name}, Ноги: {bat.num_legs}, Розмах крил: {bat.wingspan}, Звук: {bat.sound()}")

# Перевіряємо порядок виклику методів (MRO)
print(Bat.mro())  # Виведе порядок успадкування класів
