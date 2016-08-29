# Knex

http://www.knexjs.org

## Objectives
* Integrate Knex into a Node project to run queries against a database

## Raw Queries

Knex at its core is a query builder module for Node. That means you can build a query with function calls. That's a bit confusing and over-engineered unless you plan on writing code that could run on different types of databases (very rarely the case). Instead, we're going to use Knex's raw query functionality which allows us to write and run raw SQL queries against our database.


### Setup

To begin with, use npm to install the knex library along with the appropriate database module:

```bash
npm install --save knex pg
```

Then import and setup the module in your project:

```javascript
var knex = require('knex')({
	client: 'pg',
	connection: process.env.DATABASE_URL
});
```

Since we'll be using an environment variable to establish a connection with our database, we'll have to create/modify our .env file. We'll use the environment variable $DATABASE_URL for convenience since Heroku uses the same env variable for our connection string when deployed on their services.

```plaintext
DATABASE_URL=postgresql://postgres@localhost:5432/knextest
```

This is an example of a "connection string" for a database. The full syntax for a postgres connection string is:

```bash
postgresql://[user[:password]@][netloc][:port][/dbname][?param1=value1&...]
```

### Running queries

To run a raw query in Knex, we'll use the `knex.raw(query, [params])` function.

```javascript
knex.raw(`
	SELECT * FROM books
	WHERE title = ?
		AND author = ?
`, [req.query.title, 'Stephen King']).then(function(data) {
	// data will be an array where each row is an object
	// with key/value pairs for column name and value
	console.log(data);
});
```

If you'll note that the raw query contains question marks and and the second function parameter to `knex.raw()` is an array of values. When working with SQL you should **ALWAYS** avoid putting values directly into your query. This opens you up to what is called a SQL Injection Attack where users can manipulate your database and queries at will. Instead, using the question marks and an array of values to substitute in place of those question marks, database modules can safely insert data into your queries without opening yourself to injection attacks. This is known as "prepared statements".

Also to note, the backtick ( \` ) is a special multiline string delimiter that has been introduced in ES6. Node has already implemented its functionality and since SQL queries can be quite long, we want our SQL query to be written out over multiple lines to make it easier to read.

