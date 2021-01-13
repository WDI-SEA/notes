# Using Models

Just like using express and the other modules, your models must be required in order to access them in your app.
Let's start in our index.js and add the following code:

```javascript
const db = require('./models')
```

## CRUD with Sequelize \(Using our User model\)

### Create

```javascript
db.user.create({
    firstName: 'Taylor',
    lastName: 'Darneille',
    age: 27
}).then(createdUser=>{
    // the create promise returns the
    // new row of data that has been created
    // (otherwise it throws an error)
    console.log(createdUser)
    // terminates the node process at this point so that we don't have to force-quit
    process.exit()
})
```

### Read One

```javascript
db.user.findOne({
    where: {firstName: 'Taylor'}
}).then(foundUser=>{
    console.log(foundUser)
    process.exit()
})
```

What happens if you include a `where` clause that doesn't match any rows of data? Try it!

### Find or Create

The method findOrCreate can be used to check if a certain element is already existing in the database. If that is the case the method will result in a respective instance. If the element does not yet exist, it will be created with the provided attributes \(a combination of `where` and `defaults`\)

```javascript
db.user.findOrCreate({
  where: {
    firstName: 'Brian',
    lastName: 'Smith'
  },
  defaults: { age: 88 }
}).then(([user, wasCreated])=>{
  console.log(user); // returns info about the user
  process.exit()
});
```
Find out what "wasCreated" returns! What data type is this?

### Find All

findAll returns more than one instance, which is useful if you need more than one record. find only returns one record.

```javascript
db.user.findAll().then(users=>{
  console.log(users);
  // users will be an array of all User instances
});
```

### Update

```javascript
db.user.update({
    lastName: 'Taco'
  }, {
    where: {
      firstName: 'Brian'
    }
}).then(numRowsChanged=>{
    // Returns a value of how many rows were altered by this update
    console.log(numRowsChanged)
    process.exit()
});
```

See [this stack overflow](https://stackoverflow.com/questions/38524938/sequelize-update-record-and-return-result) for more on what the promise returns.

### Delete \(destroy\)

```javascript
  db.user.destroy({
    where: { firstName: 'Brian' }
  }).then(numRowsDeleted=>{
      console.log(numRowsDeleted)
    // do something when done deleting
      process.exit()
  });
```

## Promises

After a sequelize statement, we can interact with the return of that object using `.then`.

Finding a user

```javascript
db.user.findOne({where: {id: 4}})
.then(foundUser=>{
    console.log(foundUser)
})
```

```javascript
db.user.findByPk(1).then(foundUser)=>{
  console.log(foundUser);
  //res.send("myTemplate", {user: foundUser);
});
```

In a `findOrCreate`, a callback will return back an array, instead of a single object. The array parameter syntax shown below is the sequelize 5 syntax that mimics the old `.spread()` operator

```javascript
db.user.findOrCreate({
  where: { firstName: 'Brian' }
}).then(([user, created]) => {
  console.log(user); // returns info about the user
});
```

## Sequelize Promises

The main callback handlers to be used are as follows.

* `.then` - default promise called when a query is completed.
* `.catch` - triggered if something goes wrong \(an error\).
* `.finally` - triggered after all other callbacks. Can be used for cleanup.

The important thing to remember is that all queries take time and are asynchronous, so you MUST use promises to execute code that needs to happen after the query is completed.
