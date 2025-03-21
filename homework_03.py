# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії - done

alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\
"That depends a good deal on where you want to get to," said the Cat.\
"I don't much care where —" said Alice.\
"Then it doesn't matter which way you go," said the Cat.\
"—— so long as I get somewhere," Alice added as an explanation.\
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
print (alice_in_wonderland)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті - unsure/done

alice_in_wonderland = '''\'Would you tell me, please, which way I ought to go from here?\'\
\'That depends a good deal on where you want to get to,\' said the Cat.\
\'I don't much care where —\' said Alice.\
\'Then it doesn't matter which way you go,\' said the Cat.\
\'—— so long as I get somewhere,\' Alice added as an explanation.\
\'Oh, you're sure to do that,\' said the Cat, \'if you only walk long enough.\''''
print (alice_in_wonderland)

# task 03 == Виведіть змінну alice_in_wonderland на друк - unsure

alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"\
"That depends a good deal on where you want to get to," said the Cat.\
"I don't much care where —" said Alice.\
"Then it doesn't matter which way you go," said the Cat.\
"—— so long as I get somewhere," Alice added as an explanation.\
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'''
print (alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04 - done

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
print(black_sea+azov_sea)

# task 05 - done
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
together  = 375291
first = together - 222950
third = together - 250449
second = together - first - third
print(first, second, third)

# task 06 - done
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

PC = 1179 * 18
print(PC)

# task 07 - done
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019
b = 8
print (a%b)

q = 9907
w = 9
print (q%w)

e = 2789
r = 5
print (e%r)

t = 7248
y = 6
print (t%y)

u = 7128
i = 5
print (u%i)

j = 19224
k = 0
print (j%k)

# task 08 - done
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

pizza_large = 274 * 4
pizza_medium = 218 *2
juice = 35 * 4 
cake = 350
water = 21 * 3
print (pizza_large + pizza_medium + juice + cake + water)

# task 09 - done
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos = 232
photos_per_sheet = 8
print (photos/photos_per_sheet)

# task 10 - done
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
route = 1600
fuel = 9
tank = 48
print (f"Потрібно {route*fuel/100} літрів бензину")
full_fuel_route = 144
print (f'Щонайменше {full_fuel_route/tank} разів необхідно заїхати на заправку')