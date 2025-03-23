import sqlite3
import pandas as pd

# Створення підключення до бази даних (у пам'яті)
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Створення таблиць
cursor.executescript("""
CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    country TEXT
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    item TEXT,
    amount REAL,
    customer_id INTEGER,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

CREATE TABLE Shippings (
    shipping_id INTEGER PRIMARY KEY,
    status TEXT,
    customer INTEGER,
    FOREIGN KEY (customer) REFERENCES Customers(customer_id)
);
""")

# Додавання даних
customers_data = [
    (1, 'John', 'Doe', 31, 'USA'),
    (2, 'Robert', 'Luna', 22, 'USA'),
    (3, 'David', 'Robinson', 22, 'UK'),
    (4, 'John', 'Reinhardt', 25, 'UK'),
    (5, 'Betty', 'Doe', 28, 'UAE')
]

orders_data = [
    (1, 'Keyboard', 400, 4),
    (2, 'Mouse', 300, 4),
    (3, 'Monitor', 12000, 3),
    (4, 'Keyboard', 400, 1),
    (5, 'Mousepad', 250, 2)
]

shippings_data = [
    (1, 'Pending', 2),
    (2, 'Pending', 4),
    (3, 'Delivered', 3),
    (4, 'Pending', 5),
    (5, 'Delivered', 1)
]

cursor.executemany("INSERT INTO Customers VALUES (?, ?, ?, ?, ?)", customers_data)
cursor.executemany("INSERT INTO Orders VALUES (?, ?, ?, ?)", orders_data)
cursor.executemany("INSERT INTO Shippings VALUES (?, ?, ?)", shippings_data)

conn.commit()

# Функція для виконання запиту та виводу у вигляді DataFrame
def run_query(query):
    df = pd.read_sql_query(query, conn)
    print(df)

# INNER JOIN: Вибрати клієнтів та їхні замовлення
print("\nINNER JOIN (Customers & Orders):")
run_query("""
SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount
FROM Customers
INNER JOIN Orders ON Customers.customer_id = Orders.customer_id
""")

# LEFT JOIN: Всі клієнти, включаючи тих, хто не має замовлень
print("\nLEFT JOIN (Customers & Orders):")
run_query("""
SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id
""")

# RIGHT JOIN (SQLite не підтримує RIGHT JOIN напряму, використовуємо альтернативу)
print("\nRIGHT JOIN (Customers & Orders):")
run_query("""
SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount
FROM Orders
LEFT JOIN Customers ON Customers.customer_id = Orders.customer_id
""")

# CROSS JOIN: Декартовий добуток (всі можливі комбінації)
print("\nCROSS JOIN (Customers & Orders):")
run_query("""
SELECT Customers.first_name, Customers.last_name, Orders.item, Orders.amount
FROM Customers
CROSS JOIN Orders
""")

# SELF JOIN: Пошук клієнтів з однаковим віком
print("\nSELF JOIN (Customers with same age):")
run_query("""
SELECT A.first_name AS customer1, B.first_name AS customer2, A.age
FROM Customers A
JOIN Customers B ON A.age = B.age AND A.customer_id <> B.customer_id
""")

# LEFT JOIN + WHERE IS NULL: Клієнти, які не зробили жодного замовлення
print("\nCustomers without orders (LEFT JOIN + WHERE IS NULL):")
run_query("""
SELECT Customers.first_name, Customers.last_name
FROM Customers
LEFT JOIN Orders ON Customers.customer_id = Orders.customer_id
WHERE Orders.customer_id IS NULL
""")

# Закриття підключення
conn.close()
