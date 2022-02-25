# Advanced SQL

## Objectives

* Describe the uses of advanced queries like subqueries and unions
* Demonstrate ability to order data
* Demonstrate ability to aggregate and combine data

Let's create some data tables that we can run some queries on. Go to a terminal and run `psql`. Create a new database named 'advanced':

```sql
CREATE DATABASE advanced;
```

Now connect to it using `\c advanced` and create a new 'customers' table inside:

```sql
CREATE TABLE customers (
  id SERIAL PRIMARY KEY,
  name TEXT,
  age INTEGER,
  country TEXT,
  salary INTEGER
);

-- give it some data:

INSERT INTO customers (name, age, country, salary) VALUES ('Bira', 32, 'Brazil', 2000);
INSERT INTO customers (name, age, country, salary) VALUES ('Kaushik', 23, 'Kota', 2000);
INSERT INTO customers (name, age, country, salary) VALUES ('Ramesh', 25, null, 1500);
INSERT INTO customers (name, age, country, salary) VALUES ('Kaushik', 25, 'Mumbai', null);
INSERT INTO customers (name, age, country, salary) VALUES ('Amelia', 27, 'England', 8500);
INSERT INTO customers (name, age, country, salary) VALUES ('Silvana', null, null , 4500);
```

You should be able to SELECT all the data and see this output:

```sql
 id |  name   | age | country | salary 
----+---------+-----+---------+--------
  1 | Bira    |  32 | Brazil  |   2000
  2 | Kaushik |  23 | Kota    |   2000
  3 | Ramesh  |  25 |         |   1500
  4 | Kaushik |  25 | Mumbai  |       
  5 | Amelia  |  27 | England |   8500
  6 | Silvana |     |         |   4500
(6 rows)
```

Now let's make a friend for it. Create a new 'orders' table:

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  order_num TEXT,
  amount DECIMAL,
  customer_id INTEGER REFERENCES customers(id)
);

-- Give it some data
INSERT INTO orders (order_num, amount, customer_id) VALUES ('A2067O', 104.09 , 1);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('J9899P', 50.54 , 1);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('N2337B', 954.66 , 1);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('A7786C', 66.33 , 2);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('F5400B', 403.54 , 3);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('F5298H', 669.84 , 3);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('L7800M', 200.03 , 3);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('J5454G', 44.30 , 4);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('F9802B', 43.54 , 6);
INSERT INTO orders (order_num, amount, customer_id) VALUES ('B7780B', 182.72 , 6);
```

Now `SELECT * FROM orders;` and you should see this table:

```sql
 id | order_num | amount | customer_id 
----+-----------+--------+-------------
  1 | A2067O    | 104.09 |           1
  2 | J9899P    |  50.54 |           1
  3 | N2337B    | 954.66 |           1
  4 | A7786C    |  66.33 |           2
  5 | F5400B    | 403.54 |           3
  6 | F5298H    | 669.84 |           3
  7 | L7800M    | 200.03 |           3
  8 | J5454G    |  44.30 |           4
  9 | F9802B    |  43.54 |           6
 10 | B7780B    | 182.72 |           6
(10 rows)
```

## Order of SQL Clauses

![SQL Clauses](../.gitbook/assets/SQLClauses.png)

## Selecting Specific Data

It's great that we can select all records from a table but we frequently want to limit the results to a smaller set that meets some set of criteria. We saw the WHERE clause in the introduction to SQL lesson and saw how it can help us retrieve specific data. Here are a few more ways we can get more exclusive with our queries.

Remember that in SQL, our comparison operators are a little different. Equality is a single equals `=` and inequality is represented by a "greater-than-or-less-than" symbol `<>`.

```sql
- LIKE - SELECT * FROM customers WHERE name LIKE '%';
- DISTINCT - SELECT DISTINCT name FROM customers;
- ORDER BY - SELECT * FROM customers ORDER BY name DESC;
- COUNT - SELECT count(*) FROM customers;
- MAX - SELECT max(age) FROM customers;
- MIN - SELECT min(age) FROM customers;
- AND - SELECT * from customers WHERE name = 'Kaushik' AND age = 25;
- OR - SELECT * from customers WHERE name = 'Silvana' OR name = 'Bira';
- IN - SELECT * FROM customers WHERE name IN ('Amelia', 'Ramesh');
- NOT IN - SELECT * FROM customers WHERE name NOT IN ('Amelia', 'Ramesh');
- LIMIT - SELECT * FROM customers LIMIT 2;
- OFFSET - SELECT * FROM customers OFFSET 1;
- LIMIT + OFFSET - SELECT * FROM customers LIMIT 2 OFFSET 1;
- % - SELECT * FROM customers WHERE name LIKE '%a';
```

## COUNT\(\)

COUNT\(\) is an _aggregate function_.

"In database management an aggregate function is a function where the values of multiple rows are grouped together to form a single value of more significant meaning or measurement such as a set, a bag or a list." [Read more on wikipedia.](https://en.wikipedia.org/wiki/Aggregate_function)

We use an aggregate function to get the total count of customers in a table.

```sql
SELECT COUNT(*) FROM customers;
```

What about getting the count of something more specific in customer, such as the number of rows that have the age datapoint?

```sql
SELECT COUNT(age) FROM customers;
```

## GROUP BY

GROUP BY is used to pull together identical data points. For example, say we just want to see the different ages we have in our customer table, without having to look through the duplicates too.

```sql
SELECT age FROM customers GROUP BY age;
```

What if we just want to know how many different ages we have? We can combine GROUP BY and COUNT\(\):

```sql
SELECT age, COUNT(age) FROM customers GROUP BY age;
```

Or maybe we want the average salaries of the customers from each country:

```sql
SELECT country, AVG(salary) FROM customers GROUP BY country;
```

### Aliases

Aliases are a piece of a SQL query that allows you to temporarily rename a table or column for the current query.

```sql
SELECT country, avg(salary) AS avgSal FROM customers GROUP BY country;
```

### Alter Table Command

```sql
ALTER TABLE customers ADD COLUMN date DATE;

ALTER TABLE customers ALTER COLUMN name SET NOT NULL;

ALTER TABLE customers DROP date;
```

### Foreign Keys

Remember our 'orders' table:

```sql
CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  order_num TEXT,
  amount DECIMAL,
  customer_id INTEGER REFERENCES customers(id)
);
```

That last column we defined is called a **FOREIGN KEY**. Foreign keys and primary keys are related in that a foreign key is basically a reference to a primary key in another table. In this case, we have a column in our 'orders' table called `customer_id` that _references_ the primary key in the 'customers' table. This is the basis for making data relations with JOIN statements as we will see below. To summarize, the foreign key provides a sort of ownership link between the customer who has the primary key and all of that customer's orders in the related table where the `customer_id` matches the id from the 'customers' table.

### Nested queries

What if I want to get names of customers with the highest salary.

Let's try it using WHERE

```sql
SELECT name, salary FROM customers
WHERE salary = MAX(salary);
```

That will give us an error, because MAX is an aggregate function and can't be used in WHERE.

This will return the maximum salary, which we need to feed into WHERE.

```sql
SELECT name, salary FROM customers
WHERE salary = (
    SELECT MAX(salary) FROM customers
);
```

### Conditionals

#### CASE Statement

The CASE statement is used when you want to display different things depending on the data that you've queried from the database. There's two different ways to structure a CASE statement shown below. Note that in the first example you can only compare against single values while in the second example you can use actual expressions for evaluation. Also note that CASE statements require an ELSE statement.

```sql
SELECT name, age, 
    CASE WHEN age<25
    THEN 'young adult'
    ELSE 'adult' 
    END AS age_group 
FROM customers;
```

### JOINs

There are four types of JOINs in SQL:

* `LEFT JOIN`
* `RIGHT JOIN`
* `INNER JOIN`
* `FULL [OUTER] JOIN`

![4 Types of JOINs](../.gitbook/assets/sql_joins.png)

Let's look at our table for customers and our table for orders. The customers table looks like this:

```sql
 id |  name   | age | country | salary 
----+---------+-----+---------+--------
  1 | Bira    |  32 | Brazil  |   2000
  2 | Kaushik |  23 | Kota    |   2000
  3 | Ramesh  |  25 |         |   1500
  4 | Kaushik |  25 | Mumbai  |       
  5 | Amelia  |  27 | England |   8500
  6 | Silvana |     |         |   4500
(6 rows)
```

And the orders table looks like this:

```sql
 id | order_num | amount | customer_id 
----+-----------+--------+-------------
  1 | A2067O    | 104.09 |           1
  2 | J9899P    |  50.54 |           1
  3 | N2337B    | 954.66 |           1
  4 | A7786C    |  66.33 |           2
  5 | F5400B    | 403.54 |           3
  6 | F5298H    | 669.84 |           3
  7 | L7800M    | 200.03 |           3
  8 | J5454G    |  44.30 |           4
  9 | F9802B    |  43.54 |           6
 10 | B7780B    | 182.72 |           6
(10 rows)
```

As you can see, there are some customers who haven't placed orders. If we ask for the orders that correspond to customer\_id 5, we will receive a value of NULL because they haven't ordered anything.

**INNER JOIN**

The defualt join type is is inner:

```sql
-- the simplist join possible
SELECT * 
FROM customers 
JOIN orders
ON customers.id=orders.customer_id;

-- selection of only certain cols
SELECT customers.name, orders.order_num
FROM customers 
INNER JOIN orders
ON customers.id = orders.customer_id;

-- selection using 'aliasing' so you don't have to type out column names
-- aliases are defined in the FROM and JOIN clauses

-- aliases are refered to in the SELECT clause
SELECT c.name, o.order_num
-- here customers is alises as c and orders is alaised as o
FROM customers c 
INNER JOIN orders o
-- aliases are refered to in the ON clause
ON c.id = o.customer_id;
```

An `INNER JOIN` will return a dataset with all the matches from our customer and order tables where there is no NULL value on either side.

```sql
  name   | order_num 
---------+-----------
 Bira    | A2067O
 Bira    | J9899P
 Bira    | N2337B
 Kaushik | A7786C
 Ramesh  | F5400B
 Ramesh  | F5298H
 Ramesh  | L7800M
 Kaushik | J5454G
 Silvana | F9802B
 Silvana | B7780B
(10 rows)
```

_NOTE: This is the default type of JOIN so if you don't specify the type, SQL will perform an `INNER JOIN`._

**FULL \[OUTER\] JOIN**

```sql
SELECT customers.name, orders.order_num
FROM customers 
FULL OUTER JOIN orders
ON customers.id = orders.customer_id;
-- OR 
-- select cols outer join with aliases
SELECT c.name, o.order_num 
FROM customers c
FULL OUTER JOIN orders o
ON c.id=o.customer_id;
```

_NOTE: The `OUTER` is optional_

A `FULL OUTER JOIN` will do the opposite of an `INNER JOIN`, returning you a table with all possible combinations, even if NULL has to be placed in.

```sql
  name   | order_num 
---------+-----------
 Bira    | A2067O
 Bira    | J9899P
 Bira    | N2337B
 Kaushik | A7786C
 Ramesh  | F5400B
 Ramesh  | F5298H
 Ramesh  | L7800M
 Kaushik | J5454G
 Silvana | F9802B
 Silvana | B7780B
 Amelia  | 
(11 rows)
```

_TIP: The `LEFT JOIN` and `RIGHT JOIN` below can both be considered types of outer joins_

**LEFT JOIN**

```sql
SELECT customers.name, orders.order_num
FROM customers LEFT JOIN orders
ON customers.id = orders.customer_id;
-- OR
SELECT c.name, o.order_num
FROM customers c LEFT JOIN orders o
ON c.id=o.customer_id;
```

With a `LEFT JOIN` the table returned will have all values in the left table, even if there is no corresponding value on the right side.

```sql
  name   | order_num 
---------+-----------
 Bira    | A2067O
 Bira    | J9899P
 Bira    | N2337B
 Kaushik | A7786C
 Ramesh  | F5400B
 Ramesh  | F5298H
 Ramesh  | L7800M
 Kaushik | J5454G
 Silvana | F9802B
 Silvana | B7780B
 Amelia  | 
(11 rows)
```

**RIGHT JOIN**

With a `RIGHT JOIN` the table returned will have all values in the right table, even if there is no corresponding value on the left side. This is a very rare join as it would require us to have orphaned records in the orders table. That is, orders that have no related customer. This is actually impossible with the way we have the tables set up. The foreign key constraint in the orders table basically says that you can't have a value in the `customer_id` column in the orders table if that `id` doesn't exist in the customers table. So when we run this, it looks exactly like our INNER JOIN above.

```sql
  name   | order_num 
---------+-----------
 Bira    | A2067O
 Bira    | J9899P
 Bira    | N2337B
 Kaushik | A7786C
 Ramesh  | F5400B
 Ramesh  | F5298H
 Ramesh  | L7800M
 Kaushik | J5454G
 Silvana | F9802B
 Silvana | B7780B
(10 rows)
```


```sql
SELECT customers.name, orders.order_num
FROM customers 
RIGHT JOIN orders
ON customers.id = orders.customer_id;
-- OR
SELECT c.name, o.order_num
FROM customers c 
RIGHT JOIN orders o
ON c.id=o.customer_id;
```

### Unions

Unions display the results of two or more SELECT statements into one table, so the SELECT statements must have the same number of columns with the same names/data types, in the same order.

Here's a customers table:

```sql
id | name      
---+---------
 1 | Romesh  
 2 | Sally 
 3 | Vlad
 4 | Poppy
```

```sql
CREATE TABLE subscribers (
  id SERIAL PRIMARY KEY,
  name TEXT
);

-- Give it some data
INSERT INTO subscribers (name) VALUES ('Romish');
INSERT INTO subscribers (name) VALUES ('Sally');
INSERT INTO subscribers (name) VALUES ('Janice');
INSERT INTO subscribers (name) VALUES ('Poopy');
INSERT INTO subscribers (name) VALUES ('Katie');
```

Now `SELECT * FROM subscribers;` and you should see this table:


```sql
id | name      
---+---------
 1 | Romesh  
 2 | Sally 
 3 | Poppy
 4 | Janice
 5 | Kady
```

We could use this query to view the ids and names from both the customers and the subscribers tables.

```sql
SELECT id, name FROM customers UNION SELECT id, name FROM subscribers ORDER BY id;
```

```sql
id | name      
---+---------
 1 | Romesh  
 2 | Sally 
 3 | Vlad
 3 | Poppy
 4 | Poppy
 4 | Janice
 5 | Kady
```

Notice that the resulting table has fewer rows that the sum of the rows from each table. This is because UNION statements also eliminate any duplicate rows from the result. To include the duplicate rows, use UNION ALL.

```sql
SELECT id, name FROM customers UNION ALL SELECT id, name FROM subscribers ORDER BY id;
```

```sql
id | name      
---+---------
 1 | Romesh 
 1 | Romesh 
 2 | Sally
 2 | Sally
 3 | Vlad
 3 | Poppy
 4 | Poppy
 4 | Janice
 5 | Kady
```
<!-- 
## Data Relationships

[gonna do this](https://stackoverflow.com/questions/7296846/how-to-implement-one-to-one-one-to-many-and-many-to-many-relationships-while-de) 
-->