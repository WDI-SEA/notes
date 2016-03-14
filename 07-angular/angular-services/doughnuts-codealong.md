#Doughnut App

##Getting Started

Create a new folder called `doughnutapp` with the following folders and files:

```
- doughnutapp
  - js
    - app.js
  - index.html
```

Setup the HTML page with the usual tags.


###Adding Dependencies

First thing's first, let's add the correct dependencies inside the `head` tags. Additionally, add Bootstrap if you wish.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular-resource.js"></script>
<script src="js/app.js"></script>
```

Note that in order to use `$resource`, we need to include an additional dependency. We'll also need to inject `ngResource` into our app.

In `app.js`:

```js
var app = angular.module('DoughnutApp', ['ngResource']);

app.controller('DoughnutCtrl', ['$scope', function($scope) {

}]);
```

Make sure to add `ng-app` and `ng-controller` directives to `index.html` and test the app before continuing.

###Creating a Doughnut Service

Now, we're going to create a service using the factory recipe. This service will provide an object we can inject into controllers, and it'll provide functions for interacting with the Doughnut API.

We'll create this service in the same file for now.

In `app.js`, we'll create a factory and inject it into the controller.

```js
var app = angular.module('DoughnutApp', ['ngResource']);

app.factory('Doughnut', ['$resource', function($resource) {
  return $resource('http://api.doughnuts.ga/doughnuts/:id');
}]);

app.controller('DoughnutCtrl', ['$scope', 'Doughnut', function($scope, Doughnut) {
  console.log(Doughnut);
}]);
```

When we refresh the page, the contents of the Doughnut service should be logged to the browser console.

###Using the Doughnut service

In order to use the Doughnut service, we can call `get`, `query`, `save`, and `remove` from the controller.

In `app.js`:

```js
app.controller('DoughnutCtrl', ['$scope', 'Doughnut', function($scope, Doughnut) {
  $scope.doughnuts = [];
  Doughnut.query(function success(data) {
    $scope.doughnuts = data;
  }, function error(data) {
    console.log(data);
  });
}]);
```

In `index.html`:

```html
<div class="well" ng-repeat="doughnut in doughnuts">
  {{doughnut.style}} - {{doughnut.flavor}}
</div>
```

**Try it:** Use the `get` method from the Doughnut service to retrieve the second doughnut (id of 2).

###Why use a Service?

You may be wondering why we're using a service for a one-line resource. Usually, resources are more complex and can be customized as you see fit. Take a look at the [documentation for $resource](https://docs.angularjs.org/api/ngResource/service/$resource) and see what can be customized. Even if we didn't add additional customizations, the service allows many controllers to access the resource as a singleton.

Here's a trivial example of customizing our Doughnut resource, by specifying different function names.

```js
app.factory('Doughnut', ['$resource', function($resource) {
  return $resource('http://api.doughnuts.ga/doughnuts/:id', {}, {
    all: {method: 'GET', cache: false, isArray: true},
    get: {method: 'GET', cache: false, isArray: false},
    save: {method: 'POST', cache: false, isArray: false},
    update: {method: 'PUT', cache: false, isArray: false},
    delete: {method: 'DELETE', cache: false, isArray: false}
  });
}]);
```

Note that we set `isArray` to true for the GET all endpoint. We also set the `cache` to false, but it could be set to true for performance improvements. We also may want to customize the `all` endpoint in the future, if we want to limit results (imagine getting all Facebook users when calling `.all`).

##Conclusion

We've used services when working with `$http` and Bootstrap modals, and we just made our own. By doing so, we've isolated business logic out of our controllers, so that they can focus mainly on initializing and manipulating data.

Later, we'll add routing to this Doughnut app and implement all of the CRUD functions.
