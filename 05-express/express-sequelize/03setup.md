##Setup

### Setup part 1 - getting the sequelize-cli tool (you only have to do this once)

We need install a generator so we can use sequelize. Much like our other terminal apps, we will only install this once.

```
npm install -g sequelize-cli
```


### Setup part 2 - starting a new node project

Let's build our first app using Sequelize! First we need to create a node app and include our dependencies. **All in terminal**:

Create a new folder and add an index.js and .gitignore and initialize the repository

```
mkdir userapp
cd userapp
npm init
touch index.js
echo "node_modules" >> .gitignore
```

Add/save dependencies (sequelize needs pg for Postgres and pg-hstore for JSON serialization)

```
npm install --save express ejs body-parser pg pg-hstore sequelize
```

Create a database and initialize a sequelize project

```
createdb userapp
sequelize init
```

### Setup part 3 - config.json, models and migrations:

In sublime we should now see a bunch of new folders. We now have config, migrations and models. This was created for us when we ran `sequelize init`.

Let's start in the config folder and open up the config.json file. This file contains information about the database we are using as well as how to connect.

We have three settings, one for development (what we will use now), test (for testing our code), and production (when we deploy our app on AWS/Heroku).

Let's change the config.json so it looks like this.

**config/config.json**

```js
{
  "development": {
    "database": "userapp",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "test": {
    "database": "userapp",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "production": {
    "database": "userapp",
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
