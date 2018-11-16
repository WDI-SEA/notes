# Routes

A **route** is a combination of a ***URL pattern*** and ***HTTP Verb***.

### URL Pattern
The URL Patterns refer to everything that comes after the base URL (the slash and anything that follows). For example, let's look at a simple website - go to http://www.lemon-fol.io . You're looking at the home route. Now click on "projects" in the nav bar, or add /projects to the end of the URL in the URL bar. In this scenario, everything _before_ /projects is the base URL. The base URL alone took you to the home route ("/") which served the home page. The URL pattern "/projects" served different files.

Let's look at a more complex example. Go to reddit.com and search for "cute puppies". Notice what appears in the URL bar.

<p align="center">https://www.reddit.com/search?q=cute%20puppies</p>

Let's break this down:
* Base URL:
<em align="center">https://www.reddit.com<em>
* The rest that will be captured by a URL pattern:
<em align="center">/search?q=cute%20puppies</em>

In this situation, the URL pattern would look something like "/search?q=:searchedterms", where :searchedterms is a parameter that represents whatever was typed into the search bar.

URL Patterns will become more clear as we get into some examples.

## HTTP Verb

There are 4 HTTP verbs:
* get
* post
* put
* delete

These verbs represent a _method_ for the request. In other words, they tell the server what the nature of the request from the client is.

| HTTP Verb     | CRUD          | Example  |
| ------------- |:-------------:| -----------------:|
| GET           | READ          | Look at someone's profile on LinkedIn |
| POST          | CREATE        | Post on LinkedIn |
| PUT           | UPDATE        | Change your bio on LinkedIn |
| DELETE        | DELETE        | Delete a photo from LinkedIn |


## Backtrack: hello-express

Let's circle back to our home route in our ```hello-express``` project and break the code down a little more to see how routes look in express.

Here we have imported the express module, and created an instance of an express application called _app_. This code comes straight from the express [docs](https://expressjs.com/en/guide/routing.html).
```js
var express require('express');
var app = express();
```

Next, we created a home route. Here, the HTTP verb is ***get***, which we indicate using the express method, ```get()```. This method takes two parameters, (1) a URL Pattern and (2), a callback function that tells the app what to do when this route is reached.
```js
app.get('/', function(req, res) {
  res.send('Hello, World!');
});
```

The URL pattern '/' simply denotes the base URL.

The last line of code in our program, ```app.listen(8000)``` tells our app to listen to port 8000. In otherwords, it designates localhost:8000 as the base URL.

***The combination of the URL Pattern '/' and the HTTP verb 'get' ensures that this route will be reached when a GET request made by the client from the base URL.***

If you'd like, you could pull out the callback function to get even more visual clarity on what is happening here. (Run nodemon to convince yourself that this does not change any functionality of the program.)

```js
function hello(req, res) {
  res.send('Hello, World!');
}

app.get('/', hello);
```
By design, the express ```get()``` function will pass two arguments into the callback function: (1) the request object and (2) the response object. That is why we define a callback function with two parameters.

```send()``` is also an express function that takes one argument: the data you want to send to the front end. More on ```res.send()``` and related functions [here](https://fullstack-developer.academy/res-json-vs-res-send-vs-res-end-in-express/). You'll get more comfortable with all of this as we do more examples.

## 2nd Express App: Express Calculator

### Set up the project.
Create a new folder for use with the project using `mkdir node_calculator`, and cd into `cd node_calculator`

###index.js

Each route is called on our Express app, and takes a URL pattern and a callback function. The callback function gives us back the request (`req`) and response to send back to the client (`res`). Calling the `.send` function on the response sends a string back to the client.

```js
var express = require('express');
var app = express();

app.get('/', function(req, res) {
  res.send('Hello, world!');
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
