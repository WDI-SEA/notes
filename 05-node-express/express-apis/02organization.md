# Lab: Layouts and Controllers

### Prereqs:
* ability to create a basic node/express app with basic routes and views

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

## Controllers & Express Router

Controllers are more important the more views you have, so let's create a few more views.

***1.*** Inside the `views` folder, create a `faves` folder and move your `foods.ejs` and `animals.ejs` files into it.

***2.*** Inside the `views` folder, create a `hates` folder that also contains a `foods.ejs` file and an `animals.ejs` file, but design these views to display your least favorite foods and animals.

***3.*** Change the URL patterns in your existing routes and write two more routes so that your routes now reflect the new file structure of your views. 

We have been placing all routes into `index.js` when creating a Node/Express app, but this can get cumbersome when dealing with many routes. The solution is to group related routes and separate these groups into separate files. These files will go into a `controllers` folder.

***1.*** Create a `controllers` folder inside the root directory. 

***2.*** Inside the `controllers` folder, create a file called `faves.js` with the following routes:

```js
var express = require("express");
var router = express.Router();

router.get('/foods', function(req, res) {
  res.render('foods.ejs');
});

router.get('/animals', funciton(req, res) {
  res.render('animals.ejs');
});

module.exports = router;
```

***3.*** Express has a `Router()` function that will help us wrap these routes into a module that we'll export back into our main server file. Add these wrapper lines of code to `faves.js`

```js
var express = require("express");
var router = express.Router();

router.get('/foods', function(req, res) {
  res.render('foods.ejs');
});

router.get('/animals', funciton(req, res) {
  res.render('animals.ejs');
});

module.exports = router;
```
***4.*** Now back in `index.js`, we just need to add some middleware to get these routes working again!

**index.js**
```js
var faves = require("./controllers/faves") //import the faves routes
app.use("/faves", faves); //look inside `/views/faves` for the ejs files
```

Note that we defined the routes *relative* to the definition in `app.use`.

Check that these routes are working by visiting `http://localhost/faves/foods` and `http://localhost/faves/animals`.

Now finish the lab off by doing the same for your hates pages!
