CREATE TABLE student(id SERIAL PRIMARY KEY,
					first_name VARCHAR(100) NOT NULL,
					last_name VARCHAR(200) NOT NULL,
					birth_date TIMESTAMP DEFAULT '07/26/2020')


INSERT INTO student (first_name, last_name, birth_date) VALUES ('Marc','Dupont','02/11/1998'),('Yoan','Durant','12/03/2010'),
('Lea','Martin','07/24/1987'),('Sarah','Benichou','04/07/1996'),('lea','Dupont','06/14/2003'),('Omer', 'Simpson','03/10/1980')

INSERT INTO student (first_name, last_name, birth_date) VALUES ('Andres','Camhi','03/23/1993')
INSERT INTO student (first_name, last_name, birth_date) VALUES ('Perla','Scialom','12/06/1991'),('Ariel','Camhi','10/09/1995')

SELECT * FROM student
select first_name, last_name from student
SELECT first_name, last_name from student WHERE id = 2;
SELECT * from student WHERE first_name = 'Marc' and last_name = 'Dupont'
SELECT * from student WHERE first_name = 'Marc' OR last_name = 'Dupont'
SELECT * from student WHERE first_name like  '%a%' or first_name like 'A%'
SELECT * from student WHERE first_name like 'A%'
SELECT * from student WHERE first_name like '%a'
SELECT * from student WHERE first_name like '%a_'
SELECT * from student WHERE id = 1 and id = 3
SELECT * from student WHERE birth_date >= '1/01/2000'


<!-- XP NINJA -->

SELECT * from student ORDER by last_name ASC limit 4 
select * from student limit 3 offset 2