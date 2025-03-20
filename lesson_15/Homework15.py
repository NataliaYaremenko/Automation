class Rhombus:
    def __init__(self, side_a, angle_a=None, angle_b=None):
        # Перевірка, чи сума кутів angle_a та angle_b дорівнює 180 градусів
        if angle_a is not None and angle_b is not None:
            if angle_a + angle_b != 180:
                raise ValueError("The sum of angles angle_a and angle_b must be equal to 180 degrees.")
        self.side_a = side_a
        if angle_a is not None:
            self.angle_a = angle_a
        elif angle_b is not None:
            self.angle_b = angle_b

    def __setattr__(self, key, value):
        # Метод __setattr__ викликається при встановленні значення атрибутів
        # Виконує валідацію значень та автоматично обчислює залежний кут
        if key == "side_a":
            if value <= 0:
                value = abs(value)  # Якщо сторона від'ємна, беремо модуль
        elif key == "angle_a":
            if not (0 < value < 180):
                raise ValueError("Angle must be in the range of 0 to 180 degrees.")
            self.__dict__["angle_b"] = 180 - value  # Автоматично обчислюємо angle_b
        elif key == "angle_b":
            if not (0 < value < 180):
                raise ValueError("Angle must be in the range of 0 to 180 degrees.")
            self.__dict__["angle_a"] = 180 - value  # Автоматично обчислюємо angle_a
        self.__dict__[key] = value

#Bonus1
def calculate_volume(obj):
    """
    Приймає об'єкт, який має метод volume, викликає цей метод та повертає результат.

    :param obj: Об'єкт, який має метод volume
    :return: Результат виклику методу volume
    """
    if hasattr(obj, 'volume') and callable(getattr(obj, 'volume')):
        return obj.volume()
    else:
        raise AttributeError("Об'єкт не має методу 'volume'")

#Bonus2
class Person:
    def __init__(self, name, age):
        """
        Ініціалізація об'єкта класу Person.

        :param name: Ім'я особи
        :param age: Вік особи
        """
        self.name = name
        self.age = age

    def __str__(self):
        """
        Повертає рядкове представлення об'єкта у форматі
        "name=yourName, age=yourAge".
        """
        return f"name={self.name}, age={self.age}"