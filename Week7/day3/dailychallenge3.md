create  table car
(car_id serial,
brand varchar(50),
PRIMARY KEY (car_id))

create table owner (owner_id serial, name varchar(50), car_id integer,
				   PRIMARY KEY(owner_id), FOREIGN KEY (car_id) references car (car_id))

                
create table addresses(owner_id integer not null unique,
					  address varchar(50),
					  FOREIGN KEY (owner_id) references owner (owner_id))

create table colors (color_id serial,
					color_name varchar(50),
					PRIMARY KEY (color_id))

CREATE TABLE car_color (car_id integer,
					   color_id integer,
					   foreign key (car_id) references car (car_id),
					   foreign key (color_id) references colors (color_id))

SELECT * FROM owner
JOIN car on owner.car_id = car.car_id
JOIN car_color on car.car_id = car_color.car_id
JOIN colors on colors.color_id = car_color.color_id
JOIN addresses on addresses.owner_id = owner.owner_id