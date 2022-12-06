# SQL Relationships

## Objectives

* Understand the purpose and results of different types of SQL joins
* Design and normalize a database structure with 1:M and M:M relationships
* Utilize the different types of JOINs to create multi-table SQL queries

## What is a foreign key?

This is where the **relational** part comes in! Foreign keys allow entries in one table to refer to entires in another table.

What are some examples of when this would be useful?

* \(library\) books table references an authors table
* \(elementary school\) a students table refereces a classes table, which references teachers table, which references a schools table, which references a districts table, etc.

Let's build out a movie review table that allows us to keep track of reviews on the movie table from the previous lesson's `movie_lesson` database:

![Foreign Key](foreign_key.png)

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
-- adds a review to which ever movie has an id of 5
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

Here is an example of using a join to display all of the data at once:

```sql
-- Use a JOIN to see all the data at once
SELECT * FROM movies
JOIN movie_reviews ON movies.id=movie_reviews.movie_id
```

## Another Foriegn Key Example

Here, we are creating a table of students, and each student will have have a `FORIEGN KEY` of a course that they are enrolled in:

```sql
-- create a courses table
CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course TEXT
);

-- create a students table with a foriegn key
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name TEXT,
    phone VARCHAR(15),
    email TEXT,
    course_id INTEGER REFERENCES courses(id)
);

-- alternatively, you could alter the table from the first lesson
ALTER TABLE students ADD COLUMN course_id INTEGER REFERENCES courses(id);
```

## SQL Joins

### Anatomy of a Join Statement

![SQL Joins](sql-joins.png)

```sql
	SELECT * FROM tableOne
		<Full/Inner/Left/Right)> JOIN tableTwo
			ON <Condition>
```

Where `<Condition>` is a statement that usually indicates which two columns must match between two tables in order to join, but is basically the equivalent of a WHERE statement for a JOIN. The join condition is usually where the foreign key in one table matches the primary key in the other table.

```sql
	SELECT * FROM tableOne
		INNER JOIN tableTwo
			ON tableTwo.fk_tableOne = tableOne.id
```

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

## 1:M and M:M relationships

When creating a relationship between two pieces of data in different tables, think about the most logical and extensible method in order to tie pieces of data together.

Think of the type of database you might have for a social media website. You can have a table for users and a table for posts. The relationship between users and posts is that of a One-to-Many relationship. One user has many posts. Or conversely, each post has one user (author). Where does it make the most sense to put a column that stores the relationship between users and their posts? In the posts table. Only one extra column is needed in the posts table to store the user ID because each post only has one user.

Now let's extend our social media database and say that each post can have multiple categories. Does each post have only one category? No. Can we say that each category only belongs to one post? No. In this case we cannot put the foreign key column in either the posts or categories tables. We will need to create a new table called a "join table". A "join table" is just a normal table that has (at minimum) two columns that acts as a way to create any possible combination of matches between posts and their categories. This is called a Many-to-Many relationship. Each post has many categories and each category can be tied to many posts.

## Normalization

The idea behind normalization is that the data should not be repeated and proper 1:M/M:M relationships should be established. The rules of normalization are called "Normal Forms". There's technically 6 forms, but the first three are the most important.

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
