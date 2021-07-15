# Angular Components

## Objectives

* Discuss where angular components come from
* Discuss controllerAs syntax
* Build angular app using angular component

Up to this point we've been mainly utilizing controllers and directives to display sections of our angular app. While this is completely fine and considered good practice, it isn't as future-proofed as we'd like.

To make our angular app more compatible with future releases and front-end methodologies we're going to utilize the **component** feature that was added to angular 1.5.

## Beginnings

Angular components grew out of a need for a structured way of creating modularized UI elements with separated scope. But wait, you might think, isn't that what a **directive** is for?

It's true that directives give us the ability to create UI elements like that, they aren't the most efficient means. Developers began using directives in ways they weren't originally intended but were more in line with component-based app structures.

This led the people at Google to implement a new feature in Angular 1.5 that would also be a core feature in Angular 2, components. The main pull for components is that they are easier to read than directives and they also follow Google-endorsed style practices.

[John Papa's Angular Style Guide](https://github.com/johnpapa/angular-styleguide/blob/master/a1/README.md)

## controllerAs syntax

So far we have been building controllers and directives with the **$scope** service that Angular gives us. Much like this:

```javascript
angular.module('MyModule', [])
.controller('MyCtrl', ['$scope', function($scope) {
  $scope.name = 'Cool Guy';
}]);
```

```html
<div ng-controller="MyCtrl">
  <h1>{{name}}</h1>
</div>
```

While this is a useful way to instantiate and utilize controllers for angular apps, there is another way that is preferred according to the Angular community and John Papa's guide. This method is know as **controllerAs** syntax.

```javascript
angular.module('MyModule', [])
.controller('MyCtrl', MyCtrl);

function MyCtrl() {
  this.name = 'Cool Guy';
}
```

```html
<div ng-controller="MyCtrl as thing">
  <h1>{{thing.name}}</h1>
</div>
```

So instead of utilizing the **scope** to build out our data for the view model, we actually attach all our view data onto the controller instance itself! The benefits of this structure is that we avoid needlessly attaching everything to the **scope** and we get the ability to name our view model something else that is easier to read.

Read more on the benefits of this style in [John Papa's guide](https://github.com/johnpapa/angular-styleguide/blob/master/a1/README.md#style-y031)

There is one more thing we can do to improve the structure of our controller syntax and that is getting rid of the **this** keyword. As we know **this** is contextual and can lead to odd issues if over-used. To avoid this we will capture **this** in a variable and separate it from the context.

```javascript
angular.module('MyModule', [])
.controller('MyCtrl', MyCtrl);

function MyCtrl() {
  var vm = this;
  vm.name = 'Cool Guy';
}
```

```html
<div ng-controller="MyCtrl as vm">
  <h1>{{vm.name}}</h1>
</div>
```

## But...but why?!

There are many in-depth reasons we would want to use the **controllerAs** syntax which are outlined in the style guide. The short of it is that it allows us to move away from bad Angular coding practices and build more DRY apps.

The main reason for us is that **controllerAs** is utilized in the **component()** method in Angular 1.5.

So what does a component look like? Lets see:

```javascript
(function() {
  'use strict';
  
  angular.module('TestApp', [])
  .controller('TestCtrl', TestCtrl)
  .component('myComp', {
    template: '<h1>Hello {{vm.name}}</h1>',
    controller: myCompController,
    controllerAs: 'vm'
  });
})()

function TestCtrl() {
  var vm = this;
  vm.controllerName = 'Cool Guy';
}

function myCompController() {
  var vm = this;
  
  vm.name = 'Bill';
}
```

```html
<div ng-app="TestApp">
  <div ng-controller="TestCtrl as vm">
    {{vm.controllerName}}
    <my-comp></my-comp>
  </div
</div>
```
