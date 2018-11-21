# Lab: Layouts and Controllers

### Set Up a new Express App

Before we do anything else, let's set up a new basic Express app called `faves-hates-app`.

####1. Create a new project

####2. Initialize Node

####3. Install Dependencies
* express
* ejs

####4. Set up Express
* `index.js` file
* require express
* create an instace of express
* tell the app which port to listen to

####5. Set up EJS
* set view engine to ejs
* create a `views` folder

## EJS Layouts

Adding partials can dry up the code a bit, but [EJS Layouts](https://www.npmjs.com/package/express-ejs-layouts) can take this modularity even farther and make a big diffence with large applications.

EJS layouts is a node package that allows us to create a boilerplate (aka a _layout_) that we can inject whatever content into based on which route is reached. Layouts normally include header and footer content that you want to display on every page (navbar, sitemap, logo, etc.).

### Install EJS Layouts

#### Step 1: Install EJS layouts

Install `express-ejs-layouts` via npm

```
npm install express-ejs-layouts
```

#### Step 2: Set up EJS layouts

Require the module and add it to the app.

```js
var ejsLayouts = require("express-ejs-layouts");
app.use(ejsLayouts);
```

What is ```app.use()```? This is an express function that indicates _middleware_. Middleware is code that intercepts the request object when it comes in from the client, but before it hits any route. We'll see more examples of middleware later.

How are you supposed to know that ejs layouts requires middleware? [The docs.](https://www.npmjs.com/package/express-ejs-layouts)

#### Step 3: Create a Layout

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

This layout will be used by all pages, and the content will be filled in where the `<%- body %>` tag is placed. `<%- body %>` is a special tag used by `express-ejs-layouts` that cannot be renamed.

#### Step 4: Set up a few views/routes

Now we can create another page `animals.ejs` and see that it's content is placed in the page. We can create new pages without having to write the include statements for the header and footer.

First we add a simple route to `index.js`:

```js
app.get("/animals", function(req, res) {
  res.render("animals", {title: "Favorite Animals", animals: ["sand crab", "corny joke dog"]})
});
```

And we create a new file `views/animals.ejs`:

```html
<h1><%= title %></h1>
<ul>
  <% animals.forEach(function(animal) { %>
    <li><%= animal %></li>
  <% }) %>
</ul>
```

Now create a `foods` view/route that displays your favorite foods.

#### Bonus: Add Navigation

Add a simple navigation list to the to of the layout page so there's a link to every page from every page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Page</title>
</head>
<body>
  <ul>
    <li><a href="/foods">Favorite Foods</a></li>
    <li><a href="/animals">Favorite Animals</a></li>
  </ul>
  <%- body %>
</body>
</html>

```

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

Note that the routes should be defined *relative* to the definition in `app.use`. For example, the route defined above in `controllers/people.js` will be `http://localhost:3000/people`.

## Extra Resources

[Templating Your Node App](https://scotch.io/tutorials/use-ejs-to-template-your-node-application) - This site provides a good walk-through of using partials.
