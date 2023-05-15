-- When inserting into dishes, it checks if all the ingredients are available 
-- and raises an error if they are not

CREATE OR REPLACE FUNCTION check_ingredient_availability()
RETURNS TRIGGER AS $$
DECLARE
    ing_count INT;
    missing_ingredients VARCHAR[];
BEGIN
    SELECT COUNT(*) INTO ing_count FROM restaurant.raw_ingredient WHERE dish_id = NEW.dish_id AND avail = FALSE;
    IF ing_count > 0 THEN
        SELECT ARRAY_AGG(ing_name) INTO missing_ingredients FROM restaurant.raw_ingredient WHERE dish_id = NEW.dish_id AND avail = FALSE;
        RAISE EXCEPTION 'Cannot add dish. Required ingredients not available: %', missing_ingredients;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER check_ingredient_trigger
BEFORE INSERT ON restaurant.dishes
FOR EACH ROW
EXECUTE FUNCTION check_ingredient_availability();


-- Raises error if dish cost is negative while inserting
CREATE OR REPLACE FUNCTION check_dish_cost() RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        IF NEW.dish_cost < 0 THEN
            RAISE EXCEPTION 'Dish cost cannot be negative';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER dish_cost_check_trigger
    BEFORE INSERT ON restaurant.dishes
    FOR EACH ROW
    EXECUTE FUNCTION check_dish_cost();


-- Raises error if drink cost is negative while inserting
CREATE OR REPLACE FUNCTION check_drink_cost() RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        IF NEW.drink_cost < 0 THEN
            RAISE EXCEPTION 'Drink cost cannot be negative';
        END IF;
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER drink_cost_check_trigger
    BEFORE INSERT ON restaurant.bar
    FOR EACH ROW
    EXECUTE FUNCTION check_drink_cost();



