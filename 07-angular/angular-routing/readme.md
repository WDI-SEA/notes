#Angular Routing

##Objectives

* Incorporate an organized folder structure into an Angular app
* Use a configuration block to add routing to an app
* Retrieve route params from within a controller
* Compare hashbang mode to HTML5 mode when configuring the router

##Refactoring the Star Wars App

We already refactored the Star Wars app for you. Take a look at the starter code and see how everything is now organized.

* app
  * app.js
  * controllers.js
  * services.js
* views
* index.html

In more complex apps, we may even create folders for controllers and services, and create multiple modules for controllers and services. However, having just files will do just fine for this app.

Also, note that we inject dependencies needed for each module. Specifically, we:

* inject **ngResource** into StarWarsServices
* inject **StarWarsServices** into StarWarsCtrls
* inject **StarWarsCtrls** into StarWarsApp

Whew! That's a lot of dependency injection. While beyond the scope of our Angular unit, injecting dependencies makes testing in Angular easier, because we can **mock** different dependencies if needed by defining test dependencies (this would be very useful for "faking" API calls).

Moving on, let's add routing to our app.

##Using the Angular Router

We'll be using the default `ngRoute` module for routing our application (There are other third-party and beta routers available, which are linked at the bottom of the notes).

The CDN link you'll need in `index.html`:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular-route.js"></script>
```

You'll probably notice that this is a dependency, and it'll need to be injected into our app.

In `app/app.js`:

```js
var app = angular.module('StarWarsApp', ['StarWarsCtrls', 'ngRoute']);
```

And lastly, we'll need a way to switch out templates and controllers on our index page. For now, let's replace the contents of `<body></body>` with the following:

In `index.html`:

```html
<body>
  <div class="container">
    <ng-view></ng-view>
  </div>
</body>
```

`ng-view` will help complement our routes by including the template and controller of the current route. Whenever a route changes, the contents of `ng-view` are replaced with the new template and controller.

But we need routes! And controllers! And views! We already have the controller, so let's set up the view. In `app/views`, we'll create a template called `index.html` to list out all the films.

```html
<h1>Star Wars</h1>
<div class="well" ng-repeat="film in films">
  <h2>{{film.title}}</h2>
  <p>{{film.opening_crawl}}</p>
</div>
```

###Configuring Routes

In `app/app.js`, let's add the following to the bottom of the file:

```js
app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  //define routes
  $routeProvider
  .when('/', {
    templateUrl: 'views/index.html',
    controller: 'FilmsCtrl'
  });

  $locationProvider.html5Mode(false).hashPrefix('!');
}]);
```

To add additional routes, just add additional `when` conditions. Remember to define a controller (if necessary) for each page and create content in the related template files. Adding an `otherwise` condition is handy for creating a 404 page.

```js
app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  //define routes
  $routeProvider
  .when('/', {
    templateUrl: 'views/index.html',
    controller: 'FilmsCtrl'
  })
  .when('/about', {
    templateUrl: 'views/about.html'
  })
  .otherwise({
    templateUrl: 'views/404.html'
  });

  $locationProvider.html5Mode(false).hashPrefix('!');
}]);
```

**Note:** Run the app using a local HTTP server.

**Try it:** Take a moment and implement templates for an about page and 404 page.

###Linking to routes

You can link to angular routes using `<a>` link tags

```html
<a href="/#!/about">About Page</a>
```

###Wait, what's this prefix?

You'll see that Angular routes contain a "hashbang" prefix **#!**. This is necessary in order to distinguish between front-end and back-end routes. A route like `/about` would end up being routed to a server, while Angular knows that `/#!/about` is a front-end route.

We can set `html5Mode` to true if we want to get rid of the "hashbang", but it will involve some configuration on the server. Specifically for Express, you would want all routes that aren't the root route (`/`) to send the back `index.html`.

See this [StackOverflow response](http://stackoverflow.com/questions/31778324/angular-html5-mode-with-express) for more on this topic.

##Passing URL Parameters

Passing URL parameters with angular routes is similar to routes in Express or Rails. First we define a route with a parameter.

```js
.when('/films/:id', {
  templateUrl: 'views/filmShow.html',
  controller: 'FilmShowCtrl'
})
```

Then, we can access the parameter in the controller using `$routeParams` (which must be injected into the controller). So let's add another controller in `controllers.js` for getting a specific doughnut.

```js
.controller('FilmShowCtrl', ['$scope', '$routeParams', 'Films', function($scope, $routeParams, Films) {
  $scope.film = {};

  Films.get({id: $routeParams.id}, function success(data) {
    $scope.film = data;
  }, function error(data) {
    console.log(data);
  });
}]);
```

Now we need a `filmShow.html` file in the `views` folder:

```html
<h1>{{film.title}}</h1>

<div class="well">
  <p>{{film.opening_crawl}}</p>
  <small>Release date: {{film.release_date}}</small>
</div>

<a href="/#!/" class="btn btn-primary">&larr; Back</a>
```

...andddddd we need to add links to `views/index.html`

```html
<h1>Star Wars</h1>

<a href="/#!/about">About Page</a>

<div class="well" ng-repeat="film in films">
  <h2><a ng-href="/#!/films/{{film.id}}">{{film.title}}</a></h2>
</div>
```

**Note:** Why do we use `ng-href`? [Because Angular (see documentation)](https://docs.angularjs.org/api/ng/directive/ngHref)

##Programatically Navigating

You can also cause the angular router to navigate to a new route using `$location` (another service).

```js
.controller('FilmsCtrl', ['$scope', '$location', 'Films', function($scope, $location, Films) {
  // $scope.films = [];
  //
  // Films.query(function success(data) {
  //   $scope.films = data;
  // }, function error(data) {
  //   console.log(data);
  // });

  //this will redirect the home page to location
  $location.path('/about');
}])
```

This can also be used to get the current location, simply by leaving the parenthesis empty.

```js
//returns the current angular url / route
$location.path()
```

##Other Routers

* [UI Router](https://github.com/angular-ui/ui-router) - Good 3rd party router for supporting changing multiple views. Will be obsolete once the new angular router is ready.
* [New Angular router](https://angular.github.io/router/) - New router replacing `ngRoute` in angular 1.5 and 2.0. Not yet ready for production use.
