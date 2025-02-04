# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1


print(multiplication_table(3))
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two(a, b):
    add = a + b
    return add
print(sum_two(1, 2))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
lists = [1, 2, 3, 4, 5]
def add(i):
    middle = sum(lists) / len(lists)
    return middle
print(add(lists))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def numbers(i):
    reverse = i[::-1]
    return reverse
print(numbers("My Name"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def words(*i):
    long = sorted(i, key = len)
    return long[-1]
print(words('fdjklf', 'esoerio', 'czxsgggggdf'))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
'''Зробіть так, щоб кількість бананів була завжди в чотири рази більша, ніж яблук '''
apples = 2
def operation(apples):
    bananas = apples * 4
    return bananas
print(operation(apples))

# task 8
'''Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?'''
def together(Black, Azov):
    sea = Black + Azov
    return sea
print(together(436402, 37800))

# task 9
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
def computer_price(months, price):
    value = months * price
    return value
print(computer_price(18, 1179))

# task 10
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
def all(photography, photos_per_sheet):
    pages = photography/photos_per_sheet
    return pages
print(all(232, 8))