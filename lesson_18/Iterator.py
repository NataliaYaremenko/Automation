# __iter__()  __next__()

lst = iter([1, 2, 3, 4])

lst = list(lst)
lst.append(5)
print(lst)
lst = iter(lst)
print()



# Ітерабельні обєкти
# Рядки (str)
# Списки (list)
# Кортежі (tuple)
# Множини (set)
# Словники (dict)
# Діапазони (range)
# Файли (open())
# Об'єкти, що реалізують метод __iter__() або __getitem__()



numbers = [1, 2, 3, 4]  # Це ітерований об'єкт (list)
iterator = iter(numbers)  # Отримуємо ітератор

# print(next(iterator))  # 1
# print(next(iterator))  # 2
# print(next(iterator))  # 3
# print(next(iterator))  # 4
# print(next(iterator))  # Помилка StopIteration

class Counter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.current = 0

    def __iter__(self):
        return self  # Повертаємо сам ітератор

    def __next__(self):
        if self.current < self.max_count:
            self.current += 1
            return self.current
        else:
            raise StopIteration  # Закінчили ітерацію
#
# Використання
# counter = Counter(5)
#
#


class InfiniteCounter:
    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        self.current += 1
        return self.current

# counter = InfiniteCounter()
# for num in counter:
#     print(num)

