#Auth in Practice

##Objectives

* Understand and synthesize concepts of different Node components
* Use flash messages for one-time user notifications

1. Create a user table (see sequelize lesson)
  * attributes / columns
    * e-mail
    * password
    * name
2. Create a sign up form (GET /auth/signup)
  * should have form fields for each column listed above
3. Create a signup POST route
  * route: POST /auth/signup
  * Check if e-mail already registered
    * Creates new user if not registered
    * Tells user they are already registered otherwise
  * ENCRYPTS PASSWORD!!!!! (use before create)
4. Create a login form (GET /auth/login)
5. Set up sessions middleware
6. Create a login POST route (does login)
  * route: POST /auth/login
  * Checks e-mail / password against database
  * Logs user in (create session)
7. Create a GET /auth/logout route (clears the session)
8. Create getUser() method (as middleware)


##Requirements to install

* [express-session](https://www.npmjs.com/package/express-session) - handles session storage
* [bcrypt](https://www.npmjs.com/package/bcrypt) - used to encrypt passwords
* [body parser](https://www.npmjs.com/package/body-parser) - parse form data from signup, login form, etc


##Using sessions

First you need to install `express-session` through npm then you can load the middleware like this...

```js
app.use(session({
  secret:'dsalkfjasdflkjgdfblknbadiadsnkl',
  resave: false,
  saveUninitialized: true
}));
```

Once the middleware is loaded you can simply get / set data in `req.session` and it will be preserved between requests.

Do this in one route to set the value

```js
req.session.whatever="hello!!!";
```

in any subsequent route you can retrive the value like this

```js
console.log(req.session.whatever);
//outputs: "hello!!!"
```

##Peripheral concept - Flash Messages

Flash messages are temporary (one-shot) messages used to display an error or info to the user. The messages are typically stored in the session which allows us to redirect the user to a new page and display the error after redirect.

In express we use a middleware called [connect-flash](https://www.npmjs.com/package/connect-flash) to handle flash messages.

connect-flash requires session so you must load the [express-session](https://www.npmjs.com/package/express-sessions) middleware first if you want to pass flash messages between pages..

**load flash middleware**

```js
var flash = require('connect-flash');
app.use(flash());
```

**setting flash message**

```js
req.flash('danger','You must be logged in to access that page.');
res.redirect('/');
```

**retrive message**

We can retrive the message using `req.flash()` and pass that message in to the view. Once you call `req.flash()` to retrieve the messages they are deleted from the session automatically so they are only displayed once.

```js
res.render('main/index', {alerts: req.flash()});
```

**display messages**

Once we pass the alerts through to the view we can display using code like this.

This code loops through each type of message and then each message of that type and uses the message type (key) to add it as class. If you use the bootstrap alert classes (danger,warning,info,success) this will display appropriately colored alerts by default.

```js
<% if(typeof alerts !== 'undefined'){ %>
    <% for(key in alerts){ %>
        <% alerts[key].forEach(function(thisMsg){ %>
            <div class="alert alert-<%= key %>"><%= thisMsg %></div>
        <% }); %>
    <% } %>
<% } %>
```
