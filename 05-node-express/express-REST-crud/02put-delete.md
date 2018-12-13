# RESTful CRUD

## Objectives
* Use AJAX to implement PUT and DELETE routes

## Review REST

| VERB | URL | Action (CRUD) | Description |
|------|-----|---------------|-------------|
| GET | /dinosaurs | Index (Read) | lists all dinosaurs |
| GET | /dinosaurs/1 | Show (Read) | list information about a specific animal (id = 1) |
| POST | /dinosaurs | Create | creates an animal with the POST payload data |
| PUT | /dinosaurs/1 | Update | updates the data for a specific animal (id = 1) |
| DELETE | /dinosaurs/1 | Delete (Destroy) | deletes the animal with the specified id (1) |

In the previous half of this lesson, we implemented the first three routes. Here we will cover the final two routes in this RESTful routing example.

## Method-Override

  `PUT` and `DELETE` routes are not supported by HTML5. If you're wondering why, check out these discussions on [stackoverflow](https://stackoverflow.com/questions/16805956/why-dont-browsers-support-put-and-delete-requests-and-when-will-they) and [stackexchange](https://softwareengineering.stackexchange.com/questions/114156/why-are-there-are-no-put-and-delete-methods-on-html-forms). These requests are so often used that there are well-established work-arounds like [`method-override`](https://www.npmjs.com/package/method-override), which is what we will use.
  
### Middleware
`method-override` is a node package that allows us to catch incoming requests to the back-end and change the method from `POST` to `DELETE` or `PUT`. We'll use the `method-override` middleware that looks for a `_method=DELETE` or `_method=PUT` query string in the request URL and swap out the method accordingly.

_By default, `method-override` will only override `POST` methods, because having a `DELETE` or `PUT` route accessible via a `GET` request "may introduce security issues and cause weird behavior when requests travel through caches"(see the `options.methods` section of the `method-override` docs for on this)_

#### Setup:

**1.** Install `method-override` via npm.

**2.** Import the module

```js
var methodOverride = require('method-override');
```

***3.*** Configure middleware (make sure it lives above any other middleware code that uses the request method):

```js
app.use(methodOverride('_method'));
```

## DELETE

Delete should be used to delete an existing item. A delete request contains no payload (`req.body`) and no query string (`req.query`). The only data is expressed via a URL parameter which matches the item's name (`req.params.name`).

Since we can only use `POST` methods to activate the `method-override` functionality, we will use a form to submit the request. Let's start by adding a delete button (form submission) to our index page list items. Note that we must add a second `forEach` parameter in order to get access to the dinoId/index.

**dinosaurs/index.ejs**
```html
<form method="GET" action="/dinosaurs">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>

<ul>
  <% myDinos.forEach(function(dino, index) { %>
  <li><%= dino.name %> is a <%= dino.type %>
  	<form method="POST" action="/dinosaurs/<%= index %>">
  		<input type="submit" value="Delete">
  	</form>
  </li>
  <% }); %>
</ul>
```

**Server**

```js
app.delete('/teams/:name', function(req, res) {
  var teamToDelete = req.params.name;

  // delete team here

  /*
   * instead of rendering a page, send back JSON or text, which can be read
   * in the .done() promise of the AJAX call
   */
  res.send({message: 'success'});
});
```


### PUT

Put should be used to update an existing item. We'll need an example where there's a route for editing the team. Here's an example.

**EJS for /teams/Edward/edit**

```html
<form action="/teams/5" id="put-form">
  <label for="teamName">Team Name</label>
  <input type="text" name="name" value="<%= team.name %>">

  <label for="teamMembers">Team Members</label>
  <input type="text" name="members" value="<%= team.members %>">

  <input type="submit" value="Update a team">
</form>
```

Without JavaScript this form would submit as a `GET` request which means it would just go to the page that displays the team with the id of 5. Now we need to override this default behavior to initiate a `PUT` via AJAX.

**jQuery / JavaScript**

```js
$('.put-form').on('submit', function(e) {
  e.preventDefault();
  var teamElement = $(this);
  var teamUrl = teamElement.attr('action');
  var teamData = teamElement.serialize();
  $.ajax({
    method: 'PUT',
    url: teamUrl,
    data: teamData
  }).done(function(data) {
    // get data returned from the PUT route
    console.log(data);

    // do stuff when the PUT action is complete
    teamElement.remove();

    // or, you can redirect to another page
    window.location = '/teams';
  });
});
```

**Server**

```js
app.put('/teams/:name', function(req, res) {
  var teamToEdit = req.params.name;

  // Edit team here

  /*
   * instead of rendering a page, send back JSON or text, which can be read
   * in the .done() promise of the AJAX call
   */
  res.send({message: 'success'});
});
```

Here's an example repository.

https://github.com/WDI-SEA/hackathon-teams
