# User Login

We'll need to...

1. Install dependencies, `passport` and `passport-local`
2. Configure Passport to use our user model
3. Initialize Passport to use our session module
4. Add login and logout functionality to the `auth` controller

## Passport and passport-local

From the [passport website](http://www.passportjs.org/)

> Passport is authentication middleware for Node.js. Extremely flexible and modular, Passport can be unobtrusively dropped in to any Express-based web application.

Passport has a lot of different strategies for authenticating users—github, linkedin, and more! \(Passport website lists 502 different strategies!\) We're using the Local strategy.

> This module lets you authenticate using a username and password in your Node.js applications. By plugging into Passport, local authentication can be easily and unobtrusively integrated into any application or framework that supports Connect-style middleware, including Express.

## Install passport and passport-local

We'll use Passport in order to provide login functionality, and `passport-local` in order to provide local user authentication.

```text
npm i passport passport-local
```

## Configure Passport to use our user model

Create the Passport configuration inside of the config folder. This will be a javascript file

```text
touch config/ppConfig.js
```

**config/ppConfig.js**

```javascript
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const db = require('../models');

/*
 * Passport "serializes" objects to make them easy to store, converting the
 * user to an identifier (id)
 */
passport.serializeUser((user, cb) => {
  cb(null, user.id);
});

/*
 * Passport "deserializes" objects by taking the user's serialization (id)
 * and looking it up in the database
 */
passport.deserializeUser((id, cb) => {
  db.user.findByPk(id).then(user => {
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
}, (email, password, cb) => {
  db.user.findOne({ 
    where: { email }
  }).then(user => {
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

Now that we've created the configuration, we need to make our app _aware of its existence_. This can be done by requiring the configuration and including it as middleware.

**index.js**

```javascript
// require the configuration at the top of the file
const passport = require('./config/ppConfig');

// initialize the passport configuration and session as middleware
app.use(passport.initialize());
app.use(passport.session());
```

**IMPORTANT NOTE:** You must include the passport configuration **below your session configuration.** This ensures that Passport is aware that the session module exists.

## Add login and logout functionality

> Before continuing, verify that this test is passing
>
> **Auth Controller - GET /auth/login - should return a 200 response**

### Login

Luckily, all of that configuration and middleware means a straightforward login route. Let's go ahead and add the POST route for login.

**controllers/auth.js**

```javascript
// require the passport configuration at the top of the file
const passport = require('../config/ppConfig');

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

### Login after Signup

Ideally, we want to already be logged in after signup. We can modify the signup route to call the `passport.authenticate` function again. Note that we'll need to call it as an IIFE, passing the request and response.

**controllers/auth.js**

```javascript
router.post('/signup', (req, res) => {
  db.user.findOrCreate({
    where: {
      email: req.body.email
    }, defaults: {
      name: req.body.name,
      password: req.body.password
    }
  }).then(([user, created]) => {
    if (created) {
      console.log('user created');
      passport.authenticate('local', {
        successRedirect: '/',
      })(req, res);
    } else {
      console.log('email already exists');
      res.redirect('/auth/signup');
    }
  }).catch(err => {
    console.log('💩 Error occured finding or creating user');
    console.log(err);
    res.redirect('/auth/signup');
  });
});
```

### Logout

Including the Passport configuration in our app means that logging out is really really easy. You can now call a function attached to `req` to log out. Let's implement the final route.

**controllers/auth.js**

```javascript
router.get('/logout', (req, res) => {
  req.logout();
  res.redirect('/');
});
```

> This should pass the following test
>
> **Auth Controller - GET /auth/logout - should redirect to /**

## Login/Logout Finished

Congrats, your login/logout functionality should be finished! Verify by running the tests. You should have 17 passing and only one failing.

```text
npm test
```

Now for one more section...

