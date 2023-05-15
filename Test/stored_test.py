import psycopg2


string = '''
dbname='postgres'
user='dummy'
host='127.0.0.1'
port='5432'
password='123456' 
'''
# Connect to the PostgreSQL database
conn = psycopg2.connect(
    string)




def test_get_total_cost():
    try:

        cur = conn.cursor()

        cur.execute("SELECT * from restaurant.get_total_cost(21)")
        result = cur.fetchone()[0]
        expected_output = 306
        assert result == expected_output

        cur.execute("SELECT * from restaurant.get_total_cost(4)")
        result = cur.fetchone()[0]
        expected_output = 220
        assert result == expected_output

        cur.execute("SELECT * from restaurant.get_total_cost(7)")
        result = cur.fetchone()[0]
        expected_output = 37
        assert result == expected_output

        cur.execute("SELECT * from restaurant.get_total_cost(19)")
        result = cur.fetchone()[0]
        expected_output = 221
        assert result == expected_output

        cur.execute("SELECT * from restaurant.get_total_cost(16)")
        result = cur.fetchone()[0]
        expected_output = 220
        assert result == expected_output

        print("Get Total Cost Function Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing get_total_cost:", error)


def test_get_table_orders():
    try:

        cur = conn.cursor()

        cur.execute("SELECT * from restaurant.get_table_orders(4)")
        rows = cur.fetchall()
        expected_output = [
            ("Lionel Messi", 1, 10,None),
            ("Lionel Messi", 2, 10, None),
            ("Lionel Messi", 1, 15, None),
            ("Lionel Messi", 2, 15, None)
        ]

        # Compare the result with expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            trimmed_value = rows[i][0].strip()
            assert trimmed_value == expected_output[i][0]
            assert rows[i][2] == expected_output[i][2]
            assert rows[i][1] == expected_output[i][1]


        cur.execute("SELECT * from restaurant.get_table_orders(7)")
        rows = cur.fetchall()
        expected_output = [
            ("Olivia Anderson", 8, None, "Allergies: Gluten"),
            ("William Clark", 8, None, "Allergies: Gluten")
        ]

        # Compare the result with expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            trimmed_value = rows[i][0].strip()
            assert trimmed_value == expected_output[i][0]
            assert rows[i][2] == expected_output[i][2]
            assert rows[i][1] == expected_output[i][1]



      
        print("Get Total Cost Function Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing get_table_orders:", error)



def test_get_ingredient_for_dish():
    try:
        cur = conn.cursor()

        cur.execute("SELECT * from restaurant.GetIngredientsForDish(4)")
        result = cur.fetchall()

        # Expected output
        expected_output = [
            (15, 'Chicken Breast', True),
            (16, 'Lettuce', True),
            (17, 'Tomatoes', True),
            (18, 'Croutons', True),
            (19, 'Caesar Dressing', True)
        ]

        # Compare the result with expected output
        assert len(result) == len(expected_output)
        for i in range(len(result)):
            trimmed_value = result[i][1].strip()
            assert trimmed_value == expected_output[i][1]
            assert result[i][0] == expected_output[i][0]
            assert result[i][2] == expected_output[i][2]


        print("GetIngredientsForDish Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing GetIngredientsForDish:", error)

test_get_total_cost()
test_get_table_orders()
test_get_ingredient_for_dish()