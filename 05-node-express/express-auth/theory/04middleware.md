# Middleware

We want to be able to check if our user is logged in from within any of our routes. One strategy for doing this is to expand our request object \(req\) using an express middleware. Middleware is code that exists in the "middle" between receiving the request/response objects from the client and handling them on the server.

![Express Middleware](http://media.developeriq.in/images/nodeexpress_2_9_2015_1.png)

We've already used 3rd party Express middleware and we can create our own.

**Review: Loading body-parser middle ware**

```javascript
//load body parser module
var bodyParser = require('body-parser');

//tell express to "use" it as a middleware
app.use(bodyParser.urlencoded({ extended: false }));
```

**Creating our own middleware**

app.use simply accepts a function as it's parameter and gives us 3 parameters:

* `req` - the request object
* `res` - the response object
* `next` - a callback function \(moves to the next middleware\)

We can modify each of these parameters and the modification will be reflected in the next middleware and finally in our route code.

**Example**

```javascript
app.use(function(req, res, next) {
  req.getParamNames = function() {
    return Object.keys(req.params);
  }
  next();
});

// ...later on in your code...

app.get('/sum/:x/:y', function(req, res) {
  res.send(req.getParamNames());
});
//outputs: ['x','y']
```

Using this concept we can create a middleware to get our currently logged in user from the `req.session`.

