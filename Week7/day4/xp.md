SELECT first_name AS FirstName, last_name AS LastName from employees

SELECT DISTINCT department_id FROM employees

SELECT * from employees ORDER BY first_name DESC

SELECT first_name, last_name, salary, sum(salary*0.15) as PF from employees group by employee_id

SELECT first_name, last_name, employee_id, salary from employees order by salary asc

select sum(salary) from employees

select max(salary), min(salary) from employees

select avg(salary),count(salary) from employees

select count(employee_id) from employees

select distinct count(job_id) from employees
<!-- I DONT UNDERSTAND THIS QUESTION, WHAT DOES DESIGNATIONS MEAN? -->

SELECT UPPER(first_name) AS FIRST_NAME from employees

SELECT SUBSTRING(first_name,0,4)  from employees

select sum(171*214+625)

select trim(first_name) from employees

select first_name, last_name, length(concat(first_name, last_name)) as name_length from employees

SELECT first_name FROM employees limit 10

SELECT first_name, last_name, round(sum(salary/12),2) FROM employees group by employee_id

CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
country_name VARCHAR(50) NOT NULL, region_id INTEGER)

CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
country_name VARCHAR(50) NOT NULL, region_id INTEGER)

CREATE TABLE dupcountries
AS TABLE countries
WITH NO DATA;

INSERT INTO dupcountries
SELECT country_id, country_name, region_id
FROM countries

<!-- CONTINUE FROM CREATE TABLES 6. -->

CREATE TABLE jobs (jobs_id SERIAL PRIMARY KEY,
				   job_tittle VARCHAR(80) NOT NULL,
				   min_salary money,
				   max_salary money CONSTRAINT MaxSalary CHECK (max_salary < '25000'))

CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
						country_name varchar(50) NOT NULL UNIQUE CHECK(country_name IN Italy, China, India),
						region_id INTEGER NOT NULL)
						

CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
						country_name varchar(50) NOT NULL UNIQUE,
						region_id INTEGER NOT NULL)

CREATE TABLE jobs (job_id SERIAL PRIMARY KEY,
                   job_tittle VARCHAR(80) default ' ' NOT NULL ,
                   min_salary MONEY default '8000',
                   max_salary MONEY)

CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
                        country_name VARCHAR(50) UNIQUE,
                        region_id integer UNIQUE)
						
						

CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
                        country_name VARCHAR(50) UNIQUE,
                        region_id integer UNIQUE)


CREATE TABLE countries (country_id SERIAL PRIMARY KEY,
                        country_name VARCHAR(50) UNIQUE,
                        region_id integer UNIQUE)

CREATE TABLE job_history (employee_id SERIAL PRIMARY KEY,
                          start_date  DATE,
                          end_date DATE,
                          job_id INTEGER references jobs(job_id),
                          department_id INTEGER)

CREATE TABLE employees (employee_id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        email VARCHAR(50),
                        phone_number NUMERIC,
                        hire_date DATE,
                        job_id INTEGER NOT NULL,
                        salary MONEY NOT NULL,
                        comission NUMERIC,
                        manager_id INTEGER NOT NULL references departments (manager_id),
                        department_id INTEGER NOT NULL references departments(department_id))

CREATE TABLE employees (employee_id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        email VARCHAR(50),
                        phone_number NUMERIC,
                        hire_date DATE,
                        job_id INTEGER FOREIGN KEY  references jobs(job_id),
                        salary MONEY NOT NULL,
                        comission NUMERIC,
                        manager_id INTEGER NOT NULL references departments (manager_id),
                        department_id INTEGER NOT NULL references departments(department_id))

CREATE TABLE employees (employee_id SERIAL PRIMARY KEY,
                        first_name VARCHAR(50),
                        last_name VARCHAR(50),
                        salary MONEY,
                        job_id INTEGER FOREIGN KEY  references jobs(job_id))

<!-- whats up with these instructions? so confusing.. -->

RESTRICTING and SORTING


                       





