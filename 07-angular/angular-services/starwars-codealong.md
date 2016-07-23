#Star Wars App

##Getting Started

Create a new folder called `starwarsapp` with the following folders and files:

```
- starwarsapp
  - js
    - app.js
  - index.html
```

Setup the HTML page with the usual tags.

###Adding Dependencies

First thing's first, let's add the correct dependencies inside the `head` tags. Additionally, add Bootstrap if you wish.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular-resource.js"></script>
<script src="js/app.js"></script>
```

Note that in order to use `$resource`, we need to include an additional script. We'll also need to inject the dependency (named `ngResource`) into our app.

In `app.js`:

```js
angular.module('StarWarsApp', ['ngResource'])

.controller('FilmsCtrl', ['$scope', function($scope) {

}]);
```

Make sure to add `ng-app` and `ng-controller` directives to `index.html` and test the app before continuing.

###Creating a Film Service

Now, we're going to create a service for accessing Star Wars films using the factory recipe. This service will provide an object we can inject into controllers, and it'll provide functions for interacting with the Star Wars API.

We'll create this service in the same file for now.

In `app.js`, we'll create a factory and inject it into the controller.

```js
angular.module('StarWarsApp', ['ngResource'])

.factory('Films', ['$resource', function($resource) {
  return $resource('http://swapi.co/api/films/:id');
}])

.controller('FilmsCtrl', ['$scope', 'Films', function($scope, Films) {
  console.log(Films);
}]);
```

When we refresh the page, the contents of the Films service should be logged to the browser console.

###Using the Films service

In order to use the Films service, we can call `get` and `query` from the controller. If we had a complete RESTful service, we could also call `save` and `remove`.

In `app.js`:

```js
app.controller('FilmsCtrl', ['$scope', 'Films', function($scope, Films) {
  $scope.films = [];
  Films.query(function success(data) {
    $scope.films = data;
  }, function error(data) {
    console.log(data);
  });
}]);
```

In `index.html`:

```html
<div class="well" ng-repeat="film in films">
  <h2>{{film.title}}</h2>
  <p>{{film.opening_crawl}}</p>
</div>
```

But wait! You'll notice that an error appears when you reload the page. That's because `$resource` assumes that the `query` function will return an **array**, but the Star Wars API returns an **object**. Luckily, we can customize the service with our own functions. Let's modify the service like so:

```js
.factory('Films', ['$resource', function($resource) {
  return $resource('http://swapi.co/api/films/:id', {}, {
    query: { isArray: false }
  });
}])
```

This will return a resource with a modified query method.

**Try it:** Use the `get` method from the Films service to retrieve the second film (id of 2). If you're not sure how to pass the film id in, consult the documentation for `$resource`.

### Why use a Service?

You may be wondering why we're using a service for a one-line resource. Usually, resources are more complex and can be customized as you see fit. Take a look at the [documentation for $resource](https://docs.angularjs.org/api/ngResource/service/$resource) and see what can be customized. Even if we didn't add additional customizations, the service allows many controllers to access the resource as a singleton.

Here's a trivial example of customizing our Films resource, by specifying different function names.

```js
app.factory('Films', ['$resource', function($resource) {
  return $resource('http://swapi.co/api/films/:id', {}, {
    all: { method: 'GET', cache: false, isArray: false },
    get: { method: 'GET', cache: false, isArray: false },
    save: { method: 'POST', cache: false, isArray: false },
    update: { method: 'PUT', cache: false, isArray: false },
    delete: { method: 'DELETE', cache: false, isArray: false }
  });
}]);
```

Note that for a lot of APIs, `isArray` will be set to true for the GET all endpoint. This isn't the case for the Star Wars API.
We also set the `cache` to false, but it could be set to true for performance improvements.
We also may want to customize the `all` endpoint in the future, if we want to limit results
(imagine getting all Facebook users when calling `.all`).

##Conclusion

We've used services when working with `$http` and Bootstrap modals, and we just made our own. By doing so, we've isolated business logic out of our controllers, so that they can focus mainly on initializing and manipulating data.

Later, we'll add routing to this Star Wars app and implement all of the CRUD functions.

## Finished Code (Example)

Here's some example finished code. This will likely not match yours, but try playing around with the example and see if you can pull other resources from the Star Wars API!

index.html:

```html
<!DOCTYPE html>
<html ng-app="StarWarsApp">
<head>
  <title>Star Wars App</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular-resource.js"></script>
  <script src="js/app.js"></script>
</head>
<body ng-controller="HomeCtrl">
  <div>
    <input type="integer" ng-model="movieId">
    <button ng-click="getMovie(movieId)">Get</button>
    <button ng-click="getAll()">All</button>
  </div>

  <div ng-if="loading">
    Loading...
  </div>

  <div ng-if="!loading" ng-repeat="film in films">
    <h1>{{film.title}}</h1>
    <p>{{film.opening_crawl}}</p>
  </div>
</body>
</html>
```

js/app.js:

```js
var app = angular.module('StarWarsApp', ['ngResource']);

app.factory('FilmsFactory', ['$resource', function($resource) {
  // use the colon syntax to specify the id parameter in the url.
  var url = 'http://swapi.co/api/films/:id';

  return $resource(url, {}, {
    // overwrite the isArray value when querying for movies
    query: { isArray: false }
  });
}]);

app.controller('HomeCtrl', ['$scope', 'FilmsFactory', function($scope, FilmsFactory){
  $scope.movieId = 1;
  $scope.films = [];
  $scope.loading = false;

  $scope.getAll = function() {
    $scope.loading = true;
    FilmsFactory.query(function success(data) {
      $scope.films = data.results;
      $scope.loading = false;
    }, function error(data) {
      console.log('error');
      $scope.loading = false;
    });
  };

  $scope.getMovie = function(id) {
    $scope.loading = true;
    FilmsFactory.get({ id: id }, function success(data) {
      // placing data in an array in order for ng-repeat to work on a single movie
      $scope.films = [data];
      $scope.loading = false;
    }, function error(data) {
      console.log('error');
      $scope.loading = false;
    });
  };
}]);
```
