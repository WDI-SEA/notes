![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Angular with Express

##Objectives

* Review common components of an Angular app
* Review how a RESTful API is implemented in Express
* Serve an Angular app from an Express app
* Configure the Angular router to support HTML5 mode in tandem with Express

##Everything Angular

As a quick review, let's write on the board what we've learned about Angular. Here are some questions to go off of:

* How is an Angular app created?
* Where is data instantiated?
* How do we get data from other sources, like APIs?
* How do we share data across the app?
* What are all the different ways to modularized components?
* What directives have we used?

##Everything Express

Take a look at the starter code and set up the Express app. Make sure your Mongo server is running and all dependencies are installed. This app provides an API for one model.

##Adding an Angular App to Express

Angular is a front-end framework, so we can **serve** the app files and index page once using Express, as well as serve API endpoints.

Let's go back to Angular Day 1.

![spa_architecture](https://cloud.githubusercontent.com/assets/25366/8970635/896c4cce-35ff-11e5-96b2-ef7e62784764.png)

Note that serving the index page and app **once** and **only once** will make our application a single-page app. So let's take a second and add an Angular app to the starter code.

###Serving Static Files

In order to serve static files, create a folder in the root of the Express app, and add the folder so the Express app can find it. We'll call this folder `public`.

In `index.js`:

```js
app.use(express.static(path.join(__dirname, 'public')));
```

Create a file in the `public` folder called `index.html`, and for now, put some valid HTML markup in the file.

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Airplanes</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular-route.js"></script>
    <script src="app/app.js"></script>
  </head>
  <body>
    <h1>Airplanes</h1>
  </body>
</html>
```

Lastly, we'll set the very last route to the following:

```js
app.get('/*', function(req, res) {
  res.sendFile(path.join(__dirname, 'public/index.html'));
});
```

The wildcard should cover any other routes that don't match the API routes. Instead of giving a 404 error, we'll serve the single-page app and let the Angular router take control. The benefit of this? We can enable HTML5 mode in the router!

**Note:** This means that routes that should normally cause 404 errors will need to be handled by the Angular router as well. In other words, `http://localhost:3000/alsdkfjalsdf` will be sent to the front-end.

As far as the app is concerned, we can now create an app in the `public/app` folder, just as before. Let's make a simple one with only views.

In `app/app.js`:

```js
var app = angular.module('AirplaneApp', ['ngRoute']);

app.config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
  $routeProvider
  .when('/', {
    templateUrl: 'app/views/airplanes.html'
  })
  .otherwise({
    templateUrl: 'app/views/404.html'
  });

  $locationProvider.html5Mode(true);
}]);
```

Make a couple views so that we have valid pages, and replace the body of `index.html` with `<ng-view></ng-view>` tags.

```html
<body>
  <div class="container">
    <ng-view></ng-view>
  </div>
</body>
```

If you try to run the entire app now, you'll get a console error that needs to be addressed.

```
Error: [$location:nobase] $location in HTML5 mode requires a <base> tag to be present!
```

All we need is a `<base href="/">` tag in the `<head></head>` tags. See [Angular's documentation on this tag.](https://docs.angularjs.org/error/$location/nobase)
