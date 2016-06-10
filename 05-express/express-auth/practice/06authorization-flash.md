# Authorization and Flash Messages

We'll need to...

1. Include middleware for display flash messages on webpages
2. Create and include middleware for accessing the current user and flash messages.
3. Create and include authorization middleware to limit access to webpages

## Flash messages via connect-flash

#### What are flash messages?

Flash messages are temporary (one-shot) messages used to display an error or info to the user. The messages are typically stored in the session, which allows us to redirect the user to a new page and display a message after redirect. Once the user refreshes or redirects away from the page, the message will disappear from the session.

In Express, we use a middleware called [connect-flash](https://www.npmjs.com/package/connect-flash) to handle flash messages.

connect-flash requires `session`, so you **must** load the [express-session](https://www.npmjs.com/package/express-sessions) middleware first if you want to pass flash messages between pages.

#### Installing connect-flash

```
npm install --save connect-flash
```

#### Including connect-flash

**index.js**

```js
// require connect-flash at the top of the page
var flash = require('connect-flash');

/* 
 * Include the flash module by calling it within app.use().
 * IMPORTANT: This MUST go after the session module
 */
app.use(flash());
```

#### Sending flash messages

Flash messages can be sent by calling `req.flash()` within a route, and passing along a key and value. We can also configure Passport to automatically add success and failure flash messages. Let's include the following flash messages in your code, to replace your `console.log` statements. Look for the `// FLASH` comments to see where you should add flash calls.

**controllers/auth.js**

```js
var express = require('express');
var db = require('../models');
var passport = require('../config/ppConfig');
var router = express.Router();

router.get('/signup', function(req, res) {
  res.render('auth/signup');
});

router.post('/signup', function(req, res) {
  db.user.findOrCreate({
    where: { email: req.body.email },
    defaults: {
      name: req.body.name,
      password: req.body.password
    }
  }).spread(function(user, created) {
    if (created) {
      // FLASH
      passport.authenticate('local', {
        successRedirect: '/',
        successFlash: 'Account created and logged in'
      })(req, res);
    } else {
      // FLASH
      req.flash('error', 'Email already exists');
      res.redirect('/auth/signup');
    }
  }).catch(function(error) {
    // FLASH
    req.flash('error', error.message);
    res.redirect('/auth/signup');
  });
});

router.get('/login', function(req, res) {
  res.render('auth/login');
});

// FLASH
router.post('/login', passport.authenticate('local', {
  successRedirect: '/',
  failureRedirect: '/auth/login',
  failureFlash: 'Invalid username and/or password',
  successFlash: 'You have logged in'
}));

router.get('/logout', function(req, res) {
  req.logout();
  // FLASH
  req.flash('success', 'You have logged out');
  res.redirect('/');
});

module.exports = router;
```

#### Retrieve the messages in the view

We can retrieve the message using `req.flash()` and pass that message in to the view. However, we don't want to remember to do that on every route, like this:

```js
app.get('/', function(req, res) {
  res.render('index', { alerts: req.flash() });
});
```

Instead, we can create middleware to make the messages accessible in every view. This can be done by attaching the value to `res.locals`. While we're at it, let's add the currently logged in user as well. Add the following middleware after the rest of your middleware.

```js
app.use(function(req, res, next) {
  // before every route, attach the flash messages and current user to res.locals
  res.locals.alerts = req.flash();
  res.locals.currentUser = req.user;
  next();
});
```

#### Display messages and current user

Once we pass the alerts through to the view, we can display them by accessing the object as `alerts`.

In order to display the alerts, we can make a partial that renders on every page.

**views/partials/alerts.ejs**

```html
<% if (alerts.error) { %>
  <% alerts.error.forEach(function(msg) { %>
    <div class="alert alert-danger"><%= msg %></div>
  <% }); %>
<% } %>
<% if (alerts.success) { %>
  <% alerts.success.forEach(function(msg) { %>
    <div class="alert alert-success"><%= msg %></div>
  <% }); %>
<% } %>
```

Rendering the partial and the current user:

**views/layout.ejs**

```html
<%- JSON.stringify(currentUser) %>

<% include partials/alerts %>
```

#### Authorization for web pages

Lastly, let's add authorization so users need to be logged in to access certain pages. Let's create the middleware for authorization in a separate file within the middleware folder.

**middleware/isLoggedIn.js**

```js
module.exports = function(req, res, next) {
  if (!req.user) {
    req.flash('error', 'You must be logged in to access that page');
    res.redirect('/auth/login');
  } else {
    next();
  }
};
```

Whenever we want to limit access to a particular page, require this middleware on the route. The current logic will redirect the user to the login route if they're not logged in.

**index.js**

```js
// require the authorization middleware at the top of the page
var isLoggedIn = require('./middleware/isLoggedIn');

app.get('/profile', isLoggedIn, function(req, res) {
  res.render('profile');
});
```

> This should pass the following tests
> 
> **GET /profile - should redirect to /auth/login if not logged in**
> 
> **GET /profile - should return a 200 response if logged in**

## Conclusion

Congrats, you have a working application with user authentication and authorization! To ensure all components are working, run `foreman run npm test` to verify all tests pass.
