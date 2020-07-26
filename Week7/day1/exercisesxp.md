CREATE TABLE items (
 id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	price MONEY NOT NULL
)

INSERT INTO items (name, price) VALUES ('Small Desk',100), ('Large Desk',300),('Fan',80)

CREATE TABLE customers( id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50) NOT NULL,
                        last_name VARCHAR(50) NOT NULL)

INSERT INTO customers (first_name,last_name) VALUES ('Greg', 'Jones'),
('Sandra','Jones'),
('Scott', 'Scott'),
('Trevor', 'Green'),
('Melanie', 'Johnson')

SELECT * from items
SELECT * from items WHERE price > '80.00'
SELECT * from items WHERE price < '30.00'
SELECT * from customers WHERE last_name = 'Smith'
SELECT * from customers WHERE first_name != 'Craig'
