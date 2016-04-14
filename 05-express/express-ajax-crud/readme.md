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
| POST | /teams | create | create a new taco (using form data from /teams/new) |
| GET | /teams/:id | show | display a specific team |
| GET | /teams/:id/edit | edit | return an HTML form for editing a team |
| PUT | /teams/:id | update | update a specific team (using form data from /teams/:id/edit) |
| DELETE | /teams/:id | destroy | deletes a specific taco |

If you are storing something beside teams you'll use this same pattern. It could be `users`, `photos`, `books`, etc, etc.


##RESTful verbs in action

###GET

GET requests are used to GET data. Either list details about a single item or list all items of a specific type. **GET should never be used to alter data**

As we know any basic link will be a GET request automatically. Also, any form without a specified method will be a GET.

**Some common links**

```html
<a href="/teams">List all teams</a>

<a href="/teams/12">List team with id of 12</a>

<a href="/teams/new">Add a new team</a>
```

**GET form**

```html
<form action="/teams">
    <input type="text" name="q">
    <input type="submit" value="search">
</form>
```

###POST

A POST is typically used to **create** a new item of a specific type. Also, we know that to do a `POST` we must use a form with `method="post"`

**Example: New Team Form**

```html
<form method="post" action="/teams">
    <input type="text" name="name">
    <input type="text" name="members">
    <input type="submit" value="Create a team">
</form>
```

###DELETE

Delete should be used to delete an existing item. A delete request contains no payload (`req.body`) and no query string (`req.query`). The only data is expressed via a URL parameter which matches the item's database id (`req.params.id`).

There is no way to initiate a DELETE action unless we use ajax.

**HTML**

```html
<a href="/teams/5" class="delete-link">Delete team 5</a>
```

Without javascript this would link to `GET /teams/5` which would simply display the team at that route. However, we can use javascript to override the default behavior and send the request with the DELETE verb.

**jQuery / JavaScript**

```js
$('.delete-link').on('click', function(e){
    e.preventDefault();
    var myUrl = $(this).attr('href');
    $.ajax({
        method:'DELETE',
        url:myUrl
    }).done(function(){
        //do stuff when the delete action is complete
        //redirect or update view
    });
});

```


###PUT

Put should be used to update an existing item.


**HTML**

```html
<form action="/teams/5" id="put-form">
    <input type="text" name="name">
    <input type="text" name="members">
    <input type="submit" value="Update a team">
</form>
```

Without javascript this form would submit as a `GET` request which means it would just go to the page that displays the team with the id of 5. Now we need to override this default behavior to initiate a `PUT` via AJAX.

**jQuery / JavaScript**

```js
$('.put-form').on('submit', function(){
    e.preventDefault();
    var myUrl = $(this).attr('action');
    var myData = $(this).serialize()
    $.ajax({
        method:'PUT',
        url:myUrl,
        data:myData
    }).done(function(){
        //do stuff when the put action is complete
        //probably just redirect
    });
});

```
