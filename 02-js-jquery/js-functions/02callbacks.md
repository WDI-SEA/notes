# Callback Functions

* Define a callback function
* Demonstrate ability to pass a function as a parameter

Functions may seem very different than the other javascript items we've worked with before, but don't be fooled! Functions are still [_first-class_ values](http://wiki.c2.com/?FirstClass), which means you can
* store them in variables
* **pass them as arguments to other functions**
* create them within functions
* return them from functions

If this all seems very strange, you could think of a javascript function as a _javascript_ object that stores code to be run instead of key/value pairs. A **callback function** is just a regular function that we pass as an argument to another function!

Take a look at this example:

```js
function greeting() {
	console.log("Hello, World!");
}

function formalGreeting(informalGreeting) {
	informalGreeting();
	console.log("How are you?");
}

formalGreeting(greeting)
```

When we pass a function into another function as a paramenter, we are passing the _function definition_, so it can be called at a later time (hence the name _callback_). Notice the different outputs in the below example. First we print the function itself, then we _call_ the function and print the output.

```js
function returnRandom() {
	return (Math.random()*100).toFixed();
}

function yellRandom(randomNumGenerator) {
	console.log("GENERATOR DEFINITION: ", randomNumGenerator)
	console.log("YOUR RANDOM NUMBER IS: "+randomNumGenerator());
}

yellRandom(returnRandom)
```

