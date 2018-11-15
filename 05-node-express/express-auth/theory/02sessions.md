# Sessions

### What are sessions?

Sessions are used to store data about a user on the server. This can be an authenticated user or a non-authenticated user. Session data is stored on the server for each person using the website and referenced using a cookie stored on the users computer. The session cookie contains a unique key that allows the server to access the correct data for each person. The cookie is sent to the server on each request.

### Why is this useful?

Session data is retained between page loads so it allows sharing of data between requests without passing it in the url string. Sessions are also integral for user authentication.

### Using sessions in Express

To utilize sessions in Express, we need to load the session middleware. The setup is very similar to setting up the body-parser middleware.

First we need to install the npm module

```
npm install express-session --save
```

Then we need to require it and "use" it

```js
var session = require('express-session');
//...
app.use(session({
  secret: 'Super secrettttt',
  resave: false,
  saveUninitialized: true
}));
```

The initialization funciton above `session()` takes an object containing some options:

* **secret** - a unique string used to sign a cookie and prevent tampering. You should change this string to some random characters or words. It doesn't really matter what you type here as long as it's unqiue to your app. Generally, this should also be an environment variable.
* **resave** - forces re-saving of the session, even if nothing has changed.
* **saveUninitialized** - stores the session, even if we haven't stored any values to it yet.

Once the session middleware is installed, you can read/write sessions using the `req.session` object.

```js
req.session.lastPage = '/myPage';
```

Then you can retrive the data the same way

```js
//on another page
console.log(req.session.lastPage);
//outputs: /myPage
```

Each value in `req.session` will be unique to the user accessing the page. The server will know the difference between users by reading each user's cookie.
