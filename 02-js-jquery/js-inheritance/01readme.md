# JavaScript Inheritance

##Objectives

* Use prototypal inheritance to group shared properties even further
* Utilize various JavaScript methods in combination with prototypal inheritance.
* Demonstrate ability to call parent classes from a constructor
* Explore the next generation of inheritance in JavaScript using ES6 classes.

## Review

We mentioned in the prototypes lesson that a prototype is the building block of an object. When we create a new class, we can attach attributes and methods to the prototype (as a better alternative to adding them in the constructor function to save memory).

### Review of a Constructor and Prototype In JS

In JavaScript we don't have classes, so we use constructor functions to act as "blueprints" for creating objects. We can attach properties to a constructor's **prototype**, which are shared across all constructor instances.

Note that neither Person instance actually has a `greet` property. We'll be diving into how `greet` would be resolved through prototypal inheritance.

```js
function Person(name) {
	this.name = name;
}

Person.prototype.greet = function() {
	return 'Hello, my name is ' + this.name;
};

var brian = new Person('Brian');
var paul = new Person('Paul');

brian.greet(); // Hello, my name is Brian
paul.greet(); // Hello, my name is Paul
```
