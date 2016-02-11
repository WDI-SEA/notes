# Using your Models inside an app

Just like using express, body-parser, and the other modules, your models must be required
in order to access them in your app.

```js
var db = require("./models");
db.user.create({ firstName: 'Brian', lastName: 'Hague', age: 99 }).then(function(data) {
  // you can now access the newly created task via the variable data
});
```

## CRUD with Sequelize (Using our User model)

### Create

```js
db.user.create({ firstName: 'Brian', lastName: 'Hague', age: 99 }).then(function(data) {
  // you can now access the newly created task via the variable data
});
```

### Read One

```js
db.user.find({where: {id: 2}}).then(function(user) {
  // user will be an instance of User and stores the content of the table entry with id 2. if such an entry is not defined you will get null
});
```

### Find or Create

The method findOrCreate can be used to check if a certain element is already existing in the database. If that is the case the method will result in a respective instance. If the element does not yet exist, it will be created.

```js
db.user
  .findOrCreate({where: { firstName: 'Brian' }})
  .spread(function(user, created) {
    console.log(user); // returns info about the user
  });
```

### Find All

findAll returns more than one instance, which is useful if you need more than one record. find only returns one record.

```js
db.user.findAll().then(function(users) {
  console.log(users);
  // users will be an array of all User instances
});
```

### Update

```js
// method 1

db.user.find({ where: { firstName: 'Brian' } }).then(function(user){
  user.lastName = 'Taco';
  user.save().then(function() {});
});

// method 2
db.user.find({ where: { firstName: 'Brian' } }).then(function(user){
  user.updateAttributes({
    firstName: 'Taco'
  }).then(function() {});
});
```

### Delete (destroy)

```js
db.user.find({ where: { firstName: 'Brian' } }).then(function(user){
  user.destroy().then(function() {});
});
```

##Promises
After a sequelize statement, we can interact with the return of that object using `.then` and in `findOrCreate` we will use `spread`

Finding a user

```js
db.user.find({where: {id: 1}});
```

This will execute a statement to find a user, but it will not let us interact with it. Because of the asynchronous nature of a call, we need to use a Promise (a type of callback) to get that data.

```js
db.user.findById(1).then(function(foundUser) {
  console.log(foundUser);
  //res.send("myTemplate", {user: foundUser);
});
```

in a `findOrCreate`, a callback will return back an array, instead of a single object. There is a type of callback called `.spread` which will allow us to break apart that array and use similar to a traditional callback.


```js
db.user
  .findOrCreate({ firstName: 'Brian' })
  .spread(function(user, created) {
    console.log(user); // returns info about the user
  });
```

##Sequelize Promises

The main callback handlers to be used are as follows.

* `.then` - default promise called when a query is completed.
* `.spread` - used to spread an array of values to parameters. This is only used for `findOrCreate`.
* `.catch` - triggered if something goes wrong (an error).
* `.finally` - triggered after all other callbacks. Can be used for cleanup.

The important thing to remember is that all queries take time and are asynchronous, so you MUST use promises to execute code that needs to happen after the query is completed. You will usually use `then`, except for `findOrCreate`.

##findOrCreate Example

Many CRUD options will use a `.then` style promise. For the most part they function exactly have you been using them. The first parameter of the callback function will be a data object.

In a common situation of finding first, then creating. `findOrCreate` is a useful method. If used with a `.then` you might find the return object being an array. First value being the object, second value being a boolean indicating if the object was created.

Using the `.spread` method will let you use those array values as individual parameters in a similar syntax to what you were using earlier.

```js
db.author.findOrCreate({where: {name: "Brian"}}).spread(function(author, created) {
  console.log(author.get());
  console.log(created);
})
```
