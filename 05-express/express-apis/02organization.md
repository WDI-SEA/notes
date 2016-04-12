#Organizing an Express App

## Basic Express Setup

Before we do anything else, let's set up a basic express app. We need to install our dependencies, create the index.js server file, and create an index for our homepage.

```
mkdir organized-express-app
cd organized-express-app
npm install --save express ejs
```

index.js:
```
var express = require("express");
var app = express();
app.set('view engine', 'ejs');

app.get("/", function(req, res) {
  res.render("index", {title: "Favorite Foods", foods: ["sandwich", "corn dog"]})
});

app.listen(3000);
```

views/index.ejs:
```
<!DOCTYPE html>
<html>
  <head>
    <title>Webpage</title>
  </head>
  <body>
    <h1><%= title %></h1>
    <ul>
      <% foods.forEach(function(food) { %>
        <li><%= food %></li>
      <% }) %>
    </ul>
  </body>
</html>
```

## Layouts

Yesterday we used partials to create a header and a footer for our website. Adding a header and a footer to every page can be cumbersome. Why should we have to write the same lines at the beginning and end of every page? We shouldn't! There's a better way!

Instead, we can create a layout that has a special place for our page content. We can define a basic page structure made up of our header and footer and have a place in the middle where all our content will go. In order to do this, another module must be installed.

### Example

**Step 1:**
Install `express-ejs-layouts` via
```
npm install --save express-ejs-layouts
```

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

This layout will be used by all pages, and the content will be filled in where the `<%- body %>` tag is placed. `<%- body %>` is a special tag used by `express-ejs-layouts` that cannot be renamed.

Now we can create another page `animals.ejs` and see that it's content is placed in the page. We can create new pages without having to write the include statements for the header and footer.

First we add a simple route to `app.js`:

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

Add a simple navigation list to the to of the layout page so there's a link to every page from every page:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Page</title>
</head>
<body>
  <ul>
    <li><a href="/">Favorite Foods</a></li>
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
