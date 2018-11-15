# Login User with Passport

We'll need to...

1. Install dependencies, `passport` and `passport-local`
2. Configure Passport to use our user model
3. Initialize Passport to use our session module
4. Add login and logout functionality to the `auth` controller

## Install passport and passport-local

We'll use Passport in order to provide login functionality, and `passport-local` in order to provide local user authentication.

```
npm install --save passport passport-local
```

## Configure Passport to use our user model

Create the Passport configuration inside of the config folder.

**config/ppConfig.js**

```js
var passport = require('passport');
var LocalStrategy = require('passport-local').Strategy;
var db = require('../models');

/*
 * Passport "serializes" objects to make them easy to store, converting the
 * user to an identifier (id)
 */
passport.serializeUser(function(user, cb) {
  cb(null, user.id);
});

/*
 * Passport "deserializes" objects by taking the user's serialization (id)
 * and looking it up in the database
 */
passport.deserializeUser(function(id, cb) {
  db.user.findById(id).then(function(user) {
    cb(null, user);
  }).catch(cb);
});

/*
 * This is Passport's strategy to provide local authentication. We provide the
 * following information to the LocalStrategy:
 *
 * Configuration: An object of data to identify our authentication fields, the
 * username and password
 *
 * Callback function: A function that's called to log the user in. We can pass
 * the email and password to a database query, and return the appropriate
 * information in the callback. Think of "cb" as a function that'll later look
 * like this:
 *
 * login(error, user) {
 *   // do stuff
 * }
 *
 * We need to provide the error as the first argument, and the user as the
 * second argument. We can provide "null" if there's no error, or "false" if
 * there's no user.
 */
passport.use(new LocalStrategy({
  usernameField: 'email',
  passwordField: 'password'
}, function(email, password, cb) {
  db.user.find({
    where: { email: email }
  }).then(function(user) {
    if (!user || !user.validPassword(password)) {
      cb(null, false);
    } else {
      cb(null, user);
    }
  }).catch(cb);
}));

// export the Passport configuration from this module
module.exports = passport;
```

## Initialize Passport to use our session module

Now that we've created the configuration, we need to make our app *aware of its existence*. This can be done by requiring the configuration and including it as middleware.

**index.js**

```js
// require the configuration at the top of the file
var passport = require('./config/ppConfig');

// initialize the passport configuration and session as middleware
app.use(passport.initialize());
app.use(passport.session());
```

**IMPORTANT NOTE:** You must include the passport configuration **below your session configuration.** This ensures that Passport is aware that the session module exists. 

## Add login and logout functionality

> Before continuing, verify that this test is passing
> 
> **Auth Controller - GET /auth/login - should return a 200 response**

#### Login

Luckily, all of that configuration and middleware means a straightforward login route. Let's go ahead and add the POST route for login.

**controllers/auth.js**

```js
// require the passport configuration at the top of the file
var passport = require('../config/ppConfig');

router.post('/login', passport.authenticate('local', {
  successRedirect: '/',
  failureRedirect: '/auth/login'
}));
```

> This should pass the following tests
> 
> **Auth Controller - POST /auth/login - should redirect to / on success**
> 
> **Auth Controller - POST /auth/login - should redirect to /auth/login on failure**

#### Login after Signup

Ideally, we want to already be logged in after signup. We can modify the signup route to call the `passport.authenticate` function again. Note that we'll need to call it as an IIFE, passing the request and response.

**controllers/auth.js**

```js
router.post('/signup', function(req, res) {
  db.user.findOrCreate({
    where: { email: req.body.email },
    defaults: {
      name: req.body.name,
      password: req.body.password
    }
  }).spread(function(user, created) {
    if (created) {
      // replace the contents of this if statement with the code below
      passport.authenticate('local', {
        successRedirect: '/'
      })(req, res);
    } else {
      console.log('Email already exists');
      res.redirect('/auth/signup');
    }
  }).catch(function(error) {
    console.log('An error occurred: ', error.message);
    res.redirect('/auth/signup');
  });
});
```

#### Logout

Including the Passport configuration in our app means that logging out is really really easy. You can now call a function attached to `req` to log out. Let's implement the final route.

**controllers/auth.js**

```js
router.get('/logout', function(req, res) {
  req.logout();
  console.log('logged out');
  res.redirect('/');
});
```

> This should pass the following test
> 
> **Auth Controller - GET /auth/logout - should redirect to /**

## Login/Logout Finished

Congrats, your login/logout functionality should be finished! Verify by running the auth tests only. All tests should pass.

```
NODE_ENV=test foreman run node_modules/mocha/bin/mocha test/auth.test.js
```

Now for one more section...
