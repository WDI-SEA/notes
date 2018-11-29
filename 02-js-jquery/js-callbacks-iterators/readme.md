# Functional Programming

Programming with functions! Weren't we already doing that? Well yes, but we can use functions more heavily, especially in place of loops.

##Objectives

* Use callback functions with setInterval and setTimeout

* Compare and contrast the four main JavaScript iterators: forEach, map, reduce, filter
    - Name an ideal situation for each one
* Utilize callbacks with JavaScript iterators

Previously, we saw that functions can be assigned to variables. For example:

```js
var add = function(a, b) {
  return a + b
}

add(1, 2);
> 3
```

Functions are **first-class citizens** in JavaScript. This means that we can create functions, store them into variables, and pass functions into other functions. Functions are only executed when called. Try this to illustrate:

###Exercise

Try running the following in Node. What is printed to the screen?

```js
var bag = function() {
  console.log('Hello, I am a bag');
}

console.log(bag);
```

We can take advantage of this behavior by defining **callback functions**. Callback functions are passed via variable name (reference), and are *called* at a specific time.

## Do something later: Callbacks

The `setTimeout()` function takes a function and a delay in
milliseconds, and executes the function as soon as possible after that
delay has passed.

```js
var announce = function() {
  console.log('Ding!');
}

var threeSecondTimeout = setTimeout(announce, 3000);
```

This can be done via **anonymous functions** as well. Anonymous functions are functions that are not stored to a variable. They are great for functions you only need to define once. Here's an example.

```js
var fiveSecondTimeout = setTimeout(function() {
  console.log('Ding!');
}, 5000);
```

The `setInterval()` function takes a function and a delay in
milliseconds, and executes that function as closely as possible each
time that interval of milliseconds has passed.

```js
function annoy() {
  console.log('Are we there yet?');
}

setInterval(annoy, 1000);
```

Things to be careful of: you need to know what the function expects as parameters. Javascript is forgiving, but not a mind-reader.

Oh, and if you want to disable the timers before they fire, you can use the `clearTimeout(timeoutHandle)` or `clearInterval(intervalHandle)` functions:

```js
var fourSecondTimeout = setTimeout(announce, 4000);
clearTimeout(fourSecondTimeout);

clearInterval(threeSecondInterval);
clearInterval(fiveSecondInterval);
```

## Returning functions from functions

You can probably guess by now how to return a function from a
function:

```js
var drinkMaker = function(drinkType) {
  return function(drinkVolume) {
    return {
      drink: drinkType,
      volume: drinkVolume
    };
  };
};

var cocktailMaker = drinkMaker('cocktail');
var smoothieMaker = drinkMaker('smoothie');

cocktailMaker('4oz');
smoothieMaker('16oz');
```

We'll see that if we print the contents of `cocktailMaker` and `smoothieMaker`, we get functions that were returned from the function `drinkMaker`. Now, we can call these functions and pass in additional arguments. Neat!

Functional programming is a popular topic in the context of Node, so we'll be seeing more examples like these in the future. Like with iterators!

## Iterators

Iterators are examples of _functional programming_ replacements for `for` loops. We can use these functions to perform common Array operations for us.

What might we want to with an array?

* run some piece of logic on each item
* create a new array with each item being slightly transformed
* filter the array to contain only a subset of items
* combine all the items in some fashion

We could accomplish all of this using `for` loops, but writing `for` loops is error prone and tiring. JavaScript provides iterator functions for all of these common operations. They are called (respectively):

* [forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
* [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
* [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
* [reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

##General Practice

1. Declare an array
2. Call an iterator on the array
3. Pass a function to the iterator
4. Get results


##forEach

`forEach` is the _functional programming_ replacement for your standard `for` loop.  You can take the body from your `for` loop, wrap it in a function, and pass that argument to `forEach`. Let's look at an example:

```js
var friends = ["Markus", "Tim", "Ilias", "Elie"];

// old way, with a for loop
for (var i = 0; i < friends.length; i++) {
  console.log("Hello, " + friends[i] + "!");
}

// cool new way, with the .forEach iterator
friends.forEach(function (buddy) {
  console.log("Hello, " + buddy + "!");
});

// both output the same thing
// > Hello, Markus!
// > Hello, Tim!
// > Hello, Ilias!
// > Hello, Elie!
```

**Try it**

Use the `.forEach` iterator to loop over the following
array of foods and say you like them.

```js
var foods = ["pizza", "tacos", "ice cream"];

// your code here

// The output should be
// > "I like pizza"
// > "I like tacos"
// > "I like ice cream"
```

**Try it again**

Use the `.forEach` iterator to loop over the following
array of objects and say how delicious each one is.

```js
var foods = [
  {name: "Pizza", level: "very"},
  {name: "Tacos", level: "mostly"},
  {name: "Cottage Cheese", level: "not very"}
];

// your code here

// The output should be
// > Pizza is very delicious
// > Tacos is mostly delicious
// > Cottage Cheese is not very delicious
```


##map

Sometimes we want to loop over an array and build a new array in the
process. This is what `map` helps us solve. It is like `forEach`, but
it returns the new array that is created.

```js
var names = ["tim", "ilias", "elie", "markus"];

// old way with for loop
var cased = [];
for (var i = 0; i < names.length; i++) {
  cased.push(names[i].toUpperCase());
}
console.log(cased);

// new way with `map`
var cased = names.map(function (person) {
  return person.toUpperCase();
});
console.log(cased);

// Should output
// > ["TIM", "ILIAS", "ELIE", "MARKUS"]
// > ["TIM", "ILIAS", "ELIE", "MARKUS"]
```

##filter

Filter is an iterator that loops through your array and filters it
down to a subset of the original array. A callback is called on each
element of the original array: if it returns true, then the element is
included in the new array, otherwise it is excluded.

```js
var names = ["tim", "ilias", "elie", "markus"];

var isEven = function (name) {
  return name.length % 2 === 0;
};
var isOdd = function (name) {
  return name.length % 2 !== 0;
};

var evenLengthNames = names.filter(isEven);
var oddLengthNames = names.filter(isOdd);

console.log(evenLengthNames);
console.log(oddLengthNames);

// Should output
// > ["elie", "markus"]
// > ["tim", "ilias"]
```

##reduce

Reduce iterates over an array and turns it into one, accumulated
value. In some other languages it is called `fold`.

```js
var nums = [1,2,3,4];
var add = function (a, b) {
  return a + b;
};

var sum = nums.reduce(add);
console.log(sum);

// Should output:
// > 10
// which is, 1 + 2 + 3 + 4
```

Reduce also usually accepts an option third parameter that will be the
initial accumulated value. If it is omitted, then the reduction starts
with the first two values in the array.

```js
var nums = [1,2,3,4];
var add = function (a, b) {
  return a + b;
};

var sum = nums.reduce(add, 10);
console.log(sum);

// Should output:
// > 20
// which is, 10 + 1 + 2 + 3 + 4
```

## Resources

Here are some good blog posts that break down `map`, `filter`, and `reduce`.

* [Transforming Arrays with Array#map](http://adripofjavascript.com/blog/drips/transforming-arrays-with-array-map.html)
* [Transforming Arrays with Array#filter](http://adripofjavascript.com/blog/drips/filtering-arrays-with-array-filter.html)
* [Transforming Arrays with Array#reduce](http://adripofjavascript.com/blog/drips/boiling-down-arrays-with-array-reduce.html)
