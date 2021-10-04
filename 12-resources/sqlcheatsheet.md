# PostgreSQL Cheat Sheet

## Some things to note about SQL:

* All SQL statements end in a semicolon.
* You can separate statements into separate lines, for readability, as long as you declare the end with a semicolon.
* Capitalizing commands is optional, but highly recommended for readability.
* Need help, or more explanations? Try the tutorials at [PG Exercises](http://pgexercises.com/) or [Schemaverse](https://schemaverse.com/).

### PSQL Commands

```text
\list           - list all available databases
\dt             - list all tables in the current database
\d+ tablename   - look at a table's structure
\connect testdb - connect to database (specify name)
\c testdb       - connect to database (shorthand)
\conninfo       - check connection info
\?              - all psql commands
\help           - all PostgreSQL commands
\q              - quit
```

## SQL Commands

### Create a database

```sql
CREATE DATABASE databasename;
```

### Create a table

```sql
CREATE TABLE tablename (
  id SERIAL PRIMARY KEY,
  column1 INTEGER REFERENCES table2 (table2_id),
  column2 VARCHAR(15),
  column3 TEXT,
  column4 DATE NOT NULL
);
```

### INSERT data into a table

```sql
INSERT INTO tablename (column1, column2, column3, column4)
VALUES (30, 'A test', 'A lot more text than varchar', '2015-07-15');
```

### SELECT data from a table

#### Select all columns \(with wildcard\)

```sql
SELECT * FROM tablename;
```

#### SELECT specific columns

```sql
SELECT column1 FROM tablename;
SELECT column1, column2 FROM tablename;
```

#### Select distinct values from a column

```sql
SELECT DISTINCT column1 FROM tablename;
```

### Selecting using WHERE

#### SELECT using a WHERE clause

```sql
SELECT * FROM tablename
WHERE column1 = 30;
```

#### NOT EQUAL

```sql
SELECT * FROM tablename
WHERE column1 <> 1;
```

#### LIKE \(usually uses a wildcard, '%'\)

```sql
SELECT * FROM tablename
WHERE column2 LIKE '%test%';
```

#### ILIKE \(case insensitive\)

```sql
SELECT * FROM tablename
WHERE column2 ILIKE '%test%';
```

#### ORDER BY

```sql
SELECT * FROM tablename
ORDER BY name DESC;

SELECT * FROM tablename
ORDER BY name ASC;
```

#### AND/OR

```sql
SELECT * FROM tablename
WHERE column1 = 30 AND column2 = 'test' OR column3 = 'woah';
```

#### IN/NOT IN

```sql
SELECT * FROM tablename
WHERE column1 IN (30, 40) AND column2 NOT IN ('taco', 'burrito');
```

#### LIMIT \(returns the first rows\)

Example: Limit the query results by returning the first 3 results.

```sql
SELECT * FROM tablename LIMIT 3;
```

#### LIMIT + OFFSET

Example: Return results 4-6

```sql
SELECT * FROM tablename
LIMIT 3 OFFSET 3;
```

### Select an aggregate

#### COUNT

```sql
SELECT count(*) from tablename;
```

#### MAX/MIN values

```sql
SELECT max(*) from tablename;
SELECT min(*) from tablename;
```

### UPDATE data in a table

```sql
UPDATE tablename SET column1 = 40
WHERE column2 = 'A test';
```

### ALTER table columns and constraints

```sql
ALTER TABLE table1 ADD CONSTRAINT table1_id
FOREIGN KEY (table1_id) REFERENCES table2 (table2_id)
ON DELETE NO ACTION;

ALTER TABLE books ADD COLUMN year_released INTEGER;

ALTER TABLE books ALTER COLUMN name SET NOT NULL;
```

--

### DELETE data from a table

```sql
DELETE from tablename
WHERE column1 = 40;
```

### DROP a table

```sql
DROP TABLE tablename;
```

### JOINing Tables

![SQL Joins](http://www.dofactory.com/Images/sql-joins.png)

It's good to know the differences between JOINs, but you'll usually use plain JOIN, which performs an INNER JOIN by default.

```sql
SELECT * FROM person
JOIN librarycard
ON person.id = librarycard.person_id;
```

### GROUP BY

```sql
SELECT COUNT(rating) FROM movies
GROUP BY rating;
```

