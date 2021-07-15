#Angular Routing

##Objectives

* Incorporate an organized folder structure into an Angular app
* Use a configuration block to add routing to an app
* Retrieve route params from within a controller
* Compare hashbang mode to HTML5 mode when configuring the router

**Note, we'll be building upon the Star Wars app from the Angular Services codealong**

##Refactoring the Star Wars App

You'll probably notice soon that placing all of our controllers and services into `app.js` will soon become disorganized. So let's refactor the Star Wars app from earlier. Let's follow this layout.

```
- app
  - app.js
  - controllers.js
  - services.js
- views
- index.html
```

This will work for our examples in class, but for more complex apps, you will want to look at file structures that compartmentalize your app even more. [See this Scotch tutorial for details](https://scotch.io/tutorials/angularjs-best-practices-directory-structure)

Now, let's move everything out of `app.js` so that we have three modules. We'll be injecting these modules like so:

* inject **ngResource** into StarWarsServices
* inject **StarWarsServices** into StarWarsCtrls
* inject **StarWarsCtrls** into StarWarsApp

Whew! That's a lot of dependency injection. While beyond the scope of our Angular unit, injecting dependencies makes testing in Angular easier, because we can **mock** different dependencies if needed by defining test dependencies (this would be very useful for "faking" API calls).

**app.js**

```js
angular.module('StarWarsApp', ['StarWarsCtrls'])
```

**controllers.js**

```js
angular.module('StarWarsCtrls', ['StarWarsServices'])

// place your controllers down here
```

**services.js**

```js
angular.module('StarWarsServices', ['ngResource'])

// place your services down here
```

Also, make sure to **change and include those script files in index.html**

```html
<script src="app/app.js"></script>
<script src="app/services.js"></script>
<script src="app/controllers.js"></script>
```

Moving on, let's add routing to our app.

##Using the AngularUI Router

We'll be using the popular `ui.router` module for routing our application.

The CDN link you'll need in `index.html`:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.18/angular-ui-router.js"></script>
```

You'll probably notice that this is a dependency, and it'll need to be injected into our app.

In `app/app.js`:

```js
var app = angular.module('StarWarsApp', ['StarWarsCtrls', 'ui.router']);
```

And lastly, we'll need a way to switch out templates and controllers on our index page. For now, let's replace the contents of `<body></body>` with the following:

In `index.html`:

```html
<body>
  <div class="container">
    <div ui-view></div>
  </div>
</body>
```

The `ui-view` directive will help complement our routes by including the template and controller of the current route. Whenever a route changes, the contents of `ui-view` are replaced with the new template and controller.

But we need routes! And controllers! And views! We already have the controller, so let's set up the view. In `app/views`, we'll create a template called `films.html` to list out all the films.

`app/views/films.html

```html
<h1>Star Wars Films</h1>
<div class="well" ng-repeat="film in films">
  <h2>{{film.title}}</h2>
  <p>{{film.opening_crawl}}</p>
</div>
```

###Configuring Routes

In `app/app.js`, let's add the following to the bottom of the file:

```js
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');

  //define routes
  $stateProvider
  .state('films', {
    url: '/',
    templateUrl: 'views/films.html',
    controller: 'FilmsCtrl'
  });

  //$locationProvider.html5Mode(false).hashPrefix('!');
}]);
```

**Note:** Run the app using a local HTTP server.

To add additional routes, just add additional `state` functions. Remember to define a controller (if necessary) for each page and create content in the related template files. Adding the `otherwise` condition is handy for redirecting invalid routes.

```js
.config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
  $urlRouterProvider.otherwise('/');

  //define routes
  $stateProvider
  .state('films', {
    url: '/',
    templateUrl: 'views/films.html',
    controller: 'FilmsCtrl'
  })
  .state('about', {
    url: '/about',
    templateUrl: 'views/about.html'
  });
}]);
```


**Try it:** Take a moment and implement a template for an about page.

###Linking to routes

You can link to angular routes using `<a>` link tags

```html
<a href="/#/about">About Page</a>
```

###Wait, what's this prefix?

You'll see that Angular routes contain a "hashbang" prefix **#**. This is necessary in order to distinguish between front-end and back-end routes. A route like `/about` would end up being routed to a server, while Angular knows that `/#/about` is a front-end route.

We can configure our app to not use the "hashbang", but it will involve some configuration on the server. Specifically for Express, you would want all routes that aren't the root route (`/`) to send the back `index.html`.

See this [StackOverflow response](http://stackoverflow.com/questions/31778324/angular-html5-mode-with-express) for more on this topic. We'll be implementing this configuration later on.

##Passing URL Parameters

Passing URL parameters with angular routes is similar to routes in Express or Rails. First we define a route with a parameter.

```js
.state('showFilm', {
  url: '/films/:id',
  templateUrl: 'views/filmShow.html',
  controller: 'FilmShowCtrl'
})
```

Then, we can access the parameter in the controller using `$stateParams` (which must be injected into the controller). So let's add another controller in `controllers.js` for getting a specific film.

```js
.controller('FilmShowCtrl', ['$scope', '$stateParams', 'Films', function($scope, $stateParams, Films) {
  $scope.film = {};

  Films.get({id: $stateParams.id}, function success(data) {
    $scope.film = data;
  }, function error(data) {
    console.log(data);
  });
}])
```

Now we need a `filmShow.html` file in the `views` folder:

```html
<h1>{{film.title}}</h1>

<div class="well">
  <p>{{film.opening_crawl}}</p>
  <small>Release date: {{film.release_date}}</small>
</div>

<a href="/#/" class="btn btn-primary">&larr; Back</a>
```

...andddddd we need to add links to `views/films.html`

```html
<h1>Star Wars Films</h1>

<div class="well" ng-repeat="film in films track by $index">
  <h2><a ng-href="/#/films/{{$index+1}}">{{film.title}}</a></h2>
</div>
```

**Note:** Why do we use `ng-href`? [Because Angular (see documentation)](https://docs.angularjs.org/api/ng/directive/ngHref)

##Programatically Navigating

You can also cause the angular router to navigate to a new route using `$state` (another service).

```js
.controller('FilmsCtrl', ['$scope', '$state', 'Films', function($scope, $state, Films) {
  // $scope.films = [];
  //
  // Films.query(function success(data) {
  //   $scope.films = data;
  // }, function error(data) {
  //   console.log(data);
  // });

  //this will redirect to a different state
  $state.go('about');
}])
```

This can also be used to get the current state, simply by leaving the parenthesis empty.

```js
//returns the current angular state, complete with the URL, template, and controller
$state.current
```

##Resources

* [Nested State in UI Router](https://github.com/angular-ui/ui-router/wiki/Nested-States-&-Nested-Views)
* [ngRoute](https://docs.angularjs.org/api/ngRoute)
  * The official Angular router, with less functionality than UI router
