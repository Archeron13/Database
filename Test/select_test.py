import pandas as pd
import psycopg2

# Change this to your database
string = '''
dbname='postgres'
user='dummy'
host='127.0.0.1'
port='5432'
password='123456' 
'''
conn = psycopg2.connect(string)

def test_G1():
    try:            
        cur = conn.cursor()
        cur.execute("""
            SELECT o.order_id
            FROM restaurant.orders o
            JOIN restaurant.dishes d ON o.order_id = d.order_id
            JOIN restaurant.bar b ON o.order_id = b.order_id
            GROUP BY o.order_id
            HAVING COUNT(DISTINCT d.dish_id) > 0 AND COUNT(DISTINCT b.drink_id) > 0
        """)
        rows = cur.fetchall()

        expected_output = [
            (2,),
            (3,),
            (4,),
            (5,),
            (6,),
            (15,),
            (16,),
        ]
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query G1 passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing G1:", error)



def test_G2():
    try:
        cur = conn.cursor()        
        # Execute the query
        cur.execute("""
            SELECT table_no, COUNT(*) AS total_orders
            FROM restaurant.sitting
            GROUP BY table_no
            HAVING COUNT(*) > 1
        """)
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (9, 2),
            (15, 5),
            (5, 3),
            (7, 2),
            (1, 2),
            (8, 2)
        ]

        # Compare the result with the expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query G2 Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing G2:", error)

def test_O1():
    try:
        cur = conn.cursor()    
        # Execute the query
        cur.execute("""
            SELECT TRIM(cust_name), order_id, cost
            FROM restaurant.customer
            JOIN restaurant.orders ON restaurant.customer.cust_id = restaurant.orders.cust_id
            ORDER BY cost DESC
        """)
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            ("Jean Jacques Fernandes", 15, 600),
            ("Logan Laplace", 17, 600),
            ("Kristina Yunikova", 20, 560),
            ("Amom De Armado", 11, 540),
            ("Aryan Jaira", 10, 500),
            ("John Connors", 1, 490),
            ("Sarah Adams", 5, 421),
            ("Mark Manson", 18, 400),
            ("Daniel Cauchy", 21, 360),
            ("Lionel Messi", 3, 340),
            ("Jennifer Aniston", 19, 260),
            ("David Thompson", 22, 239),
            ("Robert Lewandowski", 6, 237),
            ("Olivia Anderson", 9, 234),
            ("Kylian Mbappe", 14, 231),
            ("Jane Doe", 2, 230),
            ("Florentino Perez", 16, 220),
            ("Emily Wilson", 4, 220),
            ("Rob Carlos", 13, 204),
            ("William Clark", 8, 200),
            ("Michael Johnson", 12, 120),
            ("Jennifer Davis", 7, 43)
        ]

        # Compare the result with the expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query O1 passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing Query O1:", error)

def test_O2():
    try:
        cur = conn.cursor()    
        # Execute the query
        cur.execute("""
            SELECT dish_id, TRIM(dish_name), COUNT(order_id) AS num_orders
            FROM restaurant.dishes
            GROUP BY dish_id, dish_name
            ORDER BY num_orders DESC
        """)
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (9, "Chicken Parmesan", 3),
            (4, "Garlic Bread", 3),
            (1, "Spaghetti Carbonara", 2),
            (6, "Mushroom Risotto", 2),
            (3, "Grilled Chicken Salad", 2),
            (10, "Tiramisu", 2),
            (2, "Margherita Pizza", 2),
            (8, "Fish and Chips", 2),
            (11, "Butter Chicken", 2),
            (5, "Caesar Salad", 2),
            (7, "Beef Burger", 1)
        ]

        # Compare the result with the expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query O2 passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing O2:", error)

def test_F1():
    try:
        cur = conn.cursor()    
        cur.execute("""
            SELECT TRIM(job), emp_sal, SUM(emp_sal) OVER (PARTITION BY job) AS total_salary
            FROM restaurant.employees
        """)
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            ("Assistant Manager", 4500, 4500),
            ("Bartender", 2800, 6000),
            ("Bartender", 3200, 6000),
            ("Busser", 1800, 1800),
            ("Chef", 3900, 8100),
            ("Chef", 4200, 8100),
            ("Cook", 3500, 3500),
            ("Dishwasher", 1500, 1500),
            ("Host/Hostess", 1900, 4000),
            ("Host/Hostess", 2100, 4000),
            ("Manager", 5000, 9800),
            ("Manager", 4800, 9800),
            ("Server", 2200, 2200),
            ("Waiter", 2400, 19260),
            ("Waiter", 3500, 19260),
            ("Waiter", 3000, 19260),
            ("Waiter", 3000, 19260),
            ("Waiter", 2560, 19260),
            ("Waiter", 2500, 19260),
            ("Waiter", 2300, 19260)
        ]

        # Compare the result with the expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query F1 passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing F1:", error)


def test_F2():
    try:
        cur = conn.cursor()    
        # Execute the query
        cur.execute("""
            SELECT table_no, cust_id, ROW_NUMBER() OVER (PARTITION BY table_no ORDER BY cust_id) AS row_number
            FROM restaurant.sitting
        """)
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (1, 4, 1),
            (1, 22, 2),
            (2, 1, 1),
            (3, 2, 1),
            (4, 3, 1),
            (5, 5, 1),
            (5, 6, 2),
            (5, 7, 3),
            (6, 8, 1),
            (7, 9, 1),
            (7, 10, 2),
            (8, 11, 1),
            (8, 12, 2),
            (9, 13, 1),
            (9, 14, 2),
            (10, 15, 1),
            (12, 16, 1),
            (15, 17, 1),
            (15, 18, 2),
            (15, 19, 3),
            (15, 20, 4),
            (15, 21, 5)
        ]

        # Compare the result with the expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query F2 Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing F2:", error)

def test_A1():
    try:
        cur = conn.cursor()    
        # Execute the query
        cur.execute("""
            SELECT c.corp_id, SUM((o.cost * (100 - c.discount)) / 100) AS savings
            FROM restaurant.corporation c
            JOIN restaurant.tables t ON c.table_no = t.table_no
            JOIN restaurant.sitting s ON t.table_no = s.table_no
            JOIN restaurant.orders o ON s.cust_id = o.cust_id
            GROUP BY c.corp_id
        """)
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (4, 207),
            (10, 1734),
            (6, 761)
        ]

        # Compare the result with the expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Query A1 Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing A1:", error)

def test_A2():
    try:
        cur = conn.cursor()    
        # Execute the query
        cur.execute("""
            SELECT
              COUNT(*) AS total_orders,
              SUM(cost) AS total_cost,
              AVG(cost) AS average_cost
            FROM
              restaurant.orders
        """)
        row = cur.fetchone()

        # Expected output
        expected_output = (22, 7249, 329.5)

        # Compare the result with the expected output
        assert row == expected_output

        print("Query A2 Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error A2:", error)


test_G1()
test_G2()
test_O1()
test_O2()
test_F1()
test_F2()
test_A1()
test_A2()