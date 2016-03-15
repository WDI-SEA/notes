#Intro to NoSQL

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
