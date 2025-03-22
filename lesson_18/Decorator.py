

import  logging
logger = logging()

def debug(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Виклик {func.__name__} з аргументами: {args}, {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Результат: {result}")
        except Exception as e:
            logger.error(f"Сталася помилка: {e}")
        return result
    return wrapper




@debug
def add(a, b):
    return a + b
#
# add(3, 5)


def repeat(n):
    """Фабрика декораторів, що виконує функцію n разів."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
#
@repeat(3)  # Тепер функція буде виконуватись 3 рази
def hello():
    print("Hello!")
#
hello()
#
#
import time
#
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Функція {func.__name__} виконалась за {end - start:.5f} секунд")
        return result
    return wrapper
#
@timer
def slow_function():
    time.sleep(2)
    print("Робота завершена!")

slow_function()
#


def add_greeting(cls):
    """Додає метод привітання до класу"""
    cls.greet = lambda self: print(f"Привіт! Я об'єкт {self.__class__.__name__}")
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Олексій")
p.greet()