CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(200)
    price INTEGER
);

CREATE TABLE categories (
    categories_id SERIAL PRIMARY KEY,
    category_name VARCHAR(20),
    information VARCHAR(30)
);

CREATE TABLE serial_name(
    id INT REFERENCES categories(categories_id),
    product_name VARCHAR(20) UNIQUE NOT NULL,
    order_date DATE
)
 INSERT INTO    serial_name(id, product_name) VALUES (10, "Body Wash");
 INSERT INTO    products(product_id, name, description, price) VALUES (25, "Gel", "It has creamy texture", 155)


 SELECT id FROM serial_name FULL OUTER JOIN categories ON serial_name.id = categories.categories_id