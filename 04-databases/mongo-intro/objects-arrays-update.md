# Working with Nested Objects and Arrays

One of the flexible aspects of MongoDb documents is that fields can have datatypes of arrays or objects, and Mongo gives us query operators to work with them.

Here is an insert query to make two car documents, each having an owner object and features array:

```javascript
db.cars.insertMany([
   {
      make: "Toyota",
      model: "Camry",
      year: 2020,
      owner: {
         name: "John Smith",
         address: "123 Main St, Anytown USA"
      },
      features: ["leather seats", "sunroof", "navigation system"]
   },
   {
      make: "Honda",
      model: "Civic",
      year: 2019,
      owner: {
         name: "Jane Smith",
         address: "456 Elm St, Anytown USA"
      },
      features: ["backup camera", "bluetooth", "automatic transmission"]
   }
])
```

## Querying Objects

There are [two approaches](https://www.mongodb.com/docs/manual/tutorial/query-embedded-documents/#query-on-nested-field) to querying nested objects, for examples these two `find` queries will return the same result:

```javascript
db.cars.find({ "owner.name": "Jane Smith" })
// [
//   {
//     _id: ObjectId("63c9d424924eef58fd8c333d"),
//     make: 'Honda',
//     model: 'Civic',
//     year: 2019,
//     owner: { name: 'Jane Smith', address: '456 Elm St, Anytown USA' },
//     features: [ 'backup camera', 'bluetooth', 'automatic transmission' ]
//   }
// ]
```

```javascript
db.cars.find({ owner: { name: 'Jane Smith', address: '456 Elm St, Anytown USA' } })
```

Notice how the first example can use a single nested field to match a document, whereas the second examples has to supply the entire nested object in order to match (_ie_ `db.cars.find({ owner: { name: 'Jane Smith' } })` would return null, becuase it is missing the address sub field.)

Both of these query styles work on `update` and delete queries, here is an example of one:

```javascript
// update the car's year and owner's address
db.cars.updateOne({ "owner.name": "Jane Smith" }, { $set: { year: 2021, "owner.address": "54321 nowhereville, USA" } })
```

## Querying arrays

Mongo provides two sets of operators for working with arrays, [array query operators](https://www.mongodb.com/docs/manual/tutorial/query-arrays/) and [array update operators](https://www.mongodb.com/docs/manual/reference/operator/update/#operators)

### Read Query Operators



### Update Query Operators
