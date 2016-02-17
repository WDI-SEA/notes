#Password hashing

Install bcrypt and add the following `beforeCreate` hook.

```
npm install --save bcrypt
```

In **models/user.js**

```js
'use strict';

var bcrypt = require('bcrypt');

module.exports = function(sequelize, DataTypes) {
  var user = sequelize.define('user', {
    email: DataTypes.STRING,
    name: DataTypes.STRING,
    password: DataTypes.STRING
  }, {
    classMethods: {
      associate: function(models) {
        // associations can be defined here
      }
    },
    hooks: {
      beforeCreate: function(user, options, callback) {
        if (user.password) {
          bcrypt.hash(user.password, 10, function(err, hash) {
            if (err) return callback(err);
            user.password = hash;
            callback(null, user);
          });
        } else {
          callback(null, user);
        }
      }
    }
  });
  return user;
};
```

Note that the `beforeCreate` hook is being passed `callback`, which is a function. The function is expecting the first argument to be the error (if any) and the second argument to be the user we're passing back to Sequelize. In order to hash the password, we use bcrypt. Then, we assign the hash value to the user's password.

**TRY TESTING THIS** before continuing. Also, let's add a validation so passwords must be more than 8 characters long. This should now send an error for short passwords (since we're sending out the error message in the `catch` promise on this route).

```js
//...
password: {
  type: DataTypes.STRING,
  validate: {
    len: [8, 99]
  }
}
//...
```
