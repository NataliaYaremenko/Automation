import logging

# Налаштування логера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Генератор парних чисел до N
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i


# Генератор послідовності Фібоначчі до N
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# Ітератор для зворотного виведення списку
class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]


# Ітератор для парних чисел у діапазоні від 0 до N
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 2
        if self.current > self.n:
            raise StopIteration
        return self.current


# Декоратор для логування аргументів і результату функції
def log_function(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"Виклик: {func.__name__}({args}, {kwargs}) -> {result}")
        return result

    return wrapper


# Декоратор для перехоплення винятків
def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Помилка у {func.__name__}: {e}")
            return None

    return wrapper


# Приклад використання декораторів
@log_function
@exception_handler
def divide(a, b):
    return a / b


# Тестування
if __name__ == "__main__":
    print("Парні числа до 10:", list(even_numbers(10)))
    print("Фібоначчі до 50:", list(fibonacci(50)))

    rev_iter = ReverseIterator([1, 2, 3, 4, 5])
    print("Зворотний список:", list(rev_iter))

    even_iter = EvenIterator(10)
    print("Парні числа з ітератора:", list(even_iter))

    print("Ділення 10 на 2:", divide(10, 2))
    print("Ділення 10 на 0:", divide(10, 0))
