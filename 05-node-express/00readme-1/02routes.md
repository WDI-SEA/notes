# Routes

A **route** is a combination of a _**URL pattern**_ and _**HTTP Verb**_.

### URL Pattern

The URL Patterns refer to everything that comes after the base URL \(the slash and anything that follows\). For example, let's look at a simple website - go to [http://www.lemon-fol.io](http://www.lemon-fol.io) . You're looking at the home route. Now click on "projects" in the nav bar, or add /projects to the end of the URL in the URL bar. In this scenario, everything _before_ /projects is the base URL. The base URL alone took you to the home route \("/"\) which served the home page. The URL pattern "/projects" served different files.

Let's look at a more complex example. Go to reddit.com and search for "cute puppies". Notice what appears in the URL bar: [_https://www.reddit.com/search?q=cute puppies_](https://www.reddit.com/search?q=cute%20puppies)

Let's break this down:

* Base URL \(consists of the protocol \(https\) and the domain \(www.reddit.com\):

  [_https://www.reddit.com_](https://www.reddit.com)

* URL Pattern \(think of as directories of the web app\):

  _/search_

* Query String \(a key=value way of sending data with the request\):

  _?q=cute%20puppies_

In this situation, the URL pattern would look something like "/search". When the request arrived in our route handler function (the callback in a route), we would have access to the query string key-value pairs as part of the `request` object. More on this a bit later...

URL Patterns will become clearer as we get into some examples.

## HTTP Verb

There are 4 main HTTP verbs:

* get
* post
* put
* delete

These verbs represent a _method_ for the request. In other words, they tell the server what the nature of the request from the client is.

| HTTP Verb | CRUD | Example |
| :--- | :---: | ---: |
| GET | READ | Look at someone's profile on LinkedIn |
| POST | CREATE | Post on LinkedIn |
| PUT/PATCH | UPDATE | Change your bio on LinkedIn |
| DELETE | DELETE | Delete a photo from LinkedIn |

## Backtrack: hello-express

Let's circle back to our home route in our `hello-express` project and break the code down a little more to see how routes look in express.

Here we have imported the express module, and created an instance of an express application called _app_. This code comes straight from the express [docs](https://expressjs.com/en/guide/routing.html).

```javascript
const express require('express');
const app = express();
```

Next, we created a home route. Here, the HTTP verb is _**get**_, which we indicate using the express method, `get()`. This method takes two parameters, \(1\) a URL Pattern and \(2\), a callback function that tells the app what to do when this route is reached.

```javascript
app.get('/', (req, res) => {
  res.send('Hello, World!');
});
```

The URL pattern '/' simply denotes the base URL or root of the app.

The last line of code in our program, `app.listen(8000)` tells our app to listen to port 8000. This is the actual "place" in the network layers of our operating system where the request will come in. After this starts, the full base URL of our app will be [http://localhost:8000](http://localhost:8000).

_**The combination of the URL Pattern '/' and the HTTP verb 'get' ensures that this route will be reached when a GET request made by the client from the base URL.**_

If you'd like, you could pull out the callback function to get even more visual clarity on what is happening here. \(Run nodemon to convince yourself that this does not change any functionality of the program.\)

```javascript
const hello = (req, res) => {
  res.send('Hello, World!');
}

app.get('/', hello);
```

By design, the express `get()` function will pass two arguments into the callback function:
* the request object 
* the response object 

That is why we define a callback function with two parameters.

## Anatamy of an Express Route

```
[express instance].[HTTP verb]([url pattern], [callback])
```
**And the callback looks like this:**
```
([request obj], [response obj]) => {
    // handle data here, if needed
    // call a method from the response object here
}
```

## The Request and Response Objects

Our callback functions for our routes receive two very special objects from Express. They are provided to our function very much like the `event` object holding all the event data is passed into our event listener callbacks, or like each item in an array is passed into our `forEach()` callback.

### request

The Request object, frequently abbreviated to `req`, contains all the data we would ever need about the actual request that came in. What are they requesting? What browser are they using? Bunches of other stuff. But mostly we will using three keys inside of it:

* `req.body` - this is where any submitted form data will be stored for us.
* `req.params` - this is where special route variables are stored for us.
* `req.query` - this is where the query string data is stored.

As you can see, most of the time, if we are accessing the `req` object, its because we need to get at some data being sent to us from the user.

### response

The Response object, or `res` for short, is what we use to send something back to the user's browser, or more formally, send a response to the request. There are a number of functions we can use:

* `res.send()` - sends back a simple string. Not really used in production. This is kind of like the `console.log()` for network requests. Good for testing if the route is working.
* `res.sendFile()` - more sophisticated in that it can send an entire file back but file is static.
* `res.render()` - used to render data into templates with the selected template engine. More on this later.
* `res.json()` - used to send object data back as JSON. Very common when writing a backend API. Much more on this later.

You'll get more comfortable with all of this as we do more examples.

## 2nd Express App: Fun With Routes

### Set up the project

#### 1. Create a new directory called route-fun

```bash
mkdir route-fun
```

#### 2. Initialize NPM

```bash
cd route-fun
npm init
```

#### 3. Install Express

```bash
npm i express
```

#### 4. Create entry point

```bash
touch index.js
```

#### 5. Create an instance of express

_**index.js**_

```javascript
const express = require('express');
const app = express();
```

#### 6. Establish the base URL

_**index.js**_

```javascript
const express = require('express');
const app = express();

app.listen(8000);
```

#### 7. Write a home route

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send("You've reached the home route!");
});

app.listen(8000);
```

Run nodemon and visit localhost:8000 to make sure everything is working.

### More Route Styles

#### Paths

Now let's try adding another route that has the URL pattern of a string after the root slash:

```javascript
app.get('/', (req, res) => {
  res.send('You\'ve reached the home route!');
});

app.get('/about', (req, res) => {
  res.send('This is a practice app to learn about express routes.');
});
```

Visit localhost:8000/about to view the response from this route. We have made a "directory" in our app that will deliver the results of a different function whenever someone hits our site's `/about` URL.

This is one of the primary ways in which we organize our site. Every part of our site **should** be bookmarkable in a browser - which means that each section needs a distinct URL. This is how we make our web server respond to different URLs.

#### Parameters

We can also pass variables in as part of a URL. By putting a colon before a string in our route, we can create routes with different variables, or **parameters**. These parameters are automatically pulled out for us by Express and can be accessed via the `req.params` object.

```javascript
app.get('/', (req, res) => {
  res.send("You've reached the home route!");
});

app.get('/about', (req, res) => {
  res.send('This is a practice app to learn about express routes.');
});

app.get('/:input', (req, res) => {
  console.log("req.params: ", req.params)
  res.send("Our parameter is " + req.params.input + ".");
});
```

We can name them whatever we like. The string we use after the colon will be the name of the key added to the `req.params` object which will contain whatever the user typed in there after the root slash.

We can combine parameters and paths.

```javascript
app.get("/greet/:name", (req, res) => {
  res.send("Hello " + req.params.name + "!");
});
```

And we can have more than one parameter:

```javascript
app.get("/greet/:name/:lastname", (req, res) => {
  res.send("Hello " + req.params.name + " " + req.params.lastname);
});

app.get("/multiply/:x/:y", (req, res) => {
  res.send("The answer is: " + (req.params.x * req.params.y));
});

app.get("/add/:x/:y", (req, res) => {
  res.send("The answer is: " + (req.params.x + req.params.y));
});
```

Wait, what happened with that last route?? URL parameters come in as strings, so Javascript just concatonated them instead of treating them as integers and adding them. We can fix that:

```javascript
app.get("/add/:x/:y", (req, res) => {
  res.send("The answer is: " + (parseInt(req.params.x) + parseInt(req.params.y)));
});
```

Say we want to add any number of integers together. We could use wildcard route, denoted by an asterisk!

First let's take a look at how the asterisk works:

```javascript
app.get("/add/*", function(req, res) {
  res.send(req.params);
});
```

Now let's split up the wildcard parameter and sum using _reduce_:

```javascript
app.get("/add/*", (req, res) => {
  let myParams = req.params[0].split("/");
  let result = myParams.reduce((total, num) => {
    return total + parseInt(num)
  }, 0);
  res.send("The answer is  " + result);
});
```

### Query Strings

One last thing we can do in our routes is pass in a special set of key-value pairs as the last part of the URL. They are called query strings because they are typically only included with GET requests which are conventionally used to query data from some source. The query string gives us a way to pass in additional parameters to the query.

In the following URL:

`https://www.domain.com/some/data?key1=value&key2=value2`

The query string starts at the question mark \(?\) and goes through the end of the URL. The syntax is `key=value`. If you need more than one pair, they can be separated with ampersands \(&\) as you see above.

Let's add a new route where we can play with this. After all the other routes but before the line that starts the server listening, add a new route:

```javascript
app.get("/querystring", (req, res) => {
  let printout = '';
  for (let key in req.query) {
    printout += key + ": " + req.query[key] + "<br />";
  }
  res.send("Here's what they sent: <br /><br />" + printout);
});
```

As you can see, we don't need to do anything special to our URL pattern. Any route that we make can accept a query string. All we need to do is look inside of `req.query`. This one will loop over the `req.query` object to see if it has anything and will print whatever keys it finds. We can test it by hitting our server in a browser window: `http://localhost:8000/querystring?name=Steve&food=tacos`. Try replacing those key-value pairs or adding some more.

## Conclusion

In this example, we focused on the URL patterns. The HTTP verbs will come into play more when we start working with true CRUD functionality. For now, everything is a GET request.

## Lab

Continue to the next page, or checkout the [express routes calculator](https://github.com/WDI-SEA/express-routes-calc), for labs on express routes.
