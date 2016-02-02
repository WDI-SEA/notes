![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Introduction to Node.js and Express

## Objectives
* Interact with a package manager
* Create Express routes that utilize parameters and form middleware
* Contrast and implement different HTTP verbs through Express routes
* Implement and explain the components of a basic Express app

## Review: Client-Server

* What's the front-end?
* What's the back-end?
* Why do we need a back-end?

## Node
Node is a platform that uses JavaScript for creating network applications. It allows JavaScript to be run on a server. So far, we've been using it to practice JavaScript concepts, but now we'll be using it for more interesting purposes.

We'll see that there are functions and patterns unique to Node (for example, the `require` function in Node, which is not available in the browser). Let's go over some unique aspects of Node before we get started with Express.

### Importing and Exporting Modules with Node
Node's module system allows code written in a partiuclar file (or folder) to be exported, and then imported into other files. Here's an example of a module called `Person.js` being imported into a file.

**Person.js**
```js
var Person = function(name) {
  this.name = name;
};

module.exports = Person;
```

**app.js**
```js
var Person = require('./Person.js');

var brian = new Person('Brian');
```

To view a practical example of importing and exporting modules, read
[this article](http://www.sitepoint.com/understanding-module-exports-exports-node-js/). You'll see that we can export multiple functions by assigning `module.exports` to an object. This is a pattern that we'll see frequently in Node.


### Managing Packages

The manager we use to keep track of these different groups of modules is called **npm**, short for **N**ode **P**ackage **M**anager. Think of a node package as an external library, like jQuery, but on the back-end. We can run npm to install different packages, which are stored in a file called `package.json`. We'll get into installing packages when using Express.

##Express

To create a web application using Node, we're going to import a web app server framework called Express. We can install this as a package using npm, then use it to create applications.

##Our first Express App

###Setting up a project
Create a new folder for use with the project using `mkdir node_calculator`, and cd into `cd node_calculator`

First we want to start a new project by going `npm init`. Follow the instructions, clicking `enter` through the statements. you many want to specify a version number, but most default options should be fine. It will also specify an initial file to use. The default is `index.js`, and this acts as the "entry point" into our app.

```bash
npm install --save express
touch index.js
```

###Installing nodemon
```bash
npm install -g nodemon
```

If we just ran `node nameOfFile.js`, node will not update if we make changes to the file. Nodemon solves this problem by updating the file once changes have been made. Install nodemon (only have to do this once), we will run our apps using the syntax

```bash
nodemon nameOfFile.js
```

**Note:** We've been using the `--save` and `-g` flags when installing using npm. `--save` is used when you want to add the package to your `package.json` file. `-g` installs the package globally. You'll want to reserve `-g` for packages that will be run in the command line.

###index.js

The following example shows how to get routes working in Node. A **route** is a combination of a URL pattern + HTTP Verb (get, post, put, delete). These verbs represent a method for the request.

Each route is called on our Express app, and takes a URL pattern and a callback function. The callback function gives us back the request (`req`) and response to send back to the client (`res`). Calling the `.send` function on the response sends a string back to the client.

```js
var express = require('express');
var app = express();

app.get('/', function(req, res){
  res.send('hello brian');
});

app.listen(3000);
```

###More Route Styles

By putting a colon before a string in our route, we can create routes with different variables, or **parameters**. These parameters are automatically pulled out for us by Express and can be accessed via the `req.params` object.

```js
var express = require('express');
var app = express();

app.get('/', function(req, res){
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

## Views and Templates

### Views

Fistly, we cannot keep using `res.send` to send a response. Ultimately, we'll want to send HTML files back to the client. It would be much more efficient to store them in files. Let's make a folder, `/views`, and create an `index.html` page inside.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Testing a View</title>
  </head>
  <body>
    <h1>Hello world!</h1>
  </body>
</html>
```

Let's modify the `index.js` to send this file via `.sendFile`. In order to use this function, we also need to add where `.sendFile` can find the views.

**index.js**
```js
var express = require('express'),
    app = express();

// this sets a static directory for the views
app.use(express.static(__dirname + '/views'));

app.get('/', function(req, res){
  // use sendFile to render the index page
  res.sendFile('index.html');
});

```

### Templating with ejs

The downside to this method is that we are only sending HTML files, and what if we want to customize what's on the page? On the front-end, we could manipulate the page using jQuery. But on the back-end, we can inject values into the HTML using template engines. So we're going to set up a template engine called **ejs** (embedded JavaScript) and use that instead.

We need to do a couple steps to get the template engine working.

First, install `ejs` by running `npm install --save ejs` in the command line.

Then, replace the `app.use` statement with the following statement (ejs assumed we'll be placing all template files into the `/views` folder, so it's optional if adhering to that syntax).

```js
app.set('view engine', 'ejs');
```

Also, rename the .html file to a .ejs file. We'll see that the `.ejs` extension is optional in the route, but necessary in the file's actual name.


### Templating with Variables

Templating with variables means we can pass in an object to the `.render` function and access those variables inside the ejs template.

**index.js**
```
var express = require('express'),
    app = express();

app.set('view engine', 'ejs');

app.get('/', function(req, res){
  res.render('index', {name: "Sterling Archer"});
});

```

then we need to update our `index.ejs` to use a templating variable.

**index.js**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Testing a View</title>
  </head>
  <body>
    <h1>Hello, <%= name %>!</h1>
  </body>
</html>
```

The JavaScript being embedded is enclosed by the `<% %>` tags. The addition of the `=` sign on the opening tag means that a value will be printed to the screen.

This doesn't only apply to primitive variables. We can even include variable declarations and iterators using ejs.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Testing a View</title>
  </head>
  <body>
    <h1>Hello, <%= name %>!</h1>

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


##Intro to CRUD

CRUD is an acronym that stands for Create, Read, Update, Destroy. These are the basic operations that you can perform on data. Most sites you interact with on the internet are CRUD sites. Almost everything you do on the web is a CRUD action: Creatinging a user (create), Listing comments (read) to editing your profile (update), to deleting a video you uploaded on youtube (destroy).

[Formal definition on wiki](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

####RESTful Routing

On the web the best practice for CRUD actions uses something called RESTful routing. The basic idea is your route (URL) should relate to the type of item you are interacting with.

So if you were CRUDing Animals the route would be `/animals` and the following routes would form a full set of CRUD RESTful routes

| VERB | URL | Action (CRUD) | Description |
|------|-----|---------------|-------------|
| GET | /animals | Index (Read) | lists all animals |
| GET | /animals/1 | Show (Read) | list information about a specific animal (id = 1) |
| POST | /animals | Create | creates an animal with the POST payload data |
| UPDATE | /animals/1 | Update | updates the data for a specific animal (id = 1) |
| DELETE | /animals/1 | Delete (Destroy) | deletes the animal with the specified id (1) |

[Read more on wiki](http://en.wikipedia.org/wiki/Representational_state_transfer)

##CRUD in action

For now we're just going to focus on POST and GET (Create and Read)

**Backend data store**

For this example assume we are using the following array as our data store.

```js
//data variable
var animals=[
    {name:'Neko',type:'cat'},
    {name:'Fido',type:'dog'},
    {name:'Mufasa',type:'lion'},
    {name:'Tony',type:'tiger'},
    {name:'Kuma',type:'bear'}
];
```

###Index / Read (GET)

Index is a route (URL) that lists all items of a specific type. It is a GET request to (in this example) `/animals`.

**Index route -- in index.js**

```js

//express index route for animals (lists all animals)
app.get('/animals', function(req, res){
    res.render('animals/index', {myAnimals: animals});
});
```

In the above example we load the `animals/index.ejs` view and pass it `animals` as `myAnimals`. This means in the index.ejs file we can access myAnimals directly.

**Index view -- in /views/animals/index.ejs**

```html
<ul>
    <% myAnimals.forEach(function(animal){ %>
    <li><%= animal.name %> is a <%= animal.type %></li>
    <% }); %>
</ul>
```

Here we are looping through the `myAnimals` array passed from the route and
displaying a list of all of the items.

**output would be something like this:**

* Neko is a cat
* Fido is a dog
* Mufasa is a lion
* Tony is a tiger
* Kuma is a bear

###Show / Read (GET)

Show is a route that displays a single item of a specific type. It is GET
request to (in this example) `/animals/1`

**Show route -- in index.js**

```js
//express index route for animals (lists all animals)
app.get('/animals/:idx', function(req, res){
    //get array index from url parameter
    var animalIndex = parseInt(req.params.idx);

    //render page with data of the specified animal
    res.render('animals/show', {myAnimal: animals[animalIndex]});
});
```

In the above example we load the `animals/show.ejs` view and pass it a specific
item from the `animals` array as `myAnimal`. We use the :idx url parameter to
specify which animal to display. Again, this means in the show.ejs file we can
access myAnimal directly.


```html
<%= myAnimal.name %> is a <%= myAnimal.type %>.
```

Display the animal based on the url. With the example `/animals/1` we would be
displaying the 2nd item in the array (index starting at 0) and get output like
this...

Fido is a dog.

###Create (POST)

To create an item (animal in this example) we need to make a POST to the url `/animals` with the data about that animal. We do this using a form with the method attribute set to `post` and the action set to the create url.

**frontend - form html**
```html
<form method="post" action="/animals">
    <input type="text" name="type">
    <input type="text" name="name">
    <input type="submit">
</form>
```

When the above form is submitted it will make a `POST` to the url `/animals` with the data contained in the form fields.

To receive this data we need to create a `POST` route in express and use the `body-parser` npm module to receive that data. But first, let's set up the `body-parser` module!


### BodyParser

Parsing parameters from a form needs an external module called `body-parser`.

```bash
npm install --save body-parser
```

**index.js**
```js
var express = require('express'),
    bodyParser = require('body-parser'),
    app = express();

app.set('view engine', 'ejs');

// tell your app to use the module
app.use(bodyParser.urlencoded({extended: false}));

app.get('/', function(req, res){
  res.render('index', {name: "Sterling Archer"});
});
```

Note that we set an attribute `extended` to `false` when telling our app to use the body parser. This attribute determines which library is used to parse data. Discussion on extended [here](http://stackoverflow.com/questions/29175465/body-parser-extended-option-qs-vs-querystring).

Now, if we try to add this backend route, calling `req.body` should contain the form input.

**backend - express route**
```js
app.post('/animals', function(req, res){
    //debug code (output request body)
    console.log(req.body);
    res.send(req.body);
});
```

Form data is passed as payload of the request. Every field that has a name will
be included in that payload and it is sent as form encoded text. When
`body-parser` is installed it automatically **parses** the form body into a
javascript object that we can use and it stores it in `req.body` so we can use it. All of this is done as middleware, which we just configured.

In the above example we could access the animal type form field by using
`req.body.type` and the name field by using `req.body.name`. This correlates
directly to the names given to the form fields in the **form html** above.

Generally, the code in the **express route** would contain code that would
CREATE an item in a database and redirect the user to a route with a confirmation
message of some sort or just back to the index route. For this example we're
going to use the array created above to store our data.

```js
app.post('/animals', function(req, res){
    //add item to animals array
    animals.push(req.body);

    //redirect to the GET /animals route (index)
    res.redirect('/animals');
});
```

## Wrapup

* Node.js/Express
* Routes
* Views/templates
* CRUD/RESTful
* creating an app with GET and POST
