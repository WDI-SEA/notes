#Custom Node Modules

##Objectives

* Discuss uses of custom node modules
* Utilize require and export to build module
* Utilize callbacks for async module methods

So far we have been utilizing many npm packages and node modules in our work to solve certain problems. However, what happens when there isn't an npm package for what you're looking for? Or you want to create DRY, modularized code instead of writing that dumb request 20 times?

If this is the case, then we need to write our own custom node modules.

##Getting Started: Calculator module

Let's start with a simple module that will contain some basic calculator functions.

To get started, create a new folder, and initialize npm. Next we'll create two files, one for our calculator module, and another to utilize our module.

```bash
mkdir custom-module
cd custom-module
npm init --yes
touch calculator.js
touch index.js
```

## Building the Add function

We're going to start with our **calculator.js** module file and build out the Add function:

```js
module.exports = {
  add: function(num1, num2) {
    return num1 + num2;
  }
}
```

What's happening here is we're exporting a basic Object using the ```module.exports``` property. This setting is required to allow other parts of our code to access this module, think of it as the module's public interface. Then we can add whatever properties or functions we want exposed outside our module to that object.

Next lets use ```require``` in our **index.js** to pull in the calculator module and call the add function:

```js
var calculator = require('./calculator');

var solution = calculator.add(2, 2);

console.log(solution);
```

So here we're requiring or importing our calculator module using the ```require``` function and the file path to the **calculator.js** file. We then get access to whatever we exported in that file, in this case the object that contains our add function.

###Exercise

Build out the 3 other functions for our calculator:
 - **subtract**
 - **multiply**
 - **divide**

###Making Something Useful - OMDB

While a calculator module is all well and good, it doesn't necessarily solve a problem for us. Let's test out our new module building skills by building a nice OMDB API module that makes issuing requests to OMDB easier.

First lets create a new file called **omdb_api.js** and install the ```request``` module so we can send requests:

```bash
touch omdb_api.js
npm install --save request
```

Next we need to build out our module. Lets think about what typical requests we would send to OMDB API. The two most common uses we've seen are:
  **- Searching**
  **- Find by IMDBID**

Lets start by adding the Search function.

```js
var request = require('request');

function search(searchTerm, callback) {
  var qs = {
    s: searchTerm
  }
  request({
    url: 'http://omdbapi.com',
    qs: qs
  }, function(error, response, body) {
    var data = JSON.parse(body);
    callback(data.Search);
  });
}

module.exports = {
  search: search
}
```

Let's break down a few parts of that code.

First we installed and use ```require``` to pull the newly installed ```request``` module into our custom module so that we can make ajax requests.

Next we created a new function called **search** which contains our ajax request. Note the arguments for this function. The first argument is pretty self-explanatory, it is the search term string for search omdb.

The second argument is the real magic here. The second argument is actually a function that we are going to pass into the **search** function when we call it. We call it a **callback** because it's going to call-back to the original place where called **search**.

The reason we do this is because we are executing an **asynchronous** request for OMDB data. So we don't want anything to happen until we get that data back which is why we call the **callback** function in our request promise function.

Finally lets utilize our awesome omdb module in our **index.js**:

```js
var omdbAPI = require('./omdb_api.js');

omdbAPI.search('casablanca', function(results) {
  console.log(results);
});
```

Notice that our second argument when we call **search** is an anonymous function. Javascript is nice in that it will allow us to define a function like so and pass that around into other functions, which is what we're doing here. That anonymous function will be assigned to the **callback** argument in our search function in the **omdb_api.js** file.

###Exercise
Build out the IMDB search function for our module

 ***Hint***: Check our notes in the express api's section and the OMDB API docs.
