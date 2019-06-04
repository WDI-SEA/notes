# Intro to AJAX

## Objectives

* Define AJAX and what the abbreviation stands for
* Describe the purpose of AJAX
* Utilize AJAX to fetch data from third-party APIs
* Talk about the place of AJAX in the request-response cycle
* Describe how promises work in the context of AJAX requests

AJAX (Asynchronous JavaScript and XML) is used to create asynchronous web applications. This simply means a web page that can make calls back to the server in the background without reloading the page.

## Understanding HTTP

Before we can understand AJAX we need to get a little background on HTTP. HTTP is one of many internet protocols and is the protocol used for web communcation. HTTP can only send TEXT and is a request-response protocol. This means that a server can only respond to a request from a client (usually a web browser). [Read more on wiki](http://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol).


![http diagram](./http_diagram.png)

## AJAX

Originally the only way an HTTP request could be initiated was if the user clicked a link on a webpage, or submitted a form. AJAX allows JavaScript to send requests to the server with or without user interaction. This enables page content to be updated dynamically without a full page refresh.


## AJAX in Fetch

There are many libraries that allow us to perform these AJAX requests. jQuery and Axios are a couple of the most popular implementations. However, there is one called `fetch` that is "nearly a standard" which means that we don't need any additional libraries to use it.

The most common AJAX methods are `GET` and `POST`. In this unit we'll mostly be using only `GET` but here is the distinction:

* `GET` is used to request information from a URL.
* `POST` is used to send information to a URL.

**Basic `GET` example**

```js
fetch('https://www.reddit.com/search.json?q=kittens') 
  .then(function(responseData) {
    return responseData.json();
  })
  .then(function(jsonData) {
    console.log(jsonData);
  });
```

Let's look at this syntax. It uses some **Promise** functionality that we haven't seen, which we will get to shortly. The first line calls the `fetch` function and passes in the URL that we want to request data from. Then we use the `.then` part of the promise. Think of this as a callback - the function we pass into the `.then` function will only be executed when the API call has finished retrieving the data. This is actually really great because we don't know how long the API data will take to return. So we set up the next function to happen only after the data comes back. You can think of this as the same thing as a callback but it uses newer Promise syntax (the main advantage of which is the simplified syntax).

So the first thing we do once the data is returned is call `responseData.json()` and return the result of that. This is a required step to convert the data from the stringified version that comes from the API into an actual JavaScript object that we can use in code.

Then we use `.then` again to do something with the data after it is converted. In the example above, we simply console.log it.

## Promises

Note that at the end of the AJAX request, there is a function called `.then()` that is called once the response has been received. This is an example of a **promise**. Promises are common concepts in JavaScript, and you can think of promises as a "contract" between two functions. When the `.then()` promise is attached to the AJAX function, it "promises" to run once the response comes back successful. This is due to the request-response cycle taking time, and requiring asynchronous behavior.

We will dig into Promises more deeply at a later date.

## AJAX is asynchronous

An AJAX request doesn't allow you to load things instantly. Requesting things over the network always takes time, and you need an event handler to deal with the results. Look at the following code:

```js
console.log('Script is running');

fetch('https://www.reddit.com/search.json?q=kittens') 
  .then(function(responseData) {
    return responseData.json();
  })
  .then(function(jsonData) {
    console.log("Here is the data:", jsonData);
  })

console.log('Just fired AJAX request!');
```

What order will the `console.log` statements appear?

## Using Data

What if we want to use data from an AJAX request? We'll need to keep **scope** in mind, which is the concept of **where** variables exist.

**Global variables** are variables that are visible throughout the program, and thus have **global scope**

**Local variables** are variables that are visible only inside an immediate code block, and thus have **local scope**. Therefore, any variables we declare inside a function **stop existing** once we leave the function.

Some examples:

**This code causes an error because `posts` only exists inside the immediate function its declared in**

```js
fetch('https://www.reddit.com/search.json?q=kittens')
  .then(function(data) {
    return data.json();
  })
  .then(function(json) {
    var posts = json;
});

console.log(posts);

// Output
// > Uncaught ReferenceError: posts is not defined(…)
```

**This code runs because `posts` is declared in the same scope as data.**

```js
fetch('https://www.reddit.com/search.json?q=kittens')
  .then(function(data) {
    return data.json();
  })
  .then(function(json) {
    var posts = json;
    console.log(posts);
});

// Output
// > Object {kind: "Listing", data: Object}
```

## Putting AJAX On the Page

It's no fun simply logging search results to the page. Let's put content on the page!

Let's see who is omn the International Space Station right now. First, we should make a project folder and create the correct folder structure:

1. In terminal, create a new project directory in your `code/Unit1` directory named `iss-api`
2. Go into that directory and create a `js` folder
3. Create your files: `touch index.html` and `touch js/app.js`
4. Open the whole folder up in VS Code: `code .`
5. Put in the HTML boilerplate and add your `app.js` script as the last element before the closing body tag.
6. Add an AJAX call to the ISS API:

```js
fetch('http://api.open-notify.org/astros.json')
  .then(function(data) {
    return data.json();
  })
  .then(function(json) {
    var posts = json;
    console.log(posts);
});
```

AJAX responses are usually deeply nested objects carry lots of information. We can look at an API's documentation to see what the response is supposed to look like. Orrr, we can set a breakpoint at the point when data arrives and use our debugger to play around with the object and see what data comes back.

The console.log() statement printing the response allows us to use our mouse to click on properties of the object and investigate them. Pausing the debugger at the point when
the response arrives allows us to interact with the console when the response variable is in scope. We can type commands on the console to see if they work and then copy and paste valid code back into our program.

Remember, we have two ways to set breakpoints. We can write the ```debugger``` keyword in our program when we want the program to stop. Or, we can look at the source in Chrome's
Developer Tools and click on a line to tell the browser to stop there.

Adding a console.log() will print the response every time, and gives us a line number to click on. We can follow the link to the line number and click on that line to set a
temporary breakpoint manually.

Using the ```debugger``` keyword will stop our program every time. It won't output anything to the console so we won't be able to see data once we're past that point of execution.

Use your debugging tools to investigate the response object and find out how to access the title and the url of the first result. Copy and paste parts of this line of code
into your program so you have easy access to the important parts of your search results.

![debugging view](./debugging_view.png)

Consider how the ```forEach``` and ```map``` functions may be useful tools to process these complicated objects.

Now you're cooking with gas.

## APIs to hit

Here are a few APIs you can use to practice AJAX calls. They either won't save changes, or won't allow you to use POST, PUT or DELETE, so they're safe to play with.

[Open Movie Database API](http://www.omdbapi.com/)

[Acromine Acronym API](http://www.nactem.ac.uk/software/acromine/rest.html)

[Pokemon API](http://pokeapi.co/)

[Star Wars API](https://swapi.co/)

### Cross-Origin Requests

Note that not all websites/APIs play nice with AJAX. You may see an error in the console from APIs like the [iTunes API](https://www.apple.com/itunes/affiliates/resources/documentation/itunes-store-web-service-search-api.html)

```js
fetch('http://itunes.apple.com/search?term=arcade+fire')
  .then(function(data) {
    return data.json();
  })
  .then(function(json) {
    console.log(json);
  })

// output
// > No 'Access-Control-Allow-Origin' header is present on the requested resource.
```

For security reasons, browsers often restrict requests to other websites other than your own. However, some APIs like Reddit and the GA Doughnuts API can have their **servers** configured to allow these types of requests. The browser will know to **not** restrict requests because the server will send back additional information in a **header**. Here's an example you can try, if you'd like to see what's sent back.

In the terminal:

```bash
curl -I http://api.doughnuts.ga/doughnuts

HTTP/1.1 200 OK
Date: Wed, 27 Jan 2016 19:44:30 GMT
Content-Type: application/json; charset=utf-8
Content-Length: 641
Connection: keep-alive
Set-Cookie: __cfduid=df8b7d51a2307f3b7bf782d1ce5d060011453923870; expires=Thu, 26-Jan-17 19:44:30 GMT; path=/; domain=.doughnuts.ga; HttpOnly
X-Powered-By: Express
Vary: Origin
Access-Control-Allow-Credentials: true
...
```

The header names sometimes vary, but because the **Access-Control-Allow-Credentials** was sent back by the server, the browser will let us receive data from this cross-origin request.
