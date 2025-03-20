#yield

def simple_generator(n):
    for i in range(1, n + 1):
        yield i

print(type(simple_generator))



gen = simple_generator(5)

print(type(gen))

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
print(next(gen))  # StopIteration



for value in simple_generator(5):
    print(value)

def infinite_counter():
    num = 1
    while True:
        yield num  # Повертає значення, зберігаючи стан
        num += 1

#
def large_numbers():
    for i in range(1, 1000001):
        yield i

gen = large_numbers()
print(next(gen))  # 1
print(next(gen))  # 2


numbers = [i for i in range(1, 1_000_000_000)]

for i in range(10):
    print(next(numbers))
#

def number_generator():
    for i in range(1_000_000):
        yield i


def read_large_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            yield line  # Повертає одну строку за раз, не завантажуючи весь файл у пам'ять

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b
fibo = fibonacci()

print(next(fibo))
print(next(fibo))
print(next(fibo))



