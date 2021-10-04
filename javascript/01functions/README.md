# Functions

## Objectives

* Describe a situation where you would use:
  * A function with a return value
  * A function without a return value
  * A function with a parameter
* Describe the difference between printing and returning
* Write a function with and without a return value
* Write a function with a parameter
* Write a function that operates on two or more parameters
* Identify the scope of variables inside and outside functions

## Defining a function

A function is a module that can store and invoke code. When writing repetitive code, we can isolate code into **functions** in order to reduce repetition. For example, if we needed to say "Hello World" to the screen multiple times, we can create a function like so.

```javascript
let greeting = function() {
    console.log("Hello World");
}

greeting();
```

Note that a function is assigned to a variable, and we can **call** the function by taking the variable name and appending parentheses to the end of the function variable.

**Parts of a function**

```text
let FUNCTIONNAME = function() {
    //CODE
}
```

We can also create functions that accept **parameters**, and use those parameters as variables in the function.

## Defining a function with a parameter

```javascript
let greeting = function(taco) {
    // anything inside of here will execute when called
    console.log("Good morning", taco);
}

let name = "Josh"
let name2 = "Brian"
greeting(name);
greeting(name2);
```

## Defining a function with two parameters

Functions can have multiple parameters, separated by commas.

```javascript
let greeting = function(taco, stuff) {
    // anything inside of here will execute when called
    console.log("Good morning", stuff, taco);
    console.log("taco:", taco);
    console.log("stuff:", stuff);
}

let name = "Josh"
let name2 = "Brian"
greeting(name, name2);
greeting(name2, name);
```

## Printing and returning are different

Note that functions can have **input** via parameters. They can also have **output** as return values. Returning values from a function is denoted by the keyword `return`. Also, return values are optional.

Note that printing something to the screen using `console.log` is not the same as returning values.

```javascript
let multiply = function(num1, num2) {
    console.log("inside the function");
    // return result = num1 * num2;
    return num1 * num2
}

let firstNum = 2;
let secNum = 3;
let taco = multiply(firstNum,secNum);

console.log(firstNum + " multiplied by " + secNum + " is " + taco )
```

```javascript
// With a return value
let returnHello = function (name) {
    return("Hello, " + name)
}

console.log("with a return value:", returnHello("jane") );

// Without a return value
let returnHello2 = function(name) {
    console.log("inside returnHello2: Hello, " + name);
}
returnHello2("nachos");
console.log("without a return value:", returnHello2("taco") ); //will show as undefined
```

## Declaring functions

There are two different ways to declare a function

```javascript
let multiply = function(a, b) {
    return a * b;
}

function multiply(a, b) {
    return a * b;
}
```

The difference between these two is that the first one is defined at run-time, meaning that if we try to call the function before it's declared, an error will be thrown:

```javascript
multiply(2, 2); // ERROR

let multiply = function(a, b) {
    return a * b;
}
```

The second declaration is defined at parse-time, so we can call the function wherever we'd like.

```javascript
multiply(2, 2); // success

function multiply(a, b) {
    return a * b;
}
```

Despite being more flexible, the former declaration that assigns the function to a variable is more common when developing Node applications.

### Exercises

1. What is the return value of this function when called?

```javascript
let lightsabers = function(num) {
    console.log('I have ' + num + ' lightsabers.');
}

lightsabers(2);
```

1. How would the function above be modified if the user wanted to pass in an object of lightsabers, like this one?

```javascript
let myLightsaberCollection = {
    blue: 1,
    green: 3
}

let lightsabers = function(lightsaberCollection) {
    //code here
}

lightsabers(myLightsaberCollection);

// Output
// I have 1 blue lightsaber
// I have 3 green lightsabers
```

