#Angular Directives and Filters

##Objectives

* Use ng-class for working with dynamic classes
* Use ng-if & ng-hide/ng-show to hide & show elements
* Use ng-repeat to iterate over data
* Use ng-submit to submit forms
* Explain the what filters are and how they manipulate data

##Directives

Directives are additional DOM nodes – think custom attributes on HTML tags – that Angular uses to apply behaviors to HTML elements. Angular comes with a bunch of different directives for different behaviors and gives you the ability to create your own. So far, we've used a few like `ng-app`, `ng-controller`, `ng-model`, and `ng-click`.

##Dynamic classes (ng-class)

You can use `ng-class` to dynamically change the class of a HTML element based on a value of the `$scope`.

There are two ways to do this. You can specify a variable to be passed in as a string from the controller OR you can specify an object and each key will be added as classes if the associated value is truthy.

You can also use this in conjuction with the regular `class` parameter for classes that will always be included (see class="btn" below)

```html
<div ng-class="myClassName">Welcome!</div>
<button class="btn" ng-class="{'btn-primary':primary,'btn-xs':small}">Do it</button>
```

```javascript
//inside of controller
$scope.myClassName = "well";
$scope.primary = true;
$scope.small = true;
```

##Hiding elements (ng-if, ng-hide, ng-show)

There are 3 ways to show and hide elements. All three take a boolean value (from the `$scope`) to determine if the DOM element should be visible or not.


* `ng-show` - Shows the item if the value is truthy. Hides it if it's falsey
* `ng-hide` - The exact inverse of ng-show
* `ng-if` - Works like ng-show, but completely removes the element from the DOM if ng-if is falsey.

Note that if you use `ng-if`, the element is completed removed from the DOM. This means that any click handlers will also be removed, even if the element is added again. For this reason, you'll usually want to use `ng-hide` and `ng-show`.

```html
<button class="btn" ng-click="happy = !happy" ng-class="{'btn-primary':primary,'btn-xs':small}">Do it</button>

<div ng-show="happy">I am happy</div>
<div ng-hide="happy">I am sad</div>
```

```javascript
//inside controller
$scope.happy = true;
```

##Listing items (ng-repeat)

Instead of using a for loop inside our app, we can use the `ng-repeat` directive to loop over an array and access the contents.

```html
<ul>
  <li ng-repeat="toDo in toDoList">{{toDo}}</li>
</ul>
```

```javascript
//inside controller
$scope.toDoList = [
  'Water the chia pet',
  'Take out trash',
  'Think about life'
];
```

This directive can also be used to iterate over objects, if desired.

```html
<ul>
  <li ng-repeat="(key, value) in person">{{key}} - {{value}}</li>
</ul>
```

```javascript
//inside controller
$scope.person = {
  name: 'Frankie',
  occupation: 'driver',
  age: 34
};
```

`ng-repeat` also provides some special properties inside the directive, the most useful being `$index`. You'll likely notice that AngularJS won't allow duplicates in an array. This is because it uses a function to optimize instance handling once we start adding and removing items from a collection.

To get around this, we can track elements by an identifier, like `$index`.

```html
<ul>
  <li ng-repeat="toDo in toDoList track by $index">{{toDo}}</li>
</ul>
```

```javascript
//inside controller
$scope.toDoList = [
  'Water the chia pet',
  'Take out trash',
  'Think about life',
  'Think about life'
];
```

There's great information about this directive in the [AngularJS documentation on ngRepeat](https://docs.angularjs.org/api/ng/directive/ngRepeat)

##Submitting Forms (ng-submit)

When submitting forms, it's possible to attach the `ng-click` directive to the submit button, and perform a function on click. However, since the form submits a submit action when the submit button is clicked, we can attach the `ng-submit` directive to listen for this event.

```html
<form ng-submit="submitToDo()">
  <input type="text" ng-model="toDo">
  <input type="submit">
</form>
```

```js
//inside controller
$scope.toDo = '';
$scope.submitToDo = function() {
  $scope.toDoList.push($scope.toDo);
  $scope.toDo = '';
};
```

## Filters

### What are Filters?

Filters are functions used to change and manipulate how data is displayed. This provides separation between how we **store** data and how we **display** data.

### Built-in Filters

[Filter Components](https://docs.angularjs.org/api/ng/filter)

* filter
* currency
* number
* date
* json
* lowercase
* uppercase
* limitTo
* orderBy

Let's try to add a `limitTo` filter to our list.

```html
<ul>
  <li ng-repeat="toDo in toDoList | limitTo:3 track by $index">{{toDo}}</li>
</ul>
```
