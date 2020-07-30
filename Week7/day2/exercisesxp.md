UPDATE student
set first_name = 'Lea'
WHERE
first_name='lea'

UPDATE student 
SET birth_date = '02/11/1998'
WHERE 
last_name = 'Dupont'


DELETE from student
WHERE
first_name = 'Lea' and last_name ='Dupont'

SELECT count(*) from student

SELECT count(*) from student WHERE birth_date > '1/01/2000'

ALTER TABLE student ADD COLUMN math_grade smallint

UPDATE student SET math_grade = 80
WHERE id=1 

UPDATE student SET math_grade = 90
WHERE id=2 or id =4

UPDATE student SET math_grade = 100
WHERE id=6

SELECT count(math_grade>83) FROM student

INSERT INTO student (first_name, last_name, birth_date, math_grade) VALUES ('Omer','Simpson','1980-03-10',70)

SELECT first_name, last_name, count(math_grade) from student as total_grade 
GROUP BY first_name, last_name

select sum(math_grade) from student


<!-- EXERCISE 2 -->

select * from items ORDER BY price ASC

select * from items WHERE price > '80' ORDER BY price DESC

select first_name, last_name from customers ORDER BY first_name ASC limit 3

select first_name, last_name from customers ORDER BY first_name DESC limit 2

select last_name from customers ORDER BY last_name DESC 


CREATE TABLE purchases(purchases_id integer PRIMARY KEY,
					  customer_id integer REFERENCES customers(id),
					  items_id integer REFERENCES items(id));

INSERT INTO purchases (customer_id) VALUES (2). It works (?)

INSERT INTO purchases (customer_id, items_id) VALUES (
1,1), (2,2), (3,3), (4,1), (5,2)

select * from purchases, this is useles.

select * from purchases
inner join customers 
ON customers.id = purchases.customer_id

select * from purchases
inner join customers 
ON customers.id = purchases.customer_id
WHERE id = 4

select * from purchases
inner join items 
ON items.id = purchases.customer_id
WHERE items.name = 'Large desk' OR items.name = 'small desk'

INSERT INTO purchases (items_id,customer_id) VALUES (4,3)

select * from purchases 
inner join items 
ON items.id = purchases.items_id
inner join customers
ON customers.id = purchases.customer_id



