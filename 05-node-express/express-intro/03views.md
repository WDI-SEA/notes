# Node/Express Personal Website

We're going to create a personal website with the following pages:
* Home
* About
* Blog

### Objectives:
* Practice stubbing out routes
* Learn how to set up views

### Prerequisites:
* Know how to write a GET route in Node/Express

### Part 1: Routes

We're going to stub out the routes for the home, about, and blog pages!

***1. Set up your app***
Create a new Node/Express project.

***2. Create the following routes:***

Make sure the message displays on the page when you navigate to the appropriate URL.

| Route | HTTP Verb | URL Pattern | Message |
| ----- | --------- | ----------- | ------- |
| Home | GET | / | "This is the Home Page!"
| About | GET | /about | "Some stuff about me will go here."
| Blog | GET | /blog | "A directory of all my blog posts will go here."

### Part 2: Views

Writing text to a web page using ```res.send()``` gives us something to look at, but isn't very pretty. Instead of sending plain text, let's start serving HTML files. Since each page will display different HTML, we'll have several HTML files, or _views_.

***1.*** Create a views folder inside your project directory. Inside this folder, create three HTML files:
* index.html (this is the standard filename for the view associated with the base URL)
* about.html
* blog-directory.html

***2.*** Put some basic HTML in these files so you can test them.

***3.*** In your routes, replace the ```res.send(<message>)``` with ```res.SendFile(__dirname+<relative file path>)``` ([docs](https://expressjs.com/en/api.html#res.sendFile))

```res.SendFile()``` takes an _absolute_ path, so we can't just give it ```./views/index.html```. ```__dirname``` is a Node keyword that gives us the absolute path of the current directory ([docs](https://nodejs.org/docs/latest/api/modules.html#modules_dirname)).

Your home route should look like this:
```js
app.get('/', function(req, res) {
  res.sendFile(__dirname+'/views/index.html');
});
```

Test it out to see if your HTML shows up!

***4.*** As our apps get bigger, it will make sense to group our [static files](https://www.maxcdn.com/one/visual-glossary/static-content/) in one place and avoid typing out the absolute file path all over the place. Fortunately, Express has away for us to tell it where to find all of our static files, so we can just use the filenames in our routes. ([docs](https://expressjs.com/en/starter/static-files.html))

Add this line to ```index.js```, above your routes:
```js
app.use(express.static(__dirname+'/views')));
```

What is ```app.use()```? This is an express function that indicates _middleware_. Middleware is code that intercepts the request object when it comes in from the client, but before it hits any route. We'll see more examples of middleware later.

And change replace the paths you're passing into ```res.sendFile()``` with just name of the file to be served:
```js
app.get('/', function(req, res) {
  res.sendFile('index.html');
});
```

Make sure to do this for all three routes. Now check to see that your html is coming through on the browser.