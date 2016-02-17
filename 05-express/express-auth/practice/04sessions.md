#Setting up user sessions

For sessions (remembering users are logged in), we'll need...

1. Install `express-session` middleware
2. Setup the session module
3. Test the session store by storing a value.

```
npm install --save express-session
```

####In code

In **index.js**, before including the controllers:

```js
// import express-session
var session = require('express-session');

// setup middleware
app.use(session({
  secret: 'dsalkfjasdflkjgdfblknbadiadsnkl',
  resave: false,
  saveUninitialized: true
}));
```

Note that in production environments, we'll replace the secret value with an environment variable.

**TESTING:** Once the middleware is loaded, we can get/set data in `req.session` and it will be preserved between requests.

Do this in one route to set the value before returning a response.

```js
req.session.whatever="hello!!!";
```

in any subsequent route you can retrive the value like this

```js
console.log(req.session.whatever);
//outputs: "hello!!!"
```
