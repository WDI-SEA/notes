# CRUD in MongoDB

### Creating a Database and Inserting Documents

MongoDB installs with a client app, a JavaScript-based shell, that allows us to interact with MongoDB directly.

Open a new terminal window and start a mongo shell by typing `mongo`.

The app will load and change the prompt will change to `>`.

List the shell's commands available: `> help`.

Show the list of databases: `> show dbs`.

Show the name of the currently active database: `> db`.

Switch to a different database: `> use [name of database to switch to]`.

Lets switch to the `local` database: `> use local`.

Show the collections of the current database `> show collections`.

#### Creating a new Database

To create a new database in the Mongo Shell, we simply have to _use_ the database. Lets create a database named _myDB_:

```text
> use myDB
```

#### Inserting Data into a Collection

This how we can create and insert a document into a collection named _people_:

```text
> db.people.insert({
  name: "Fred",
  age: 21
})
```

Using a collection for the first time creates it!

#### Adding Lots of New Documents

In a moment we'll practice querying our database, but let's get more data in there. Here are few more documents to put in your _people_ collection. We can simply provide this **array** to the _insert_ method and it will create a document for each object in the array.

```javascript
db.people.insert(
[
  {
    "name": "Emma",
    "age": 20
  },
  {
    "name": "Ray",
    "age": 45
  },
  {
    "name": "Celeste",
    "age": 33
  },
  {
    "name": "Stacy",
    "age": 53
  },
  {
    "name": "Katie",
    "age": 24
  },
  {
    "name": "Adrian",
    "age": 47
  }
])
```

## Querying Documents

To list all documents in a collection, we use the _find_ method on the collection without any arguments:

```text
> db.people.find()
```

Again, unlike the rows in a relational database, our documents don't have to have the same fields!

### More Specific Queries

We can also use the `find()` method to query the collection by passing in an argument – a JS object containing criteria to query with.

```text
> db.people.find({name: "Adrian"})
```

There are a handful of special criteria variables we can use, too. Here's how we can use MongoDB's `$gt` query operator to return all _people_ documents with an age greater than 20:

```text
> db.people.find({age: { $gt: 20}})
```

MongoDB comes with a slew of built-in [query operators](http://docs.mongodb.org/manual/reference/operator/query/#query-selectors) we can use to write complex queries.

**How would we write a query to retrieve people that are less than or equal to age 24?**

This sorts our age query and sorts by _name_:

```text
> db.people.find({age: {$gt: 20}}).sort({name: 1})
```

The "1" indicates ascending order.

[This documentation](http://docs.mongodb.org/manual/core/read-operations-introduction/) provides more detail about reading data.

## Updating Data

In MongoDB, we use the `update()` method of collections by specifying the _update criteria_ \(like we did with `find()`\), and use the `$set` action to set the new value.

```text
> db.people.update({name: "Adrian"}, {$set: { age: 99 } })
```

By default `update()` will only modify a single document. However, with the `multi` option, we can update all of the documents that match the query.

```text
> db.people.update( { name: { $lt: "M" } }, { $inc: { age: 10 } }, { multi: true } )
```

We used the `$inc` update operator to increase the existing value.

Here is the [list of Update Operators](http://docs.mongodb.org/manual/reference/operator/update/) available.

## Removing Data

We use the `remove()` method to data from collections.

If you want to completely remove a collection, including all of its indexes, use `db.[name of the collection].drop()`.

Call `remove({})` on the collection to remove all docs from a collection. Note: all documents will match the "empty" criteria.

Otherwise, specify a criteria to remove all documents that match it:

```text
>db.people.remove( { age: { $lt: 16 } } )
```

