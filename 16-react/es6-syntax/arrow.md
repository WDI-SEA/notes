# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) ES6 - Arrow Functions


### Learning Objectives
*After this lesson, you will be able to:*
- Create arrow functions
- Create arrow functions with implicit returns
- Describe the `this` binding


## Arrow Functions

"function", "function", "function"... Are you tired of writing that word? So are we. The arrow function `=>` is a more concise syntax for declaring functions. It looks like a little rocket arrow, in fact, and something that cool isn't usually in JavaScript. Arrow functions are not _only_ different in syntax, however - their scope is also different from a regular `function` declaration.

### Basic Syntax

Using the function keyword, to create a function that adds two to an argument, you'd write:

```javascript
function addTwo(num) {
  return num + 2;
}
```

> Here, we are naming our function `addTwo` and it takes in one parameter, `num`.

Using arrow syntax, you'd write:

```javascript
var addTwo = num => {
  return num + 2;
}
```

> Here, we declare our function as a variable: `var AddTwo`. To pass in the variable, we put it after an equal sign: `var addTwo = num`. Then we have the arrow function and the actual function definition.

If there are multiple parameters passed into an arrow function, you put them in parentheses, just like a traditional function. Before, using the function keyword, you would write:

```javascript
function multiply(x, y) {
  return x * y;
}
```

With the arrow syntax, it's:
```javascript
var multiply = (x, y) => {
  return x * y;
}
```

#### Do you remember `const`?
Anything that was a `var` in ES6 is better practice to write as a `let` or a `const`.
You can write functions using `const` or `let` as well. This can be helpful to know that the function's assignment later cannot change (in the case of `const`) or explicitly declared as can (in the case of `let`). Using `let` or `const` with a function is not necessary, but in some cases it's good practice (more on that later).

So now with the arrow syntax, we had:
```javascript
var addTwo = num => {
  return num + 2;
}
```
And we can simply change the `var` to a `const`.
```javascript
const addTwo = num => {
  return num + 2;
}
```
Another thing to note is that if the function does nothing except a return, we can simplify it even further. All of these function declarations are valid:

```javascript
// traditional
function addTwo(num) {
  return num + 2;
}

// arrow syntax
const addTwo = num => {
  return num + 2;
}

// now even further simplified
const addTwo = num => num + 2;
```
> note that we dropped the curly braces and `return` keyword

You can play with arrow functions in [this CodePen](https://codepen.io/SuperTernary/pen/qjQPzY). Remember, you can also use ES6 syntax in the Chrome dev-tools console, and your Create React App projects are transpiled with Babel, so you can use ES6 there too.


### Implicit return

Continuing a thought, the last thing we noted is that if the function does nothing except a return, we can simplify it even further:

```javascript
const addTwo = num => num + 2;
```
> We dropped the curly braces and `return` keyword.

If there is no block following the arguments of an arrow function (meaning nothing in `{ }` curly braces), whatever follows is the return value of the function. The `addTwo` example above simply returns the value of `num + 2`. This is called an **implicit return**.
```js
const addTwo = num => num + 2;
```
**Importantly**, we can only use implicit return for functions which only contain a `return` statement.

Consider these two functions.

- `addTwo` can be simplified to one line, as it's just a `return` statement.
- `mutateNumbers` contains more than just a return statement, so we still need the curly braces.

```javascript
const addTwo = num => {
  return num + 2;
}

// The same with implicit return
const addTwo = num => num + 2;

// Cannot have implicit return
const mutateNumbers = num => {
  newNum = 6;
  alert(newNum);
  return num + newNum;
}
```

Using implicit returns can shorten our syntax and make our code more readable. The following function `lowercaseListOfWords` takes one argument- an array of strings- and returns a new array of lowercase strings.

Written with functions, this would look something like:

```javascript
function lowercaseListOfWords(arrayToModify) {
  return arrayToModify.map(function(word) {
    return word.toLocaleLowerCase();
  });
}
```

However, using ES6, the arrow function, and implicit returns, we can make that one (albeit long!) line:

```javascript
const lowercaseListOfWords = arrayToModify => arrayToModify.map(word => word.toLocaleLowerCase());
```

**Importantly**, one gotcha to be aware of with implicit returns is that object literals must be wrapped in parentheses, so the interpreter (browser, compiler, etc.) can distinguish them from blocks. An example:

```javascript
const isItActive = isActive => ({ active: isActive });
```

> This function only returns one thing, but because it implicitly returns an object literal, it must be wrapped in parentheses.

Play around with implicit returns from arrow functions [in this CodePen](https://codepen.io/SuperTernary/pen/ZymXgK?editors=001).

### This binding - and the lack thereof

So - now that we've learned all the fun syntax of the arrow function, let's talk about the benefits of actually using it.

In non-arrow functions, every function defines its own `this`. There are tons of hacks to preserve the context, like `var that = this` and using `.bind(this)`. This might look familiar:

```javascript
function eatBreakfast(pancakes) {
  var that = this;
  that.food = 'Knife please?';
  Waiter.bringCutlery(function (silverware) {
    that.food = silverware;
  });
}
```

Another popular variant is `var self = this`. Whatever hack you've been using, you don't need to do it anymore!

Arrow functions don't change the definition of `this`. So, if `this` is already defined in the scope, and you call an arrow function, you can access `this` directly.

```javascript
// Original function
function eatBreakfast(pancakes) {
  var that = this;
  that.food = 'Knife please?';
  Waiter.bringCutlery(function (silverware) {
    that.food = silverware;
  });
}

// Equivalent arrow function
const eatBreakfast = pancakes => {
  this.food = 'Knife please?';
  Waiter.bringCutlery((silverware) => this.food = silverware);
}
```

> Check it out - the arrow function can be anywhere you declare a function!
