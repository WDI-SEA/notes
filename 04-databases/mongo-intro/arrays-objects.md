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

Notice how the first example can use a single nested field to match a document, whereas the second examples has to supply the entire nested object in order to match (_ie_ `db.cars.find({ owner: { name: 'Jane Smith' } })` would return null, because it is missing the address sub field.)

Both of these query styles work on `update` and delete queries, here is an example of one:

```javascript
// update the car's year and owner's address
db.cars.updateOne({ "owner.name": "Jane Smith" }, { $set: { year: 2021, "owner.address": "54321 nowhereville, USA" } })
```

## Querying arrays

Mongo provides two sets of operators for working with arrays, [array query operators](https://www.mongodb.com/docs/manual/tutorial/query-arrays/) and [array update operators](https://www.mongodb.com/docs/manual/reference/operator/update/#operators)

### Read Query Operators

Finding an array that contains a value is simple:

```javascript
db.cars.find({ features: "sunroof"})
```

If you want to match elements in an array with multiple items, you can use the `$all` operator

```javascript
db.cars.find({ features: { $all: ["sunroof", "navigation system"]} })
```

Using the `$size` operator to find all cars that have a specified number of features:

```javascript
db.cars.find({features: {$size: 3}})
```

### Update Query Operators

#### Adding to an array

The `$push` operator adds a value to the end of an array:

```javascript
db.cars.updateOne({ features: "sunroof"}, { $push: { features: "Complimentary Sunglasses" } })
```

Using the `$addToSet` operator to add a new feature to the features array if it doesn't already exist:

```javascript
db.cars.updateMany({make: "Toyota"}, {$addToSet: {features: "cruise control"}})
```

#### Changing the value of a specific index

The `$set` operator used along with the dot notation used to access objects can be used to edit a specific value at a given index:

```javascript
db.cars.updateMany({make: "Toyota"}, {$set: {"features.1": "power windows"}})
```

#### Removing from an array


The`$pop` operator removes the first or last element of an array. Pass `$pop` a value of `-1` to remove the first element of an array and `1` to remove the last element in an array:

```javascript
db.cars.updateMany({make: "Honda"}, {$pop: {features: -1}})
```

`$pull` can be used to remove a value from an array, and `$pullAll` can be given an array of values to remove:

```javascript
db.cars.updateMany({make: "Toyota"}, {$pull: {features: "cruise control"}})
```

```javascript
db.cars.updateMany({make: "Honda"}, {$pullAll: {features: [ "backup camera",  "bluetooth"]}})
```
