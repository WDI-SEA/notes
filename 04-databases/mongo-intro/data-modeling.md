# Data Modeling

## Data Modeling in MongoDB

There are two ways to modeling related data in MongoDB:

* via [embedding](https://www.mongodb.com/basics/embedded-mongodb)
* via [referencing](https://www.mongodb.com/docs/manual/tutorial/model-referenced-one-to-many-relationships-between-documents/) \(linking\)

Both approaches can be used simultaneously in the same document.

### Embedded Documents

In MongoDB, by design, it is common to **embed** data in a parent document.

Modeling data with the **embedded** approach is different than what we've seen in a relational DB where we spread our data across multiple tables. However, this is the way MongoDB is designed to work and is the reason MongoDB can read and return large amounts of data far more quickly than a SQL DB that requires join operations.

To demonstrate **embedding**, we will add another person to our _people_ collection, but this time we want to include contact info. A person may have several ways to contact them, so we will be modeling a typical one-to-many relationship.

## Modeling Data

Let's walk through this command by entering it together:

```javascript
db.people.insertOne({
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

**What do you imagine could be a downside of embedding data?**

If the embedded data's growth is unbound, MongoDB's maximum document size of 16 megabytes could be exceeded.

The above approach of embedding _contact_ documents provides a great deal of flexibility in what types and how many contacts a person may have. However, this flexibility slightly complicates querying.

However, what if our app only wanted to work with a person's multiple _emails_ and _phoneNumbers_?

**Knowing this, pair up and discuss how you might alter the above structure.**

#### Referencing Documents

We can model data relationships using a **references** approach where data is stored in separate documents. These documents, due to the fact that they hold different types of data, are likely be stored in separate collections.

It may help to think of this approach as _linking_ documents together by including a reference to the related document's _\_id_ field.

Let's create a _bankAccounts_ collection to demonstrate the **references** approach.

```javascript
db.bankAccounts.insertOne({
  amount: 4403
})
```

This bank account might be a _joint account_, owned by more than one person.

For the sake of _data consistency_, keeping the account data in its own document would be a better design decision. In more clear terms, it would not be a good idea to store a bank account's balance in more than one place.

In our app, we have decided that all bank accounts will be retrieved through a person. This decision allows us to include a reference on the person document only.

Implementing the above scenario is as simple as assigning a _bankAccount_ document's _\_id_ to a new field in our person document:

```javascript
db.people.insertOne({
    name: "Miguel",
    age: 46,
    bankAccount: db.bankAccounts.findOne()._id
})
```

Again, because there are no "joins" in MongoDB, retrieving a person's bank account information would require a separate query on the _bankAccounts_ collection.

It is possible to 'join' refernces using mongo's [aggregate() pipeline](https://www.mongodb.com/docs/manual/reference/operator/aggregation-pipeline/) along with the `$match` operator and the `$lookup` operator.

```javascript
db.people.aggregate([
   { $match: { name: "Miguel" }},  // what to search for
   { $lookup: {
        from: "bankAccounts",      // collection to join
        localField: "bankAccount", // field from the document we match
        foreignField: "_id",       // field from the documents we are joining
        as: "personBankAccount"    // what to name the ouput array
   }}
])
```

## Data Modeling Best Practices - Discussion

MongoDB was designed from the ground up with application development in mind. More specifically, what can and can't be done in regards to data is enforced in your application, not the database itself \(like in a SQL database\).

Here are a few things to keep in mind:

* For performance and simplicity reasons, lean toward _embedding_ over _referencing_.
* Prefer the _reference_ approach when the child data could be unbound in amount.
* Prefer the _reference_ approach when multiple parent documents access the same child document and that child's document changes frequently.
* Obtaining _referenced_ documents requires multiple queries by your application.
* In the _references_ approach, depending upon your application's needs, you may choose to maintain links to the related document's _\_id_ in either document, or both.

For more details regarding data modeling in MongoDB, start with [this section of mongoDB's documentation ](http://docs.mongodb.org/manual/core/data-modeling-introduction/) or this [hour long YouTube video](https://www.youtube.com/watch?v=PIWVFUtBV1Q)

## Conclusion

* What are some of the differences between Mongo & Postgres databases?
* How do you add a document to a collection in the Mongo shell?
* Describe the difference between embedding & referencing documents. Give an example of when you might use each.

