# Database
The repository of my project for Databases 2023.

___

![Logical Model](Docs/Logical_Model.png?raw=true)

___

![Physical Model](Docs/description.md?raw=true)

| Table Name       | Field Name        | Description                                                      | Data Type    |
|------------------|-------------------|------------------------------------------------------------------|--------------|
| Customers        | cust_id           | The identification number of the customer. Cannot be null.        | INTEGER      |
|                  | cust_name         | Name of the customer.                                            | TEXT         |
| Orders           | order_id          | The identification number of the order. Cannot be null.           | INTEGER      |
|                  | cust_id           | The identification number of the customer to whom the order belongs. Cannot be null. | INTEGER      |
|                  | cost              | The cost of the order. Cannot be null.                            | INTEGER      |
| Bar              | drink_id          | The identification number of the drink. Cannot be null.           | INT          |
|                  | order_id          | The identification number of the order which contains this drink. Cannot be null. | INT          |
|                  | drink_avail       | If the drink is available or not. Cannot be null.                 | BOOL         |
|                  | drink_cost        | The cost of the drink. Cannot be null.                            | INT          |
| Dishes           | dish_id           | The identification number of the dish. Cannot be null.            | INT          |
|                  | order_id          | The identification number of the order which contains this dish. Cannot be null. | INT          |
|                  | est_time          | The estimated time for the dish to be prepared in minutes.        | INT          |
|                  | dish_name          | The name of the dish. Cannot be null.                            | char(50)          |
|                  | dish_cost         | The cost of the dish.                                              | INT          |
| Employees        | emp_id            | The identification number of the employee. Cannot be null.        | INT          |
|                  | job               | The job that the employee works.                                  | TEXT         |
|                  | emp_sal           | The salary of the employee. Cannot be null.                       | INT          |
|                  | present           | Whether the employee is present today or not.                     | BOOL         |
| Table            | table_no          | The identification number of the table. Cannot be null.           | INT          |
|                  | emp_id            | The employees serving the table. Cannot be null.                  | INT          |
|                  | addit_req         | Any additional requests from the customer of the table.           | TEXT         |
| Corporation      | corp_id           | The identification number of the corporation.                     | INT          |
|                  | table_no          | The table number where the members of the corporation are situated. | INT          |
|                  | discount          | The discount offered to the corporate. Cannot be null.            | INT          |
|                  | corp_name         | The name of the corporation.                                     | TEXT         |
| Raw Ingredient   | ing_id            | The identification number of the ingredient. Cannot be null.      | INT          |
|                  | dish_id           | The identification number of the dish which uses this ingredient. | INT          |
|                  | ing_name           | The name of the  ingredient.                                     | Char          |
|                  | avail             | The availability of the ingredient. Cannot be null.               | BOOL         |
| Sitting          | cust_id            | The identification number of the customer. Cannot be null.      | INT          |
|                   | table_no            | The number of the table where the customer is sitting.         | INT          |

___
### Task 3: [DDL.sql](https://github.com/Archeron13/Database/blob/main/scripts/DDL.sql)
___
### Task 4: [insert_query.sql](https://github.com/Archeron13/Database/blob/main/scripts/insert_query.sql)
___
### Task 5: [CRUD.sql](https://github.com/Archeron13/Database/blob/main/scripts/CRUD.sql)
___
### Task 6 
1. ## Queries: [select.sql](https://github.com/Archeron13/Database/blob/main/scripts/select.sql)
2. ## Tests: [select_test.sql](https://github.com/Archeron13/Database/blob/main/Test/select_test.py)
___
### Task 7: [select_test.sql](https://github.com/Archeron13/Database/blob/main/Test/select_test.py)
___
### Task 8: [index.sql](https://github.com/Archeron13/Database/blob/main/scripts/index.sql)
___
### Task 9
1. ## Queries: [views.sql](https://github.com/Archeron13/Database/blob/main/scripts/views.sql)
2. ## Tests: [view_test.py](https://github.com/Archeron13/Database/blob/main/Test/views_test.py)
___
### Task 10
1. ## Queries: [stored.sql](https://github.com/Archeron13/Database/blob/main/Test/views_test.py)
2. ## Tests: [stored_test.py](https://github.com/Archeron13/Database/blob/main/Test/stored_test.py)
___
### Tasl 11: [triggers.sql](https://github.com/Archeron13/Database/blob/main/scripts/triggers.sql)




