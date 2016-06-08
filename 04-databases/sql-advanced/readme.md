# Advanced SQL

## Objectives
* Utilize different ways to filter data in the WHERE clause
* Understand the uses of advanced queries like subqueries and joins
* Be able to normalize a database structure

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

## GROUP BY

We use an aggregate function to get the total count of movies in a table.
```sql
SELECT COUNT(*) FROM movies;
```

What about getting the count of something more specific in movies, such as the count of each rating?
```sql
SELECT COUNT(rating) FROM movies;
```

We get the same result. GROUP BY allows you to 'group' the table by a specific attribute, which is then provided to the aggregate function.
```sql
SELECT rating, COUNT(rating) FROM movies
GROUP BY rating;
```


## Joins and FK

![SQL Joins](http://www.dofactory.com/Images/sql-joins.png)

### Inner Join
- Produces only the results from both tables that match the join condition.

### Full Join
- Produces all the results from both tables regardless of whether or not there is any row in either table that matches the join condition. 

### Left Join
- Produces all results from the left table regardless of whether or not there is a matching row in the right table and only results from the right table that have a matching row from the left table based on the join condition.

### Right Join
- ***Opposite*** of a **Left Join**: Produces all results from the right table regardless of whether or not there is a matching row in the left table and only results from the left table that have a matching row in the right table based on the join condition.

### Cross Join
- Produces a **cartesian product** of both joined tables (all rows in the left table match all rows in the right table, giving NxM results). There is **NO** join condition for a cross join.


```sql
CREATE TABLE authors (
	author_id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE books (
	book_id SERIAL PRIMARY KEY,
	name VARCHAR(100),
	author_id INTEGER
);

INSERT INTO authors (name) VALUES ('Elie'), ('Bob'), ('Mary');

INSERT INTO books (name, author_id) VALUES ('Book 1', 1), ('Book 2', 2);
INSERT INTO books (name) VALUES ('Book 3'), ('Book 4');


SELECT * FROM authors
JOIN books
    ON authors.author_id = books.author_id
ORDER BY authors.author_id ASC;
```

- Replace the 'JOIN' above with a Left/Right/Full/Inner/Cross Join in the query above and see what the results are.

## Alter Table Command

```sql
ALTER TABLE books ADD CONSTRAINT author_id
FOREIGN KEY (author_id) REFERENCES authors (author_id)
ON DELETE NO ACTION;

ALTER TABLE books ADD COLUMN year_released INTEGER;

ALTER TABLE books ALTER COLUMN name SET NOT NULL;
```

### Easier to add Constraints when creating a table
```sql
DROP TABLE books;
CREATE TABLE books (
	book_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	author_id INTEGER REFERENCES authors
);
```

## Nested queries

What if I want to do something very specific, but I need to get groups of results? For example:

1. Get titles of movies with the highest ratings.
2. Get titles of movies with the lowest ratings.

Let's try it using WHERE

```sql
SELECT title FROM movies
WHERE rating = MAX(rating);
```

That will give us an error, because MAX is an aggregate function and can't be used in WHERE.

Solution: Nested queries.

```sql
SELECT MAX(rating) FROM movies;
```

This will return the maximum rating, which we need to feed into WHERE.

```sql
SELECT title FROM movies
WHERE rating = (
	SELECT MAX(rating) FROM movies
);
```

## Normalization

The idea behind normalization is that the data should not be repeated. The rules of normalization are called "Normal Forms". There's technically 6 forms, but the first three are the most important.

### First Normal Form (1NF):

1. Each **column name** must be unique.
2. Each **column value** must be a single value.
3. Each **row** must be unique.
4. There are **no repeating groups**.

Additionally:
- Choose a primary key

Reminder:
- A primary key is ***unique, not null, and unchangeable***. A primary key can either be a single column or combination of columns.

| Student | Age | Subject |
|---------|-----|---------|
| Adam | 15 | Biology, Maths |
| Alex  | 14 | Maths |
| Stuart | 17 | Maths |

vs


| Student | Age | Subject |
|---------|-----|---------|
| Adam | 15 | Biology |
| Adam | 15 | Maths |
| Alex  | 14 | Maths |
| Stuart | 17 | Maths |

### Second Normal Form (2NF):

1. Table is in 1NF.
2. All non-primary-key columns are fully dependent on the primary key.

With our 1NF table from above, if Student is our primary key, Subject does not depend on the Student for its existence. Biology does not require Adam for its existence. In this case, Subject should be moved to a new table.

| Student | Age |
|---------|-----|
| Adam | 15 |
| Alex | 14 |
| Stuart | 17 |

And...

| Student | Subject |
|---------|---------|
| Adam | Biology |
| Adam | Maths |
| Alex | Maths |
| Stuart | Maths |

### Third Normal Form (3NF):

1. Table is in 1NF and 2NF.
2. Non-primary-key columns do not depend on other non-primary-key columns.

The number of enrolled students in a course depend on the Subject, not the student.

| Student | Subject | Enrolled |
|---------|---------|---------|
| Adam | Biology | 3 |
| Adam | Maths | 5 |
| Alex | Maths | 5 |
| Stuart | Maths | 5 |

vs

| Student | Subject |
|---------|---------|
| Adam | Biology |
| Adam | Maths |
| Alex | Maths |
| Stuart | Maths |

And

| Subject | Enrolled |
|---------|---------|
| Biology | 3 |
| Maths | 5 |

### 3.5NF, 4NF, and 5NF

Not as important and are more difficult to explain, but basically come as a consequence of thinking logically about your database design. Basically don't repeat data (foreign keys to other tables don't count as that is not the data itself). Think about the relationships between your pieces of data and set up your 1:M/M:1 and M:M relationships with appropriate columns or join tables.

See also: http://www.slideshare.net/kosalgeek/database-normalization-1nf-2nf-3nf-bcnf-4nf-5nf

### Aliases

Aliases are a piece of a SQL query that allows you to temporarily rename a table or column for the current query. This is useful for creating shorthand names for tables when using table prefixes, renaming columns, or differentiating tables when you join the same table more than once in a query (eliminating ambiguity).

####
```sql
SELECT
    users.userID AS 'id',
    users.username AS 'name'
FROM users;
```

--

```sql
SELECT * FROM authors a
    INNER JOIN books b
        ON a.author_id = b.author_id
ORDER BY a.author_id ASC;
```

--

```sql
SELECT * FROM crew
    LEFT JOIN users photographer
        ON crew.fk_photographer = photographer.userID
    LEFT JOIN users director
        ON crew.fk_director = director.userID
    LEFT JOIN users model
        ON crew.fk_model = model.userID
ORDER BY crew.crewID ASC;
```

### Conditionals

#### CASE Statement
The CASE statement is used when you want to display different things depending on the data that you've queried from the database. There's two different ways to structure a CASE statement shown below. Note that in the first example you can only compare against single values while in the second example you can use actual expressions for evaluation. Also note that CASE statements require an ELSE statement.

```sql
SELECT
    CASE users.age
        WHEN 0 THEN 'baby'
        WHEN 15 THEN 'teen'
        ELSE 'adult'
    END CASE AS 'age'
FROM users;
```

--

```sql
SELECT
    CASE
        WHEN users.age < 13 THEN 'preteen'
        WHEN users.age < 20 THEN 'teen'
        ELSE 'adult'
    END CASE AS 'UserAge'
FROM users;
```

#### IF Statement

CASE statements, as in programming, are just another way of structuring some if/then/else logic. In SQL we also have IF/ELSIF/ELSE statements.

```sql
SELECT
    IF users.age < 13 THEN
        'preteen'
    ELSIF users.age < 20 THEN
        'teen'
    ELSE
        'adult'
    END IF AS 'UserAge'
FROM users;
```
