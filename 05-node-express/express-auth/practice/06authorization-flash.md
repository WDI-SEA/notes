# Authorization and Flash messages

We'll need to...

1. Include middleware for display flash messages on webpages
2. Create and include middleware for accessing the current user and flash messages.
3. Create and include authorization middleware to limit access to webpages

## Flash messages via connect-flash

### What are flash messages?

Flash messages are temporary \(one-shot\) messages used to display an error or info to the user. The messages are typically stored in the session, which allows us to redirect the user to a new page and display a message after redirect. Once the user refreshes or redirects away from the page, the message will disappear from the session.

In Express, we use a middleware called [connect-flash](https://www.npmjs.com/package/connect-flash) to handle flash messages.

connect-flash requires `session`, so you **must** load the [express-session](https://www.npmjs.com/package/express-sessions) middleware first if you want to pass flash messages between pages.

### Installing connect-flash

```text
npm install connect-flash
```

### Including connect-flash

**index.js**

```javascript
// require connect-flash at the top of the page
const flash = require('connect-flash');

/* 
 * Include the flash module by calling it within app.use().
 * IMPORTANT: This MUST go after the session module
 */
app.use(flash());
```

### Sending flash messages

Flash messages can be sent by calling `req.flash()` within a route, and passing along a key and value. We can also configure Passport to automatically add success and failure flash messages. Let's include the following flash messages in your code, to replace your `console.log` statements. Look for the `// FLASH` comments to see where you should add flash calls.

**controllers/auth.js**

```javascript
var express = require('express');
var db = require('../models');
var passport = require('../config/ppConfig');
var router = express.Router();

router.get('/signup', function(req, res) {
  res.render('auth/signup');
});

router.post('/signup', (req, res) => {
  db.user.findOrCreate({
    where: { email: req.body.email },
    defaults: {
      name: req.body.name,
      password: req.body.password
    }
  }).then(([user, created]) => {
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
  }).catch(error => {
    // FLASH
    req.flash('error', error.message);
    res.redirect('/auth/signup');
  });
});

router.get('/login', (req, res) => {
  res.render('auth/login');
});

// FLASH
router.post('/login', passport.authenticate('local', {
  successRedirect: '/',
  failureRedirect: '/auth/login',
  failureFlash: 'Invalid username and/or password',
  successFlash: 'You have logged in'
}));

router.get('/logout', (req, res) => {
  req.logout();
  // FLASH
  req.flash('success', 'You have logged out');
  res.redirect('/');
});

module.exports = router;
```

### Retrieve the messages in the view

We can retrieve the message using `req.flash()` and pass that message in to the view. However, we don't want to remember to do that on every route, like this:

```javascript
app.get('/', (req, res) => {
  res.render('index', { alerts: req.flash() });
});
```

Instead, we can create middleware to make the messages accessible in every view. This can be done by attaching the value to `res.locals`. While we're at it, let's add the currently logged in user as well. Add the following middleware after the rest of your middleware in `server.js`.

```javascript
app.use((req, res, next) => {
  // before every route, attach the flash messages and current user to res.locals
  res.locals.alerts = req.flash();
  res.locals.currentUser = req.user;
  next();
});
```

### Display messages and current user

Once we pass the alerts through to the view, we can display them by accessing the object as `alerts`.

In order to display the alerts, we can make a partial that renders on every page.

**views/partials/alerts.ejs**

```markup
<% if (alerts.error) { %>
  <% alerts.error.forEach(msg => { %>
    <div class="alert alert-error"><%= msg %></div>
  <% }); %>
<% } %>
<% if (alerts.success) { %>
  <% alerts.success.forEach(msg => { %>
    <div class="alert alert-success"><%= msg %></div>
  <% }); %>
<% } %>
```

Rendering the partial and the current user:

**views/layout.ejs**

```markup
<% include partials/alerts %>
```

While we're on the layout, let's add some conditional rendering for the nav bar. We added `req.flash()` messages to `res.locals` but we also added a `currentUser`. That means that we will have access to that variable from any of our EJS pages. The value will be truthy if there is a user logged in and falsy if not.

**views/layout.ejs**

```markup
<header>
  <nav>
    <ul>
      <% if (!currentUser) { %>
        <li><a href="/auth/signup">Signup</a></li>
        <li><a href="/auth/login">Login</a></li>
      <% } else { %>
        <li><a href="/auth/logout">Logout</a></li>
        <li><a href="/profile">Profile</a></li>
      <% } %>
    </ul>
  </nav>
</header>
```

### Authorization for web pages

Lastly, let's add authorization so users need to be logged in to access certain pages. Let's create the middleware for authorization in a separate file within the middleware folder.

**middleware/isLoggedIn.js**

```javascript
module.exports = (req, res, next) => {
  if (!req.user) {
    req.flash('error', 'You must be logged in to access that page');
    res.redirect('/auth/login');
  } else {
    next();
  }
};
```

Whenever we want to limit access to a particular page, require this middleware on the route. The current logic will redirect the user to the login route if they're not logged in.

**server.js**

```javascript
// require the authorization middleware at the top of the page
const isLoggedIn = require('./middleware/isLoggedIn');

app.get('/profile', isLoggedIn, (req, res) => {
  res.render('profile');
});
```

> This should pass the following tests
>
> **GET /profile - should redirect to /auth/login if not logged in**
>
> **GET /profile - should return a 200 response if logged in**

If you want to lock down all the routes in a specific controller, you can add the `isLoggedIn` middleware when you use the middleware.

```javascript
app.use('/dinos', isLoggedIn, require('./routes/dinos'));
```

## Conclusion and CSRF

Congrats, you have a working application with user authentication and authorization! To ensure all components are working, run `npm test` to verify all tests pass.

See a finished OAuth example here:

[https://github.com/sixhops/oauth-boilerplate](https://github.com/sixhops/oauth-boilerplate)

### Additional: Cross-Site Request Forgeries

Something we did not cover in this walk-through, which is part of the [OWASP Top 10 Web Application Security Flaws](http://www.veracode.com/directory/owasp-top-10) is **Cross-Site Request Forgeries \(CSRF\)**.

CSRF is a security flaw where a third-party site attempts to make a request to your site with your site's session cookie. For example, if I'm logged into Reddit, I could come across a link that looks like this:

```markup
<a href="http://www.reddit.com/accounts.php?action=delete">Delete account. Are you sure?</a>
```

But what if I was in a comment section, and someone decided to disguise this link?

```markup
<a href="http://www.reddit.com/accounts.php?action=delete">Free subscription!</a>
```

This would delete my account! To prevent this forgery, we can generate a unique token on the server that must be sent with this delete request, then verify the token on the server.

```markup
<a href="http://www.reddit.com/accounts.php?action=delete&csrf_token=aGIe3Sl8a9FlsdLkJVZ">Free subscription!</a>
```

For time's sake, we won't be implementing this together. However, there's an Express module called [csurf](https://github.com/expressjs/csurf) that can be used to protect against CSRF attacks via tokens. Feel free to look at the examples and implement this on your own. When working in Rails, this functionality will be included automatically.

Another note, this protection does not apply to APIs. APIs should use a key instead.

