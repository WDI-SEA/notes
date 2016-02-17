#Peripheral concept - Flash Messages

Flash messages are temporary (one-shot) messages used to display an error or info to the user. The messages are typically stored in the session, which allows us to redirect the user to a new page and display the error after redirect.

In express we use a middleware called [connect-flash](https://www.npmjs.com/package/connect-flash) to handle flash messages.

connect-flash requires `session` so you must load the [express-session](https://www.npmjs.com/package/express-sessions) middleware first if you want to pass flash messages between pages.

Let's modify our secret route so users are redirected home if not logged in. They'll also see a flash message.

```
npm install --save connect-flash
```

####In code

**index.js**

```js
// import and use flash as middleware
var flash = require('connect-flash');
app.use(flash());

// modify the secret route, place below the session middleware
app.get('/secret', function(req, res) {
  if (req.currentUser) {
    res.render('secret');
  } else {
    req.flash('danger', 'You must be logged in to view this page');
    res.redirect('/');
  }
});
```

####Retrieve the messages

We can retrive the message using `req.flash()` and pass that message in to the view. Once you call `req.flash()` to retrieve the messages they are deleted from the session automatically so they are only displayed once.

In **index.js**

```js
// modify the index route
app.get('/', function(req, res) {
  res.render('index', {alerts: req.flash()});
});
```

**Display messages**

Once we pass the alerts through to the view, we can display by accessing the object.

This code loops through each type of message and then each message of that type and uses the message type (key) to add it as class. If you use the bootstrap alert classes (danger, warning, info, success) this will display appropriately colored alerts by default.

Place the following in your layout (or in a partial, depending on how your views are set up).

```js
<% if (typeof alerts !== 'undefined') { %>
  <% for (key in alerts) { %>
    <% alerts[key].forEach(function(thisMsg) { %>
      <div class="alert alert-<%= key %>"><%= thisMsg %></div>
    <% }); %>
  <% } %>
<% } %>
```

Take a moment to look at the finished auth example (located in the branch `express-auth`).
