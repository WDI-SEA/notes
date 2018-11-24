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
| GET | /dinosaurs | Index (Read) | lists all animals |
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

### 2. Set up Index / Read (GET) route

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

In the above example we load the `dinosaurs/index.ejs` view and pass it `dinoData` as `myAnimals`. Now we can access myDinos directly in the `index.ejs` file.

### 3. Show / Read (GET)

_Show_ is a route that displays a single item of a specific type. It is a GET
request to (in this example) `/dinosaurs/1`

Create a `dinosaurs/show.ejs` file:

```html
<%= myDino.name %> is a <%= myDino.type %>.
```

**Show route -- in index.js**

```js
//express index route for animals (lists all animals)
app.get('/animals/:idx', function(req, res) {
  // get animals
  var animals = fs.readFileSync('./data.json');
  animals = JSON.parse(animals);

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




Display the animal based on the url. With the example `/animals/1` we would be
displaying the 2nd item in the array (index starting at 0) and get output like
this...

Fido is a dog.

###Create (POST)

To create an item (animal in this example) we need to make a POST to the url `/animals` with the data about that animal. We do this using a form with the method attribute set to `post` and the action set to the create url.

**frontend - form html**
```html
<form method="POST" action="/animals">
  <label for="animalType">Type</label>
  <input type="text" name="type">

  <label for="animalName">Name</label>
  <input id="animalName" type="text" name="name">

  <input id="animalType" type="submit">
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
var express = require('express');
var bodyParser = require('body-parser');
var app = express();

app.set('view engine', 'ejs');

// tell your app to use the module
app.use(bodyParser.urlencoded({extended: false}));
```

Note that we set an attribute `extended` to `false` when telling our app to use the body parser. This attribute determines which library is used to parse data. Discussion on extended [here](http://stackoverflow.com/questions/29175465/body-parser-extended-option-qs-vs-querystring).

Now, if we try to add this backend route, calling `req.body` should contain the form input.

**backend - express route**
```js
app.post('/animals', function(req, res) {
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
going to use the JSON file created above to store our data. This will involve three steps:

* Reading the JSON file
* Pushing the new animal to the object
* Writing the new JSON file

```js
app.post('/animals', function(req, res) {
  // read animals file
  var animals = fs.readFileSync('./data.json');
  animals = JSON.parse(animals);

  // add item to animals array
  animals.push(req.body);

  // save animals to the data.json file
  fs.writeFileSync('./data.json', JSON.stringify(animals));

  //redirect to the GET /animals route (index)
  res.redirect('/animals');
});
```

####Additional: Show / Read (GET) with a Form

There may be instances where you need to GET animals, but you don't want them all. A good example is filtering animals with a specific name via a search bar.

In these cases, you don't want to use a POST action, because POST is reserved for creating new resources. Instead, we can create another form with a GET method, and read the data via a **querystring**.

**Animals index page**

```html
<form method="GET" action="/animals">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>
```

Note that this form will submit to the same page. We'll need to see if there's a querystring, then filter the animals if one is present.

```js
app.get('/animals', function(req, res){
  var animals = fs.readFileSync('./data.json');
  animals = JSON.parse(animals);

  var nameFilter = req.query.nameFilter;

  if (nameFilter) {
    animals = animals.filter(function(animal) {
      return animal.name.toLowerCase() === nameFilter.toLowerCase();
    });
  }

  res.render('animals/index', {myAnimals: animals});
});
```

## Wrapup

* Node.js/Express
* Routes
* Views/templates
* CRUD/RESTful
* creating an app with GET and POST
