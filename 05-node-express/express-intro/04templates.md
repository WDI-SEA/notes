# Templates

### Pre-reqs:
* Express Personal Website from views lesson

## Template Engines

The downside to this method is that we are only sending HTML files, but what if we want to customize what's on the page? On the front-end, we could manipulate the DOM with Javascript, that's certainly an option! But what if we want to display data that we pull from a database? ***Template engines*** allow us to inject values into the HTML, and even script logic into the HTML. This will be extremely useful for building in CRUD functionality and full stack apps in general. ([docs](https://expressjs.com/en/guide/using-template-engines.html))

### EJS: Embedded Javascript

There are several javascript template engines for express, one of the most popular of which, is [EJS](https://www.npmjs.com/package/ejs), available via npm. Let's update our express personal website views with EJS.

#### Install EJS

Add EJS to your personal website project using npm:

```bash
npm install ejs
```

#### Set the view engine to EJS

Above your routes, add an ```app.set(name, value)``` statement [ docs(https://expressjs.com/en/api.html#app.set) ] where the name is the ```view engine``` property and the value is ```ejs```.

```js
app.set('view engine', 'ejs');
```
#### Adapt your routes to ejs

***1.*** Rename the .html files to .ejs files.

***2.*** Replace your ```res.sendFile(<absolute path>)``` statements with ```res.render(<file name>)``` statements.

***3.*** Ejs assumes a lot about the path to the template files, so as long as they are nested in a ```views``` folder and have ```.ejs``` extensions, you can simply pass the filename (no extension, though it wont break it if you include it) into ```res.render()```.

Your home route should look like this:
```js
app.get('/', function(req, res) {
  res.render('index.ejs');
});
```

### The Cool Part: Templating with Variables

_Templating with variables_ means we can pass in an object to `res.render()` and access the values stored in it as variables inside the ejs template.

This is best demonstrated with an example. Create an object with at least one key-value pair and pass that object in as the second argument to the render function in one of your routes:

**index.js**
```js
app.get('/', function(req, res) {
  res.render('index', {name: "Sterling Archer", age: 35});
});
```

We now have access to a _name_ variable inside our ```index.ejs``` file! We can access this variable by embedding it into the html using this notation: ```<%= embedded js goes here %>```.

For example:
**index.ejs**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, <%= name %>!</h1>
  </body>
</html>
```

The _any JavaScript_ can be embedded using the `<% %>` tags. The addition of the `=` sign on the opening tag means that a value will be _printed to the screen_. 

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, <%= name %>!</h1>
    <h2>You are <%= age*7 %> in dog years.</h2>
  </body>
</html>
```

`<%  %>` _without_ the `=`  will not print out the expression, but it will execute it. This comes in handy for `if` statements and loops.

This doesn't only apply to primitive variables. We can even include variable declarations and iterators using ejs.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, <%= name %>!</h1>
    <% var dogAge = age*7 %>
    <h2>You are <%= dogAge %> in dog years.</h2>
    <% var status %>
    <%if (dogAge<100) {%>
      <% status = 'young' %>
    <%} else {%>
      <% status = 'old' %>
    <% } %>
    <h3>This means you are <%=status%>!</h3>

    <% var obsessions = ['spying', 'sarcasm', 'Kenny Loggins']; %>

    <ul>
    <% obsessions.forEach(function(item) { %>
      <li><%= item %></li>
    <% }); %>
    </ul>
  </body>
</html>
```

### Partials

Partials can be used to modularize views and reduce repetition. A common pattern is to move the header and footer of a page into separate views, or partials, then render them on each page.

#### Example

**partials/header.ejs**
```html
<!DOCTYPE html>
<html>
<head>
  <title>My Site</title>
</head>
<body>
```

**partials/footer.ejs**
```html
</body>
</html>
```

**index.ejs**
```html
<% include ../partials/header.ejs %>

<h1>Welcome to my site!</h1>

<% include ../partials/footer.ejs %>
```
