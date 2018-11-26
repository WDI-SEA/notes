# CRUD in Express

## Objectives

* Name the HTTP Verb associated with each CRUD function
* Name the two HTTP verbs that HTTP understands
* Name the two HTTP verbs in which you must utilize AJAX to make HTTP understand them

## Review CRUD

Recall CRUD from the SQL database lessons. Most sites you interact with on the internet are CRUD sites. Almost everything you do on the web is a CRUD action. For example:
* ***Create*** a youtubeuser, a video, a comment
* ***Read*** comments, view videos, etc.
* ***Update*** your profile, edit a video title, etc.
* ***Delete*** a video, comment, or an entire channel!

[Formal definition on wiki](http://en.wikipedia.org/wiki/Create,_read,_update_and_delete)

## RESTful Routing

RESTful Routing is the (best) practice of choosing routes (URL patterns + HTTP verbs) that reflect the CRUD functionality of that route.
A RESTful route incorporates:
* the _item or data_ you're interacting with
* the _CRUD action_ you're performing on that item or data

On the web the best practice for CRUD actions uses something called RESTful routing. The basic idea is your route (URL) should relate to the type of item you are interacting with, as well as the action you'll be performing to change/view the state of the item(s).

### Example: Dinosaurs
So if you were CRUDing a database of dinosaurs, the following routes would form a full set of CRUD RESTful routes

| VERB | URL | Action (CRUD) | Description |
|------|-----|---------------|-------------|
| GET | /dinosaurs | Index (Read) | lists all dinosaurs |
| GET | /dinosaurs/1 | Show (Read) | list information about a specific animal (id = 1) |
| POST | /dinosaurs | Create | creates an animal with the POST payload data |
| PUT | /dinosaurs/1 | Update | updates the data for a specific animal (id = 1) |
| DELETE | /dinosaurs/1 | Delete (Destroy) | deletes the animal with the specified id (1) |

[Read more on wiki](http://en.wikipedia.org/wiki/Representational_state_transfer)

## CRUD in action: Dinosaur App

So far, we've only been rendering views, which is why we've been using GET for all of our routes. Now that we're working with data, we'll start to see how the other HTTP verbs come into play. Here we will focus on GET and POST.

### 1. Set up a new express app called `crud_dinosaurs`.

Incorporate `express-ejs-layouts`.

**Backend data store**

We'll start workign with data from an actual database soon, but for now we'll just focus on routes and use, a JSON object as our data store. In the root of the project, create a `dinosaurs.json` file with the following contents:

```json
[
  {
    "name":"Littlefoot",
    "type":"apatosaurus"
  },
  {
    "name":"Cera",
    "type":"triceratops"
  },
  {
    "name":"Ducky",
    "type":"saurolophus"
  },
  {
    "name":"Petrie",
    "type":"pteranodon"
  },
  {
    "name":"Spike",
    "type":"stegosaurus"
  }
]
```

### 2. Index / Read (GET) route

Index is a route (URL) that lists all items of a specific type. It is a GET request to (in this example) `/dinosaurs`.

Format the ejs to display the data. Assume that we will pass the data in as `myDinos`.

**Index view -- in /views/dinosaurs/index.ejs**
```html
<ul>
  <% myDinos.forEach(function(dino) { %>
  <li><%= dino.name %> is a <%= dino.type %></li>
  <% }); %>
</ul>
```

To access our data, we'll use the `fs` (filesystem) core module. Import this module in `index.js`
```js
var fs = require('fs');
```

Now let's pull in our data and take a took at it. 

```js
// lists all dinosaurs
app.get('/dinosaurs', function(req, res) {
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  console.log(dinosaurs);
});
```
 ***Note:*** This `console.log()` is in our server file, which means it will print to our terminal, NOT the browser inspector.
 
 That doesn't look very helpful, does it? That's because we're pulling in a JSON object, which isn't quite the same as a normal JS object. JSON (JavaScript Object Notation), is a standard format for data that is being transmitted (sent back and forth), and it needs to be _parsed_, or converted to a true JS data type - in this case, an array.  Read more about working with JSON [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON).

Try parsing the data before printing it:
```js
// lists all dinosaurs
app.get('/dinosaurs', function(req, res) {
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  var dinoData = JSON.parse(dinosaurs);
  console.log(dinoData);
});
```

That's more like it! Now lets send it to our EJS file:

```js
// lists all dinosaurs
app.get('/dinosaurs', function(req, res) {
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  var dinoData = JSON.parse(dinosaurs);
  res.render('dinosaurs/index', {myDinos: dinoData});
});
```

In the above example we load the `dinosaurs/index.ejs` view and pass it `dinoData` as `mydinosaurs`. Now we can access myDinos directly in the `index.ejs` file.

### 3. Show / Read (GET) route

_Show_ is a route that displays a single item of a specific type. Since we're still just reading data, it is a GET
request to (in this example) `/dinosaurs/1`

Create a `dinosaurs/show.ejs` file:

```html
<%= myDino.name %> is a <%= myDino.type %>.
```

Now let's write our show route. We can access the index from the url through the `req.params` object, but it will be a string. In order to use in to access an array value, we need to cast it to an integer.

**Show route -- in index.js**
```js
//express show route for dinosaurs (lists one dinosaur)
app.get('/dinosaurs/:idx', function(req, res) {
  // get dinosaurs
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  var dinoData = JSON.parse(dinosaurs);

  //get array index from url parameter
  var dinoIndex = parseInt(req.params.idx);

  //render page with data of the specified animal
  res.render('dinosaurs/show', {myDino: dinoData[dinoIndex]});
});
```

In the above example we load the `dinosaurs/show.ejs` view and pass it a specific
item from the `dinoData` array as `myDino`. We use the `:idx` url parameter to
specify which animal to display. This means in the `show.ejs` file we can
access myDino directly.

### 4. New / Read (GET) route

To create an item (dinosaur in this example) we need to get the data about that item, so we'll use a [form](https://www.w3schools.com/html/html_forms.asp).

Form tags have two attributes that are very import for their CRUD functionality:
* ***method:*** HTTP verb - `GET` or `POST`. You will use POST most often because it is significantly more secure. Read about the difference between these two methods by scrolling down to the "When to Use GET" AND "When to Use Post" sections of [this page](https://www.w3schools.com/html/html_forms.asp).
* ***action:*** This value should be a path. Specifically, it is the url pattern associated with the route that will handle the data - in this case, that will be the `/dinosaurs` POST route we will write.

Create a `dinosaurs/new.ejs` view that contains an html form:

```html
<form method="POST" action="/dinosaurs">
  <label for="dinosaureType">Type</label>
  <input type="text" name="type">

  <label for="dinosaurName">Name</label>
  <input id="dinosaurName" type="text" name="name">

  <input id="dinosaurType" type="submit">
</form>
```

Now write a `GET` route so we can view this form at `localhost:3000/dinosaurs/new`:

```js
app.get('/dinosaurs/new', function(req, res){
  res.render('dinosaurs/new');
});
```
Not working? Make sure this route is _above_ the show (`/dinosaurs/:idx`) route, otherwise the show route will catch the request and pass in "new" as `req.params.idx`.

### 5. Create (POST) route

When the above form is submitted it will make a `POST` to the url `/dinosaurs` with the data contained in the form fields. To receive this data, we need to create the `POST` route and use the node package `body-parser` to make the data readable. (If it bothers you that we're glazing over how the data comes through before we send it through something like `body-parser`, read [this article](https://medium.com/@adamzerner/how-bodyparser-works-247897a93b90). It will always make sense to use some sort of framework like `body-parser` in practice, but if you're interested in capturing the raw data, see [this article](https://itnext.io/how-to-handle-the-post-request-body-in-node-js-without-using-a-framework-cd2038b93190).)

***body-parser*** will store the data submitted from the form in a user-friendly `req.body` object.

install `body-parser` via npm and add it to your server file:

***index.js***
```js
var express = require('express');
var app = express();
var ejsLayouts = require('express-ejs-layouts');
var fs = require('fs');
var bodyParser = require('body-parser'); //

app.set('view engine', 'ejs');
app.use(ejsLayouts);
app.use(bodyParser.urlencoded({extended: false}));

.
.
.
```

The `bodyParser.urlencoded()` middleware tells body-parser to capture urlencoded data (form data) and store it in `req.body`. The `{extended: false}` option ensures that the values in this body will either be strings or arrays. More on this [here](https://www.npmjs.com/package/body-parser#bodyparserurlencodedoptions). Further discussion on it [here](http://stackoverflow.com/questions/29175465/body-parser-extended-option-qs-vs-querystring).

Now, if we can access the form data in a POST route!

***index.js***
```js
app.post('/dinosaurs', function(req, res) {
  console.log(req.body);
});
```

Try adding a new dinosaur and make sure you see the appropriate data come through in the terminal when you submit the form.


**body-parser Summary:**
Form data is passed as payload of the request. Every field that has a name will
be included in that payload and it is sent as form encoded text. When
`body-parser` is installed it automatically **parses** the form body into a
javascript object that we can use and it stores it in `req.body` so we can use it. All of this is done as middleware, which we just configured.

**The `name` attribute matters!**
In the above example we could access the dinosaur type form field by using
`req.body.type` and the name field by using `req.body.name`. This correlates
directly to the _names_ given to the form fields in the **form html** above.

Generally, the code in the **express route** would contain code that would
CREATE an item in a database and redirect the user to a route with a confirmation
message of some sort or just back to the index route. For this example we're
going to use the JSON file created above to store our data. This will involve three steps:

* Reading the JSON file
* Pushing the new animal to the object
* Writing the new JSON file

```js
app.post('/dinosaurs', function(req, res) {
  // read dinosaurs file
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  dinosaurs = JSON.parse(dinosaurs);

  // add item to dinosaurs array
  dinosaurs.push(req.body);

  // save dinosaurs to the data.json file
  fs.writeFileSync('./dinosaurs.json', JSON.stringify(dinosaurs));

  //redirect to the GET /dinosaurs route (index)
  res.redirect('/dinosaurs');
});
```

`JSON.stringify` does the opposite of `JSON.parse` - it converts javascript data into json data.

### Show / Read (GET) with a Form

There may be instances where you need to `GET` dinosaurs, but you don't want them all. A good example is filtering dinosaurs with a specific name via a search bar.

In these cases, you don't want to use a POST action, because POST is reserved for creating new resources. Instead, we can create another form with a `GET` method, and read the data via a **querystring**. This is an appropriate use of the `GET` form method because the user input is not sensitive.

Add a form to `dinosaurs/index.ejs`

```html
<form method="GET" action="/dinosaurs">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>
```

The idea here is that the search bar allows the user to filter what's on the page, so it will be a `GET` request to `/dinosaurs`... but we already have a route for that! When you submit a form using the `GET` method, the key/value pairs are appended to the URL in a _query string_. Try searching for a dinosaur now and notice what happens to the URL. This query string, like parameters (`req.params`) is available via the request object. We'll use a conditional to check if there's a querystring, then filter the dinosaurs if one is present.

```js
app.get('/dinosaurs', function(req, res) {
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  var dinoData = JSON.parse(dinosaurs);

  var nameFilter = req.query.nameFilter;

  if (nameFilter) {
    dinoData = dinoData.filter(function(dino) {
      return dino.name.toLowerCase() === nameFilter.toLowerCase();
    });
  }

  res.render('dinosaurs/index', {myDinos: dinoData});
});
```
