# Using Models 

*Updated for ECMAScript 2017 async/await and Sequelize 6*

Just like using express and the other modules, your models must be required in order to access them in your app.
Let's start in our index.js and add the following code:

```javascript
const db = require('./models')
```

## Sequelize Promises

Database operations can take a little bit of time, so they return *thenable promises* that resolve when the transaction is complete. It is possible to use `.then()` syntax with *callbacks* **OR** `async/await` where you `await` queries in `async functions`. The [sequelize 6 api docs](https://sequelize.org/master/index.html) use `async/await`.

### `.then()` syntax:

* `.then` - default promise called when a query is completed.
* `.catch` - triggered if something goes wrong \(an error\).
* `.finally` - triggered after all other callbacks. Can be used for cleanup.

```javascript
// using .thens and callbacks to find a user by primary key (id)
db.user.findByPk(1)
  .then(foundUser)=>{
    console.log(foundUser);
  })
  .catch(error => console.log('I only happen when there is an error!', error))
  .finally(() => console.log('I always happend no matter what!'))
```

### `async/await` syntax:

* `await` can only be used inside of an `async function`.
* `try/catch` blocks are used to handle errors.
* `finally` blocks can also be used for cleanup

```javascript
// using async/await to find a user by primary key (id)
async function findUserById() {
  try {
    const foundUser = await db.user.findByPk(1)
    console.log(founduser)
  } catch (error) {
    console.log('I only happen when there is an error!', error)
  } finally {
    console.log('I always happend no matter what!')
  }
}
```

The important thing to remember is that all queries take time and are asynchronous, so you MUST use promises to execute code that needs to happen after the query is completed.

## CRUD with Sequelize \(Using our User model\)

### Create

To create a single row in a table, the `create()` method can be used:

Simple insert query docs can be found [here](https://sequelize.org/master/manual/model-querying-basics.html#simple-insert-queries)

```javascript
async function createUser() {
  try {
    // the create promise returns the
    // new row of data that has been created
    // (otherwise it throws an error)
    const newUser = await db.user.create({
        firstName: 'Taylor',
        lastName: 'Darneille',
        age: 27
    })
    console.log(newUser)
  } catch (err) {
    console.log(err)
  }
}

createUser()
```

### Read

`findAll()` returns more than one instance, which is useful if you need more than one record. 

FindAll query docs can be found [here](https://sequelize.org/master/manual/model-querying-basics.html#simple-select-queries)

```javascript
async function readAllUsers() {
  try {
    const allUsers = await db.user.findAll()
    console.log(allUsers);
  } catch (error) {
    console.log(error)
  }
}

readAllUsers()
```

By supplying a `WHERE` clause as a *query options* object, you can narrow the results:

```javascript
async function findSpecificUser() {
  try {
    const allUsers = await db.user.findAll({
      where: {
        firstName: 'Taylor'
      }
    })
    console.log(allUsers);
  } catch (error) {
    console.log(error)
  }
}

findSpecificUser()
```

What happens if you include a `where` clause that doesn't match any rows of data? Try it!

### Update

To update a row you can use `update()`. It takes two objects as arguments: what to update and the regular options object.

Simple Update query docs can be found [here](https://sequelize.org/master/manual/model-querying-basics.html#simple-update-queries)

```javascript
async function updateUser(){
  try {
    // Returns a value of how many rows were altered by this update
    const numRowsChanged = await db.user.update({ lastName: 'Taco' }, {
      where: {
        firstName: 'Brian'
      }
    })
    console.log(numRowsChanged)
  } catch(error) {
    console.log(error)
  }
}

updateUser()
```

See [this stack overflow](https://stackoverflow.com/questions/38524938/sequelize-update-record-and-return-result) for more on what the promise returns.

### Delete \(destroy\)

The `destroy()` method works like a `find()` but returns the number of rows deleted.

Simple destroy query docs can be found [here](https://sequelize.org/master/manual/model-querying-basics.html#simple-delete-queries)

```javascript
async function destroyUser() {
  try {
    const numRowsDeleted = await db.user.destroy({
      where: { 
        firstName: 'Brian' 
      }
    })
    console.log(numRowsDeleted)
  } catch (error) {
    console.log(error)
  }
}

destroyUser()
```

## Sequalize Finder Methods

Sequelize has some useful *finder* methods that rely on combining SQL `SELECT` queries with common useful tasks. We have already seen the `findAll()` and `findByPk()` finders.

Finder query docs can be found [here](https://sequelize.org/master/manual/model-querying-finders.html#-code-findone--code-)


### Find or Create

In a `findOrCreate`, the promise returns back an array, instead of a single object. The syntax shown in called *array destructuring*. You can read more about it [here at MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

The method findOrCreate can be used to check if a certain element is already existing in the database. If that is the case the method will result in a respective instance. If the element does not yet exist, it will be created with the provided attributes \(a combination of `where` and `defaults`\)

Find or create query docs can be found [here](https://sequelize.org/master/manual/model-querying-finders.html#-code-findorcreate--code-)

```javascript
async function findOrCreateUser(){
  try {
    // the findOrCreate promise returns an array with two elements,
    // so 'array destructuring' is used to assign the names to the elements
    const [user, created] = await db.user.findOrCreate({
      // where is used search for values in columns
      where: {
        firstName: 'Brian',
        lastName: 'Smith'
      },
      // defaults will be used to fill columns not 
      // in the where clause in the case of a create
      defaults: { age: 88 }
    })
    // sick ternery operator! 
    console.log(`${user.firstName} was ${created ? 'created' : 'found'}`)
  } catch (error) {
    console.log(error)
  }
}

findOrCreateUser()
```

Find out what "created" returns! What data type is this?

### Find One

To read a single row, the `findOne()` method can be used

```javascript
async function readOneUser(){
  try {
    // the findOne promise returns the first found row
    const foundUser = await db.user.findOne({
      where: {firstName: 'Taylor'}
    })
    console.log(foundUser)
    
  } catch (err) {
    console.log(err)
  }
}

readOneUser()
```

## Query Operators

Query Operators such as SQL's `LIKE` and number comparisons can be used in query options with sequelize's operators.

Sequelize docs on operators can be found [here](https://sequelize.org/master/manual/model-querying-basics.html#operators)

The first step is to require sequelize at the top of your file:

```javascript
const db = require('./models')
// using 'object destructuring assignment'
const { Op } = require("sequelize") // add me to the top with your models require!
```

When you specify an attribute in a the where options, you substitute a hardcoded value with an operator.

Using an `[Op.gt]` (greater than) operator in a findAll's options:

```javascript
async function findOldUsers() {
  try {
    // when options get verbose, you can create them in a separate object!
    const options = {
      where: {
        age: {
          [Op.gt]: 25
        }
      }
    }
    const allUsers = await db.user.findAll(options)
    console.log(allUsers);
  } catch (error) {
    console.log(error)
  }
}

findOldUsers()
```

Using `[Op.Like]` with the SQL `%` wildcard to search by a user's firstName:

```javascript
async function findUserLike() {
  try {
    // when options get verbose, you can create them in a separate object!
    const options = {
      where: {
        firstName: {
          [Op.like]: 'Tay%'
        }
      }
    }
    const allUsers = await db.user.findAll(options)
    console.log(allUsers);
  } catch (error) {
    console.log(error)
  }
}

findUserLike()
```

## Oh Sequlize, You Thought of Everything

There are many, many other useful methods that sequelize provides to explore in the docs: 

[Limiting Results](https://sequelize.org/master/manual/model-querying-basics.html#limits-and-pagination) with a `limit` key in the query options

[Ordering and Grouping Results](https://sequelize.org/master/manual/model-querying-basics.html#ordering) Ordering requires an `order` key in the query options that can take an array for the value, grouping is a simple key value pair `group: 'column'`.

[Utility Methods](https://sequelize.org/master/manual/model-querying-basics.html#utility-methods) such as `count` and `max` 

[Bulk create](https://sequelize.org/master/manual/model-querying-basics.html#creating-in-bulk) with an array of objects, similar seeding databases. Less good for standard usage however because `bulkCreate()` doesn't run validations the way `create()` does unless you configure it to.

[Postgres](https://sequelize.org/master/manual/model-querying-basics.html#postgres-only-range-operators) has some neat and exclusive operators.

Oh Snap! You can make [raw SQL queries](https://sequelize.org/master/manual/raw-queries.html) too!

Consider the following SQL query:

```sql
SELECT * FROM users WHERE age > 5 ORDER BY age DESC LIMIT 3;
```

This is the sequelize version:

```javascript
async function complexQuery(){
  try{
    /**
    * find users where age is greater than 5
    * order by age
    * limit 3 results
    */
    const options = {
      where: {
        age: {
          [Op.gt]: 5
        }
      },
      order: [
        ['age', 'DESC'],
      ],
      limit: 3,
    }
    const users = await db.user.findAll(options)
    users.forEach(user => {
      console.log(user.firstName)
    })
  } catch (error) {
    console.log(error)
  }
}

complexQuery()
```