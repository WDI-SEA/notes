# RESTful CRUD

## Objectives
* Use AJAX to implement PUT and DELETE routes

## DELETE

Delete should be used to delete an existing item. A delete request contains no payload (`req.body`) and no query string (`req.query`). The only data is expressed via a URL parameter which matches the item's name (`req.params.name`).

There is no way to initiate a DELETE action unless we use AJAX. So let's try it out.

Let's start by adding a delete link to our index page list items. Note that we must add a second `forEach` parameter in order to get access to the dinoId/index.

**dinosaurs/index.ejs**
```html
<form method="GET" action="/dinosaurs">
  <label for="nameFilter">Filter by Name</label>
  <input id="nameFilter" type="text" name="nameFilter">
  <input type="submit">
</form>

<ul>
  <% myDinos.forEach(function(dino, index) { %>
  <li><%= dino.name %> is a <%= dino.type %><a href="/dinosaurs/<%= index %>" class="delete-link">Delete</a></li>
  <% }); %>
</ul>
```

Without JavaScript, this would link to `GET /teams/Edward` which would simply display the team at that route. However, we can use JavaScript to override the default behavior and send the request with the DELETE verb.

**jQuery / JavaScript**

```js
$('.delete-link').on('click', function(e) {
  e.preventDefault();
  var teamElement = $(this);
  var teamUrl = teamElement.attr('href');
  $.ajax({
    method: 'DELETE',
    url: teamUrl
  }).done(function(data) {
    // get data returned from the DELETE route
    console.log(data);

    // do stuff when the DELETE action is complete
    teamElement.remove();

    // or, you can redirect to another page
    window.location = '/teams';
  });
});
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
