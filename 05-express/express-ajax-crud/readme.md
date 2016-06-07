#RESTful CRUD

##Objectives

* Review RESTful routing
* Use AJAX to implement PUT and DELETE routes

>Representational State Transfer (REST) is a software architecture style consisting of guidelines and best practices for creating scalable web services. REST is a coordinated set of constraints applied to the design of components in a distributed hypermedia system that can lead to a more performant and maintainable architecture.

Source: [wikipedia](http://en.wikipedia.org/wiki/Representational_state_transfer)

##RESTful routing example

Imagine we have an app that stores teams signing up for a hackathon. We would create a model called team which would represent a single team with their name and their members. The data would be stored in a table called teams (where we store many teams). The routes would also be the plural "teams".


| Verb | Path | Action | Used for |
|----|----|----|----|
| GET | /teams | index | display a list of all teams |
| GET | /teams/new | new | return an HTML form for creating a new team |
| POST | /teams | create | create a new team (using form data from /teams/new) |
| GET | /teams/:name | show | display a specific team |
| GET | /teams/:name/edit | edit | return an HTML form for editing a team |
| PUT | /teams/:name | update | update a specific team (using form data from /teams/:name/edit) |
| DELETE | /teams/:name | destroy | deletes a specific team |

If you are storing something beside teams you'll use this same pattern. It could be `users`, `photos`, `books`, etc.

Previously, we implemented the first four routes. Also, we can find a way to implement the route `GET /teams/:name/edit`. But what about DELETE and PUT? Forms don't support these methods, so we'll need to use AJAX.

##DELETE

Delete should be used to delete an existing item. A delete request contains no payload (`req.body`) and no query string (`req.query`). The only data is expressed via a URL parameter which matches the item's name (`req.params.name`).

There is no way to initiate a DELETE action unless we use AJAX. So let's try it out.

**HTML**

```html
<a href="/teams/Edward" class="delete-link">Delete team Edward</a>
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


###PUT

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
$('.put-form').on('submit', function(){
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
