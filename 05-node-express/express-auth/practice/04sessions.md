# User Sessions

We'll need to...

1. Install `express-session` middleware
2. Setup the session module

In order to save whether the user is logged in or not, we'll need to create a persistent session for each user. Each session will associate data with a user, and each user will be mapped to their data via a value stored in a cookie. Instead of directly altering the session, we'll use a third-party module called Passport to do it for us.

## Install express-session

```
npm install --save express-session
```

## Setup the session module

**index.js**

```js
// at the very top, require express-session
var session = require('express-session');

/*
 * setup the session with the following:
 * 
 * secret: A string used to "sign" the session ID cookie, which makes it unique
 * from application to application. We'll hide this in the environment
 *
 * resave: Save the session even if it wasn't modified. We'll set this to false
 *
 * saveUninitialized: If a session is new, but hasn't been changed, save it.
 * We'll set this to true.
 */
app.use(session({
  secret: process.env.SESSION_SECRET,
  resave: false,
  saveUninitialized: true
}));
```

**.env**

```
SESSION_SECRET=tacocat
```

## Session finished

To verify that this session works, we'll start setting up Passport and login functionality in the next section. There are no tests associated with the sessions right now.

Additionally, you'll need to run your app and tests using `foreman` in order to read the environment variable.
