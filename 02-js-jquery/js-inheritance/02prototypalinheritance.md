#Prototypal Inheritance

### What is Inheritance, and why do we want to use it?

Inheritance is a way for objects to inherit properties from other objects. This allows for your code to be organized and prevent needless repetition.

For example, there are many types of boats in the world, but all of them have properties in common. We can organize our objects so that all the different types of boats (steamboat, sailboat, motorboat) inherit properties that they share, instead of repeating them in each object.

**The repetitive way**
```js
function Sailboat(length, width, sails) {
  this.length = length;
  this.width = width;
  this.sails = sails;
}

function Steamboat(length, width, smokeStacks) {
  this.length = length;
  this.width = width;
  this.smokeStacks = smokeStacks;
}

function Motorboat(length, width, motors) {
  this.length = length;
  this.width = width;
  this.motors = motors;
}
```

**The inheritance way**
```js
function Boat(length, width) {
  this.length = length;
  this.width = width;
}

function Sailboat(length, width, sails) {
  Boat.call(this, length, width);
  this.sails = sails;
}
Sailboat.prototype = Object.create(Boat.prototype);
Sailboat.prototype.constructor = Sailboat;


function Steamboat(length, width, smokeStacks) {
  Boat.call(this, length, width);
  this.smokeStacks = smokeStacks;
}
Steamboat.prototype = Object.create(Boat.prototype);
Steamboat.prototype.constructor = Steamboat;


function Motorboat(length, width, motors) {
  Boat.call(this, length, width);
  this.motors = motors;
}
Motorboat.prototype = Object.create(Boat.prototype);
Motorboat.prototype.constructor = Motorboat;
```

By using the inheritance method, not only do we group shared properties into another object, but we can attach functions to the superclass's object's prototype, and now all boats have that function!
```js
Boat.prototype.getDimensions = function() {
  console.log('This boat has a width of ' + this.width + ' and a length of ' + this.length);
}
```

Now the Sailboat, Steamboat, and Motorboat can all use the `getDimensions` function, through what's called the **prototype chain**.



![Prototype Chain](images/prototype-chain.jpg)

Whenever an object doesn't directly have a function or property, it traverses up the prototype chain to see if any parents have it. In this case, SailBoat, Steamboat, and Motorboat go up to their parent (Boat) and see that Boat has a `getDimensions` function.


### Inheriting Via Prototypes: A Closer look

We have previously mentioned that objects can inherit properties and methods from other objects. In JavaScript we use prototypes to do this and it is called inheritance. The formal term for this inheritance via prototypes is called prototypal inheritance.

Inheritance is done in a few steps

1. In the subclass (the child class that will get methods and properties from its parent), call the superclass (also known as parent class) using `call`. We'll pass along `this`, which is initially an empty object, and let the superclass take care of attaching properties.

2. Set the prototype of the subclass to a new instance of the superclass. This connects the subclass and superclass as "links" in the prototype chain.

3. Set the constructor of the subclass equal to it's constructor function (which was overwritten when the prototype was set to the superclass).

Why do we reset the constructor? See [this](http://stackoverflow.com/questions/8453887/why-is-it-necessary-to-set-the-prototype-constructor) answer.

Given the following example, let's create a Student class that inherits from Person.
```js
function Person(name) {
  this.name = name
}

Person.prototype.greet = function() {
  return 'Hello, my name is ' + this.name;
};

function Student(name, course) {
  Person.call(this, name);
  this.course = course;
};

Student.prototype = Object.create(Person.prototype);
Student.prototype.constructor = Student;
```


Why do we use `call` when calling the parent class? Why not just run `Person(name)`?

It all comes down to `this`. In our Person constructor, `this` refers to the name of the new Person object being created. However, inside the Student constructor, `this` refers to the new Student object being created.

`call` gives us a way to redefine what `this` represents. Let's dive more into the use of `call`, and its sibling, `apply`.
