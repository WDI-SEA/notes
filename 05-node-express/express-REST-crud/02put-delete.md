# Put and Delete

## Objectives

* Use `method-override` to implement `PUT` and `DELETE` routes in `express`.

## Review REST

| VERB | URL | Action \(CRUD\) | Description |
| :--- | :--- | :--- | :--- |
| GET | /dinosaurs | Index \(Read\) | lists all dinosaurs |
| GET | /dinosaurs/new | New \(Read\) | shows a form to make a new dinosaur |
| POST | /dinosaurs | Create \(Create\) | creates an dinosaur with the POST payload data |
| GET | /dinosaurs/:id | Show \(Read\) | list information about a specific dinosaur \(i.e. /dinosaurs/1\) |
| GET | /dinosaurs/edit/:id | Edit \(Read\) | shows a form for editting a specific dinosaurs \(i.e. /dinosaurs/edit/1\) |
| PUT | /dinosaurs/:id | Update \(Update\) | updates the data for a specific dinosaur \(i.e. /dinosaurs/1\) |
| DELETE | /dinosaurs/:id | Destroy \(Delete\) | deletes the dinosaur with the specified id \(i.e. /dinosaurs/1\) |

In the previous half of this lesson, we implemented the first four routes. Here we will cover the final three routes in this RESTful routing example.

## Method-Override

`PUT` and `DELETE` routes are not supported by HTML5. If you're wondering why, check out these discussions on [stackoverflow](https://stackoverflow.com/questions/16805956/why-dont-browsers-support-put-and-delete-requests-and-when-will-they) and [stackexchange](https://softwareengineering.stackexchange.com/questions/114156/why-are-there-are-no-put-and-delete-methods-on-html-forms). These requests are so often used that there are well-established work-arounds like [`method-override`](https://www.npmjs.com/package/method-override), which is what we will use.

### Middleware

`method-override` is a node package that allows us to catch incoming requests to the back-end and change the method from `POST` to `DELETE` or `PUT`. We'll use the `method-override` middleware that looks for a `_method=DELETE` or `_method=PUT` query string in the request URL and swap out the method accordingly.

_By default, `method-override` will only override `POST` methods, because having a `DELETE` or `PUT` route accessible via a `GET` request "may introduce security issues and cause weird behavior when requests travel through caches"\(see the `options.methods` section of the `method-override` docs for more on this\)_

#### Setup:

**1.** Install `method-override` via npm.

**2.** Import the module

```javascript
const methodOverride = require('method-override');
```

_**3.**_ Configure middleware \(make sure it lives above any other middleware code that uses the request method\):

```javascript
app.use(methodOverride('_method'));
```

## DELETE

Delete should be used to delete an existing item. A delete request contains no payload \(`req.body`\) and no query string \(`req.query`\). The only data is expressed via a URL parameter which matches the item's name \(`req.params.name`\).

Since we can only use `POST` methods to activate the `method-override` functionality, we will use a form to submit the request. Let's start by adding a delete button \(form submission\) to our index page list items. Note that we must add a second `forEach` parameter in order to get access to the dinoId/index.

**dinosaurs/index.ejs**

```markup
<form method="GET" action="/dinosaurs">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>


<ul>
  <% myDinos.forEach(function(dino, index) { %>
  <li><%= dino.name %> is a <%= dino.type %>
      <form method="POST" action="/dinosaurs/<%= index %>/?_method=DELETE">
          <input type="submit" value="Delete">
      </form>
  </li>
  <% }); %>
</ul>
```

**index.js**

```javascript
app.delete('/dinosaurs/:idx', function(req, res){
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  dinosaurs = JSON.parse(dinosaurs);

  // remove the deleted dinosaur from the dinosaurs array
  dinosaurs.splice(req.params.idx, 1)

  // save the new dinosaurs to the data.json file
  fs.writeFileSync('./dinosaurs.json', JSON.stringify(dinosaurs));

  //redirect to the GET /dinosaurs route (index)
  res.redirect('/dinosaurs');
});
```

### PUT

First we need a way for the user to edit an item. Add an edit link to the dinosaurs index.

**/dinosaurs/index.ejs**

```markup
<form method="GET" action="/dinosaurs">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>


<ul>
  <% myDinos.forEach(function(dino, index) { %>
  <li><%= dino.name %> is a <%= dino.type %>
      <a href="/dinosaurs/edit/<%= index %>">Edit</a>
      <form method="POST" action="/dinosaurs/<%= index %>/?_method=DELETE">
          <input type="submit" value="Delete">
      </form>
  </li>
  <% }); %>
</ul>
```

Now we have to create a form for editting the information and submitting the `PUT` request.

**/dinosaurs/edit.ejs**

```markup
<form method="POST" action="/dinosaurs/<%=dinoId%>/?_method=PUT">
    <label>Name</label>
    <input type="text" name="name" value="<%= dino.name %>">
    <label>Type</label>
    <input type="text" name="type" value="<%= dino.type %>">
    <input type="submit">
</form>
```

We need a `GET` route to view this form!

**index.js**

```javascript
app.get('/dinosaurs/edit/:idx', function(req, res){
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  let dinoData = JSON.parse(dinosaurs);
  res.render('dinosaurs/edit', {dino: dinoData[req.params.idx], dinoId: req.params.idx});
});
```

Finally we can write our `PUT` route! The form submission will return the editted values through `req.body`, just like we saw with the `new.ejs` view and `POST` route. Now all we need to do is edit the JSON accordingly.

**index.js**

```javascript
app.put('/dinosaurs/:idx', function(req, res){
  let dinosaurs = fs.readFileSync('./dinosaurs.json');
  dinosaurs = JSON.parse(dinosaurs);

  //re-assign the name and type fields of the dinosaur to be editted
  dinosaurs[req.params.idx].name = req.body.name;
  dinosaurs[req.params.idx].type = req.body.type;

   // save the editted dinosaurs to the data.json file
  fs.writeFileSync('./dinosaurs.json', JSON.stringify(dinosaurs));
  res.redirect('/dinosaurs');
});
```

