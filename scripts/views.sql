

-- Gives a masked view of all the customer
CREATE VIEW restaurant.customer_view AS
SELECT 
    CONCAT(
        LEFT(cust_name, 1),
        REPEAT('*', LENGTH(cust_name) - 1 - POSITION(' ' IN cust_name)),
        ' ',
        LEFT(SUBSTRING(cust_name FROM POSITION(' ' IN cust_name)+1), 1),
        REPEAT('*', LENGTH(SUBSTRING(cust_name FROM POSITION(' ' IN cust_name)+1)) - 1)
    ) AS masked_name
FROM 
    restaurant.customer;


--Gives a masked view of all the customers and their table
CREATE VIEW restaurant.sitting_view AS
SELECT
    s.table_no,
    CONCAT(
        LEFT(c.cust_name, 1),
        REPEAT('*', LENGTH(c.cust_name) - 1 - POSITION(' ' IN c.cust_name)),
        ' ',
        LEFT(SUBSTRING(c.cust_name FROM POSITION(' ' IN c.cust_name) + 1), 1),
        REPEAT('*', LENGTH(SUBSTRING(c.cust_name FROM POSITION(' ' IN c.cust_name) + 1)) - 1)
    ) AS masked_name
FROM
    restaurant.sitting s
JOIN
    restaurant.customer c ON s.cust_id = c.cust_id;

-- Shows how much every customer is spending and how far it is from the average, as well as masked custoemr name
CREATE VIEW restaurant.spending_stats_view AS
SELECT
    cust_id,
    CONCAT(
        LEFT(cust_name, 1),
        '****',
        ' ',
        LEFT(SUBSTRING(cust_name FROM '\w+\s+(\w+)'), 1),
        '****'
    ) AS masked_name,
    cost,
    cost - avg_spending AS spend_difference
FROM
    (
        SELECT
            c.cust_id,
            c.cust_name,
            o.cost,
            AVG(o.cost) OVER () AS avg_spending
        FROM
            restaurant.customer c
        LEFT JOIN
            restaurant.orders o ON c.cust_id = o.cust_id
    ) AS subquery;


-- Gives the table by the order of spending
CREATE VIEW restaurant.most_spending_table AS
SELECT
    s.table_no,
    SUM(o.cost) AS total_spending
FROM
    restaurant.sitting s
JOIN
    restaurant.orders o ON s.cust_id = o.cust_id
GROUP BY
    s.table_no
ORDER BY
    total_spending DESC;


-- Gives the ingredients that are used the most
CREATE VIEW restaurant.most_used_ingredients AS
SELECT
    r.ing_id,
    TRIM(r.ing_name),
    COUNT(*) AS ingredient_count
FROM
    restaurant.raw_ingredient r
JOIN
    restaurant.dishes d ON r.ing_id = d.dish_id
GROUP BY
    r.ing_id, r.ing_name
ORDER BY
    ingredient_count DESC


-- Gives the cust_id,cust_name and the waiter serving them
CREATE VIEW restaurant.customer_waiter_view AS
SELECT s.cust_id, TRIM(c.cust_name), t.emp_id AS waiter_id
FROM restaurant.sitting s
JOIN restaurant.tables t ON s.table_no = t.table_no
JOIN restaurant.customer c ON s.cust_id = c.cust_id;


