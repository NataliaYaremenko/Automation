class TestDataIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self  # Повертаємо сам ітератор

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration  # Закінчили ітерацію

# Приклад використання
test_data = TestDataIterator(["user1", "user2", "admin", "guest"])
for login in test_data:
    print(f"Тестуємо вхід для користувача: {login}")



def read_test_data(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()  # Повертає одну строку за раз

# Використання
for test_case in read_test_data("test_data.txt"):
    print(f"Виконання тесту: {test_case}")


import random

def infinite_login_attempts():
    users = ["user1", "user2", "admin", "guest"]
    while True:
        yield random.choice(users)  # Повертає випадкового користувача

# Використання (обмежуємо 5 спроб)
login_gen = infinite_login_attempts()
for _ in range(5):
    print(f"Перевіряємо логін для: {next(login_gen)}")



import logging

logging.basicConfig(level=logging.INFO)

def log_test_case(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Запуск тесту: {func.__name__}")
        result = func(*args, **kwargs)
        logging.info(f"Результат: {result}")
        return result
    return wrapper

@log_test_case
def test_login():
    return "Успішний логін!"

test_login()
