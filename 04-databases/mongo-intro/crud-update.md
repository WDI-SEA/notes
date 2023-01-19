# MongoDb CRUD intro

## Learning objectives

* Understanding the basics of using the MongoDB shell (`mongosh`)
* Connect to a MongoDB instance
* Create and manipulate collections
* Perform CRUD operations on mongo documents
* Develop a solid understanding of how to use the `mongosh` shell to manage MongoDB databases

## Using `mongosh`

The MongoDB shell, also known as `mongosh`, is a command-line interface for interacting with MongoDB databases. It allows you to perform various tasks such as creating, updating, and querying documents within your databases.

Start the MongoDB shell by typing `mongosh` and pressing return. You can then use the following commands while inside `mongosh`:

| command                                 | action                                                      |
| --------------------------------------- | ----------------------------------------------------------- |
| `show dbs`                              | Shows a list of all available databases                     |
| `use <database>`                        | Switches to the specified database (does not need to exist) |
| `db`                                    | Shows the current database you are using                    |
| `show collections`                      | Shows a list of all collections in the current database     |
| `db.createCollection('collectionName')` | Creates a new collection with 'collectionName'              |
| `db.collectionName.drop()`              | Deletes the collection 'collectionName'                     |

In MongoDB, a database is created automatically when you first insert data into it. So, there's no command to create a database explicitly. Its is also optional to create a collection prior to inserting documents into it. If you attempt to insert a document into a collection that does not exist, MongoDB will first create the collection and then insert the document into it.

### Executing basic JavaScript in `mongosh`

Although most of the commands that you use in the `mongosh` shell are MongoDB-specific commands, `mongosh` can also execute basic js. This can be partiularly useful when working with arrays of MongoDB documents.

Here are some examples of executing basic JavaScript in the `mongosh` shell:

```javascript
// Basic Arithmitic works
1 + 2 // 3
5 * 10 // 50
```

```javascript
// Variable assignment. let and const work too
var x = 10
var y = 20
x + y // 30
```

```javascript
// there is no console, but we can use the print() funciton
print("Hello, MongoDB!") // Hello, MongoDB!
```

```javascript
// Using the Date() constructor:
var today = new Date()
print(today) // ISODate("2022-08-07T20:45:09.908+03:00")
```

```javascript
// Using the Math library
Math.PI // 3.141592653589793
Math.round(Math.PI) // 3
```

```javascript
// using an array iteration method
var myArray = [1, 2, 3, 4, 5]
myArray // [ 1, 2, 3, 4, 5 ]
myArray.forEach(element => print(element))
// 1
// 2
// 3
// 4
// 5
```

## Document CRUD

We will practice CRUD on a `people` collection. Each _person_ document wil have fields `firstName`, `lastName`, `email`, and `age`. Lets get started by connecting to the database and creating a collection.

```javascript
use introDb
// switched to db introDb
db.createCollection("people")
// { "ok" : 1 }
```

We don't need to do anything to enforce a schema, or define what fields each person will have, we can just start CRUDing.

### Create

#### Creating one document

We can use the following methods to create new entries in our collection:

* [db.collection.insertOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertOne/#mongodb-method-db.collection.insertOne)
* [db.collection.insertMany()](https://www.mongodb.com/docs/manual/reference/method/db.collection.insertMany/#mongodb-method-db.collection.insertMany)

This how we can create and insert a document into our people collection:

```javascript
db.people.insertOne({
    firstName: "Weston", 
    lastName: "Bailey", 
    email: "weston.bailey@generalassemb.ly", 
    age: 35
})
// {
//         "acknowledged" : true,
//         "insertedId" : ObjectId("5f2c8f4b4f4e4a29bcf5f5f5")
// }
```

#### Creating Many Documents

If we want to bulk insert documents, we can use the `insertMany` method, and supply it with an array:

```javascript
db.people.insertMany(
    [
        { firstName: "Taylor", lastName: "Darneille", email: "taylor.darneille@generalassemb.ly", age: 29},
        { firstName: "April", lastName: "Gonzales", email: "april.gonzales@generalassemb.ly", age: 30},
        { firstName: "Gabe", lastName: "Gongoso", email: "gabriel.gangoso@generalassemb.ly", age: 26}
    ]
)
// {
//   acknowledged: true,
//   insertedIds: {
//     '0': ObjectId("63c98eef924eef58fd8c3335"),
//     '1': ObjectId("63c98eef924eef58fd8c3336"),
//     '2': ObjectId("63c98eef924eef58fd8c3337")
//   }
// }
```

When insert queries are successful, they will return the ids of the newly created documents.

It is worth noting that documents do not need to have a consistent structure: 

```javascript
db.people.insertOne({
    firstName: "Doireann",
    lastName: "Herold",
    email: "N/A",
    formerTeamMember: true
})
// {
//   acknowledged: true,
//   insertedId: ObjectId("63c99ef1924eef58fd8c333a")
// }
```

### Read

To perform read queries, we have the following methods:

* [db.collection.find()](https://www.mongodb.com/docs/manual/reference/method/db.collection.find/#mongodb-method-db.collection.find) 
* [db.collection.findOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOne/)

#### Reading all Documents in a collection

We can read every document in a collection by supplying an empty object `{}` as the arguments to `db.collection.find()`:


```javascript
db.people.find({})
// returns array of all people
```

#### Matching fields when reading

We can provide key/value pairs to `db.collection.find()` to match specific documents:

```javascript
db.people.find({firstName: "Taylor" })
db.people.find({firstName: "Weston", lastName: "Bailey"})
// returns array of matching documents
```

If you would like to only return the first matched document, you can use the `db.collection.findOne({})` method. It returns the very first matched document it encounters, and is most useful when finding documents by their id:

```javascript
// note the _ before '_id'
// you will need to copy a valid ObjectId returned form your database for this example
db.people.findOne({ _id: ObjectId("63c99020924eef58fd8c3338") })
// returns a single entry
```

#### Sorting the results

We can use the [.sort()](https://www.mongodb.com/docs/manual/reference/method/cursor.sort/) method to sort the results of a read query. We can supply a field to sort by, and direction to sort in with `1` indicating an ascending sort, and `-1` indicating a descending sort.

```javascript
db.people.find({}).sort({ firstName: 1 })
// returns documents alphabetized with "A"s at the top
db.people.find({}).sort({ firstName: -1 })
// returns documents alphabetized with "Z"s at the top
```

#### Limiting the results

The [limit()](https://www.mongodb.com/docs/manual/reference/method/cursor.limit/) method limits the returned queries by a numerical argument:

```javascript
db.people.find({}).limit(2)
// returns only two documents
```

#### Chaining methods

Methods can be chained together like so:

```javascript
db.people.find({}).sort({ firstName: 1 }).limit(2)
// sorts by firstName ascending and returns the top 2 results
```

#### Query Operators

MongoDb provides us with [query operators](https://www.mongodb.com/docs/manual/reference/operator/query/) that allow us to perform more specific queries. Here are some examples of using common query operators:

```javascript
// find all documents where the age field is greater than 29
db.people.find({age: {$gt: 29}})
```

```javascript
// find all documents where the age field is less than or equal to 30
db.people.find({age: {$lte: 30}})
```

```javascript
// match a substring with regular expression
db.people.find({email: {$regex: "general"}})
```

```javascript
// Find all documents where the formerTeamMember field exists
db.people.find({formerTeamMember: {$exists: true}})
```

```javascript
// find all documents that do not match a certain name
db.people.find({name: {$ne: "Weston"}})
```

```javascript
// find all documents with either one name or another
db.people.find({$or: [{firstName: "April"}, {firstName: "Gabe"}]})
```

### Update

The following methods are most useful for updating documents, however there are some others that have more esoteric use cases, and are linked in a later section.

* [db.collection.updateOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateOne/#mongodb-method-db.collection.updateOne) update the individual fields of a document
* [db.collection.updateMany()](https://www.mongodb.com/docs/manual/reference/method/db.collection.updateMany/#mongodb-method-db.collection.updateMany) update individula fields of many documents
* [db.collection.replaceOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.replaceOne/#mongodb-method-db.collection.replaceOne) completely replace an entire document

When using `updateOne` and `updateMany` methods, we use the `$set` operator to provide new values to be updated in the db. They both have the same argument interface as well: `updateOne({ read query }, { update query }, { options })`. We will touch on the `{ options }` in a later section.



#### Update Operators

https://www.mongodb.com/docs/manual/reference/operator/update/

#### Upserting

https://www.mongodb.com/docs/manual/reference/method/Bulk.find.upsert/

#### Others

* [db.collection.findOneAndReplace()](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOneAndReplace/#mongodb-method-db.collection.findOneAndReplace)
* [db.collection.findOneAndUpdate()](https://www.mongodb.com/docs/manual/reference/method/db.collection.findOneAndUpdate/#mongodb-method-db.collection.findOneAndUpdate)
* [db.collection.findAndModify()](https://www.mongodb.com/docs/manual/reference/method/db.collection.findAndModify/#mongodb-method-db.collection.findAndModify)
* [db.collection.bulkWrite()](https://www.mongodb.com/docs/manual/reference/update-methods/#std-label-additional-updates)

### Destroy

* [db.collection.deleteOne()](https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteOne/#mongodb-method-db.collection.deleteOne) 
* [db.collection.deleteMany()](https://www.mongodb.com/docs/manual/reference/method/db.collection.deleteMany/#mongodb-method-db.collection.deleteMany)

## Working with Nested Objects and Arrays

## Data Modeling

### Embedded docs

### Referenced Docs

## Working with Embedded docs

Crud on embedded work history

https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/

#### Using Array Update Operators

https://www.mongodb.com/docs/manual/reference/operator/update/#array

## Mongo References

Crud on Bank Accounts





