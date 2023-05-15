--CRUD QUERIES

----------------------------------------------------------------------------------------------------
                                        --Read--

-- #1 To find the employee waiting the most tables
SELECT emp_id, COUNT(table_no) AS num_tables
FROM restaurant.tables
GROUP BY emp_id
ORDER BY num_tables DESC
LIMIT 1;

-- #2 To find the most ordered dish
SELECT dish_id, dish_name, COUNT(order_id) AS num_orders
FROM restaurant.dishes
GROUP BY dish_id, dish_name
ORDER BY num_orders DESC
LIMIT 1;

-- #3 To find the table with highest number of people
SELECT table_no, COUNT(cust_id) AS num_customers
FROM restaurant.sitting
GROUP BY table_no
ORDER BY num_customers DESC
LIMIT 1;

--#4 To find dish with most ingredient
SELECT dish_id, COUNT(ing_id) AS num_ingredients
FROM restaurant.raw_ingredient
GROUP BY dish_id
ORDER BY num_ingredients DESC
LIMIT 1;

-----------------------------------------------------------------------------------------------------
                                            -- Update--
                                            
--5 Update the job of an employee
UPDATE restaurant.employees
SET job = 'Manager'
WHERE emp_id = 1;

--6
INSERT INTO restaurant.orders (order_id, cust_id, cost)
VALUES (23, 1, 50);

--7
UPDATE restaurant.bar
SET drink_avail = false
WHERE drink_id = 3;

----------------------------------------------------------------------------------------------------
                                            -- Delete--

--8 Remove customer that are not at a table
DELETE FROM restaurant.customer
WHERE cust_id NOT IN (
    SELECT DISTINCT cust_id
    FROM restaurant.sitting
);

-- 9 Remove an dish
DELETE FROM restaurant.dishes
WHERE dish_id = 2;

----------------------------------------------------------------------------------------------------
                                            -- Createa--

-- 10 Insert value into table
insert into restaurant.customer VALUES (24,'Tommy Vercetti');
