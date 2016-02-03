# JavaScript Inheritance

##Objectives

* Use prototypal inheritance to group shared properties even further
* Understand the process of calling parent classes from a constructor.
* Utilize various JavaScript methods in combination with prototypal inheritance.
* Explore the next generation of inheritance in JavaScript using ES6 classes.

## Review

We mentioned in the prototypes lesson that a prototype is the building block of an object. When we create a new class, we can attach attributes and methods to the prototype (as a better alternative to adding them in the constructor function to save memory).

### Review of a Constructor and Prototype In JS

In javascript we don't have classes, so we use constructor functions and prototypes to create them.

```js
function Person(name) {
	this.name = name;
}

Person.prototype.greet = function() {
	return "Hello, my name is " + this.name;
};
```
