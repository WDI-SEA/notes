#Bootstrap Modals

##Controllers and Templates Everywhere!

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
