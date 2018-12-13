# Lab: Layouts and Controllers

Express gives us a lot of flexibility out of the box (configuration over convention). While this is a good thing, it can become a problem when we don't take the time to organize our project.

### Objectives

* Utilize layouts and controllers in an Express app

### Prereqs:
* ability to create a basic node/express app with basic routes and views

### Set Up a new Express App

Before we do anything else, let's set up a new basic Express app called `faves-hates-app`.

#### 1. Create a new project

#### 2. Initialize Node

#### 3. Install Dependencies
* express
* ejs

#### 4. Set up Express
* `index.js` file
* require express
* create an instance of express
* tell the app which port to listen to

#### 5. Set up EJS
* set view engine to ejs
* create a `views` folder

## EJS Layouts

Adding partials can dry up the code a bit, but [EJS Layouts](https://www.npmjs.com/package/express-ejs-layouts) can take this modularity even farther and make a big diffence with large applications.

EJS layouts is a node package that allows us to create a boilerplate (aka a _layout_) that we can inject content into based on which route is reached. Layouts normally include header and footer content that you want to display on every page (navbar, sitemap, logo, etc.).

### Install EJS Layouts

#### Step 1: Install EJS layouts

Install `express-ejs-layouts` via npm

```
npm install express-ejs-layouts
```

#### Step 2: Set up EJS layouts

Require the module and add it to the app.

***index.js***
```js
var express = require('express');
var app = express();
var ejsLayouts = require('express-ejs-layouts');

app.set('view engine', 'ejs');
app.use(ejsLayouts);

app.listen(3000)
```

What is ```app.use()```? This is an express function that indicates _middleware_. Middleware functions intercepts the request object when it comes in from the client, but before it hits any route. We'll see more examples of middleware later.

How are you supposed to know that ejs layouts requires middleware? [The docs.](https://www.npmjs.com/package/express-ejs-layouts)

#### Step 3: Create a Layout

In the root of the views folder, add a layout called `layout.ejs`. It _must_ be called `layout.ejs`, as mandated by `express-ejs-layouts`.

**layout.ejs**
```html
<!DOCTYPE html>
<html>
<head>
  <title>Faves&Hates</title>
</head>
<body>
  <%- body %>
</body>
</html>
```

This layout will be used by all pages, and the content will be filled in where the `<%- body %>` tag is placed. `<%- body %>` is a special tag used by `express-ejs-layouts` that cannot be renamed.

#### Step 4: Use the Layout

In the views folder, create a `home.ejs` file:

***home.ejs***
```html
<h1>This is the home page!</h1>
```

Now create a home route in `index.js` below the middleware:

```js
app.get('/', function(req, res) {
  res.render('home');
});
```

Ejs will assume that `home` means `home.ejs`. Now starte nodemon and check that your home page renders as desired.

#### Step 5: Set up a few more views/routes
***index.js***
```js
app.get('/animals', function(req, res) {
  res.render('animals', {title: 'Favorite Animals', animals: ['sand crab', 'corny joke dog']})
});
```
***animals.ejs***
```html
<h1><%= title %></h1>
<ul>
  <% animals.forEach(function(animal) { %>
    <li><%= animal %></li>
  <% }) %>
</ul>
```

Visit `localhost:3000/animals` to make sure that all is well.

Now create a `foods` view/route that displays your favorite foods, just like you did with animals.

#### Bonus: Add Navigation

Add a simple navigation list to the to of the layout page so there's a link to every page from every page:

***layout.ejs***
```html
<!DOCTYPE html>
<html>
<head>
  <title>Faves&Hates</title>
</head>
<body>
  <ul>
    <li><a href='/foods'>Favorite Foods</a></li>
    <li><a href='/animals'>Favorite Animals</a></li>
  </ul>
  <%- body %>
</body>
</html>

```

## Controllers & Express Router

Controllers become important organizational tools when you start making apps with several views, so let's create a few more views.

***1.*** Inside the `views` folder, create a `faves` folder and move your `foods.ejs` and `animals.ejs` files into it.

***2.*** Inside the `views` folder, create a `hates` folder that also contains a `foods.ejs` file and an `animals.ejs` file, but design these views to display your least favorite foods and animals.

***We have been placing all routes into `index.js` when creating a Node/Express app, but this can get cumbersome when dealing with many routes. The solution is to group related routes and separate these groups into separate files. These files will go into a `controllers` folder.***

***3.*** Create a `controllers` folder inside the root directory the all routes except for the home route. 

***4.*** Inside the `controllers` folder, create a file called `faves.js` with the following routes:

```js
app.get('/foods', function(req, res) {
  res.render('faves/foods', {title: 'Favorite Foods', foods: ['coconut', 'avocado']});
});

app.get('/animals', function(req, res) {
  res.render('faves/animals', {title: 'Favorite Animals', animals: ['sand crab', 'corny joke dog']})
});

```

But wait! `app` doesn't exist in this file! Express has a `Router()` function that will help us wrap these routes into a module that we'll export back into our main server file.

***5.***  Add these wrapper lines of code to `faves.js`, and replace `app` with `router`.

```js
var express = require('express');
var router = express.Router();

router.get('/foods', function(req, res) {
  res.render('faves/foods', {title: 'Favorite Foods', foods: ['coconut', 'avocado']});
});

router.get('/animals', function(req, res) {
  res.render('faves/animals', {title: 'Favorite Animals', animals: ['sand crab', 'corny joke dog']})
});

module.exports = router;
```
***6.*** Now back in `index.js`, we just need to add some middleware to get these routes working again!

**index.js**
```js
app.use('/faves', require('./controllers/faves'));
```

Note that we defined the routes *relative* to the definition in `app.use`. In other words, take note that our URL patterns in `faves.js` don't inclued `'/faves'`, because that is taken care of by the middleware.

Check that these routes are working by visiting `http://localhost/faves/foods` and `http://localhost/faves/animals`.

Now finish the lab off by doing the same for your hates pages!
