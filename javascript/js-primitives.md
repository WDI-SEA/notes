# Primitives

## Objectives

* Briefly describe the history of JavaScript and its purpose as a language
* Define JavaScript variables and data structures
* Utilize primitives and operators in order to solve problems using JavaScript
  * Manipulate integers, floating point, and decimal numbers
  * Manipulate strings
  * Use booleans as return values, as variables, and in the context of a conditional

## History

**Then**

* developed by Brendan Eich \(for Netscape, now Mozilla\)
* 10 days
* went through a few different names before settling on JavaScript \(Java was popular\)
* taken to [ECMA](https://en.wikipedia.org/wiki/Ecma_International) for standardization

**Now**

* JavaScript is THE front-end language
* clunky, [things to complain about](http://wtfjs.com/), but it works and is web-driven!
* tons of open source libraries
* also used as a backend language, using Node.js
* working on [ECMAScript 6](https://github.com/lukehoban/es6features)

### Repl.it

[Repl.it](https://repl.it/) is a quick and easy tool for practicing Javascript \(and other languages!\) that we'll use throughout the class. Here is a [Repl.it](https://repl.it/@tmdarneille/JSPrimitives#index.js) with the code from this lesson you can reference later, but for now open up a new repl of your own to code along to this lesson in!

## Comments

Comments come in two forms

### Line comments

```javascript
// descriptive stuff
```

### Multi-line comments

```javascript
/**
  These
  are
  comments on
  many lines
*/
```

## Numbers

Numbers are one of the _types_ of **values** we want to be able to interact and play with in JS.

### Integers

```text
 ..., -1, 0, 2, 3, 4, 5, ...
```

### Floats \(or Decimal numbers\)

```text
 2.718, 3.14, .5, .25, etc
```

In JS these are both the same **type** of object, which it calls _Numbers_.

This can infrequently cause problems!

```javascript
0.1 * 0.2 = 0.020000000000000004
```

[How to deal with floating point precision in JavaScript](http://stackoverflow.com/questions/1458633/how-to-deal-with-floating-point-number-precision-in-javascript)

### Exercise

```javascript
2 + 2 * 3
```

How would you get the `2 + 2` to execute before the `* 3`? In other words, how would you change this expression to get 12?

## Strings

Strings are collections of letters and symbols known as **Characters**, and we use them to deal with words and text in Javascript. Strings are just another type of **value** in Javascript.

```javascript
"John"
'Jane'
```

### Exercise

You can use operators on strings too! Try typing `"John" + "Jane"`. This is called String concatenation

### Tangent: Type coercion

\[Type coercion is the process of converting value from one type to another\]\([https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/\#:~:text=Type coercion is the process,Symbol \(added in ES6](https://www.freecodecamp.org/news/js-type-coercion-explained-27ba3d9a2839/#:~:text=Type%20coercion%20is%20the%20process,Symbol%20%28added%20in%20ES6)\).\)

Try this...

```javascript
"1" + 1
```

Without removing the quotes, how would you get this to equal 2?

## Booleans

Booleans are a type that can only have one of two values: true or false.

```javascript
true
false
```

## Operator Review

```text
+ (add)
- (subtract)
* (multiply)
/ (divide)
% (modulus)
```

### Special Number Operators

Javascript can be a little cheap with the number of operations it allows you to do. For example, how is someone supposed to square a number or cube a number easily? Luckily there is a special `Math` object with some very useful methods.

* Taking a number to some `power`? Then just use `Math.pow`

```javascript
// 3^2 becomes
Math.pow(3, 2);
// => 9

// 2^4 becomes
Math.pow(2, 4);
// => 16
```

* Taking a square root

```javascript
// √(4) becomes
Math.sqrt(4);
// => 2
```

* Need a `random` number? Then use `Math.random`.

```javascript
// The following only returns a random decimal
Math.random();
// => .229375290430

/**
  The following will return a
  random number between 0 and 10
*/
Math.random() * 10;
```

* Since Numbers can be **Floats** or **Integers** we often want to get rid of remaining decimal places, which can be done using `Math.floor`.

```javascript
// Remove the decimal
Math.floor(3.14)
// => 3

Math.floor(3.9999)
// => 3
```

## Variables

Having made some expressions it becomes evident we want to store these values.

```javascript
var myNumber = 1;
// or also

var myString = "Greetings y'all!";
```

The main note to make here is that these variables should always have the `var` keyword and use `camelCase`

## Objects Everywhere

In Javascript we just discussed two types of values we can use. We call these values objects, which for now just means that in addition to storing some data you also get to use some helpful methods when you are working with them.

In JavaScript, almost everything is an object \(primitive types are the exception\).

* If you want to turn a number into a string you can use a helpful method called `toString`.

```javascript
myNumber.toString()
// => "1"
```

### Common String / Number methods

* Numbers
  * `.toString()` - converts a number to a string
  * `.toFixed()`, - converts a number to a fixed string representation
    * More info: [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Number/toFixed](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/toFixed)
  * `parseInt('33')` - converts a string to an integer
  * `parseFloat('3.1')` - converts a string to a floating point number
* Strings
  * `.split('')` - converts a string into an array split in a provided character
  * `.indexOf('s')` - returns the index of the first appearance of a provided string
  * `.toUpperCase()` - converts a string to all caps
  * `.toLowerCase()` - converts a string to all lowercase
  * `.replace('old', 'new')` - replaces the first appearance of a string with a new string

Note that most of these functions are called on an object, while functions like `parseInt()` and `parseFloat()` only take in arguments.

### Reference

[Values, variables, and literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Values,_variables,_and_literals)

[re-introduction to JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

[MDN JavaScript documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

