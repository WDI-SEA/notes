
# Intro to SQL

## Introduction To SQL and Databases

### Objectives

* Describe the purpose of a database
* Connect to a PostgreSQL database using `psql`
* Use SQL to create a database, tables, and entries
* Use SQL CRUD operations to insert, select, update, and delete data
* Define the purpose of Primary and Foreign Keys

### What is a database?

* It is a program that enforces structure on your data and allows a computer to quickly retreive data.
* A database should support CRUD operations.
  * **CRUD:** Create, Read, Update, Destroy
* Sometimes called a DBMS \(Database Management System\)

### Why Use a Database?

Discuss as a class. Why is it better than just writing to files?

* Data is structured
* Can store [master data and transactional data](https://www.quora.com/What-is-the-difference-between-transactional-data-and-master-data)
* Data retrevial is fast
* Has a system for remote access \(data is often stored on a remote server\)
* Has a system for backup

### Types of Databases

#### RDBMS

\(Relational Database Management System\) The most common type of database today is a **relational database**. Relational databases have tabular data with rows for each instance of data and columns for each attribute of that data. Tables may refer to one another. Relational databases typically use **SQL** \(Structured Query Language\).

![diagram of example relational database](https://image.slidesharecdn.com/databasemanagementsystem-161020091729/95/database-management-system-9-638.jpg?cb=1476955074)

**Brands of Relational Databases**

* Postgres
* MySQL
* Oracle \(Commercial Product with lots of features\)
* Microsoft SQL Server
* SQLite \(Good for mobile development/Small applications\)

#### Cloud Storage

This is a very vague term and can be used to mean lots of things. Typically it is a system in which your data is stored and managed by a company so you don't have to worry about losing it. Examples included AWS \(Amazon Web Services\), Rackspace, MS Azure

#### NoSQL

There is also a school of thought called NoSql \(literally Not SQL\). Instead of data being stored in tables, it is often a Key Value storage system and is not relational. This is typically used in applications where a database needs to scale well. Example technologies include MongoDB, Apache CouchDB, SimpleDB.

### How are databases used in the wild?

For learning and testing purposes, we will be using Postgres on the same machine that our web server is running. In the real world, your database will be on a separate machine, called a **database server**.

A database server is a computer or group of computers that is dedicated to storing your data and handling remote requests to retreive that data. Even in a very simple configuration, the database server will have at least 1 backup machine that keeps an exact copy of the database just in case the main database server goes down.

### SQL: Structured Query Language

**A Brief History of Databases**

Before the notion of an RDBMS \(like PostreSQL\) and a standard language for querying that data was created \(SQL\), there were many database vendors. Each vendor had different ways of storing data and very different ways of retreiving the data afterwards. Moving data from one system to another was very costly. Luckly, in the 1970s, SQL was created and later turned into a standard. Modern relational databases are now based on the SQL standard, so moving from Postgres to Oracle is not nearly as much of a challenge as it used to be.
### SQL is known as an `ACID`ic database

`ACID` is an acronym for `A`tomicity, `C`onsistency, `I`solation, and `D`urability

`A`tomicity means a single database `transaction` will not interfere with another -- they are both isolated and `atomic`

`C`onsistency guarantees that a transaction never leaves your database in a half-finished state.

`I`solation keeps transactions separated from each other until they’re finished.

`D`urability guarantees that the database will keep track of pending changes in such a way that the server can recover from an abnormal termination -- if it crashes it can uncrash.

## psql

Today we're using [PostgreSQL](https://www.postgresql.org/download/macosx/), often called Postgres. Postgres is based off an older database system called Ingres. That's where the name comes from.


**psql** is a command line tool to interact with postgres databases, by default it connects to the localhost database with the name of the current user and provides a `repl` for `SQL` commands.

* In your terminal, type `psql` to begin using psql.

The psql shell has some of it's own commands.

* type `\?` to view them all.

Note that all psql commands start with `\` except for `q`.

To _quit_ psql and return to the home terminal:

```bash
username #\q
```

Here is a handy cheatsheet for some of the most useful `psql` shell commands:

| Function | Command | Description |
| ------ | ------- | ---------- |
| quit | `\q` | quit the shell |
| help | `\?` | list help for the psql shell |
| help | `\h` | list all possible `SQL` commands |
| help | `\h  SELECT` | get help for a specific SQL command  |
| list | `\l` | lists all availible dbs found in the cluster |
| connect | `\c` | connect to a database |
| describe tables | `\dt` | list all the tables in the current database |
| describe table | `\d table_name` | lists a table's columns and datatypes |
| edit command | `\e` | opens last command in your shell's default editor |
| expanded display | `\x off  (on or auto)` | will change the wrap behavior of column display |
| import  | `\i file-name.sql` | imports a `.sql` file and runs the commands |

## SQL Loves Acronyms

### **CRUD**

Database **CRUD** Describe the four basic types of database `transactions`

Stands for `C`reate, `R`ead, `U`pdate and `D`estroy. This is the lifecycle of data in an applicatoin. In SQL, CRUD can be mapped to the following **INSERT, SELECT, UPDATE, DELETE**. We will walk through examples in this section.

* To`CREATE` something new in a SQL database an **INSERT** command is used
* To `READ` infomation from from a SQL databaes a **SELECT** command is used
* To `UPDATE` an item from in a SQL databaes an **UPDATE** command is used
* To `DESTROY` infomation from from a SQL databaes a **DELETE** command is used

## Writing SQL Queries

Most database products have the notion of separate databases. Lets create one for the lesson.

```sql
CREATE DATABASE testdb;
```

To view all the databases that exist on your machine, type `\l`. You should see `testdb` in this list.

Connect to the database: `\connect testdb`

Once we connect, our command prompt should look similar to this: `testdb=#`

To view the tables in the database you're connected to, type `\dt`. \(This stands for "display tables".\)

At this point we should have a database with no tables in it. So now we need to create tables - using SQL **\(NOT to be confused with the psql app itself\)**

**ALL SQL COMMANDS MUST BE ENDED WITH A SEMICOLON IN THE PSQL SHELL** It doesn't matter how many lines you take up to write the SQL statements because it won't run until you type a semi-colon.

Note that psql will not accept values with double quotes, only single quotes.

#### CREATE-ing a Table

This is an example of a students table. \(We will talk about the primary key soon.\)

`CREATE TABLE table_name ( column_name data_type, column_name data_tpye )`

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone VARCHAR(15),
    email TEXT
);
```

Check that it's there:

```text
\dt
```

Look at the table structure

```text
 \d students
```

#### INSERT-ing Data

`INSERT INTO table_name (first_col, second_col) VALUES (first_col_data, second_col_data)`

```sql
INSERT INTO students
(name, phone, email)
VALUES ('William Smith', '(415)555-5555', 'bill@example.com');
```

```sql
INSERT INTO students
(name, phone, email)
VALUES ('Bob Jones', '(415)555-5555', 'bob@example.com');
```

#### SELECT-ing Data

`SELECT columns FROM table_name`

```sql
SELECT * FROM students;
```

```sql
SELECT * FROM students WHERE name = 'Bob Jones';
```

```sql
SELECT id, name FROM students;
```

### UPDATE-ing Data

The update statement is defined [here](http://www.postgresql.org/docs/9.1/static/sql-update.html) in the postgres docs. It is used to change existing data in our database.

Update statements are formatted like this: `UPDATE FROM table WHERE boolean(condition)`

```sql
UPDATE students SET email='bobby@example.com' WHERE name = 'Bob Jones';
```

### DELETE-ing Data

Deleting works similarly to a select statement. Here are the [docs on delete](http://www.postgresql.org/docs/8.1/static/sql-delete.html)

the syntax is `DELETE FROM table WHERE boolean(condition)`

```sql
DELETE FROM students WHERE name = 'Mary';
```
`->DELETE 0`


```sql
DELETE FROM students WHERE email = 'bobby@example.com';
```
`->DELETE 1`

#### DROP-ing a Table

```sql
DROP TABLE students;
```

### Database Schema Design

The **schema** of the database is the set of CREATE TABLE commands that specify what the tables are and how they relate to each other. For our very simple database example, here is the schema:

We typed

```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone VARCHAR(15),
    email TEXT
);
```

```text
testdb=# \d students
                                   Table "public.students"
 Column |         Type          | Collation | Nullable |               Default                
--------+-----------------------+-----------+----------+--------------------------------------
 id     | integer               |           | not null | nextval('students_id_seq'::regclass)
 name   | text                  |           |          | 
 phone  | character varying(15) |           |          | 
 email  | text                  |           |          | 
Indexes:
    "students_pkey" PRIMARY KEY, btree (id)
```

### What is a Primary Key?

It denotes an attribute on a table that can uniquely identify the row.

#### What does SERIAL Do?

SERIAL tells the database to automatically assign the next unused integer value to id whenever we insert into the database and do not specify id. In general, if you have a column that is set to SERIAL, it is a good idea to let the database assign the value for you.

### Data Types

Similar to how Javascript has types of data, SQL defines types that can be stored in the DB. Here are some common ones:

* Serial
* Integer
* Numeric // Numbers are exact, no rounding error
* Float // Rounding error is possible, but operations are faster than Numeric
* Text, Char\(set number of characters\), Varchar\(max number of characters\)
* Timestamp
* Boolean \(True or False\)

All postgres datatypes can be found [here](https://www.postgresql.org/docs/9.5/datatype.html)

### READING with More Advanced SELECT Queires

A select statement allows you to get data from the database. Here are the [docs on select](http://www.postgresql.org/docs/9.0/static/sql-select.html). Also, postgres has a good [tutorial on select](http://www.postgresql.org/docs/7.3/static/tutorial-select.html). I'd recommend looking at the tutorial sometime after the lesson.

Create a new database to hold a movies table:

```sql
CREATE DATABASE movie_lesson;
```

Connect to the new database:

```sql
\connect movie_lesson;
```

Given this table:

```sql
CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title TEXT,
  description TEXT,
  rating INTEGER
);
```

And these insert statements:

```sql
INSERT INTO movies (title, description, rating) VALUES('Cars', 'a movie', 9);
INSERT INTO movies (title, description, rating) VALUES('Back to the Future', 'another movie', 9);
INSERT INTO movies (title, description, rating) VALUES('Dude Wheres My Car', 'probably a bad movie', 3);
INSERT INTO movies (title, description, rating) VALUES('Godfather', 'good movie', 9);
INSERT INTO movies (title, description, rating) VALUES('Mystic River', 'did not see it', 7);
INSERT INTO movies (title, description, rating) VALUES('Jurassic Park', 'dinos and Jeff Goldblum', 10);
INSERT INTO movies (title, description, rating) VALUES('Argo', 'a movie', 8);
INSERT INTO movies (title, description, rating) VALUES('Gigli', 'really bad movie', 1);
```

This will select all the attributes from the movies table unconditionally. Make sure not to forget the semi-colon at the end of each statement.

```sql
SELECT * FROM movies;
```

We may not want all attribues though. Let's say instead we only care about the titles of the movie and the description. Here is the query we'd use:

```sql
SELECT title, description FROM movies;
```

This will select the titles from movies table where the rating is greater than 4.

```sql
SELECT title FROM movies WHERE rating > 4;
```

You can also have more complex queries to get data. The following query finds all the movies with a rating greater than 4 and with a title of Cars.

```sql
SELECT title FROM movies WHERE rating > 4 AND title = 'Cars';
```

SQL also supports an OR statement. The following query will return any movie with a rating greater than 4, or any movies with the title Gigli. In other words, if a movie called Gigli is found with a rating equal to 1, it will still be returned along with any movie with a rating greater than 4.

```sql
SELECT title FROM movies WHERE rating > 4 OR title = 'Gigli';
```

Let's say that we just want a list of the best movies of all time. We can do a select statement that ensures ordering. The DESC keyword tells it to order the rating in descending order. ASC is the default.

```sql
SELECT title, rating FROM movies ORDER BY rating DESC;
```

**Note:** If no order by clause is specified, the database does not give any guarantees on what order your data will be returned in. At times it may seem like data you are getting back is in sorted order, but make sure not to rely on that in your code. Only rely on a sort if you also have an ORDER BY clause.

We've gotten a list of movies back, but it's way too long for our uses. Let's instead only get the top 5 movies that are returned using LIMIT:

```sql
SELECT title, rating FROM movies ORDER BY rating DESC LIMIT 5;
```
#### Exercise

Write a query on the movie table to return the worst movie of all time. There should be only 1 result returned. The result should include the title, description and rating of the movie.

For example, if we do not think Gigli was actually that bad, and we want to change the rating to a 2, we can use an update statement:

```sql
UPDATE movies SET rating=2 WHERE title='Gigli';
```

### Deleting

The statement below deletes the Dude Wheres My Car row from the database:

```sql
DELETE FROM movies WHERE title='Dude Wheres My Car';
```

We could also use compound statements here:

```sql
DELETE FROM movies WHERE id < 9 AND rating = 2;
```
### Foreign Keys

This is where the **relational** part comes in! Foreign keys allow entries in one table to refer to entires in another table.

What are some examples of when this would be useful?

* \(library\) books table references an authors table
* \(elementary school\) a students table refereces a classes table, which references teachers table, which references a schools table, which references a districts table, etc.

Let's build out the books and authors tables listed above:

```sql
-- a table that holds movie reviews
CREATE TABLE movie_reviews (
  id SERIAL PRIMARY KEY,
  description TEXT,
  reviewer TEXT,
  score INT,
  -- a foreing key that lets us find the movie that this review is for
  movie_id INT REFERENCES movies(id)
);
```

```sql
-- adds a review to which ever movie has an id o 5
INSERT INTO movie_reviews (description, reviewer, score, movie_id)
VALUES ('pretty good', 'The Critic', 5); 
```

```sql
-- nested queries to find movies and add reviews to them
INSERT INTO movie_reviews (description, reviewer, score, movie_id)
VALUES ('Love them Dinos', 'The Critic', 10,  
  -- the parans  ()  allow one query to be inside another
  (SELECT id FROM movies WHERE title='Jurassic Park')
);
```

```sql
INSERT INTO movie_reviews (description, reviewer, score, movie_id)
VALUES ('Cars p good', 'The Critic', 7,  
  (SELECT id FROM movies WHERE title='Cars')
);
```

```sql
INSERT INTO movie_reviews (description, reviewer, score, movie_id)
VALUES ('Awesome for Sci-fi nerds', 'The Critic', 9,  
  (SELECT id FROM movies WHERE title='Back to the Future')
);
```

Use select statements to view the tables and make sure everything worked as expected.

```sql
SELECT * FROM movies;
SELECT * FROM movie_reviews;
```

```sql
-- Use a JOIN to see all the data at once
SELECT * FROM movies
JOIN movie_reviews ON movies.id=movie_reviews.movie_id
```

How does the data displayed differ from the different select commands?

### ER Diagrams

Creating an ER diagram can be useful if you are designing a DB with lots of tables and relationships to one another. It may be useful to revist ER Diagrams after you have a firm understanding of databases. Here are some useful resources:

* [Wikipedia - ER Diagram](http://en.wikipedia.org/wiki/Entity-relationship_model)
* [Ultimate Guide To ER Diagrams](http://creately.com/blog/diagrams/er-diagrams-tutorial/) - Not so ultimate, but a good intro. 

## Working with `.sql` files in the `psql` shell

`.sql` files can be written and ran like any other langauge. From within the `psql` the command `\i <relative path to file>.sql` will import and run a `.sql` file.

* `mkdir advanced-sql` to create a folder for the sql files
* `touch create-example-db.sql` to make your first `.sql` file to run
* add the following `SQL` example:

```sql
-- comments in SQL start with tow dashes btw
/*
multiline line comments work like this 
this file will create a db called example_books and connect to it, CREATE a book table, add CREATE information and then READ all 
*/
-- create the db
CREATE DATABASE "example_books";

-- connect to it (psql commands are valid)
\connect example_books

-- create the tables

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  title TEXT,
  author TEXT
);

-- CREATE some data
INSERT INTO books (title, author) VALUES ('Do Androids Dream of Electric Sheep?', 'Phillip K. Dick');
INSERT INTO books (title, author) VALUES ('Ubik', 'Phillip K. Dick');
-- single qoutes are escaped by doubling them up ''
INSERT INTO books (title, author) VALUES ('Cat''s Cradle', 'kurt Vonnegut');
INSERT INTO books (title, author) VALUES ('Breakfast of Champions', 'kurt Vonnegut');

-- READ some data
SELECT * FROM books;
```

### LAB:

[Where in the world is Carmen San Diego?](https://github.com/WDI-SEA/sql-carmen-san-diego)
