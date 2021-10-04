# Create the User

We'll need to...

1. Install an additional dependency: `bcrypt`
2. Create the user model
3. Validate the user's name, email, and password
4. Hash the user's password before saving it to the database
5. Create methods to validate passwords and protect the password data

## Installing bcrypt

In order to hash passwords, we'll need to install `bcrypt`.

```text
npm i bcrypt
```

## Creating the user model

We can create a user model using the Sequelize CLI. Let's create a user with a name, email, and password. You can add more attributes later if you'd like.

```text
sequelize model:create --name user --attributes email:string,name:string,password:string

sequelize db:migrate
```

> This should pass the following test
>
> **Creating a User - should create successfully**

## Validate the user's name, email, and password

Now that we have a user, we want to limit the values we can assign to a user's name, email, and password. Here are some examples.

* User's email should be a valid address
* User's name should be between 1-99 characters
* User's password should be between 8-99 characters

In order to do this, we can use Sequelize validations. Note that by adding a `msg` within each validation, we'll be able to give a user-friendly message if a validation fails. This will be handled in our routes later.

[Sequelize Validation Documentation](https://sequelize.org/v5/manual/models-definition.html)

**models/user.js**

```javascript
{
  email: {
    type: DataTypes.STRING,
    validate: {
      isEmail: {
        msg: 'Invalid email address'
      }
    }
  },
  name: {
    type: DataTypes.STRING,
    validate: {
      len: {
        args: [1, 99],
        msg: 'Name must be between 1 and 99 characters'
      }
    }
  },
  password: {
    type: DataTypes.STRING,
    validate: {
      len: {
        args: [8, 99],
        msg: 'Password must be between 8 and 99 characters'
      }
    }
  }
}
```

> This should pass the following tests
>
> **Creating a User - should throw an error on invalid email addresses**
>
> **Creating a User - should throw an error on invalid name**
>
> **Creating a User - should throw an error on invalid password**

## Hash the user's password before saving

Currently, we're saving user passwords as plain text. This is bad! Very bad!

* If someone gained access to our database, they would have a collection of emails and passwords. Since most people use the same password across different accounts, this can have drastic identity and legal consequences.
* _We the developers_ shouldn't be able to see our users' passwords, for the same reasons above.

Therefore, we need to hash the password before it ever reaches the database. We can use a `beforeCreate` hook to do this automatically on every model's creation.

**models/user.js**

```javascript
// at the very top, require bcrypt
const bcrypt = require('bcrypt');

module.exports = (sequelize, DataTypes) => {
  const user = sequelize.define('user', {
    // ...
  }, {
    hooks: {
      beforeCreate: (pendingUser, options) => {
        if (pendingUser && pendingUser.password) {
          // hash the password
          let hash = bcrypt.hashSync(pendingUser.password, 12);
          // store the hash as the user's password
          pendingUser.password = hash;
        }
      }
    }
  });
  user.associate = function(models) {
    // associations can be defined here
  };

  return user;
};
```

> This should pass the following test
>
> **Creating a User - should hash the password before save**

## Validating and Protecting the Password

Now that user passwords are hashed, we need to solve the last two problems with the user model.

* Comparing a password a user inputs to the user's hash in the database.
* Keeping the hash hidden

In order to perform these actions, we'll create two methods that can be called on user objects.

* To validate the password, we'll create an instance method called `validPassword` to accept a password as a parameter, then compare the password to the hash.
  * **Example**

    ```javascript
    user.validPassword('password'); // return true or false
    ```
* To hide the hash from the user object, we'll _override_ an instance method called `toJSON`, which will leave the hash out of the user's JSON object.
  * **Example**

    ```javascript
    user.toJSON(); // returns { name: 'Tosspot', email: 'gavin.scotsman@ga.co' }
    ```

**models/user.js**

```javascript
  // ...

  user.associate = function(models) {
    // associations can be defined here
  };

  // Compares entered password to hashed password
  user.prototype.validPassword = function(passwordTyped) {
    return bcrypt.compareSync(passwordTyped, this.password);
  };

  // remove the password before serializing
  user.prototype.toJSON = function() {
    let userData = this.get();
    delete userData.password;
    return userData;
  }

  return user;
}
```

> This should pass the following tests
>
> **User instance methods - validPassword - should validate a correct password**
>
> **User instance methods - validPassword - should invalidate an invalid password**
>
> **User instance methods - toJSON - should return a user without a password field**

## User Finished

Congrats, your user should be finished! Verify by running the user tests only. All tests should pass.

```text
NODE_ENV=test node_modules/mocha/bin/mocha test/user.test.js
```

