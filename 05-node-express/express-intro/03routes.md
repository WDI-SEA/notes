#First Express App with Routes

##Our first Express App

###Setting up a project
Create a new folder for use with the project using `mkdir node_calculator`, and cd into `cd node_calculator`

###index.js

The following example shows how to get routes working in Node. A **route** is a combination of a URL pattern + HTTP Verb (get, post, put, delete). These verbs represent a method for the request.

Each route is called on our Express app, and takes a URL pattern and a callback function. The callback function gives us back the request (`req`) and response to send back to the client (`res`). Calling the `.send` function on the response sends a string back to the client.

```js
var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.send('hello brian');
});

app.listen(3000);
```

###More Route Styles

By putting a colon before a string in our route, we can create routes with different variables, or **parameters**. These parameters are automatically pulled out for us by Express and can be accessed via the `req.params` object.

```js
var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.send('hello brian');
});

app.get("/greet/:name/:lastname", function(req, res) {
  res.send("Hello " + req.params.name + " " + req.params.lastname);
});

app.get("/multiply/:x/:y", function(req, res) {
  res.send("The answer is: " + (req.params.x * req.params.y));
});

app.get("/add/:x/:y", function(req, res) {
  res.send("The answer is: " + (parseInt(req.params.x) + parseInt(req.params.y)));
});
```

In addition to having routes where different portions of the URL are different paramaters, we can use the generic string of the URL in our route logic using the wildcard.

```js
app.get("/add/*", function(req, res) {
  var myParams = req.params[0].split("/")
  var result = myParams.reduce(function(total, num) {
    return total + parseInt(num)
  }, 0);
  res.send("The answer is  " + result);
});
```

This will give you a URL like `http://localhost:3000/add/5/3/3/2/3` and give you an answer.

###Running your Project
If `"main": "index.js"` is in your `package.json`, then running `nodemon` will automatically start your project and serving your file.
