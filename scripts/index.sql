
CREATE INDEX idx_customer_id ON restaurant.customer (cust_id);

CREATE INDEX idx_employee_id ON restaurant.employees (emp_id);

CREATE INDEX idx_table_no ON restaurant.tables (table_no);

CREATE INDEX idx_sitting_table_no ON restaurant.sitting (table_no);

CREATE INDEX idx_sitting_cust_id ON restaurant.sitting (cust_id);

CREATE INDEX idx_order_id ON restaurant.orders (order_id);

CREATE INDEX idx_order_cust_id ON restaurant.orders (cust_id);

CREATE INDEX idx_bar_order_id ON restaurant.bar (order_id);

CREATE INDEX idx_dishes_order_id ON restaurant.dishes (order_id);

CREATE INDEX idx_raw_ingredient_id ON restaurant.raw_ingredient (ing_id);

CREATE INDEX idx_raw_ingredient_dish_id ON restaurant.raw_ingredient (dish_id);

CREATE INDEX idx_corporation_id ON restaurant.corporation (corp_id);

CREATE INDEX idx_corporation_table_no ON restaurant.corporation (table_no);



