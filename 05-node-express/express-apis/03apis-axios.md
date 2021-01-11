# APIs with Express \(axios\)

### Objectives

* Describe the purpose of using an API on the backend.
* Create an application that uses an API and the `axios` module.

In order to get around issues such as [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Access_control_CORS) and API access control, we can communicate with other servers through our server. In this case, our server acts as both a client and a server. We'll be doing some requests using the `axios` Node module.

To use the module, install it using npm.

```bash
npm i axios
```

Here's an example from NPM's homepage for the `axios` module. Let's take a look at it.

```javascript
const axios = require('axios');

// Make a request for a user with a given ID
axios.get('/user?ID=12345')
  .then(function (response) {
    // handle success
    console.log(response);
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .finally(function () {
    // always executed
  });
```

Identify what's necessary for making a server-side request.

* axios module import
* axios.get function
  * URL
  * any other data or headers that need to be passed \(optional\)
  * `then` promise \(the code that runs once the request finishes\)
    * handle a success
    * catch any raised exceptions or errors \(optional\)
    * run something at the end regardless \(optional\)

### Incorporating `axios` into Express

In order to incorporate the `axios` module into Express, we can set up a basic Express application and place the request code inside a route.

This can be done by creating a new directory, running `npm init`, then installing the correct dependencies \(refer back to the notes if you forgot\). Here's an example app.

#### Example

**server.js**

```javascript
const express = require('express');
const axios = require('axios');
const app = express();

app.get('/', (req, res)=>{
    axios.get('http://www.google.com')
      .then(response=>{
        // handle success
        console.log(response)
      })
  })

app.listen(3000);
```

Take a look inside the object you get back. You'll see that the html comes back inside the `data` field of the object. Like `fetch`, `axios` also has a wrapper it gives us in the response. So let's modify our console.log to get back just the data we're looking for, and change it to a `res.send` so we see it in the browser:

```javascript
app.get('/', (req, res)=>{
    axios.get('http://www.google.com')
      .then(response=>{
        // handle success
        res.send(response.data)
      })
})
```

Note that this app sends out the HTML for [http://www.google.com](http://www.google.com), minus the images due to the images having links **relative** to [http://localhost:3000](http://localhost:3000)

Let's use a more useful source of data that we can parse, like OMDB \(Open Movie Database\)

### Fetching JSON data

Let's modify the example above to make a request to OMDB's API. [OMDB Link](http://www.omdbapi.com/)

**We'll be using this endpoint:** [http://www.omdbapi.com/?s=star+wars&apikey=yourkey123](http://www.omdbapi.com/?s=star+wars&apikey=yourkey123)

#### Modified Example

**server.js**

```javascript
const express = require('express');
const axios = require('axios');
const app = express();

app.get('/', (req, res)=>{
  axios.get(`http://www.omdbapi.com/?apikey=${process.env.API_KEY}&s=star+wars`)
    .then((response)=>{
        res.send(response.data)
    })
})

app.listen(3000);
```

**API Keys**

Notice that OMDB API has a key requirement for their API. That's okay, it just means we'll need to register for a key real quick before running the example. Don't worry - it's free and only takes a few minutes. Lots of APIs will require keys, so let's get into the habit!

> Protip: Never share your API keys! These should go in `.env` files and never, ever be pushed up to Github or anywhere else online. The `.env` file can be added to your `.gitignore` file to make git ignore it!

**Things to Note**

* After getting the response back, we need to look inside response.data to see what was actually returned from the api. That's where axios puts the data. The response object you get back from axios is actually a wrapper that contains the api data among other things.
* It's very important to call `res.send` in the correct place \(the axios 'then' promise\)
  * Try putting `res.send` outside of the 'then'. You'll get an error!

## Additional Topics

* [API Information](../../12-resources/apis.md)
* [Using APIs with Client/Secret Keys \(Foreman\)](../../00-config-deployment/deploy-rails/foreman.md)

