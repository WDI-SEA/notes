# Getting started with Sequelize

##Objectives
* Identify an ORM
* Weigh pros and cons between ORMs and raw SQL queries
* Use the Sequelize CLI to create and migrate models
* Utilize Sequelize to create, find, and delete database records
* Comprehend the purpose of promises and their use in Sequelize

## Key terms + definitions

#### ORM

An ORM (Object Relational Mapper) is a piece/layer of software that helps map objects to our database. This means we can just use JavaScript to create and work with our data instead of writing raw SQL queries.

You can read some more about the benefits of using an ORM [here](http://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it)

**Exercise:** What are 3 pros of an ORM? What are 3 cons?

#### Sequelize

From the Sequelize docs "To put it in a nutshell, it's an ORM (Object-Relational-Mapper). The library is written entirely in JavaScript and can be used in the Node.JS environment." In other words, Sequelize is an ORM that works with relational databases and Node.js. It allows us to do many things including:

- Represent models and their data.
- Represent associations between these models.
- Validate data before they gets persisted to the database.
- Perform database operations in an object-oriented fashion.

#### Model

A model is a class that maps to the data relation (table) and potentially bridges tables. You can think of a model as the blueprint for what each row of data is going to contain. Unlike a migration, you perform CRUD on instances of your models.

#### Migration

Migrations (also known as 'schema evolution' or 'mutations') are a way of changing your database schema from one version into another. You can think of a migration as the creation or changes you want to make to a database table or column. Before you can start manipulating your models, you need to create and run a migration. Examples of migrations are creating, deleting and altering tables (and their existing columns).

##Setup

### Setup part 1 - getting the sequelize-cli tool (you only have to do this once)

We need install a generator so we can use sequelize. Much like our other terminal apps, we will only install this once.

`npm install -g sequelize-cli`


### Setup part 2 - starting a new node project

Let's build our first app using Sequelize! First we need to create a node app and include our dependencies. **All in terminal**:

Create a new folder and add an index.js and .gitignore and initialize the repository

```
mkdir sequelize_app
cd sequelize_app
npm init
touch index.js
touch .gitignore
```

Add the node_modules folder to our .gitignore

```
echo "node_modules" >> .gitignore
```

Add/save dependencies (sequelize needs pg for Postgres and pg-hstore for JSON serialization)

```
npm install --save express ejs body-parser pg pg-hstore sequelize
```

Create a database and initialize a sequelize project
```
createdb sequelize_app
sequelize init
```

### Setup part 3 - config.json, models and migrations:

In sublime we should now see a bunch of new folders. We now have config, migrations and models. This was created for us when we ran `sequelize init`.

Let's start in the config folder and open up the config.json file. This file contains information about the database we are using as well as how to connect.

We have three settings, one for development (what we will use now), test (for testing our code), and production (when we deploy our app on AWS/Heroku).

Let's change the config.json so it looks like this (we will not be using the test or production environments, so just ignore those for now).

**config/config.json**
```js
{
  "development": {
    "database": "sequelize_app",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "test": {
    "database": "sequelize_app",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "production": {
    "database": "database_production",
    "host": "127.0.0.1",
    "dialect": "postgres"
  }
}
```

The only thing we are actually changing for database setup, is the **database name**. If you have a username and password for your Postgres server, you'd include those as well.

When we deploy to Heroku, they will provide us a long url that contains password and login that will be secure when deployed. More on this later.

Once this is complete, let's move to the models folder.

## Creating a model and a matching migration

In order to create a model, we start with `sequelize model:create` and then specify the name of the model using the `--name` flag. Make sure your models are **always** singular (table name in plural, model name in singular). After passing in the `--name` flag followed by the name of your model, you can then add an `--attributes` flag and pass in data about your model. Generating the model also generates a corresponding migration. You only need to do this once for your model.

```bash
sequelize model:create --name user --attributes firstName:string,lastName:string,age:integer,email:string
```

If you want to make changes to your model after generating it - all you have to do is make a change and save it before running the migrate command.

> Make sure you do **not** have any spaces between each of the attributes and their data types. Convention matters!


This will generate the following migration

**migrations/*-create-user.js**
```js
"use strict";
module.exports = {
  up: function(migration, DataTypes, done) {
    migration.createTable("users", {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: DataTypes.INTEGER
      },
      firstName: {
        type: DataTypes.STRING
      },
      lastName: {
        type: DataTypes.STRING
      },
      age: {
        type: DataTypes.INTEGER
      },
      email: {
        type: DataTypes.STRING
      },
      createdAt: {
        allowNull: false,
        type: DataTypes.DATE
      },
      updatedAt: {
        allowNull: false,
        type: DataTypes.DATE
      }
    }).done(done);
  },
  down: function(migration, DataTypes, done) {
    migration.dropTable("Users").done(done);
  }
};
```

And a corresponding model:

**models/user.js**
```js
"use strict";

module.exports = function(sequelize, DataTypes) {
  var user = sequelize.define("user", {
    firstName: DataTypes.STRING,
    lastName: DataTypes.STRING,
    age: DataTypes.INTEGER,
    email: DataTypes.STRING
  }, {
    classMethods: {
      associate: function(models) {
        // associations can be defined here
      }
    }
  });

  return user;
};
```

## What is this "associate" thing in my model?

In this function, we specify any relations/associations (one to one, one to many or many to many) between our models (hasMany or belongsTo). We'll discuss this more in class, but always remember, the association goes in the model and the foreign keys go in the migration.

## Validations

Sequelize has a bunch of validations we can add to our models to ensure that our data has met certain criteria before add it to our database. To include validations in your model, wrap them in a validate object. An examples of this is validating an email address (making sure it has a @ etc. as well as ensuring that it is never null):

Read more about diffrent types of validations
http://docs.sequelizejs.com/en/latest/docs/models/#model-validations

**models/user.js**
```js
module.exports = function(sequelize, DataTypes) {
  var user = sequelize.define("user", {

    email: {
      type: DataTypes.STRING,
      validate: {
        isEmail: true
       }
    },
  },

    {
    classMethods: {
      associate: function(models) {
        // associations can be defined here
      }
    }
  });

  return user;
};
```

## Migrations

`sequelize migration:create --name migrationNameGoesHere`

This command creates a migration file, which is empty by default. Similar to Rails, you must specify the type of migration for both `up` and `down` methods.
The `up` method is the migration you want to run, while the `down` method is the reverse.

For example, if I add a column in `up`, I would also want to remove that same column in `down`.

[Migration Functions: http://docs.sequelizejs.com/en/latest/docs/migrations/#functions](http://docs.sequelizejs.com/en/latest/docs/migrations/#functions)

## Running a migration

Whenever we generate a migration, we have to run the migration to execute the `up` method (which we have in our migration - when we undo a migration we run the down method).
To run the `up` method, run in terminal `sequelize db:migrate`. For the `down` method, run `sequelize db:migrate:undo`.

NOTE: When creating your own migrations, you should specify actions for both `up` and `down` methods. Otherwise, running the down method will not revert your migration.

[Migration Documentation](http://docs.sequelizejs.com/en/latest/docs/migrations/#functions)

## Using your Models inside an app

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


## Useful Sequelize Documentation Links
* Models
  * [Data types](http://docs.sequelizejs.com/en/latest/docs/models-definition/#data-types)
  * [Validations](http://docs.sequelizejs.com/en/latest/docs/models-definition/#validations)
* Querying
  * [Query usage (comparable to SELECT, INSERT, COUNT, MAX, etc.)](http://docs.sequelizejs.com/en/latest/docs/models-usage/)
  * [Destroying records (comparable to DELETE)](http://docs.sequelizejs.com/en/latest/docs/instances/#destroying-deleting-persistent-instances)
  * [Attribute selection](http://docs.sequelizejs.com/en/latest/docs/querying/#attributes)
  * [Querying Basics and Operators (comparable to AND/OR/LIKE/IN)](http://docs.sequelizejs.com/en/latest/docs/querying/#basics)
  * [Pagination and Limiting (comparable to OFFSET, LIMIT)](http://docs.sequelizejs.com/en/latest/docs/querying/#pagination-limiting)
  * [Ordering (comparable to ORDER BY)](http://docs.sequelizejs.com/en/latest/docs/querying/#ordering)
* Configuration and Commands
  * [Sequelize CLI and Migrations](http://docs.sequelizejs.com/en/latest/docs/migrations/#the-cli)
