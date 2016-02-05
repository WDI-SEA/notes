#Bootstrap Directives and Animation

##Objectives

* Use third-party directives in an Angular application
* Utilize the concepts of dependency injection and templates with Bootstrap

##Bootstrap JS in Angular

You may have noticed that we left out `bootstrap.js` and `jquery.js` when working with our Angular apps. The reason for this is that we haven't used jQuery, and AngularJS is designed to be a *replacement* for jQuery in most regards. Instead of manipulating the DOM with handlers to events, we're letting directives handle manipulation for us.

Our events are also **data-driven**, meaning actions like `ng-submit` and `ng-repeat` affect the DOM depending on the data we provide to it.

Therefore, we need a set of directives to use Bootstrap JS elements, such as carousels, modals, dropdowns, etc.

##Bootstrap Directives

We can use Angular UI's Bootstrap directives in order to use different Bootstrap components. All we need is the `bootstrap.css` file and the directives script.

In `<head></head>` of the starter code, add:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular-animate.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-bootstrap/0.14.3/ui-bootstrap-tpls.js"></script>
<script src="js/app.js"></script>
```

Then, create an Angular application in `js/app.js`. Make sure to add the directives to the HTML file to bootstrap the application. Also, add `ngAnimate`, because we'll also be utilizing some animations.

```js
var app = angular.module('BootstrapApp', ['ngAnimate']);

app.controller('BootstrapCtrl', ['$scope', function($scope) {

}]);
```

##Adding a Navbar using ng-include

Partials are a common concept in web frameworks, and Angular is no exception. We can create "partial" views and render them in our app using the `ng-include` directive. Let's do this as we create a navigation bar.

Create a folder for holding views.

```bash
mkdir views

touch views/navbar.html
```

Create a navbar in `navbar.html`.

Then, use `ng-include` to include the partial, using the absolute path of the partial inside single quotes (this treats the path as a string).

Inside `index.html`:

```html
<div ng-include="'/views/navbar.html'"></div>
```

Lastly, if we try to render this page, there will be a cross origin error. So make sure to run a local HTTP server to load the partial (you should have a `srv` alias setup for this).

### Utilizing Angular Directives

Playing around with the navigation bar, you may notice that the "hamburger icon" dropdown does not work in mobile view. In order to utilize this, we'll have to add directives to create the **collapse** effect.

All of the Bootstrap directives are contained in an Angular module, so let's inject the Bootstrap UI module as a dependency for the app.

In `app.js`

```js
var app = angular.module('BootstrapApp', ['ngAnimate', 'ui.bootstrap']);
```

####Practice

Implement the **collapse** effect so that the navigation bar correctly collapses in mobile view. The [Bootstrap UI documentation](https://angular-ui.github.io/bootstrap) should be very helpful.

##Bootstrap Modals - Controllers and Templates Everywhere!

Most of the Bootstrap directives are straightforward, but the modals provide challenges relating to scope, controllers, and service injection.

We'll start off by creating a template for the modal content.

In `views/modal.html`:

```html
<div>
  <div class="modal-header">
    <button type="button" class="close" ng-click="close()">&times;</button>
    <h4 class="modal-title">Welcome to my Modal!</h4>
  </div>
  <div class="modal-body">

  </div>
  <div class="modal-footer">
    <button type="button" class="btn btn-default" ng-click="close()">Close</button>
    <button type="button" class="btn btn-primary" ng-click="saveChanges()">Save changes</button>
  </div>
</div>
```

We'll be adding more to the modal's body, so stay tuned.

Now, we need a way to open this modal once a button has been clicked. Let's create a button to do so.

In `index.html`

```html
<button type="button" class="btn btn-default" ng-click="open()">Open the modal!</button>
```

Now in order to open the modal, we're going to do the following:

1. Create a function called `open` in the Angular application.
2. Inject a dependency for utilizing modals.
3. Create another controller specifically for the modal instance.

In `js/app.js`

```js
app.controller('BootstrapCtrl', ['$scope', '$uibModal', function($scope, $uibModal) {
  $scope.navCollapsed = true;

  $scope.open = function() {
    $uibModal.open({
      animation: true,
      templateUrl: '/views/modal.html',
      controller: 'ModalInstanceCtrl'
    });
  };
}]);

app.controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', function($scope, $uibModalInstance) {
  $scope.close = function() {
    $uibModalInstance.dismiss('close');
  };

  $scope.saveChanges = function() {
    $uibModalInstance.dismiss('close');
  };
}]);
```

So let's breakdown what all this code implements.

* In order to open a modal, we need to inject a component called a **service** into our controller. In this case, Bootstrap UI provides a service called `$uibModal`.
  * This service provides functions for modals
* We can call `$uibModal.open` to open a new modal instance with parameters. We have to specify the location of the **template** and the **controller** used for the modal instance
* The controller `ModalInstanceCtrl` provides a controller specifically for a modal instance. The `$scope` in this controller is **separate** from the scope of the controller that called it.
  * `$uibModalInstance` represents the modal instance, and we can call functions like `dismiss` and `close` in order to perform operations on the instance.

###Passing Data between Controllers

We may have an instance where data needs to be passed from the main controller to the modal instance controller. In that case, the Bootstrap UI modal service provides some functionality to pass data back and forth.

* Including a `resolve` object to the modal instance serves as a "gateway" for passing data to the modal controller
  * Once data is passed into the object, it can be accessed by including it as a dependency in the controller
  * Attach the data from the dependency to the controller's `$scope`
* Data can be passed back to the main controller by passing it as an argument to the `$uibModalInstance.close` function
  * Once the data is passed, it can be accessed in the main controller through `result`, a promise.

###The Final Code

**js/app.js**
```js
var app = angular.module('BootstrapApp', ['ngAnimate', 'ui.bootstrap']);

app.controller('BootstrapCtrl', ['$scope', '$uibModal', function($scope, $uibModal) {
  $scope.navCollapsed = true;
  $scope.selectedItem = '';

  $scope.open = function() {
    var modalInstance = $uibModal.open({
      animation: true,
      templateUrl: '/views/modal.html',
      controller: 'ModalInstanceCtrl',
      resolve: {
        items: function() {
          return ['Larry', 'Curly', 'Moe'];
        }
      }
    });

    modalInstance.result.then(function(selectedItem) {
      $scope.selectedItem = selectedItem;
    });
  };
}]);

app.controller('ModalInstanceCtrl', ['$scope', '$uibModalInstance', 'items', function($scope, $uibModalInstance, items) {
  $scope.items = items;
  $scope.selectedItem = items[0];
  $scope.selectItem = function(item) {
    $scope.selectedItem = item;
  }

  $scope.close = function() {
    $uibModalInstance.dismiss('close');
  };

  $scope.saveChanges = function() {
    $uibModalInstance.close($scope.selectedItem);
  };
}]);
```

**views/modal.html**
```html
<div>
  <div class="modal-header">
    <button type="button" class="close" ng-click="close()">&times;</button>
    <h4 class="modal-title">Welcome to my Modal!</h4>
  </div>
  <div class="modal-body">
    <button class="btn btn-primary" ng-repeat="item in items" ng-click="selectItem(item)">{{item}}</button>
    <div>
      Selected Item: {{selectedItem}}
    </div>
  </div>
  <div class="modal-footer">
    <button type="button" class="btn btn-default" ng-click="close()">Close</button>
    <button type="button" class="btn btn-primary" ng-click="saveChanges()">Save changes</button>
  </div>
</div>
```

**index.html**
```html
<div ng-include="'/views/navbar.html'"></div>
<button type="button" class="btn btn-default" ng-click="open()">Open the modal!</button>
{{ selectedItem }}
```
