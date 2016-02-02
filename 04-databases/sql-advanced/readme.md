# Advanced SQL

## Objectives
* Utilize different ways to filter data in the WHERE clause
* Understand the uses of advanced queries like subqueries and joins

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

INSERT INTO authors (name) VALUES ('Elie');
INSERT INTO authors (name) VALUES ('Bob');
INSERT INTO authors (name) VALUES ('Mary');

INSERT INTO books (name, author_id) VALUES ('Book 1', 1);
INSERT INTO books (name, author_id) VALUES ('Book 2', 2);
INSERT INTO books (name, author_id) VALUES ('Book 3', 3);
INSERT INTO books (name) VALUES ('Book 4');


SELECT * FROM authors a
JOIN books b
ON a.author_id = b.author_id
ORDER BY a.author_id ASC;
```

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



