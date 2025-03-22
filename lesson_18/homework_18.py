#Реалізуйте ітератор для зворотного виведення елементів списку.
class MyIterator:
    def __init__(self, llist):
        self.llist = llist
        self.last = len(llist) - 1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.last >=0:
            output = self.llist[self.last]
            self.last -=1
            return output

numbers = [1, 2, 3, 4]
my_list = MyIterator(numbers)

print(next(my_list))
print(next(my_list))
print(next(my_list))

#Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class Odd:
    def __init__(self, first):
        self.first = first
        self.number = 2

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.number <= self.first:
            odd = self.number
            self.number += 2
            return odd
        else:
            raise StopIteration ("Enough")
        
my_odd = Odd(10)
for i in my_odd:
    print(i)
        
#Напишіть декоратор, який логує аргументи та результати викликаної функції.
import logging
logging.basicConfig(level=logging.INFO)
def logging(fun):
    def wrapper(*args, **kwargs):
        result = fun(*args, **kwargs)
        logging.info(f'Test {fun.__name__} added with the result: {args}, {kwargs}')
        return result
    return wrapper

@logging
def add(c, m):
    return c + m

add(1, 2)
#Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

#Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def fun(N):
    number = 0
    while number <= N:
        yield number
        number += 2

N = int(input("Введіть значення N: "))
for output in fun(N):
    print(output)

#Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def Fibonacci(N):
    a, b = 0, 1
    while a <= N:
        yield a 
        a, b = b, a + b

N = int(input("Введіть значення N: "))
for output in Fibonacci(N):
    print(output)




    