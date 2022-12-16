# Setup

## Setup part 1 - getting the sequelize-cli tool \(you only have to do this once\)

We need to install a generator so we can use sequelize. Much like our other terminal apps, we will only install this once.

```text
npm install -g sequelize-cli
```

## Setup part 2 - starting a new node project

Let's build our first app using Sequelize! First we need to create a node app and include our dependencies. **All in terminal**:

**Create a new folder and add an index.js and .gitignore and initialize the repository**

```text
mkdir userapp
cd userapp
npm init -y
touch index.js
echo "node_modules" >> .gitignore
```

**Add/save dependencies \(sequelize needs pg for Postgres\)**

```text
npm install pg sequelize
```

**Initialize a sequelize project**

```text
sequelize init
```

## Setup part 3 - config.json, models and migrations:

In the text editor we should now see a bunch of new folders. We now have config, migrations and models. This was created for us when we ran `sequelize init`.

Let's start in the config folder and open up the config.json file. This file contains information about the database we are using as well as how to connect.

We have three settings, one for development \(what we will use now\), test \(for testing our code\), and production \(when we deploy our app on AWS/Heroku\).

Let's change the config.json so it looks like this.

**config/config.json**

```javascript
{
  "development": {
    "database": "userapp_development",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "test": {
    "database": "userapp_test",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "production": {
    "database": "userapp_production",
    "host": "127.0.0.1",
    "dialect": "postgres"
  }
}
```

* If the dialects defaults to mySql, change them to postgres
* change the database names
* if you have a username and password for your Postgres server, you must include those as well


When we deploy to Heroku, they will provide us a long url that contains password and login that will be secure when deployed. More on this later.

#### A note for Linux and WSL users

Since you need to provide a username and password in your `config.json`, the easiest way to configure this to work quickly and easily is to make a special sequelize user. Run the following commands in your `psql` shell:

```sql
CREATE USER sequelize WITH SUPERUSER PASSWORD 'sequelize';
ALTER USER sequelize WITH SUPERUSER;
```
Now your `config.json` should look like this:

```json
{
  "development": {
    "username": "sequelize",
    "password": "sequelize",
    "database": "database_development",
    "host": "127.0.0.1",
    "dialect": "postgres"
  }
}
```

#### Create a database inside of Postgres

Once your config.json has been populated with a `"database"` key, you can use the command 

```bash
sequelize db:create
``` 
and sequelize will check the `"database"`key definded the `config.json` and make the appropriate database. 

It is also possible to create the database using a `createdb` command in `zsh` or a `CREATE DATABASE` command in `psql`, but make sure the name lines up with your `config.json`.

Once this is complete, let's shift our attention to "models".

### Create a model and a matching migration

In order to create a model, we start with `sequelize model:create` and then specify the name of the model using the `--name` flag. Make sure your models are **always** singular \(table name in plural, model name in singular\). See the Table Name Inference section of [these docs](https://sequelize.org/master/manual/model-basics.html#:~:text=Models%20are%20the%20essence%20of,and%20their%20data%20types) for more. After passing in the `--name` flag followed by the name of your model, you can then add an `--attributes` flag and pass in data about your model. Generating the model also generates a corresponding migration. You only need to do this once for your model.

```bash
sequelize model:create --name user --attributes firstName:string,lastName:string,age:integer,email:string
```

> Make sure you do **not** have any spaces between each of the attributes and their data types. Convention matters!

This will generate the following model:

**models/user.js**

```javascript
'use strict';
const {
  Model
} = require('sequelize');
module.exports = (sequelize, DataTypes) => {
  class user extends Model {
    /**
     * Helper method for defining associations.
     * This method is not a part of Sequelize lifecycle.
     * The `models/index` file will call this method automatically.
     */
    static associate(models) {
      // define association here
    }
  };
  user.init({
    firstName: DataTypes.STRING,
    lastName: DataTypes.STRING,
    age: DataTypes.INTEGER,
    email: DataTypes.STRING
  }, {
    sequelize,
    modelName: 'user',
  });
  return user;
};
```

If you want to make changes to your model after generating it - all you have to do is make a change in this file and save it **before** running the migrate command.

And a corresponding migration:

**migrations/\*-create-user.js**

```javascript
'use strict';
module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.createTable('users', {
      id: {
        allowNull: false,
        autoIncrement: true,
        primaryKey: true,
        type: Sequelize.INTEGER
      },
      firstName: {
        type: Sequelize.STRING
      },
      lastName: {
        type: Sequelize.STRING
      },
      age: {
        type: Sequelize.INTEGER
      },
      email: {
        type: Sequelize.STRING
      },
      createdAt: {
        allowNull: false,
        type: Sequelize.DATE
      },
      updatedAt: {
        allowNull: false,
        type: Sequelize.DATE
      }
    });
  },
  down: async (queryInterface, Sequelize) => {
    await queryInterface.dropTable('users');
  }
};
```

## What is this "associate" thing in my model?

In this function, we specify any relations/associations \(one to one, one to many or many to many\) between our models \(hasMany or belongsTo\). We'll discuss this more, but always remember, the association goes in the model and the foreign keys go in the migration.

## Running the migration

To run the migration, use the following command.

```text
sequelize db:migrate
```

If you need to undo the last migration, this command will undo the last migration that was applied to the database.

```text
sequelize db:migrate:undo
```

Use the `psql` shell to verify that your database and table was created:

```bash
psql
\l
\c userapp_development
\dt
```

