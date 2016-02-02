![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# API Authentication with Express - Tokens

### Objectives
- Understand why authentication tokens are commonly used when interacting with APIs
- Add a token strategy to an application
- Authenticate a user based on their token

## Tokens, The Basics

The technique we're going to use today for API authentication revolves around **tokens**. Tokens are, at their simplest, a unique string that is usually auto-generated. They provide information that authenticates a user with a server, based on a hashing algorithm and token signature.

If we trust that we've designed it that way, then we can use a string of characters to determine the identity of a user and whether the user is logged in.

### Kicking it up a notch

That's the overall gist of what tokens do, but today we're going to use a specific type of token. It's a fairly new type of token, that's becoming widely used and trusted in web applications, and it's called a **JSON Web Token** or JWT (pronounced `jot`).

It is the same idea – a single string of characters to authenticate – only it's a string of characters built by encrypting actual information.

You can play with encoding/decoding the data over at their site as an example. Head on over to [jwt.io](http://jwt.io/#debugger).

![JWTs](https://cloud.githubusercontent.com/assets/25366/9151601/2e3baf1a-3dbc-11e5-90f6-b22cda07a077.png)

#### Just like cookies, mmmm....

In the example above, you'll notice that there are 3 parts. The payload is the one we care the most about, and it holds whatever data we decide to put in there. It's very much like a cookie; we put as few things in there as possible – just the pieces we really need.

Applications can save a JWT somewhere on a user's computer, just like a cookie. Because JWTs can be encrypted into a single string, we can _also_ send it over HTTP easily. Which means it'll work in any server/client scenario you can imagine. Quite nice.

## Starter Express App

Now, before we talk specifically about JWTs, we've built a really basic starter Express app to hack on for a few minutes. Take 5 minutes to look through it and see what you notice. There are one or two things you might see that are different, but get familiar with what we're working with.

## What's different? - Demo (10 mins)

You might notice some interesting things in `models/user.js`.

#### 1. Crafting our JSON Return

Unless we modify the code, our JSON objects will get returned in our API with every piece of information in the database. But the fact is, you may sometimes want to omit certain things (like password hashes), or you might also just want to have your JSON look a certain way.

One way to do this is to _transform_ your model's schema.

```js
UserSchema.set('toJSON', {
    transform: function(doc, ret, options) {
        var returnJson = {
            id: ret._id,
            email: ret.email,
            name: ret.name
        };
        return returnJson;
    }
});
```

This is an example of whitelisting, but you could also blacklist if that's easier, by deleting key/value pairs instead:

```js
UserSchema.set('toJSON', {
  transform: function(doc, ret, options) {
    delete ret.password;
    return ret;
  }
});
```

#### 2. Encrypting Passwords in the Model

```js
// Let's encrypt our passwords using only the model!
// This is a hook, a function that runs just before you save.
UserSchema.pre('save', function(next) {
  var user = this;

  // only hash the name if it has been modified (or is new)
  if (!user.isModified('password')) return next();
  // bcrypt can come up with a salt for us (just pass it a number)
  user.password = bcrypt.hashSync(user.password, 10);

  next();
});
```

Now, we're going to protect the `/api/users` route via JWT token authentication. In order to do so, we'll be adding a new route called `POST /api/auth` in order to create the token. Then, we'll verify each route with the token by passing it in the headers.

## The Main Feature, JWTs

We'll have to install a couple npm modules to start working with JWTs & authenticating via tokens.

```
npm install --save jsonwebtoken express-jwt
```

Now, of course, we have to require them. Later, you could extract this to a config file if you'd like, but for now let's throw it in `index.js`:

```js
var express = require('express');
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var expressJWT = require('express-jwt');
var jwt = require('jsonwebtoken');
var User = require('./models/user');
var app = express();

// A secret phrase that only your app knows, so encryption can be consistent. We'll use this later.
var secret = "mysupersecretpassword";
```

Now there are 3 things we're going to need to write:

- An endpoint to create a token
- A middleware that will check for the token
- An error handler for when there _isn't_ a token

That's it.

## Creating a token

We're going to put our auth route/endpoint right in `index.js`. You could (and probably should later) extract it out, so that `index.js` doesn't become cluttered.

onsidering we're _creating_ a token, we'll be using the `POST` HTTP verb.

```js
//index.js
app.post('/api/auth', function(req, res) {
    // some code to check that a user's credentials are right #bcryptmaybe?
    // collect any information we want to include in the token, like that user's info

    // make a token already & send it as JSON
});
```

Psuedocode successful. Let's fill out these bits.

```js
//index.js
app.post('/api/auth', function(req, res) {
  // some code to check that a user's credentials are right #bcryptmaybe?
  // collect any information we want to include in the token, like that user's info
  User.findOne({email: req.body.email}, function(err, user) {
    if (err || !user) return res.send({message: 'User not found'});
    user.authenticated(req.body.password, function(err, result) {
      if (err || !result) return res.send({message: 'User not authenticated'});

      // make a token & send it as JSON
      var token = jwt.sign(user, secret);
      res.send({user: user, token: token});
    });
  });
});
```

We'll see that first, we find a user by their email address and see if we get a result. If not, we'll say that the user was not found. Second, we'll authenticate the user using a similar instance method as we did with session authentication. We'll only send back a token if the user is authenticated.

The next part, we're using our `jwt` library, and it just takes a few arguments. This comes from the documentation, but basically we pass it the _payload_, aka `user`, and pass it that secret phrase we made earlier (so that tokens can be encrypted consistently), and we have a token.

Finally, we just send the data back to the client. Let's try our endpoint and see if we get a token back, using something like [Insomnia](http://insomnia.rest/) or [Postman](https://www.getpostman.com/).

We should get back something like this:

```js
// http://localhost:3000/api/auth
{
  "user": {
    "id": "5654f779fa0e9c97831c2784",
    "email": "bhague1281@gmail.com",
    "name": "Brian Hague"
  },
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IjU2NTRmNzc5ZmEwZTljOTc4MzFjMjc4NCIsImVtYWlsIjoiYmhhZ3VlMTI4MUBnbWFpbC5jb20iLCJuYW1lIjoiQnJpYW4gSGFndWUifQ.HcL1Cd5wtON15ZlMm7siyi0hvSUe7hsIsfzgvVR7U7c"
}
```

## A middleware to check for our token

Next up, we have to start restricting access. This is suprisingly easy, since we're using `expressJWT`. It's built in.

Far above your routes, add this in your `index.js`:

```js
app.use('/api/users', expressJWT({secret: secret}).unless({method: 'POST'}));
```

Hello, middleware. It sits between the request & your code, and because it's above any routes you have set up, it'll run first.

It uses the library and checks for a token. That's it. If there is a token, it keeps going & runs your app like normal. It throws your `user` (the payload you embedded in the JWT), into `request.user` _for_ you.

So on any particular route or controller action, you should be able to say, `request.user.name` and get back the user's name. You could use that for looking them up in the database, storing their information in an embedded document, whatever you need.

And hopefully it's apparent, but you can customize the URLs you need to restrict. We happened to have chosen this one in particular, but you could easily do the same for all of the users resource, all of your API, or whatever you like.

That's it. Now the last step.

## An error handler for when there isn't a token

_Technically_, our app is good to go. If you try to access one of your users, you won't be able to. You'll see a bunch of junk that looks like this:

<img width="795" src="https://cloud.githubusercontent.com/assets/25366/9152366/3074b6be-3dda-11e5-8104-dba53428e936.png">

Lovely. So our last step is to pretty that up with a little error handling.

Just after your middleware, let's make another tiny little middleware:

```js
// JWT access control. Important to have these before our routes, so it can run first!
app.use('/api/users', expressJWT({secret: secret}).unless({method: 'POST'}));
app.use(function (err, req, res, next) {
  // send an appropriate status code & JSON object saying there was an error, if there was one.
});
```

We just need an `if` statement.

```js
// JWT access control. Important to have these before our routes, so it can run first!
app.use('/api/users', expressJWT({secret: secret}).unless({method: 'POST'}));
app.use(function (err, req, res, next) {
  // send an appropriate status code & JSON object saying there was an error, if there was one.
  if (err.name === 'UnauthorizedError') {
    res.status(401).send({message: 'You need an authorization token to view this information.'})
  }
});
```

Boom! Now let's see what happens when we try to access a user.

## Wait, don't leave us – how _do_ we access it?

Last but not least, we need to access the resource.

You've got it all built, and this final piece will complete the puzzle.

**You send along your token via an Authorization header**, with a value of `"Bearer mylongtokengoesrighthere"` Try this out using Postman.

If you're using a tool other than CURL, look for where you can add in custom headers:

So, just like a client would have to, you'd:

1. POST to your `authorizations` endpoint!
2. Copy that token!
3. GET to the users endpoint, with an Authorization header!

And there you have it. It's really only a few lines of code we had to write, and once you combine it with bcrypt and hashed passwords, you've got yourself a secure API that can be authorized with a single string of characters.

## Conclusion

- What is a JWT? Why is useful for authorizing an API?
- How do you create a JWT in an endpoint in your Express app?
- How do you secure an endpoint using a JWT?
