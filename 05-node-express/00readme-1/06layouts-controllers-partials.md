# Layouts and Controllers

Express gives us a lot of flexibility out of the box \(configuration over convention\). While this is a good thing, it can become a problem when we don't take the time to organize our project.

### Objectives

* Utilize layouts and controllers in an Express app

### Prereqs:

* ability to create a basic node/express app with basic routes and views

### Set Up a new Express App

Before we do anything else, let's set up a new basic Express app called `love-it-or-leave-it`.

#### 1. Create a new project

#### 2. Initialize NPM

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

## Page Layouts using partials

Adding partials can dry up the code a bit, and by adding a header and a footer partial we can create 'wrappers' that make it easy to templatize our views.

_**index.js**_

```javascript
const express = require('express')

const app = express()

app.set('view engine', 'ejs')

app.listen(3000)
```

### Create a Layout

In the root of the `views` folder, create a `partials` folder, and touch two files in it touch two files:

* `header.ejs`
* `footer.ejs`

we are going to use these to files to wrap our `ejs` templates with an html boilerplate, and any other code we would like on every page to show, such as nav links. We can also include css and js files in `header.ejs` to apply those css and js files to all of our views.

**views/partials/header.ejs**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love It or Leave It</title>
</head>
<body>
    
<!-- notice how there are no closing tags for html and for body, this is important! -->
```

**views/partials/footer.ejs**

```html
</body>
</html>
```

We will wrap all of our `ejs` files with the header and footer.

### Use the Layout

In the views folder, create a `home.ejs` file:

_**views/home.ejs**_

```html
<%- include('header.ejs') %>

<h1>This is the home page!</h1>

<%- include('footer.ejs') %>                                 
```

Now create a home route in `index.js` below the middleware:

```javascript
app.get('/', (req, res) => {
  res.render('home');
});
```

Ejs will assume that `home` means `home.ejs`. Now start nodemon and check that your home page renders as desired.

### Set up a few more views/routes

_**index.js**_

```javascript
app.get('/animals', (req, res) => {
  res.render('animals', {animals: ['sand crab', 'corny joke dog']})
});
```

_**views/animals.ejs**_

```html
<%- include('header.ejs') %>

<h1>Favorite Animals</h1>
<ul>
  <% animals.forEach((animal) => { %>
    <li><%= animal %></li>
  <% }) %>
</ul>

<%- include('footer.ejs') %>  
```

Visit `localhost:3000/animals` to make sure that all is well.

### Exercise

* Create a `foods` route and view that displays your favorite foods, just like you did with animals.
* Create a `movies` route and view that displays your _least_ favorite movies.
* Create a `products` route and view that displays your _least_ favorite products.

### Bonus: Add Navigation

Add a simple navigation list to the top of the layout page so there's a link to every page from every page:

_**views/partials/header.ejs**_

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love It or Leave It</title>
</head>
<body>
  <ul>
    <li><a href='/foods'>Favorite Foods</a></li>
    <li><a href='/animals'>Favorite Animals</a></li>
    <li><a href='/movies'>Worst Movies</a></li>
    <li><a href='/products'>Worst Products</a></li>
  </ul>
```

### Bonus: Serve a Static css file

We in order to [serve static assests](https://expressjs.com/en/starter/static-files.html) with express (css, js, or image files for example), we have to tell express explicity what folder to use:

**index.js**

```javascript
const express = require('express')

const app = express()

app.set('view engine', 'ejs')

// tell express to send static assets, and where to find them
app.use(express.static('public'))

app.get('/', (req, res) => { 
    res.render('home')
})
```

What is `app.use()`? This is an express function that indicates _middleware_. Middleware functions intercepts the request object when it comes in from the client, but before it hits any route. We'll see more examples of middleware later.

Now, we can create the folder `public` that we told express about in the top level of our project, giving our directories this structure:

```text
├── index.js
├── package-lock.json
├── package.json
├── public
└── views
```

Touch a css file named `styles.css` in the public folder, and add some styles to it:

```css
body {
    background-color: orange;
}
```

this is our project's current directory structure:

```text
├── index.js
├── package-lock.json
├── package.json
├── public
│   └── styles.css
└── views
    ├── home.ejs
    └── partials
        ├── footer.ejs
        └── header.ejs
```

In order to link up our stylesheet, we can add it to our header file like so:

**views/partials/header.js**

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Love It or Leave It</title>
    <!-- when referencing static assets in our public folder, './' refers to the public folder -->
    <link rel="stylesheet" href="./styles.css" />
</head>
<body>
```

## Controllers & Express Router

Controllers become important organizational tools when you start making apps with several views, so let's organize the routs/views we have into two sections: `love-it` and `leave-it`.

_**1.**_ Change your routes to have the following url patterns:

* `/loveit/food`
* `/loveit/animals`
* `/leaveit/movies`
* `/leaveit/products`

Now check that these new url patterns render the expected html, and fix your nav bar to have the correct links.

_**We have been placing all routes into `index.js` when creating a Node/Express app, but this can get cumbersome when dealing with many routes. The solution is to group related routes and separate these groups into separate files. These files will go into a `controllers` folder.**_

_**2.**_ Create a `controllers` folder inside the root directory that will contain all routes except for the home route.

_**3.**_ Inside the `controllers` folder, create a file called `loveit.js`, and copy your two `loveit` routes into this file.

with the following routes:

```javascript
app.get('/loveit/foods', (req, res) => {
  res.render('foods', {foods: ['coconut', 'avocado']});
});

app.get('/loveit/animals', (req, res) => {
  res.render('animals', {animals: ['sand crab', 'corny joke dog']})
});
```

But wait! `app` doesn't exist in this file! Express has a `Router()` function that will help us wrap these routes into a module that we'll export back into our main server file.

_**4.**_ Add these wrapper lines of code to `loveit.js`, and replace `app` with `router`.

```javascript
const express = require('express');
const router = express.Router();

router.get('/loveit/foods', (req, res) => {
  res.render('foods', {foods: ['coconut', 'avocado']});
});

router.get('/loveit/animals', (req, res) => {
  res.render('animals', {animals: ['sand crab', 'corny joke dog']})
});

module.exports = router;
```

_**5.**_ Now back in `index.js`, we just need to add some middleware to get these routes working again!

**index.js**

```javascript
app.use('/loveit', require('./controllers/loveit'));
```

This middelware says _"Dear Express, if you get a request for a url pattern that starts with `/loveit`, please go to the `loveit` controller file to find the relevant routes."_ SO, by the time express is looking in the right controller file, it already has processed the `/loveit` part of the url pattern, thus, we can now remove that part from the routes in `controllers/loveit.js`:

```javascript
const express = require('express');
const router = express.Router();

router.get('/foods', (req, res) => {
  res.render('foods', {foods: ['coconut', 'avocado']});
});

router.get('/animals', (req, res) => {
  res.render('animals', {animals: ['sand crab', 'corny joke dog']})
});

module.exports = router;
```

Note that we defined the routes _relative_ to the definition in `app.use`. In other words, take note that our URL patterns in `loveit.js` don't inclued `'/loveit'`, because that is taken care of by the middleware.

Check that these routes are working by visiting `http://localhost/loveit/foods` and `http://localhost/loveit/animals`.

Finally, it is standard to organize your views the same way you organize your routes. This means we should create a subdirectory inside of `views` called `loveit` and move our `animals.ejs` and `food.ejs` files into it.

We also need ot update our `res.render()` lines accordingly:

```javascript
const express = require('express');
const router = express.Router();

router.get('/foods', (req, res) => {
  res.render('loveit/foods', {foods: ['coconut', 'avocado']});
});

router.get('/animals', (req, res) => {
  res.render('loveit/animals', {animals: ['sand crab', 'corny joke dog']})
});

module.exports = router;
```

Now finish the lab off by doing the same for your leave-it routes/pages!