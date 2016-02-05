#Lets code!

Now we will be implementing the topics you just researched. Come up with a working example, and be ready to teach the class.

##Bcrypt

Implement code to use bcrypt to encrypt a plain text string AND then use `.compare()` to check it.

This can be done in a **stand alone .js file**. Be aware that bcrypt takes time so it uses a callback.

##Sequelize validations

Implement a validation on your OMDB app to require submitted comments to be between `20` and `200` characters.

Test that it works. Use .catch() to send a message to the user. It can just use res.send() for now if you want. If you have extra time, try to make the message render on the page.

##Sequelize hooks

Use sequelize hooks to convert all comments posted to your OMDB app to lowercase before they are created. The hook should be created in your model.

If you have more time try coming up with another use for a hook in the same project.

##Sessions

Use sessions to implement a back button on your OMDB app. 

The link should be on the movie detail page and link back to the watch list page OR search results page depending on which page they came from.

##Middleware

Create a middleware (on one of your existing projects) that adds a function `.log` to your `req` object. It should be created using `app.use()` which means that in any other route you should be able to call `req.log()`.

`req.log` should take 1 parameter that is the message to log. It should output

* The current date/time
* The current route's url
* The message provided

**usage example**

```js
app.get('/movies/:id',function(req,res){
    req.log('loading a movie');
});

//output...
//4/8/2015, 10:18:32 AM   /movies/4   loading a movie
```

 
