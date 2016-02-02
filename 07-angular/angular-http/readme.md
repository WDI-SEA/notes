![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Angular $http

##Objectives

* Use $http to access an API resource

##What is $http?

`$http` is a core Angular service provided for you to use. It allows the browser to send HTTP requests and responses, similar to AJAX calls in jQuery.

##Using $http
We can use the `$http` service to request data from an external source. `$http` can be incorporated into an Angular app via dependency injection. This can happen on either the module or controller.

In our example, we'll include `$http` as a dependency for each controller. Specifically, we'll be using `$http` to access a public API that allows Cross Origin Resource Sharing (CORS).

###Getting Started

Take a look at the sample code, which should have scaffolds for `index.html` and `js/app.js`. Add the following to `app.js`:

```javascript
var movieApp = angular.module('MovieApp', []);

movieApp.controller('SearchCtrl', ['$scope', '$http', function($scope, $http) {

}]);
```

Yes, we are making yet another OMDB app. This time, with Angular.

So let's setup what we'll need to perform a request to OMDB.

* A method to search for a movie (form input)
* A model to store the search term
* A URL to send the term to (OMDB)
* A function to receive and process the response

First, let's setup the form and model. (don't forget to setup `ng-app` and `ng-controller` first)

In `index.html`

```html
<h1>Movie App</h1>
<form class="form" ng-submit="search()">
  <div class="form-group">
    <label>Search for a Movie:</label>
    <input type="text" class="form-control" ng-model="searchTerm">
    <input type="submit" class="btn btn-primary">
  </div>
</form>
```

We'll see that we created a model called `searchTerm` bound to the input field, and a function called `search()` to execute when the form submits.

Now for the controller. Inside the `SearchCtrl` within `js/app.js`:

```javascript
$scope.searchTerm = '';

$scope.search = function() {
  var req = {
    url: "http://www.omdbapi.com",
    method: 'GET',
    params: {
      s: $scope.searchTerm,
    }
  }

  $http(req).then(function success(res) {
    //do something with the response if successful
    console.log(res);
  }, function error(res) {
    //do something if the response has an error
    console.log(res);
  });
};
```

We just added a variable called `searchTerm` to `$scope`, as well as added the `search()` function. We also created an object to store the URL and search params (those search params will be converted to a querystring by `$http`).

Lastly, we call `$http` to perform a request with the `req` object, then expect success and error callbacks. Try running this code and see what `res` contains. Note that `res` is the entire response, and we need to call `res.data` to access the payload of the response.

###Rendering Movies

In order to render movies to the page, we need to attach the data received to `$scope`. Let's add a `movies` variable to the controller's scope, and assign the data if the response is OK:

```js
$scope.movies = [];

$http.get(req).then(function success(res) {
  if (res.status === 200) {
    $scope.movies = res.data.Search;
  }
  console.log(res);
}, function error(res) {
  console.log(res);
});
```

Note that we obtain `res.data.Search` because the response is an object with a key called `Search`. The value associated with this key has our results.

Printing them out requires `ng-repeat` in `index.html`

```html
<div class="well" ng-repeat="movie in movies track by $index">
  {{movie}}
</div>
```

You'll see that each `movie` is an object. Take a few minutes and clean this up so each **well** displays the title and poster of each movie.

**Related:** Use `ng-src` when including Angular markup in an image link. It's a common problem that pops up. [Link to the ngSrc documentation.](https://docs.angularjs.org/api/ng/directive/ngSrc)
