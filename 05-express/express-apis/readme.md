![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Express APIs

##Objectives

* Review the components of an Express application
* Utilize layouts and controllers in an Express app
* Understand the purpose of using APIs on the backend.
* Create an application that uses an API and the `request` module.

## Review

Express gives us a lot of flexibility out of the box (configuration over convention). While this is a good thing, it can become a problem when we don't take the time to organize our project.

## Layouts

Another layout option is to create a layout and have a body that is replaced with content (more similar to Rails, with a predetermined header/footer). In order to do this, another module must be installed.

### Example

**Step 1:**
Install `express-ejs-layouts` via the command `npm install --save express-ejs-layouts`

**Step 2:**
Require the module and add it to the app.
```js
var ejsLayouts = require("express-ejs-layouts");
app.use(ejsLayouts);
```

**Step 3:**
In the root of the views folder, add a layout called `layout.ejs`

**layout.ejs**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Page</title>
</head>
<body>
  <%- body %>
</body>
</html>
```

This layout will be used by all pages, and the content will be
filled in where the `<%- body %>` tag is placed.


## Controllers

We have been placing all routes into `index.js` when creating a Node/Express app, but this can get cumbersome when dealing with many routes. The solution is to separate routes into separate files and attach the routes to the Express router.

**index.js**
```js
var peopleCtrl = require("./controllers/people")
app.use("/people", peopleCtrl);
```

**controllers/people.js**
```js
var express = require("express");
var router = express.Router();

router.get("/", function(req, res) {

});

module.exports = router;
```

## APIs

In order to get around issues such as [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) and API access control, we can communicate with other servers through our server. In this case, our server acts as both a client and a server. We'll be doing some requests using the `request` Node module.

```bash
npm install --save request
```

Here's an example from NPM's homepage for the `request` module.

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

