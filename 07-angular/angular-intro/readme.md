#Intro to Angular

##Objectives

* Understand the purpose and reasoning for using Angular as a frontend framework
* Create an Angular app as a self-container module
* Bootstrap an Angular module to a HTML page
* Utilize and load controllers
* Implement two-way data binding using data attached to a controller's `$scope`


##Your Guide to AngularJS

![Angular over time](feelings_about_angularjs_over_time.png)
[Angular documentation](https://docs.angularjs.org/api)


##Angular Intro

Angular is an open source JS framework maintained by Google. It was created nearly 6 years ago - its longevity is a testament to its capability and usefulness. AngularJS is one of the most widely adopted MVC JS frameworks in use today and is a valuable job skill to put on your resume.

AngularJS provides the following benefits when used to develop web apps:
- Enables us to organize and structure **single page apps** using the popular MVC design pattern
- Makes us more productive when developing web apps because it provides features, such as data binding, that requires less code from the developer
- Provides methods to inject dependencies, which make testing easier


#### The Components of AngularJS

![angular_components](https://cloud.githubusercontent.com/assets/25366/8970275/a1ab2ee2-35fd-11e5-8b23-65f4159ff7d6.jpg)

#### Modules

Modules are containers for related code.  The concept of *modules* is prevalent throughout programming, and here, it's considered to be a container for our app.

#### Config & Routes

Each AngularJS module has a *config* method that allows us to provide code that runs when a module is loaded.  The *config* method is used most commonly to setup routing, which allows your app to have multiple views.

#### Controller

Controllers in AngularJS serve two primary purposes:

- Initialize the data used for the view they are attached to
- Contain the primary code to respond to user events, such as when a user clicks on a button

A controller is a JS constructor function that is instantiated by the _ng-controller_ directive.

#### Services & Factories

Services provide a way to organize related code and data that can be shared by controllers and even other services. Unlike controllers, which are instantiated and destroyed as the views they are attached to come into and out of view, services are created once (singletons) and persist for the life of the application.

Services should be used to hold the bulk of your application's logic and data, thus keeping controllers focused on what they are responsible for.

#### Directives

Directives are "markers" in HTML - most commonly as attributes and custom element tags. When processed by AngularJS's HTML compiler, they attach behavior to DOM elements or even transform them and/or their children.


#### Filters

Filters are used to transform data. They are very flexible and can be used for formatting text in a view, such as making it all uppercase, or used to filter and sort an array of items.

#### The AngularJS Mindset

Programming a web app with AngularJS requires a different mindset. To use AngularJS effectively, it helps to think of your application being driven by data - you change data, the app responds. We naturally think more procedurally when coding, we attach an event handler and write code to respond.

Let's look at an example of the different approaches.  Say we want an edit form to show when a button is clicked:

- Procedurally, we would attach an event handler to the button. The handler code would select the element and set its display property to something besides "none".
- Using AngularJS, we declare a click handler on the Button element.  The handler could set a variable named editMode equal to true, and the view would respond automatically.
- Remember, drive your application using data - your data model is the single source of truth!

### SPA Architecture

Single Page Applications (SPA) are all the rage today. A misconception is that a SPA has only a single view - this is far from the truth!  The single page aspect of a SPA refers to a single page coming from the server, such as our _index.html_ page.  Once loaded, the SPA changes views by using _client-side_ routing, which loads partial HTML snippets called templates.

![spa_architecture](https://cloud.githubusercontent.com/assets/25366/8970635/896c4cce-35ff-11e5-96b2-ef7e62784764.png)

Client-side routing requires something known as a _router_.  A router in AngularJS, at a minimum, is used to define our routes, specify the template for that route, and specify which controller to attach to that view.

Notice that it's possible to recreate this SPA architecture using jQuery, but it would be cumbersome and hard to organize.

##Basic Angular Setup - Modules, Controllers, Views

Like a few frameworks we've seen, there's not a particular way to organize your application to make Angular work. We'll have to create our own, but let's try to keep it standard.

In your starter folder, you'll see some empty files and a couple of folders.

First, let's get Angular from [Google's CDN](https://developers.google.com/speed/libraries/#angularjs) and paste into script tag in the `<head></head>`

```html
 <head>
   <meta charset="utf-8">
   <title>Intro to Angular</title>
   <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.js"></script>
 </head>
```

Now, we set up a module. Go to your `app.js` file, and all it takes is this little line:

```js
// Define a new module. The first argument is what we want to call our app, the second is an array of dependencies (which we don't need at the moment, so there are none)
var introApp = angular.module('IntroToAngularApp', []);
```

This sets our app up. It's important to include that array when defining a module, even if there are no dependencies – that tells Angular we're initializing a module.

Now, back in our HTML, make sure your `app.js` is included in a script tag, and add an `ng-app` directive in the `<html>` tag.
```html
<!DOCTYPE html>
<html ng-app="IntroToAngularApp">
  <head>
    <meta charset="utf-8">
    <title>Intro to Angular</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.js"></script>
    <script src="js/app.js"></script>
  </head>
```

Since we defined it in `app.js` with a name of `IntroToAngularApp`, we just reference what we named it here. This tells the HTML to use that module.

Now, let's just check to make sure it worked. If it worked correctly, we should be able to put some simple expression in our HTML, and Angular will render it.

```html
<body>
{{ 1 + 1 }}
</body>
```

If Angular's working, it'll add our numbers together and spit out a 2 on the page – that's how templating works in Angular, inside curly brackets.

Open it up in a browser to check. And remember – if it doesn't work, check your browser's console for errors!

##Create an Angular controller

So, in Angular's flavor of MVC, controllers are intended to primarily:

1. Respond to user actions.
2. Provide data to the view (occasionally referred to the view-model).

Now, lets stub out a new controller and plug it into our module:

Let's place the following in `app.js`

```javascript
introApp.controller('HomeCtrl', ['$scope', function($scope) {

}]);
```

Pretty much everything you do in Angular will depend on a controller. You can add a controller to your module using the `controller` method which takes 2 parameters.

* Name of the controller
* An array containing the dependencies and initialization function for this controller.

###Scope

The scope (represented in Angular as `$scope`) is where you will store all of your data in a controller. Any data stored in the scope will be available in the view within the DOM object that has the `ng-controller` directive.

####Dependency Injection

To access the `$scope` object we need to inject it as a dependency. This is done by including it as a string in the array before the function AND defining it as a parameter within the function.

You can load as many dependencies as you want, but it is vital that the strings in the array are in the same order as the parameter in the function.

```javascript
introApp.controller('HomeCtrl', ['$scope', '$http', function($scope, $http) {

}]);
```

In the above example we load `$scope` and `$http`. Notice the strings `$scope` and `$http` and the 2 parameters `$string` and `$http`. The strings tell it what to load and the parameters are how you access it within the function. This is done because the variables names can end up changing during JavaScript minification. You can technically name the parameters (in the function) whatever you want, but it's good practice to name them they same as the dependency that you are loading.

Side note: `$http` is the angular http (ajax) module. We'll learn about that later. It is just used above to demonstrate how to load multiple dependencies.

###Initializing scope

Once you load the `$scope` dependency you just use it like any other object. You can define whatever keys you want and assign them any value. the value will then be available in the view.

```javascript
introApp.controller('HomeCtrl', ['$scope', function($scope) {
  $scope.name = 'Bill Murray';
}]);
```

###Load the controller on a page

Controllers can be attached to DOM elements using the `ng-controller` directive.

```html
<div ng-controller="HomeCtrl"></div>
```

Then you can reference variables attached to `$scope` in the view like this:

```html
<div ng-controller="HomeCtrl">
  Hello, {{name}}
</div>
```

##Two-way data binding

Angular uses two-way data binding. This means that if any data in `$scope` is changed in the controller, it is reflected in the view AND if the data is changed in the view, it is updated in the controller.

###ng-model

The easiest way to achieve two-way data binding is using the `ng-model` directive. `ng-model` can be used on any form element and creates a two-way data binding to the value of the `$scope` key specified.

Expanding on the example above (same controller code) you can do the following...

```html
<div ng-controller="HomeCtrl">
  Hello, {{name}}
  <input type="text" ng-model="name">
</div>
```

Now if the user types something into the input box, `$scope.name` will be updated in the controller, which also means the `{{name}}` will be updated to match.

##Handling user events

Angular can also handle user events using other directives. One of the most common directives is `ng-click`.

###ng-click

To detect a click event we use the `ng-click` directive and give it a function to call when the user clicks an element. This function is attached to the `$scope` just like a value.

```javascript
introApp.controller('HomeCtrl', ['$scope', function($scope) {
  //default
  $scope.happy = false;

  //toggle function
  $scope.toggleHappy = function() {
    $scope.happy = !$scope.happy;
  }
}]);
```

```html
<button ng-click="toggleHappy()">Toggle Happy</button>
<p>{{happy}}</p>
```

clicking the button will cause happy to switch `$scope.happy` true to false.

Alternatively, you can put any code directly in the `ng-click`, but it is generally smart to use functions instead. However, for simple one-liners, it's generally OK.

```html
<button ng-click="happy = !happy;">Toggle Happy</button>
<p>{{happy}}</p>
```

Again, notice that in the controller it is `$scope.happy`, but in the view (html) it is just `happy` (without `$scope`).

##Controllers Instantiate Data

As a wrapup to Angular, know that controllers are just functions that can include dependencies and data instantiation. Every time the `ng-controller` directive is used, a controller is instantiated. To illustrate this, try to copy/paste your controller `div` and see what happens.

```html
<body>
  <div ng-controller="HomeCtrl">
    Hello, {{name}}
    <input type="text" ng-model="name">

    <div>
      <button ng-click="happy = !happy;">Toggle Happy</button>
      <p>{{happy}}</p>
    </div>
  </div>
  <div ng-controller="HomeCtrl">
    Hello, {{name}}
    <input type="text" ng-model="name">

    <div>
      <button ng-click="happy = !happy;">Toggle Happy</button>
      <p>{{happy}}</p>
    </div>
  </div>
</body>
```

You'll see that each instance of `ng-controller` has its own set of data. Pretty sweet!

##Conclusion

As you can see, the structure of Angular differs significantly from other frontend frameworks we've been using, like jQuery. Take a moment and review:

* How do you make modules and controllers in Angular?
* What must we do in order to bootstrap an Angular app to a page?
* Compare and contrast jQuery and AngularJS in the context of adding a click event.
