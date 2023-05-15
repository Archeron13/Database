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

# Create a cursor to execute SQL queries
cur = conn.cursor()

# Test the customer_view
def test_customer_view():
    cur = conn.cursor()
    try:
        # Retrieve data from the customer_view
        cur.execute("SELECT * FROM restaurant.customer_view")
        rows = cur.fetchall()

        # Expected masked names
        expected_masked_names = [
            "J****** C******",
            "J** D**",
            "L**** M****",
            "E***** W*****",
            "D******* T*******",
            "S**** A****",
            "R********** L**********",
            "J**** D****",
            "W**** C****",
            "O******* A*******",
            "A**** J****",
            "A******** D********",
            "M****** J******",
            "R***** C*****",
            "K***** M*****",
            "J**************** J****************",
            "F**** P****",
            "L****** L******",
            "M***** M*****",
            "J****** A******",
            "K******* Y*******",
            "D***** C*****"
        ]

        # Print the masked names


        # Assert the expected masked names
        for i, row in enumerate(rows):
            assert row[0] == expected_masked_names[i]

        print("Customer View Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing customer_view:", error)



def test_sitting_view():
    try:
        # Retrieve data from the sitting_view
        cur.execute("SELECT * FROM restaurant.sitting_view")
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (2, "J****** C******"),
            (3, "J** D**"),
            (4, "L**** M****"),
            (1, "E***** W*****"),
            (5, "D******* T*******"),
            (5, "S**** A****"),
            (5, "R********** L**********"),
            (6, "J**** D****"),
            (7, "W**** C****"),
            (7, "O******* A*******"),
            (8, "A**** J****"),
            (8, "A******** D********"),
            (9, "M****** J******"),
            (9, "R***** C*****"),
            (10, "K***** M*****"),
            (12, "J**************** J****************"),
            (15, "F**** P****"),
            (15, "L****** L******"),
            (15, "M***** M*****"),
            (15, "J****** A******"),
            (15, "K******* Y*******"),
            (1, "D***** C*****")
        ]

        # Compare the result with expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Sitting View Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing sitting_view:", error)


def test_most_spending_table():
    try:
        # Retrieve data from the most_spending_table view
        cur.execute("SELECT * FROM restaurant.most_spending_table")
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (15, 2040),
            (8, 1040),
            (5, 897),
            (12, 600),
            (1, 580),
            (2, 490),
            (7, 434),
            (4, 340),
            (9, 324),
            (10, 231),
            (3, 230),
            (6, 43)
        ]

        # Compare the result with expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Most Spending Table Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing most_spending_table:", error)

def test_most_used_ingredients_view():
    try:
        cur.execute("SELECT * FROM restaurant.most_used_ingredients")

        rows = cur.fetchall()

        # Define the expected output
        expected_output = [
            (4, "Parmesan Cheese", 3),
            (9, "Basil", 3),
            (11, "Bacon", 2),
            (1, "Pasta", 2),
            (5, "Spaghetti Sauce", 2),
            (10, "Pasta", 2),
            (8, "Mozzarella Cheese", 2),
            (3, "Eggs", 2),
            (6, "Pizza Dough", 2),
            (2, "Bacon", 2),
            (7, "Tomato Sauce", 1)
        ]
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Sitting View Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error Sitting View TEst", error)


def test_customer_waiter_view():
    try:

        cur.execute("SELECT * FROM restaurant.customer_waiter_view")
        rows = cur.fetchall()

        # Expected output
        expected_output = [
            (1, "John Connors", 2),
            (2, "Jane Doe", 3),
            (3, "Lionel Messi", 4),
            (4, "Emily Wilson", 1),
            (5, "David Thompson", 5),
            (6, "Sarah Adams", 5),
            (7, "Robert Lewandowski", 5),
            (8, "Jennifer Davis", 1),
            (9, "William Clark", 2),
            (10, "Olivia Anderson", 2),
            (11, "Aryan Jaira", 3),
            (12, "Amom De Armado", 3),
            (13, "Michael Johnson", 4),
            (14, "Rob Carlos", 4),
            (15, "Kylian Mbappe", 5),
            (16, "Jean Jacques Fernandes", 12),
            (17, "Florentino Perez", 1),
            (18, "Logan Laplace", 1),
            (19, "Mark Manson", 1),
            (20, "Jennifer Aniston", 1),
            (21, "Kristina Yunikova", 1),
            (22, "Daniel Cauchy", 1)
        ]

        # Compare the result with expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Customer Waiter View Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing customer_waiter_view:", error)


def test_spending_stats_view():
    try:

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the SELECT query on the spending_stats_view
        cursor.execute("SELECT * FROM restaurant.spending_stats_view")
        rows = cursor.fetchall()

        # Expected output
        expected_output = [
            (1, "J**** C****", 490, 160.5),
            (2, "J**** D****", 230, -99.5),
            (3, "L**** M****", 340, 10.5),
            (4, "E**** W****", 220, -109.5),
            (6, "S**** A****", 421, 91.5),
            (7, "R**** L****", 237, -92.5),
            (8, "J**** D****", 43, -286.5),
            (9, "W**** C****", 200, -129.5),
            (10, "O**** A****", 234, -95.5),
            (11, "A**** J****", 500, 170.5),
            (12, "A**** D****", 540, 210.5),
            (13, "M**** J****", 120, -209.5),
            (14, "R**** C****", 204, -125.5),
            (15, "K**** M****", 231, -98.5),
            (16, "J**** J****", 600, 270.5),
            (17, "F**** P****", 220, -109.5),
            (18, "L**** L****", 600, 270.5),
            (19, "M**** M****", 400, 70.5),
            (20, "J**** A****", 260, -69.5),
            (21, "K**** Y****", 560, 230.5),
            (22, "D**** C****", 360, 30.5),
            (5, "D**** T****", 239, -90.5)
        ]

        # Compare the result with expected output
        assert len(rows) == len(expected_output)
        for i in range(len(rows)):
            assert rows[i] == expected_output[i]

        print("Spending Stats View Test Passed!")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error testing spending_stats_view:", error)

test_customer_view()
test_sitting_view()
test_most_spending_table()
test_most_used_ingredients_view()
test_customer_waiter_view()
test_spending_stats_view()