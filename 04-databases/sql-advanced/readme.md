# Advanced SQL

## Objectives
* Describe the uses of advanced queries like subqueries and unions
* Demonstrate ability to order data
* Demonstrate ability to aggregate and combine data

## Order of SQL Clauses

![SQL Clauses](SQLClauses.png)

## Selecting specific data

Not equal - `<>`

```
- LIKE - SELECT * FROM students WHERE name LIKE '%';
- DISTINCT - SELECT DISTINCT name FROM students;
- ORDER BY - SELECT * FROM students ORDER BY name DESC;
- COUNT - SELECT count(*) FROM students;
- MAX - SELECT max(age) FROM students;
- MIN - SELECT min(age) FROM students;
- AND - SELECT * from students WHERE name = 'Elie' AND age = 26;
- OR - SELECT * from students WHERE name = 'Elie' OR name ='Mary';
- IN - SELECT * FROM students WHERE name IN ('Bob', 'Tom');
- NOT IN - SELECT * FROM students WHERE name NOT IN ('Bob', 'Tom');
- LIMIT - SELECT * FROM students LIMIT 2;
- OFFSET - SELECT * FROM students OFFSET 1;
- LIMIT + OFFSET - SELECT * FROM students LIMIT 2 OFFSET 1;
- % - SELECT * FROM students WHERE name LIKE '%b';
```

Let's suppose we have a *customer* table with the following data:

```sql
 id |  name   | age |  country  | salary 
----+---------+-----+-----------+--------
  1 | Ramesh  |  32 | Ahmedabad |   2000
  3 | Kaushik |  23 | Kota      |   2000
  2 | Ramesh  |  25 |           |   1500
  4 | Kaushik |  25 | Mumbai    |       
  5 | Hardik  |  27 | Bhopal    |   8500
  6 | Komal   |     |           |   4500
```

## COUNT()

COUNT() is an *aggregate function*.

"In database management an aggregate function is a function where the values of multiple rows are grouped together to form a single value of more significant meaning or measurement such as a set, a bag or a list." [Read more on wikipedia.](https://en.wikipedia.org/wiki/Aggregate_function)

We use an aggregate function to get the total count of customers in a table.
```sql
SELECT COUNT(*) FROM customer;
```

What about getting the count of something more specific in customer, such as the number of rows that have the age datapoint? 
```sql
SELECT COUNT(age) FROM customer;
```

## GROUP BY

GROUP BY is used to pull together identical data points. For example, say we just want to see the different ages we have in our customer table, without having to look through the duplicates too.
```sql
SELECT age FROM customer GROUP BY age;
```

What if we just want to know how many different ages we have? We can combine GROUP BY and COUNT():
```sql
SELECT age, COUNT(age) FROM customer GROUP BY age;
```

Or maybe we want the average salaries of the customers from each country:
```sql
SELECT country, AVG(salary) FROM customer GROUP BY country;
```

### Aliases

Aliases are a piece of a SQL query that allows you to temporarily rename a table or column for the current query.

```sql
SELECT country, avg(salary) AS avgSal FROM customer GROUP BY country;
```

### Alter Table Command

```sql
ALTER TABLE customer ADD COLUMN date DATE;

ALTER TABLE customer ALTER COLUMN name SET NOT NULL;

ALTER TABLE customer DROP date;
```

### FOREIGN KEYS
```sql
CREATE TABLE merch_order (
	id SERIAL PRIMARY KEY,
	num_items INTEGER,
	customer_id INTEGER REFERENCES customer(id)
);
```

### Nested queries

What if I want to get names of customers with the highest salary.

Let's try it using WHERE

```sql
SELECT name, salary FROM customer
WHERE salary = MAX(salary);
```

That will give us an error, because MAX is an aggregate function and can't be used in WHERE.

This will return the maximum rating, which we need to feed into WHERE.

```sql
SELECT name, salary FROM customer
WHERE salary = (
	SELECT MAX(salary) FROM customer
);
```

### Conditionals

#### CASE Statement
The CASE statement is used when you want to display different things depending on the data that you've queried from the database. There's two different ways to structure a CASE statement shown below. Note that in the first example you can only compare against single values while in the second example you can use actual expressions for evaluation. Also note that CASE statements require an ELSE statement.

```sql
SELECT name,
	age, 
		CASE WHEN age<25
		THEN 'young adult'
		ELSE 'adult' 
		END AS age_group 
FROM customer;
```


### JOINs
### JOINs

There are four types of JOINs in SQL:
* `LEFT JOIN`
* `RIGHT JOIN`
* `INNER JOIN`
* `FULL [OUTER] JOIN`

![4 Types of JOINs](https://www.dofactory.com/Images/sql-joins.png)

Let's look at a company with a table for customers and a table for orders.
The customer table looks like this:
```sql
 id  | first_name | last_name   | email 
-----+------------+-------------+------------------------
  1  | Romesh     | Ranganathan | romeshranga@email.com
  4  | Jameela    | Jamil       | jjamil@goodplace.com
  6  | David      | ODogherty   | florencefalls@email.com
  9  | Jackie     | Chan        | chankongsan@email.cn
  10 | Aldis      | Hodge       | hardison@email.com
 ```
 and the order table looks like this:
 ```sql
 id  | order_number | amount | customer_id 
-----+--------------+--------+-------------
  1  | A2067O       | 104.09 | 1
  2  | J9899P       | 50.54  | 2
  3  | N2337B       | 954.66 | 3
  4  | A7786C       | 66.33  | 3
  5  | F5400B       | 403.54 | 4
  6  | F5298H       | 669.84 | 5
  7  | L7800M       | 200.03 | 8
  8  | J5454G       | 44.30  | 7
  9  | F9802B       | 43.54  | 9
  10 | B7780B       | 182.72 | 9
 ```
 As you can see, there are some customers who haven't placed orders and some orders by customers who are no longer in the table (let's say, for example, the company deletes customers who haven't bought anything from them in 10 years). If we ask for the orders that correspond to Aldis Hodge, we will receive a value of NULL because he hasn't ordered anything. Similarly, if we request the customer that purchased order J5454G, we will also receive a value of NULL because the customer who had the id of 7 is no longer in the database.
 _NOTE: Since ORDER is the name of both our table and a SQL command, we should use double quotes when refering to the table name_
 
 **INNER JOIN** 
```sql
SELECT c.first_name, o.order_number FROM customer c
INNER JOIN "order" o
ON c.id=o.customer_id;
```
An `INNER JOIN` will return a table with all the matches from our customer and order tables where there is no NULL value on either side. 
```sql
 first_name | order_number 
------------+--------------
  Romesh    | A2067O   
  Jamella   | F5400B   
  Jackie    | F9802B   
  Jackie    | B7780B  
```
_NOTE: If you don't specify the type, SQL will perform an `INNER JOIN`._

**FULL [OUTER] JOIN**
```sql
SELECT c.first_name, o.order_number FROM customer c
FULL OUTER JOIN "order" o
ON c.id=o.customer_id;
```
_NOTE: The `OUTER` is optional_
A `FULL OUTER JOIN` will do the opposite of an `INNER JOIN`, returning you a table with all possible combinations, even if NULL has to be placed in.
```sql
 first_name | order_number 
------------+--------------
  Romesh    | A2067O   
  NULL      | J9899P   
  NULL      | N2337B   
  NULL      | A7786C   
  Jamella   | F5400B   
  NULL      | F5298H   
  NULL      | L7800M   
  NULL      | J5454G   
  Jackie    | F9802B   
  Jackie    | B7780B   
  Aldis     | NULL   
```
_TIP: `LEFT JOIN` and `RIGHT JOIN` can both be considered types of outer joins_

**LEFT JOIN**
```sql
SELECT c.first_name, o.order_number FROM customer c
LEFT JOIN "order" o
ON c.id=o.customer_id;
```
With a `LEFT JOIN` the table returned will have all values in the left table, even if there is no corresponding value on the right side.
```sql
 first_name | order_number 
------------+--------------
  Romesh    | A2067O   
  Jamella   | F5400B   
  Jackie    | F9802B   
  Jackie    | B7780B   
  Aldis     | NULL   
```

**RIGHT JOIN**
```sql
SELECT c.first_name, o.order_number FROM customer c
RIGHT JOIN "order" o
ON c.id=o.customer_id;
```
With a `RIGHT JOIN` the table returned will have all values in the right table, even if there is no corresponding value on the left side.
```sql
 first_name | order_number 
------------+--------------
  Romesh    | A2067O   
  NULL      | J9899P   
  NULL      | N2337B   
  NULL      | A7786C   
  Jamella   | F5400B   
  NULL      | F5298H   
  NULL      | L7800M   
  NULL      | J5454G   
  Jackie    | F9802B   
  Jackie    | B7780B  
```

### Unions

Unions display the results of two or more SELECT statements into one table, so the SELECT statements must have the same number of columns with the same names/data types, in the same order.

Let's try viewing the ids and names from both the customer and the subscriber tables.

```sql
SELECT id, name FROM customer UNION SELECT id, name FROM subscriber ORDER BY id;
```

Notice that the resulting table has fewer rows that the sum of the rows from each table. This is because UNION statements also eliminate any duplicate rows from the result. To include the duplicate rows, use UNION ALL.

```sql
SELECT id, name FROM customer UNION ALL SELECT id, name FROM subscriber ORDER BY id;
```
