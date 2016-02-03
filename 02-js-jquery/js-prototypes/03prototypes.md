# Prototypes

One of the more complex concepts in JavaScript is prototypes. You can think of a Prototype as the building block for your object (and remember that everything in JavaScript is an object). For any object you create, you can attach methods and properties to its prototype. So in our constructor functions, we can attach methods and properties to the prototype so that every object we create from it will have these properties and methods!

**Example**

```js
function Person(name) {
  this.name = name;
}

Person.prototype.sayHi = function() {
  console.log("Hi " + this.name);
}
```

But wait a second....how is the prototype different than just adding a method to the constructor function? Let's examine these two pieces of code.

###Attaching a method to the constructor function:

```js
function Person(name){
  this.name = name;
  this.sayHi = function(){
    alert("Hi " + this.name);
  };
}

var elie = new Person("Elie");
elie.sayHi();
```

###Attaching a method to the prototype:

```js
function Person(name){
  this.name = name;
};

Person.prototype.sayHi = function() {
  console.log("Hi " + this.name);
};

var elie = new Person("Elie");
elie.sayHi();
```

So...these both work, but how are they different, and which one is better? The answer is the second one, here's why:

* When we attach methods to the constructor function, these methods are written each time a new instance of the object is created, which is a waste of memory.
* By attaching the method to the prototype, we only have to declare it once.

**Try it:** Run the following code in the browser console, and expand each object. Look at the contents. Note that each object has its own version of the `volume` function, even though each copy does the same thing.

```js
function Box(length, width, height) {
  this.length = length;
  this.width = width;
  this.height = height;
  this.volume = function() {
    console.log(this.length * this.width * this.height);
  }
}

var boxes = [];
for (var i = 1; i <= 100; i++) {
  boxes.push(new Box(i, i, i));
}

console.log(boxes);
```

**Try it:** Run the following code in the browser console, and expand each object. Note that each object does not have a `volume` function, and that's because it exists in the prototype. Since a constructor only has one prototype, there's only one `volume` function.

```js
function Box(length, width, height) {
  this.length = length;
  this.width = width;
  this.height = height;
}

Box.prototype.volume = function() {
  console.log(this.length * this.width * this.height);
}

var boxes = [];
for (var i = 1; i <= 100; i++) {
  boxes.push(new Box(i, i, i));
}

console.log(boxes);
```

##Practical Purpose for Prototypes and Constructors

Let's now take this a step further - how is it that all arrays in JavaScript have methods like `.forEach` and `.map`? How is it that all strings in JavaScript have methods like `.indexOf`?

**The answer:** These methods are part of that object's prototype. Even further, objects can inherit properties and methods from other objects (that's how the boolean and number objects have the `.toString` function)

**Try it:** Try accessing the `.forEach` and `.map` functions that belong to the Array's prototype.

```js
Array.prototype.forEach

Array.prototype.map
```
