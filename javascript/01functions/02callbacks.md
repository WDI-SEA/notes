# Callbacks

* Define a callback function
* Demonstrate ability to pass a function as a parameter

Functions may seem very different than the other javascript items we've worked with before, but don't be fooled! Functions are still [_first-class_ values](http://wiki.c2.com/?FirstClass), which means you can

* store them in variables
* **pass them as arguments to other functions**
* create them within functions
* return them from functions

If this all seems very strange, you could think of a javascript function as a _javascript_ object that stores code to be run instead of key/value pairs. A **callback function** is just a regular function that we pass as an argument to another function!

Take a look at this example:

```javascript
const greeting = () => {
    console.log("Hello, World!");
}

const formalGreeting = (informalGreeting) => {
    informalGreeting()
    console.log("How are you?")
}

formalGreeting(greeting)
```

When we pass a function into another function as a paramenter, we are passing the _function definition_, so it can be called at a later time \(hence the name _callback_\). Notice the different outputs in the below example. First we print the function itself, then we _call_ the function and print the output.

```javascript
const returnRandom = () => {
    return (Math.random()*100).toFixed();
}

const yellRandom = (randomNumGenerator) => {
    console.log("GENERATOR DEFINITION: ", randomNumGenerator)
    console.log("YOUR RANDOM NUMBER IS: "+randomNumGenerator());
}

yellRandom(returnRandom)
```

## Anonymous Functions

If you define a function that is _only_ going to be used as a callback, and not called anywhere else, you can pass skip the functioning declaration and just define it as an **anonymous function** within the encompassing function call itself. An **anonymous function** is a function that isn't stored in a variable.

```javascript
const formalGreeting = (informalGreeting) => {
    informalGreeting()
    console.log("How are you?")
}

formalGreeting(()=>{
    console.log("Hello, World!");
})
```

**Exercise:** call `testTypes` and pass in a anonymous function that takes one argument and prints that argument using `console.log`.

```javascript
const testTypes = (someFunc) => {
    console.log("num input:")
    someFunc(0)
    console.log("bool input:")
    someFunc(true)
    console.log("str input:")
    someFunc('some string')
    console.log("numInput:")
    someFunc([1,2,'3'])
}
```

