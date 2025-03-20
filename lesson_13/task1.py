import csv

# Шлях до файлів
#У папці csv поточної директорії
file1 = "csv/r-m-c.csv"
file2 = "csv/rmc.csv"
result_file = "csv/result_instructor.csv"

# Зчитування даних з першого файлу
with open(file1, mode='r', encoding='utf-8') as f1:
    reader1 = csv.reader(f1)  # Створюємо об'єкт reader для читання CSV
    header1 = next(reader1)  # Зчитуємо заголовок першого файлу
    data1 = []  # Список для збереження даних
    for row in reader1:  # Ітеруємося по кожному рядку файлу
        data1.append(tuple(row))  # Додаємо кожен рядок у список як кортеж

# Зчитування даних з другого файлу
with open(file2, mode='r', encoding='utf-8') as f2:
    reader2 = csv.reader(f2, delimiter=";")  # Створюємо об'єкт reader для другого файлу
    #delimiter=";" - додаємо цей аргумент, оскільки він є роздільником
    header2 = next(reader2)  # Зчитуємо заголовок другого файлу
    data2 = []  # Список для збереження даних
    for row in reader2:  # Ітеруємося по кожному рядку файлу
        data2.append(tuple(row))  # Додаємо кожен рядок у список як кортеж

# Перевірка, чи заголовки співпадають
if header1 != header2:  # Порівнюємо заголовки з обох файлів
    raise ValueError("Заголовки файлів не співпадають!")  # Генеруємо помилку, якщо заголовки різні

# Видалення дублікатів
unique_data = list(set(data1).symmetric_difference(set(data2)))  # Знаходимо унікальні записи через symmetric_difference

# Запис результатів у новий файл
with open(result_file, mode='w', encoding='utf-8', newline='') as result:
    writer = csv.writer(result)  # Створюємо writer для запису у CSV
    writer.writerow(header1)  # Записуємо заголовок у результуючий файл
    writer.writerows(unique_data)  # Записуємо унікальні дані у файл

# Виведення результату
print(f"Дублікати видалено. Результат збережено у {result_file}.")
