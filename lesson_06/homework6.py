#1.	Напишіть функцію, яка приймає список чисел і повертає новий список,
# що містить лише парні числа.
lst = [1, 2, 4, 5, 6]

def check(i):
    if i%2==0:
        return i
def parni(numbers):

    result = list(filter(check, numbers))
    #OR - result = sorted(iterablle, reverse = True)
    #OR - result = filter(check, numbers)
    return result
print(parni(lst))


#3.	Напишіть програму, яка за допомогою filter залишає
# тільки числа більше 10 зі списку чисел.
lst = [20, 4, 50, 7, 8, 10, 9, 11]

def criteria(i):
    if i > 10:
        return i

def greater_10(numbers):
    result = list(filter(criteria, numbers))
    return result
print(greater_10(lst))

#Functions
def oeration(nums):
    for i in nums:
        return i

print(oeration(1, 2))

''''''
def open(i):
    a = i + 2
print(open(1))

''''''
def operation(i):
    if i%2==0:
        return i

if operation(2):
    print('Yes')
''''''
 #lambda
def suma(a, b):
    return a + b
lambda a, b: a + b

''''''
lst = [1, 2, 3, 4, 5]

result = list(filter(lambda x: x%2, lst))
print(result)
''''''
lst = [(1, 10), (2, 7), (4, 50)]

result = list(sorted(lst, key = lambda x: x[1]))
print(result)
''''''
lst = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2, lst))
print(result)
''''''
#reduce
from functools import reduce
lst = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x+y, lst)
print(result)
''''''
#not used argument
def operation(var):
    return 1
print(operation(1))
#or
def operation():
    return 1
print(operation(1))
#defaulted argument
def greeting(name="Guest"):
    return f"Hello, {name}!"
print(greeting("Naataliia"))
#
def greeting(name, surname):
    return f"My name is {name}. My surname is {surname}"
print(greeting("Nataliia", "Dow"))
#or print(greeting(surname ="Dow", name = "Dow"))

#
def devide(a , b):
    return a / b
print(devide(10))
#
x = int(input('Enter your number a: '))
y = int(input('Enter your number b: '))

def divide (a=1, b=2):
    return a / b

print(devide(x, y))
#*args,
def greeting(*names):
    print(list(names))
greeting("Natalia", 'Kyrylo')
#kwargs
def greeting(*names, **names1):
    print(list(names, names1))
greeting("Natalia", 'Kyrylo', name1 = 'Ola')
#FIRST = POSITION, THEN - NAMED
def sum(a, b, /, c):
    return a+b+c
print(sum(1,2,c = 3))
#bad choise
def date_format(day, month, year, sep="."):
    lst= [str(day), str(month), str(yesr)]
    result = sep.join(lst)
    return result
#good choise
def date_format(day, month, year, sep="."):
    if 1<=day<=31:
        day = str(day)
        if len(day) == 1:
    else:
        print('Incorrect day!')
    lst = [day, str, str]
    result = sep.join(lst)
    return result
#grades
def compare_grades(grades1, grades2):
    keys1 = set(grades1.keys())
    keys2 = set(grades2.keys())
    all_keys = keys1.intersection(keys2)

    result = {}
    for key in all_keys:
        result[key] = grades1.get(key, 0) - grades2.get(key, 0)
    return result
print(compare_grades(grades_1, grades_2))
#EXEPTION
def find_value_by_key(dict, key):
    try:
        return dict[key]
    except ZeroDivisionError:
#   except Exception as e:
        return "No"
#       return f"Error was happened: {e}"
print(find_value_by_key({"name":'Natalia'}, 'Name'))

#
def find_value_by_key(dict, key):
    try:
        print(dict[key])
    except Exeption as e:
        print(f"During {find_value_by_key.__name__} {e} was happened")
    else:
        print("Code is correct")
    finally:
        print("Program is finished")

find_value_by_key({"name":'Natalia'}, 'Name')
#
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("zero is not possible")
    return a/b
print(divide(10, 0))
#
def date(day, month):
    if day > 31:
        raise ValueError("Days are incorrect!")
    return str(day) + "." + str(month)
print(date(40, 12))
#
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#homework1
lst_homework = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']
def homework(lst):
    for val in lst:
        lst1 = val.split(',')
        try:
            lst2 = [int(i) for i in lst1]
            res = sum(lst2)
        except:
            res = 'I cannot'
        finally:
            result.append(res)
    return result
print(homework(lst_homework))
#homework2
def calculate_sum_from_file(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        "File was not found"
        return "File was not found"
print(calculate_sum_from_file('example1.txt'))
#function
def function_name(arg1, arg2):
    print('inside function_name arg1 is:', arg1)
    print('inside function_name arg2 is:', arg2)
    res = arg1+arg2
    return res
result = function_name(1, 2)
print('result is', result)
#
def add_to_list(value, list_to_add=None):
    if list_to_add is None:
        list_to_add = []
    list_to_add.append(value)
    return list_to_add
new_list = add_to_list(True)
print(new_list)
#
def functions(a, b,c):
    print(f'a is {a}, {type(a)}')
    print(f'b is {b}, {type(b)}')
    print(f'c is {c}, {type(c)}')
    return
functions((1, '2', True))
#
my_dict = {'a': 10,'b':20, 'c' : 22}
def custom(a, b, c=10, *args, **kwargs):
    print(a, b, c, d)
    return
