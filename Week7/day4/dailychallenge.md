CREATE TABLE orders (order_id SERIAL PRIMARY KEY,
                    order_date DATE DEFAULT NOW(),
                    order_total MONEY NOT NULL)

CREATE TABLE items (item_id SERIAL PRIMARY KEY,
                    item_name VARCHAR(50) NOT NULL,
                    item_price MONEY NOT NULL,
                    qty SMALLINT,
                    order_id int, FOREIGN KEY (order_id) references orders (order_id))


CREATE or REPLACE FUNCTION total(ord_id int) 
RETURNS money AS $total_price$
BEGIN
   RETURN(SELECT order_total FROM orders WHERE orders.order_id = ord_id);
END;
$total_price$ LANGUAGE plpgsql;


<!-- function doesnt work. -->