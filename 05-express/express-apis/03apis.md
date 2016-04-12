# APIs with Express

In order to get around issues such as [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) and API access control, we can communicate with other servers through our server. In this case, our server acts as both a client and a server. We'll be doing some requests using the `request` Node module.

To use the module, install it using npm.

```bash
npm install --save request
```

Here's an example from NPM's homepage for the `request` module. Let's take a look at it.

```js
var request = require('request');
request('http://www.google.com', function (error, response, body) {
  if (!error && response.statusCode == 200) {
    console.log(body) // Show the HTML for the Google homepage.
  }
});
```

Identify what's necessary for making a server-side request.

* module import
* request function
  * URL
  * any other data or headers that need to be passed (optional)
  * callback function (the code that runs once the request finishes)
    * checking for errors
    * checking the response code
    * handling the body of the response

You can make a `.js` file that only has this code, and try running it with Node. See what happens.

###Incorporating `request` into Express

In order to incorporate the `request` module into Express, we can set up a basic Express application and place the request code inside a route.

This can be done by creating a new directory, running `npm init`, then installing the correct dependencies (refer back to the notes if you forgot). Here's an example app.

####Example

**index.js**

```js
var express = require('express');
var request = require('request');
var app = express();

app.get('/', function(req, res) {
  request('http://www.google.com', function (error, response, body) {
    if (!error && response.statusCode == 200) {
      res.send(body);
    }
  });
});

app.listen(3000);
```

Note that this app sends out the HTML for http://www.google.com, minus the images due to the images having links **relative** to http://localhost:3000

Let's use a more useful source of data that we can parse, like OMDB (Open Movie Database)

###Fetching JSON data

Let's modify the example above to make a request to OMDB's API. [OMDB Link](http://www.omdbapi.com/)

**We'll be using this endpoint:** http://www.omdbapi.com/?s=star+wars

####Modified Example

**index.js**

```js
var express = require('express');
var request = require('request');
var app = express();

app.get('/', function(req, res) {
  var qs = {
    s: 'star wars'
  };

  request({
    url: 'http://www.omdbapi.com',
    qs: qs
  }, function (error, response, body) {
    if (!error && response.statusCode == 200) {
      var dataObj = JSON.parse(body);
      res.send(dataObj.Search);
    }
  });
});

app.listen(3000);
```

**Things to Note**

* In order to pass a query string to OMDB, we can create an object with key-value pairs.
  * We also need to modify our request so it takes an object with the `url` and `qs`.
* After getting the response back, we need to **parse** the body using `JSON.parse`. Otherwise, we'll be treating the body as a string instead of an object.
* It's very important to call `res.send` in the correct place (the request callback)
  * Try putting `res.send` outside of the `request` function two lines down. You'll get an error!

### Creating UI From JSON
Requests allows us to get data, but it's not displayed very pretty. Let's build a template to display the data.

Create a file `views/results.ejs` to display all of the results:

```html
<!DOCTYPE>
<html>
  <head>
    <title>Star Wars</title>
  </head>
  <body>
    <h1>Star Wars</h1>
    <% results.forEach(function(result) { %>
      <% include ../partials/result %>
    <% }); %>
  </body>
</html>
```

Create a file `partials/result.ejs` to define how each result should be displayed.
Creating a directory called `partials` is a good way to organize sites. Create files
that represent entire pages under `views` and place templates for small components of
the site in the `partials` directory.


```html
<h2>
  (<%= result.Year %>) <%= result.Title %>
</h2>
<img src="<%= result.Poster %>">
```

Render the page with the parsed results passed as a paramter:
```js
var dataObj = JSON.parse(body);
res.render("results", {results: dataObj.Search});
```
