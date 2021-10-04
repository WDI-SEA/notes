# Object Literals and String Interpolation

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) ES6 - Object Literals and String Interpolation

### Learning Objectives

_After this lesson, you will be able to:_

* Simplify expressions using object literals
* Simplify expressions using template literals
* Define imports without global variables

This is the last bit of ES6 we'll check out before doing an exercise!

## Object literal shorthand

Object literal shorthand is a simple but useful bit of syntactic sugar. If you want to assign a variable as the value of the key of the same name, you don't have to write it twice. _What?_

If we declare a variable, `price`, and set it equal to 100: `const price = 100;`

We then have an object called `item`. Now, `item` also has a variable of how much that item costs, which happens to also be `price`. They are different variables \(one is global, and the other is specific to the `item` object\); they just happen to share the same name. So our `item` object might be:

```javascript
const item = {
  price: 15,
};
```

Now, let's say that when we initialize `item`, instead of hard-coding a number into the initialization, we want to set `price` to be whatever the global price is. This global price is also stored in a variable called `price`, right?

It looks like this:

```javascript
const price = 100;

const item = {
  price: price
};
```

It's weird looking, but it works.

Well, it turns out that having two different variables with the same name and setting them equal to each other is a pretty common thing to do. ES6 decided to just simplify this by dropping the duplicate and having it mean the same thing. So now we can do:

```javascript
const price = 100;

const item = {
  price
};
```

Less to write, and less to read when you come back to it. A win-win!

## Template literals

Template literals bring us string interpolation in JavaScript. This means we can create dynamic strings with more readable syntax.

Before ES6, we had:

```javascript
const name = 'Mike';
const greeting = 'Hi, ' + name + '.';
```

Now, using template literals, we can make this easier:

```javascript
const name = 'Mike';
const greeting = `Hi, ${name}.`;
```

> Note that now, we can directly refer to the variable using ${} syntax within our string.

In fact, combining an arrow function with a template literal, we can do this:

```javascript
const greeting = name => `Hi, ${name}.`;
```

[Check it out in CodePen!](https://codepen.io/SuperTernary/pen/eRQeOR?editors=001)

## Lastly! Imports and modules

In ES6, you can import modules directly without declaring them as global variables. This makes namespacing your app a non-issue. Before module imports, namespace was often a primary concern in JavaScript.

So, if you want export my `addTwo` function as a module, you can create a file called "addTwo.js":

```javascript
const addTwo = num => num + 2;

export default addTwo;
```

And in another file, say "app.js", i can import it:

```javascript
import addTwo from './addTwo';

addTwo(3); // 5
```

You can also export multiple modules from a file, like so:

```javascript
// in arithmetic.js
export const addTwo = num => num + 2;

export const addThree = num => num + 3;
```

And somewhere else:

```javascript
import { addTwo, addThree } from './arithmetic';
```

