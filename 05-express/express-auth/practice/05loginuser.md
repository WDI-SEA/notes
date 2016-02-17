#Add functionality to the login POST route

Before we can implement the login route, we need to create a function to check if the password matches. Then, we'll call the function and login the user if everything matches.

####In code

In **models/user.js**

```js
classMethods: {
  associate: function(models) {
    // associations can be defined here
  },
  authenticate: function(email, password, callback) {
    this.find({
      where: {email: email}
    }).then(function(user) {
      if (!user) callback(null, false);
      bcrypt.compare(password, user.password, function(err, result) {
        if (err) return callback(err);
        callback(null, result ? user : false);
      });
    }).catch(callback);
  }
},
```

In **controllers/auth.js**

```js
router.post('/login', function(req, res) {
  var email = req.body.email;
  var password = req.body.password;
  db.user.authenticate(email, password, function(err, user) {
    if (err) {
      res.send(err);
    } else if (user) {
      req.session.userId = user.id;
      res.redirect('/');
    } else {
      res.send('user and/or password invalid');
    }
  });
});
```

Now **TEST** and verify your code works. Debug if necessary.

###Logging out

In order to log out, or clear the session, our last route is an easy one.

In **controllers/auth.js**

```js
router.get('/logout', function(req, res) {
  req.session.userId = false;
  res.redirect('/');
});
```

In order to test this functionality, we're also going to set up middleware to have the current user available in each route:

In **index.js**

```js
// import models
var db = require('./models');

// add middleware to get the user into the request and template engine
app.use(function(req, res, next) {
  if (req.session.userId) {
    db.user.findById(req.session.userId).then(function(user) {
      req.currentUser = user;
      res.locals.currentUser = user;
      next();
    });
  } else {
    req.currentUser = false;
    res.locals.currentUser = false;
    next();
  }
});
```

Note that we're querying the database and retrieving the user based on the `userId` in the session. Note also that `res.locals` will allow us to access `currentUser` in the views. [Documentation.](http://expressjs.com/en/api.html#res.locals)

Try using `currentUser` in **views/layout.ejs**.

```html
<div>Current User: <%= currentUser.name %></div>
```
