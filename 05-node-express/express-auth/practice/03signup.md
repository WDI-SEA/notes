# User Signup

We'll need to...

1. Double-check our signup form
2. Create a POST route for receiving the new user's data
3. Create a new user within the POST route
4. Redirect to either the home page or signup page, depending on if there's an error

## Double-check the signup form

Take a look at the current signup form and `GET /auth/signup` route. Some things you'll want to know about:

* The signup form's action
* The signup form's data
* The signup form's route
* Can we access the signup form?

> Before continuing, verify that this test is passing
> 
> **Auth Controller - GET /auth/signup - should return a 200 response**

## Creating a POST route

To receive the user's data, let's create a signup route.

**controllers/auth.js**

```js
router.post('/signup', (req, res) => {
  // try sending back the form data
  res.send(req.body);
});
```

Verify that this works. While spitting back form data verifies this route's functionality, we don't really want this. We want to implement the following logic:

* Take the user's data from `req.body`
* Find or create a new user, based on the email address provided
  * If the *user wasn't created*, the email address must already exist. Let's redirect back to the signup form so the user can fix this error.
  * If the *user was created*, we're successful! Redirect back to the home page
  * If an *error occurs*, it'll most likely be due to a validation error. Let's redirect back to the signup form so the user can fix this error.

**controllers/auth.js**

```js
// at the very top, include the database models
const db = require('../models');

router.post('/signup', (req, res) => {
  // find or create a user, providing the name and password as default values
  db.user.findOrCreate({
    where: { email: req.body.email },
    defaults: {
      name: req.body.name,
      password: req.body.password
    }
  }).then(([user, created]) => {
    if (created) {
      // if created, success and redirect home
      console.log(`${user.name} was created!`);
      res.redirect('/');
    } else {
      // if not created, the email already exists
      console.log('Email already exists');
      res.redirect('/auth/signup');
    }
  }).catch(error => {
    // if an error occurs, let's see what the error is
    console.log('An error occurred: ', error.message);
    res.redirect('/auth/signup');
  });
});
```

> This should pass the following tests
> 
> **Auth Controller - POST /auth/signup - should redirect to / on success**
> 
> **Auth Controller - POST /auth/signup - should redirect to /auth/signup on failure**

