#Intro to MongoDB

##Objectives

* Describe how Mongo databases came about & why they're useful
* Compare and contrast NoSQL with SQL
* Define what a document is in the context of MongoDB
* Explain the difference between embedded and referenced documents, and how we use each to model relationships in MongoDB
* Issue basic CRUD commands to a database from the Mongo Shell

##What is MongoDB?

MongoDB (short for hu**mongo**us) is one of the new breeds of databases known as NoSQL databases. NoSQL databases are heavily used in realtime, big data and social media applications and generally called NoSQL because they do things a little differently than traditional SQL databases. It is a schemaless document-based datastore. This means it doesn't have `tables`. It instead has `documents`.

###Data Format

* A MongoDB database consists of documents.
* A document in MongoDB is composed of field and value pairs.

```js
{
  _id: ObjectId("5099803df3f4948bd2f98391"),
  name: { first: "Alan", last: "Turing" },
  birth: new Date('Jun 23, 1912'),
  death: new Date('Jun 07, 1954'),
  contribs: [ "Turing machine", "Turing test", "Turingery" ],
  views: 1250000
}
```

**What does this data structure remind you of?** JSON!

A MongoDB *document* is very much like JSON, except it is stored in the database in a format known as **BSON** (think - Binary JSON).

BSON basically extends JSON with additional data types, such as **ObjectID** and **Date** shown above.

Read more about MongoDB here: [MongoDB Documentation](http://docs.mongodb.org/manual/)

###MongoDB vs. Relational Databases

![MongoDB vs Relational Databases](http://4.bp.blogspot.com/-edz2_QrFvCE/UnzBhKZE3FI/AAAAAAAAAEs/bTEsqnZFTXw/s1600/SQL-MongoDB+Correspondence.PNG)

#### Key Differences of MongoDB

- Schema-less
The documents in a MongoDB collection can have completely different types and number of fields from each other. **How does this compare to a SQL database like PostgreSQL?**

- No Table Joins
In a SQL DB, we break up related data into separate tables.

In MongoDB, we often _embed_ related data in a single document, you'll see an example of this later.

The supporters of MongoDB highlight the lack of table joins as a performance advantage since joins are expensive in terms of computer processing.


##Installation

Before we can begin we need install the MongoDB server. We can simply install it from brew, but then we also need to create a data directory and take ownership of it so MongoDB will have access to it.

```
#Update Homebrew
brew update

#Install MongoDB
brew install mongodb

#make data directory
sudo mkdir -p /data/db

#get your user name
whoami

#set data directory permissions
sudo chown -R USERNAME:wheel /data
```

###Starting and Stopping

We have to remember to start and stop our MongoDB server.

```
#Start the MongoDB server
mongod
```

Press `control-c` to stop the server.


### Creating a Database and Inserting Documents

MongoDB installs with a client app, a JavaScript-based shell, that allows us to interact with MongoDB directly.

Start the app in terminal by typing `mongo`.

The app will load and change the prompt will change to `>`.

List the shell's commands available: `> help`.

Show the list of databases: `> show dbs`.

Show the name of the currently active database: `> db`.

Switch to a different database: `> use [name of database to switch to]`.

Lets switch to the `local` database: `> use local`.

Show the collections of the current database `> show collections`.

#### Creating a new Database

To create a new database in the Mongo Shell, we simply have to _use_ the database.  Lets create a database named _myDB_:

```
> use myDB
```

#### Inserting Data into a Collection

This how we can create and insert a document into a collection named _people_:

```
> db.people.insert({
  name: "Fred",
  age: 21
})
```

Using a collection for the first time creates it!

#### Adding Lots of New Documents

In a moment we'll practice querying our database, but let's get more data in there. Here are few more documents to put in your _people_ collection. We can simply provide this __array__ to the _insert_ method and it will create a document for each object in the array.

```js
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

```
> db.people.find()
```

Again, unlike the rows in a relational database, our documents don't have to have the same fields!

### More Specific Queries

We can also use the `find()` method to query the collection by passing in an argument – a JS object containing criteria to query with.

```
> db.people.find({name: "Adrian"})
```

There are a handful of special criteria variables we can use, too. Here's how we can use MongoDB's `$gt` query operator to return all _people_ documents with an age greater than 20:

```
> db.people.find({age: { $gt: 20}})
```

MongoDB comes with a slew of built-in [query operators](http://docs.mongodb.org/manual/reference/operator/query/#query-selectors) we can use to write complex queries.

__How would we write a query to retrieve people that are less than or equal to age 24?__


This sorts our age query and sorts by _name_:

```
> db.people.find({age: {$gt: 20}}).sort({name: 1})
```
The "1" indicates ascending order.

[This documentation](http://docs.mongodb.org/manual/core/read-operations-introduction/) provides more detail about reading data.

## Updating Data

In MongoDB, we use the `update()` method of collections by specifying the _update criteria_ (like we did with `find()`), and use the `$set` action to set the new value.

```
> db.people.update({name: "Adrian"}, {$set: { age: 99 } })
```

By default `update()` will only modify a single document. However, with the `multi` option, we can update all of the documents that match the query.

```
> db.people.update( { name: { $lt: "M" } }, { $inc: { age: 10 } }, { multi: true } )
```
We used the `$inc` update operator to increase the existing value.

Here is the [list of Update Operators](http://docs.mongodb.org/manual/reference/operator/update/) available.

## Removing Data

We use the `remove()` method to data from collections.

If you want to completely remove a collection, including all of its indexes, use `db.[name of the collection].drop()`.

Call `remove({})` on the collection to remove all docs from a collection. Note: all documents will match the "empty" criteria.

Otherwise, specify a criteria to remove all documents that match it:

```
>db.people.remove( { age: { $lt: 16 } } )
```

## Data Modeling in MongoDB

There are two ways to modeling related data in MongoDB:

- via __embedding__
- via __referencing__ (linking)

Both approaches can be used simultaneously in the same document.

### Embedded Documents

In MongoDB, by design, it is common to __embed__ data in a parent document.

Modeling data with the __embedded__ approach is different than what we've seen in a relational DB where we spread our data across multiple tables. However, this is the way MongoDB is designed to work and is the reason MongoDB can read and return large amounts of data far more quickly than a SQL DB that requires join operations.

To demonstrate __embedding__, we will add another person to our _people_ collection, but this time we want to include contact info. A person may have several ways to contact them, so we will be modeling a typical one-to-many relationship.

## Modeling Data

Let's walk through this command by entering it together:

```js
> db.people.insert({
    name: "Manny",
    age: 33,
    contacts: [
      {
        type: "email",
        contact: "manny@domain.com"
      },
      {
        type: "mobile",
        contact: "(555) 555-5555"
      }
    ]})
```

__What do you imagine could be a downside of embedding data?__

If the embedded data's growth is unbound, MongoDB's maximum document size of 16 megabytes could be exceeded.

The above approach of embedding _contact_ documents provides a great deal of flexibility in what types and how many contacts a person may have.  However, this flexibility slightly complicates querying.

However, what if our app only wanted to work with a person's multiple _emails_ and _phoneNumbers_?

__Knowing this, pair up and discuss how you might alter the above structure.__

#### Referencing Documents

We can model data relationships using a __references__ approach where data is stored in separate documents. These documents, due to the fact that they hold different types of data, are likely be stored in separate collections.

It may help to think of this approach as _linking_ documents together by including a reference to the related document's *_id* field.

Let's create a  _bankAccounts_ collection to demonstrate the __references__ approach.

```
db.bankAccounts.insert({
  amount: 4403
})
```

This bank account might be a _joint account_, owned by more than one person.

For the sake of _data consistency_, keeping the account data in its own document would be a better design decision. In more clear terms, it would not be a good idea to store a bank account's balance in more than one place.

In our app, we have decided that all bank accounts will be retrieved through a person. This decision allows us to include a reference on the person document only.

Implementing the above scenario is as simple as assigning a _bankAccount_ document's *_id* to a new field in our person document:

```js
> db.people.insert({
    name: "Miguel",
    age: 46,
    bankAccount: db.people.findOne()._id
})
```

Again, because there are no "joins" in MongoDB, retrieving a person's bank account information would require a separate query on the _bankAccounts_ collection.


## Data Modeling Best Practices - Discussion

MongoDB was designed from the ground up with application development in mind. More specifically, what can and can't be done in regards to data is enforced in your application, not the database itself (like in a SQL database).

Here are a few things to keep in mind:

- For performance and simplicity reasons, lean toward _embedding_ over _referencing_.
- Prefer the _reference_ approach when the child data could be unbound in amount.
- Prefer the _reference_ approach when multiple parent documents access the same child document and that child's document changes frequently.
- Obtaining _referenced_ documents requires multiple queries by your application.
- In the _references_ approach, depending upon your application's needs, you may choose to maintain links to the related document's *_id* in either document, or both.

For more details regarding data modeling in MongoDB, start with [this section of mongoDB's documentation ](http://docs.mongodb.org/manual/core/data-modeling-introduction/) or this [hour long YouTube video](https://www.youtube.com/watch?v=PIWVFUtBV1Q)


## Conclusion
- What are some of the differences between Mongo & Postgres databases?
- How do you add a document to a collection in the Mongo shell?
- Describe the difference between embedding & referencing documents. Give an example of when you might use each.
