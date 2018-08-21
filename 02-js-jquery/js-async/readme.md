# Async

## Objectives

* Identify situations where the `async` module would be needed
* Utilize `async` control flow functions for asynchronous function calls

## What is Async?

It helps to know the dictionary definitions of synchronous and asynchronous:

_[synchronous](https://www.merriam-webster.com/dictionary/synchronous): happening, existing, or arising at exactly the same time_

_[asynchronous](https://www.merriam-webster.com/dictionary/asynchronous): not simultaneous or concurrent in time_ 

Async is a JavaScript module available for Node.js and the browser. It provides a set of utilities for working with functions asynchronously. We'll be focusing our attention to Async's control flow functions, mainly `series`, `parallel`, `concat`, and `waterfall`.

## Why Use Async?

There are situations where functions will need to be run without conflicting with each other. This is one of the benefits/drawbacks of asynchronous behavior in JavaScript. A great example is data scraping multiple pages. If you were to data scrape pages using a loop, the requests would all run at the same time.

```js
var request = require('request');

var urls = ['http://www.google.com', 'http://www.yelp.com', 'http://www.twitter.com'];
var allData = [];

//this would work correctly to a point, but would be disastrous if there were, say, 1000 URLs in the urls array
urls.forEach(function(url) {
  request(url, function(err, response, data) {
    allData += data;
  });
});

//this would not work correctly
console.log(allData);
```

Using the `async` module will allow us to control the flow of how these functions are run, and when we can access all of the data.

## Using Async

First, let's install the `async` module.

```
npm install async
```

### Series

The `.series` function can pass in an array of functions, along with a callback function to execute once the array of functions is completed. Each function in the array takes in a callback function as a parameter, then executes the callback when the function is finished (passing an error and results). Functions will be executed in order until completed, then the final callback is executed.

```js
var async = require('async');

// functions
function fn1(callback) {
  console.log(1);
  callback(null, 1);
}

function fn2(callback) {
  console.log(2);
  callback(null, 2);
}

function fn3(callback) {
  console.log(3);
  callback(null, 3);
}

// async series
async.series([fn1, fn2, fn3], function(err, results) {
  console.log('Done!');
  console.log(results);
});
```

### Parallel

The `.parallel` function also accepts an array of functions, along with a callback function. However, the functions aren't executed one after another. They start in parallel, and the final callback is executed once the array of functions is done executing. Note that the functions are started, but not executed, in parallel. So if the functions don't take any time to complete, they'll execute in series (just as before).

```js
var async = require('async');

//functions
function fn1(callback) {
  setTimeout(function() {
    console.log(1);
    callback(null, 1);
  }, 5000);
}

function fn2(callback) {
  setTimeout(function() {
    console.log(2);
    callback(null, 2);
  }, 1000);
}

function fn3(callback) {
  setTimeout(function() {
    console.log(3);
    callback(null, 3);
  }, 10000);
}

//async parallel
async.parallel([fn1, fn2, fn3], function(err, results) {
  console.log('Done!');
  console.log(results);
});
```

### Waterfall

The `.waterfall` function is similar to `.series`, but allows arguments to be passed from one function to the next. This is ideal if multiple API calls are being made, and the results of one call are required for the next call.

```js
var async = require('async');

//functions
function fn1(callback) {
  var initial = 55;
  callback(null, 55);
}

function fn2(num1, callback) {
  num1 += 5;
  callback(null, num1)
}

function fn3(num1, callback) {
  num1 += 40;
  callback(null, num1);
}

//async waterfall
async.waterfall([fn1, fn2, fn3], function(err, results) {
  console.log('Done!');
  console.log(results);
});
```

### Concat

Lastly, `.concat` allows you to pass in an array of values and an iterator (instead of passing in an array of functions). This allows functions to be more reusable, as in the instance of making requests. These functions occur in parallel.

```js
var async = require('async');
var request = require('request');

//urls to make requests to
var urlsToGet = ['https://www.reddit.com/search.json?q=politics',
                 'https://www.reddit.com/search.json?q=puppies',
                 'https://www.reddit.com/search.json?q=drake'];

//create an iterator to get the first title for each URL
var getFirstTitle = function(url, callback) {
  request(url, function(err, response, data) {
    var firstTitle = JSON.parse(data).data.children[0].data.title;
    callback(null, firstTitle);
  });
};

//get each title, then print the results
async.concat(urlsToGet, getFirstTitle, function(err, results) {
  console.log(results);
});
```

### Concat Example 2: Seattle Neighborhoods

For those who created the Seattle neighborhoods scraper, we didn't forget about you! Here's an example that takes the neighborhood data we scraped and retrieves the description for each Seattle neighborhood. Comments are provided, so take a moment and decipher the code.

```js
// importing modules
var request = require('request');
var cheerio = require('cheerio');
var async = require('async');

// // make a request to the Visit Seattle and scrape neighorhood names and links
request('http://www.visitseattle.org/things-to-do/neighborhoods/', function (error, response, data) {
  var $ = cheerio.load(data);

  // scrape neighborhood names and links, and store as an array of objects
  var neighborhoods = $('.info-window-content').map(function(index, element) {
    return {
      name: $(element).find('h4').text(),
      link: $(element).find('a').attr('href')
    };
  }).get();
//   console.log("printing neighborhoods from request:", neighborhoods);
//   // pass the neighborhood data to fetchDescriptions
  fetchDescriptions(neighborhoods);
});

// this function takes neighborhood data and requests descriptions from each link
function fetchDescriptions(neighborhoodData) {
  // using async.parallel to retrieve data from all neighborhoods at once
  async.concat(neighborhoodData, getNeighborhoodDescription, function(err, results) {
    // here are the neighborhoods with descrptions. Let's print them out
    results.forEach(function(result) {
      console.log(result.name);
      console.log(result.description);
      console.log('----------------');
    });
  });
}

// this function runs for each neighborhood link. We'll go and scrape a descrption
function getNeighborhoodDescription(neighborhood, cb) {
  request(neighborhood.link, function(error, response, data) {
    var $ = cheerio.load(data);

    // get the first paragraph (the description) and store in the neighborhood object
    neighborhood.description = $('h2').first().text();

    // return the appended neighborhood object to the async.concat call
    cb(null, neighborhood);
  });
}
```

## Wrapup

This is just a sampling of the various utilities included in the `async` module. Some other useful functions include `.forever`, `.until`, `.queue`, and `.times`. For usage samples, see the documentation:

https://github.com/caolan/async
