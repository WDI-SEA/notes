# Get and Post

So far, we've only been rendering views, which is why we've been using GET for all of our routes. Now that we're working with data, we'll start to see how the other HTTP verbs come into play. Here we will focus on `GET` and `POST`.

## Objectives

* Implement `GET` and `POST` routes in `express`.

### 1. Set up a new express app called `RESTful_creatures`.

Incorporate `express-ejs-layouts`.

**Backend data store**

We'll start working with data from an actual database soon, but for now we'll just focus on routes and use, a JSON object as our data store. In the root of the project, create a `dinosaurs.json` file with the following contents:

```javascript
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

### 2. Index / Read \(GET\) route

Index is a route \(URL\) that lists all items of a specific type. It is a GET request to \(in this example\) `/dinosaurs`.

Format the ejs to display the data. Assume that we will pass the data in as `myDinos`.

**Index view -- in /views/dinosaurs/index.ejs**

```markup
<ul>
  <% myDinos.forEach(function(dino) { %>
  <li><%= dino.name %> is a <%= dino.type %></li>
  <% }); %>
</ul>
```

To access our data, we'll use the `fs` \(filesystem\) core module. Import this module in `index.js`

```javascript
const fs = require('fs');
```

Now let's pull in our data and take a took at it.

```javascript
// lists all dinosaurs
app.get('/dinosaurs', function(req, res) {
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  console.log(dinosaurs);
});
```

_**Note:**_ This `console.log()` is in our server file, which means it will print to our terminal, NOT the browser inspector.

That doesn't look very helpful, does it? That's because we're pulling in a JSON object, which isn't quite the same as a normal JS object. JSON \(JavaScript Object Notation\), is a standard format for data that is being transmitted \(sent back and forth\), and it needs to be _parsed_, or converted to a true JS data type - in this case, an array. Read more about working with JSON [here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON).

Try parsing the data before printing it:

```javascript
// lists all dinosaurs
app.get('/dinosaurs', function(req, res) {
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  let dinoData = JSON.parse(dinosaurs);
  console.log(dinoData);
});
```

That's more like it! Now lets send it to our EJS file:

```javascript
// lists all dinosaurs
app.get('/dinosaurs', function(req, res) {
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  let dinoData = JSON.parse(dinosaurs);
  res.render('dinosaurs/index', {myDinos: dinoData});
});
```

In the above example we load the `dinosaurs/index.ejs` view and pass it `dinoData` as `mydinosaurs`. Now we can access myDinos directly in the `index.ejs` file.

### 3. Show / Read \(GET\) route

_Show_ is a route that displays a single item of a specific type. Since we're still just reading data, it is a GET request to \(in this example\) `/dinosaurs/1`

Create a `dinosaurs/show.ejs` file:

```markup
<%= myDino.name %> is a <%= myDino.type %>.
```

Now let's write our show route. We can access the index from the url through the `req.params` object, but it will be a string. In order to use in to access an array value, we need to cast it to an integer.

**Show route -- in index.js**

```javascript
//express show route for dinosaurs (lists one dinosaur)
app.get('/dinosaurs/:idx', function(req, res) {
  // get dinosaurs
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  let dinoData = JSON.parse(dinosaurs);

  //get array index from url parameter
  let dinoIndex = parseInt(req.params.idx);

  //render page with data of the specified animal
  res.render('dinosaurs/show', {myDino: dinoData[dinoIndex]});
});
```

In the above example we load the `dinosaurs/show.ejs` view and pass it a specific item from the `dinoData` array as `myDino`. We use the `:idx` url parameter to specify which animal to display. This means in the `show.ejs` file we can access myDino directly.

### 4. New / Read \(GET\) route

To create an item \(dinosaur in this example\) we need to get the data about that item, so we'll use a [form](https://www.w3schools.com/html/html_forms.asp).

Form tags have two attributes that are very import for their CRUD functionality:

* _**method:**_ HTTP verb - `GET` or `POST`. You will use POST most often because it is significantly more secure. Read about the difference between these two methods by scrolling down to the "When to Use GET" AND "When to Use Post" sections of [this page](https://www.w3schools.com/html/html_forms.asp).
* _**action:**_ This value should be a path. Specifically, it is the url pattern associated with the route that will handle the data - in this case, that will be the `/dinosaurs` POST route we will write.

Create a `dinosaurs/new.ejs` view that contains an html form:

```markup
<form method="POST" action="/dinosaurs">
  <label for="dinosaurType">Type</label>
  <input id="dinosaurType" type="text" name="type">

  <label for="dinosaurName">Name</label>
  <input id="dinosaurName" type="text" name="name">

  <input type="submit">
</form>
```

Now write a `GET` route so we can view this form at `localhost:3000/dinosaurs/new`:

```javascript
app.get('/dinosaurs/new', function(req, res){
  res.render('dinosaurs/new');
});
```

Not working? Make sure this route is _above_ the show \(`/dinosaurs/:idx`\) route, otherwise the show route will catch the request and pass in "new" as `req.params.idx`.

### 5. Create \(POST\) route

When the above form is submitted it will make a `POST` to the url `/dinosaurs` with the data contained in the form fields. To receive this data, we need to create the `POST` route and use some middleware to make the data readable. This middleware is new to `express` and prior to version 4, we had to manually install the `body-parser` node package in order to use it. \(If it bothers you that we're glazing over how the data comes through before we send it through something like `body-parser`, read [this article](https://medium.com/@adamzerner/how-bodyparser-works-247897a93b90). It will always make sense to use some sort of framework like `body-parser` in practice, but if you're interested in capturing the raw data, see [this article](https://itnext.io/how-to-handle-the-post-request-body-in-node-js-without-using-a-framework-cd2038b93190).\)

This middleware will store the data submitted from the form in a user-friendly `req.body` object.

_**index.js**_

```javascript
const express = require('express');
const app = express();
const ejsLayouts = require('express-ejs-layouts');
const fs = require('fs');

app.set('view engine', 'ejs');
app.use(ejsLayouts);
//body-parser middleware
app.use(express.urlencoded({extended: false}));

.
.
.
```

The `express.urlencoded()` middleware tells body-parser to capture urlencoded data \(form data\) and store it in `req.body`. The `{extended: false}` option ensures that the values in this body will either be strings or arrays. More on this [here](https://www.npmjs.com/package/body-parser#bodyparserurlencodedoptions). Further discussion on it [here](http://stackoverflow.com/questions/29175465/body-parser-extended-option-qs-vs-querystring).

Now, if we can access the form data in a POST route!

_**index.js**_

```javascript
app.post('/dinosaurs', function(req, res) {
  console.log(req.body);
});
```

Try adding a new dinosaur and make sure you see the appropriate data come through in the terminal when you submit the form.

**body-parser Summary:** Form data is passed as the payload of the request. Every field that has a name will be included in that payload and it is sent as form encoded text. When `body-parser` is used, it automatically **parses** the form body into a javascript object that we can use and it stores it in `req.body` so we can use it \(similar to how we convert API responses to JSON. All of this is done as middleware, which we just configured.

**The `name` attribute matters!** In the above example we could access the dinosaur type form field by using `req.body.type` and the name field by using `req.body.name`. This correlates directly to the _names_ given to the form fields in the **form html** above.

Generally, the code in the **express route** would contain code that would CREATE an item in a database and redirect the user to a route with a confirmation message of some sort or just back to the index route. For this example we're going to use the JSON file created above to store our data. This will involve three steps:

* Reading the JSON file
* Pushing the new animal to the object
* Writing the new JSON file using [fs.writeFileSync](https://nodejs.org/api/fs.html#fs_fs_writefile_file_data_options_callback) \(this will replace the old dinosaurs.json\)

```javascript
app.post('/dinosaurs', function(req, res) {
  // read dinosaurs file
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
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

### Show / Read \(GET\) with a Form

There may be instances where you need to `GET` dinosaurs, but you don't want them all. A good example is filtering dinosaurs with a specific name via a search bar.

In these cases, you don't want to use a POST action, because POST is reserved for creating new resources. Instead, we can create another form with a `GET` method, and read the data via a **querystring**. This is an appropriate use of the `GET` form method because the user input is not sensitive.

Add a form to `dinosaurs/index.ejs`

```markup
<form method="GET" action="/dinosaurs">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>
```

The idea here is that the search bar allows the user to filter what's on the page, so it will be a `GET` request to `/dinosaurs`... but we already have a route for that! When you submit a form using the `GET` method, the key/value pairs are appended to the URL in a _query string_. Try searching for a dinosaur now and notice what happens to the URL. This query string, like parameters \(`req.params`\) is available via the request object. We'll use a conditional to check if there's a querystring, then filter the dinosaurs if one is present.

```javascript
app.get('/dinosaurs', function(req, res) {
  var dinosaurs = fs.readFileSync('./dinosaurs.json');
  var dinoData = JSON.parse(dinosaurs);

  var nameFilter = req.query.nameFilter;

  if (nameFilter) {
      dinoData = dinoData.filter(dino => dino.name.toLowerCase() === nameFilter.toLowerCase());
  }

  res.render('dinosaurs/index', {myDinos: dinoData});
});
```

