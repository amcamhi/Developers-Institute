UPDATE film SET language_id = 5 WHERE rental_rate BETWEEN 4 and 5

store_id and address_id are FOREIGN KEYS.
When inserting a new customer, we need to specify those values and they need to match with some number on the child tables.

INSERT INTO customer (store_id, first_name, last_name, email,address_id, activebool, active)
VALUES(2,'Rick','Sanchez','rick@sth.com', 200, true, 1)

INSERT INTO film (title,
    description,
    release_year,
    language_id,
    rental_duration,
    rental_rate,
    length,
    replacement_cost,
    rating)
	VALUES ( 'GOT', 'Kings And Queens','2020',1,7,5,191,18.99,'PG-13')ç

DROP TABLE customer_reviews (DIDNT COMPLETE XPGOLD FROM DAY2), IF THERE IS A FOREIGN KEY THAT IS USED IN OTHER TABLES, THERE MIGHT BE SOME ERRORS.



SELECT 
	actor.first_name,
	actor.last_name,
	film.title,
	film.description,
	film_actor.actor_id,
	film_actor.film_id 
FROM 
	film_actor
	INNER JOIN actor ON actor.actor_id = film_actor.actor_id
	INNER JOIN film ON film.film_id = film_actor.film_id
	
WHERE actor.first_name = 'Penelope' and actor.last_name = 'Monroe'



SELECT 
	film.title,
	film.length,
	film.rating,
	film_category.film_id,
	category.name as category
FROM
	film_category
	INNER JOIN film ON film.film_id = film_category.film_id
	INNER JOIN category ON category.category_id = film_category.category_id
WHERE 
	film.length < 60 AND film.rating = 'R'and category.name = 'Documentary'



SELECT 
		DISTINCT
		film.title,
		film.rental_rate,
		rental.rental_date,
		customer.first_name,
		customer.last_name
FROM 
		customer
		INNER JOIN rental ON rental.customer_id = customer.customer_id
		INNER JOIN inventory ON inventory.store_id = customer.store_id
		INNER JOIN film ON film.film_id = inventory.film_id
WHERE
	customer.first_name = 'Matthew'
	and customer.last_name = 'Mahan'
	and film.rental_rate > 4.0
	and rental.rental_date 
	BETWEEN '2005-07-28' AND '2005-08-01'

CORRECTION TO THE ABOVE?
<!-- SELECT film.title, film.rental_rate, rental.return_date, customer.customer_id, film.description
FROM customer
INNER JOIN rental
ON customer.customer_id = rental.customer_id
INNER JOIN inventory
ON rental.inventory_id = inventory.inventory_id
INNER JOIN film
ON inventory.film_id = film.film_id
WHERE rental.return_date BETWEEN '2005-07-28' AND '2005-08-01' AND film.rental_rate > 4.00 AND rental.customer_id = 323; -->


SELECT 
		customer.first_name,
		customer.last_name,
		film.title,
		film.description,
		film.replacement_cost
FROM 
	customer
	JOIN rental ON rental.customer_id = customer.customer_id
	JOIN inventory ON inventory.inventory_id = rental.inventory_id
	JOIN film ON film.film_id = inventory.film_id

WHERE customer.first_name = 'Matthew' and film.description ILIKE '%boat%' ORDER BY film.replacement_cost DESC 


SELECT 
		actor.first_name,
		actor.last_name,
		film.title,
		category.name
FROM 
	category
	JOIN film_category ON category.category_id = film_category.category_id
	JOIN film ON film.film_id = film_category.film_id
	JOIN film_actor ON film_actor.film_id = film.film_id
	JOIN actor ON film_actor.actor_id = actor.actor_id
	
WHERE 
	actor.first_name = 'Joe' and actor.last_name = 'Swank'



INSERT INTO rental (rental_date, customer_id, inventory_id,staff_id)
		VALUES (now(),603,100, 2), (now(),603,101,2), (now(),603,102,2)


<!-- not sure how to do .8 returning movies -->
