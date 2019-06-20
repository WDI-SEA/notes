# Using your Models inside an app

Just like using express, body-parser, and the other modules, your models must be required
in order to access them in your app.

```js
var db = require("./models");
db.user.create({
  firstName: 'Brian',
  lastName: 'Hague',
  age: 99
}).then(function(data) {
  // you can now access the newly created task via the variable data
});
```

## CRUD with Sequelize (Using our User model)

### Create

```js
db.user.create({
  firstName: 'Brian',
  lastName: 'Hague',
  age: 99
}).then(function(data) {
  // you can now access the newly created task via the variable data
});
```

### Read One

```js
db.user.findOne({
  where: {id: 2}
}).then(function(user) {
  // user will be an instance of User and stores the content of the table entry with id 2. if such an entry is not defined you will get null
});
```

### Find or Create

The method findOrCreate can be used to check if a certain element is already existing in the database. If that is the case the method will result in a respective instance. If the element does not yet exist, it will be created with the provided attributes (a combination of `where` and `defaults`)

```js
db.user.findOrCreate({
  where: {
    firstName: 'Brian',
    lastName: 'Smith'
  },
  defaults: { age: 88 }
}).spread(function(user, created) {
  console.log(user); // returns info about the user
});
```

**NOTE:** The `findOrCreate` method historically had a different way of using the promise that returned with the data. You can see it in the code above. While other database read functions use the `.then` promise resolution function, the `findOrCreate` uses `.spread()`. This is because it returns not only the data that was found or created, it also returns a boolean true or false value indicating whether the record was created or not. If the value is `true` then the record was not found and had to be created. If it is `false` then the record already existed in the db and was retrieved. These two values are sent to our function in an array. By using the `.spread()` method, we can unpack that array into two individual variables (which above are called `user` and `created`.)

In Sequelize version 5, which was released in March 2019, the library has better support for JavaScript promises. As a result, they are telling us a new way to use the promise for this function:

```js
db.user.findOrCreate({
  where: {
    firstName: 'Brian',
    lastName: 'Smith'
  },
  defaults: { age: 88 }
}).then(function([user, created]) {
  console.log(user); // returns info about the user
});
```

The difference here is that we are no longer using the odd `.spread()` method. Instead, we are using the standard `.then()` promise function. And inside that promise callback function, we wrap our two variables in a literal array. This will achieve the same effect of providing both the data and the boolean to your promise handler function. This will probably be the preferred way of doing this in future versions of Sequelize since the `.spread()` function is actually a feature of another node module called Bluebird. If Sequelize can move away from requiring a 3rd party library, they probably will want to do that so favor the `.then()` way of using it moving forward.

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
db.user.update({
  lastName: 'Taco'
}, {
  where: {
    firstName: 'Brian'
  }
}).then(function(user) {
  // do something when done updating
});
```

### Delete (destroy)

```js
db.user.destroy({
  where: { firstName: 'Brian' }
}).then(function() {
  // do something when done deleting
});
```

## Promises
After a sequelize statement, we can interact with the return of that object using `.then` and in `findOrCreate` we can use `.spread`.

Finding a user

```js
db.user.findOne({where: {id: 1}});
```

This will execute a statement to find a user, but it will not let us interact with it. Because of the asynchronous nature of a call, we need to use a Promise (a type of callback) to get that data.

```js
db.user.findByPk(1).then(function(foundUser) {
  console.log(foundUser);
  //res.send("myTemplate", {user: foundUser);
});
```

In a `findOrCreate`, a callback will return back an array, instead of a single object. There is a type of callback called `.spread` which will allow us to break apart that array and use similar to a traditional callback.

```js
db.user.findOrCreate({
  where: { firstName: 'Brian' }
}).spread(function(user, created) {
  console.log(user); // returns info about the user
});
```

But as mentioned above, it looks like this syntax will be replaced with more standard promise syntax moving forward. THis would be the new way to use the `findOrCreate` promise:

```js
db.user.findOrCreate({
  where: { firstName: 'Brian' }
}).then(function([user, created]) {
  console.log(user); // returns info about the user
});
```

## Sequelize Promises

The main callback handlers to be used are as follows.

* `.then` - default promise called when a query is completed.
* `.spread` - used to spread an array of values to parameters. This is only used for `findOrCreate`.
* `.catch` - triggered if something goes wrong (an error).
* `.finally` - triggered after all other callbacks. Can be used for cleanup.

The important thing to remember is that all queries take time and are asynchronous, so you MUST use promises to execute code that needs to happen after the query is completed. You will usually use `then`, except possibly for `findOrCreate` (but only if you need to support old versions.)

