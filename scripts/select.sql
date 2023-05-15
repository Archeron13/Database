
-----------------------------------------------------------------------------------------------------
                                            -- Group By + Having--

--#1 Query to return orders that have food AND
SELECT o.order_id
FROM restaurant.orders o
JOIN restaurant.dishes d ON o.order_id = d.order_id
JOIN restaurant.bar b ON o.order_id = b.order_id
GROUP BY o.order_id
HAVING COUNT(DISTINCT d.dish_id) > 0 AND COUNT(DISTINCT b.drink_id) > 0;

--#2 Query to return the table_no and the total order from tables containing only table with
-- more than 1 orders
SELECT table_no, COUNT(*) AS total_orders
FROM restaurant.sitting
GROUP BY table_no
HAVING COUNT(*) > 1;



-----------------------------------------------------------------------------------------------------
                                            -- Order By -


--#1 Query to return customer_name,order and cost
SELECT cust_name, order_id, cost
FROM restaurant.customer
JOIN restaurant.orders ON restaurant.customer.cust_id = restaurant.orders.cust_id
ORDER BY cost DESC;


--#2 Query to show the most ordered dish
SELECT dish_id, dish_name, COUNT(order_id) AS num_orders
FROM restaurant.dishes
GROUP BY dish_id, dish_name
ORDER BY num_orders DESC;



-----------------------------------------------------------------------------------------------------
                                            --  <func>(...) OVER(...):--

-- #1 Calculate total salary for each job category
SELECT job, emp_sal, SUM(emp_sal) OVER (PARTITION BY job) AS total_salary
FROM restaurant.employees;

--#2 Assign a row number to each person at a table
SELECT table_no, cust_id, ROW_NUMBER() OVER (PARTITION BY table_no ORDER BY cust_id) AS row_number
FROM restaurant.sitting;

-----------------------------------------------------------------------------------------------------
                                            -- Aggregate Function--


--#1 Returns how much money is saved due to discount given to corporations
SELECT c.corp_id, SUM((o.cost * (100 - c.discount)) / 100) AS savings
FROM restaurant.corporation c
JOIN restaurant.tables t ON c.table_no = t.table_no
JOIN restaurant.sitting s ON t.table_no = s.table_no
JOIN restaurant.orders o ON s.cust_id = o.cust_id
GROUP BY c.corp_id;

-- #2 Gives total number of orders,total cost and average cost of orders
SELECT
  COUNT(*) AS total_orders,
  SUM(cost) AS total_cost,
  AVG(cost) AS average_cost
FROM
  restaurant.orders;

