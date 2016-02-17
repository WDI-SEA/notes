#Creating the User

We'll need to...

1. Install sequelize, along with the postgres adapters
2. Initialize sequelize in our app
3. Modify the `config.json` file to the correct settings
4. Create the database
5. Create the user model
6. Check the user model and migration
7. Run migration

####In code

```
npm install --save sequelize pg pg-hstore

sequelize init
```

```
sequelize model:create --name user --attributes email:string,name:string,password:string

sequelize db:migrate
```

###Testing the User

Create a test file and ensure you can create and find users.


###Add functionality to the signup POST route

We'll need to create a new user with a **unique** email address, that hashes the password appropriately. To do so, we will...

1. Modify the `POST /auth/signup` route so a new user is created
  * We'll verify this works before adding password hashing
  * We need to make sure the user doesn't already exist via the email address
2. Install bcrypt for password hashing
  * Incorporate bcrypt into a `beforeCreate` hook.
  * Test that bcrypt works
3. Add additional validations as necessary

####In code

**controllers/auth.js**

```js
// import models at the top
var db = require('../models');

// alter the POST signup route
router.post('/signup', function(req, res) {
  db.user.findOrCreate({
    where: {
      email: req.body.email
    },
    defaults: {
      name: req.body.name,
      password: req.body.password
    }
  }).spread(function(user, created) {
    res.redirect('/');
  }).catch(function(err) {
    res.send(err);
  });
});
```

**TRY TESTING THIS** before continuing. And don't use an actual password, because it's not hashed!
