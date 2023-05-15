-- Gets the total cost of an order with discount subtracted
CREATE OR REPLACE FUNCTION restaurant.get_total_cost(p_order_id INT) RETURNS INT AS $$
DECLARE
    total_cost INT;
    discount INT;
BEGIN
    SELECT cost INTO total_cost FROM restaurant.orders WHERE order_id = p_order_id;

    SELECT restaurant.corporation.discount INTO discount FROM restaurant.corporation 
    JOIN restaurant.tables ON restaurant.corporation.table_no = restaurant.tables.table_no
    JOIN restaurant.sitting ON restaurant.tables.table_no = restaurant.sitting.table_no
    WHERE restaurant.sitting.cust_id = p_order_id;

    IF discount IS NOT NULL THEN
        total_cost := total_cost - (total_cost * discount / 100);
    END IF;

    RETURN total_cost;
END;
$$ LANGUAGE plpgsql;

-- Returns all the dishes and drinks on the given table
CREATE OR REPLACE FUNCTION restaurant.get_table_orders(table_no INT) RETURNS TABLE (
    cust_name CHAR(50),
    dish_id INT,
    drink_id INT,
    addit_req TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT c.cust_name, d.dish_id, b.drink_id, t.addit_req
    FROM restaurant.customer c
    JOIN restaurant.orders o ON c.cust_id = o.cust_id
    LEFT JOIN restaurant.dishes d ON o.order_id = d.order_id
    LEFT JOIN restaurant.bar b ON o.order_id = b.order_id
    JOIN restaurant.sitting s ON c.cust_id = s.cust_id
    JOIN restaurant.tables t ON s.table_no = t.table_no
    WHERE t.table_no = get_table_orders.table_no
    ORDER BY c.cust_name;
END;
$$ LANGUAGE plpgsql;


-- Get all the ingredients of the given dish
CREATE FUNCTION restaurant.GetIngredientsForDish(p_dish_id INT) 
RETURNS TABLE (ing_id INT, ing_name CHAR(50), avail BOOL) AS $$
BEGIN
    RETURN QUERY
    SELECT ing.ing_id, ing.ing_name, ing.avail
    FROM restaurant.raw_ingredient AS ing
    WHERE ing.dish_id = p_dish_id;
END;
$$ LANGUAGE plpgsql;





