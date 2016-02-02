![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Javascript Primitives

## Objectives

* understand the history of JavaScript and its purpose as a language
* conceptualize JavaScript variables and data structures
* utilize primitives and operators in order to solve problems using JavaScript

## History

**Then**
* developed by Brendan Eich (for Netscape, now Mozilla)
* 10 days
* went through a few different names before settling on JavaScript (Java was popular)
* taken to [ECMA](https://en.wikipedia.org/wiki/Ecma_International) for standardization

**Now**
* JavaScript is THE front-end language
* clunky, [things to complain about](http://wtfjs.com/), but it works and is web-driven!
* tons of open source libraries
* also used as a backend language, using Node.js
* working on [ECMAScript 6](https://github.com/lukehoban/es6features)

## Comments

Comments come in two forms

  * line comments

   ```js
   // descriptive stuff
   ```
  * multiline comments

  ```js
  /**
    These
    are
    comments on
    many lines
  */

  ```
## Numbers

Numbers are one of the *types* of **values** we want to be able to interact and play with in JS.

* Integers

  ```
   ..., -1,0, 2, 3, 4, 5, ...
  ```
* Floats (or Decimal numbers)

  ```
   2.718, 3.14, .5, .25, etc
  ```

In JS these are the same **type** of object, which it calls *Numbers*, so if you know floats and integers don not go looking for them.

This can infrequently cause problems!

```js
0.1 * 0.2 = 0.020000000000000004
```

[How to deal with floating point precision in JavaScript](http://stackoverflow.com/questions/1458633/how-to-deal-with-floating-point-number-precision-in-javascript)

### Exercise

```js
2 + 2 * 3
```

How would you get the 2+2 to execute before the * 3? In other words, how would you change this expression to get 12?

## Strings

Strings are collections of letters and symbols known as **Characters**, and we use them to deal with words and text in Javascript. Strings are just another type of **value** in Javascript.

```js
"John"
"Jane"
```

### Exercise

You can use operators on strings too! Try typing "John" + "Jane". How would you keep this from looking weird? This is called String concatenation

### Tangent: Type coercion

Try this: "1" + 1

Without removing the quotes, how would you get this to equal 2?

## Booleans

Strings are a type that can only have one of two values: true or false.

```js
true
false
```

### Exercise

! is the negation operator. !true = false, and !false = true.

Experiment and see what happens when you use ! with other datatypes.

== is an equality operator. See what happens when you enter 1 == 1. Try 1 == 2.

Try typing (1 == 1) + 1. What do you think will happen?

!= is an inequality operator. Try typing 1 != 1.

## Operator Review

- + (add)
- - (subtract)
- * (multiply)
- / (divide)
- % (modulus)


### Special Number Operators

Javascript can be a little cheap with the number of operations it allows you to do. For example, how is someone supposed to square a number or cube a number easily? Luckily there is a special `Math` object with some very useful methods.

* Taking a number to some `power`? Then just use `Math.pow`

```js
// 3^2 becomes
Math.pow(3,2)
=> 4
// 2^4 becomes
Math.pow(2,4)
=> 16
```
* Taking a square root

```js
// √(4) becomes
Math.sqrt(4)
=> 2
```
* Need a `random` number? Then use `Math.random`.

```js
// The following only returns a random decimal
Math.random()
=> .229375290430
/**
  The following will return a
  random number between 0 and 10
*/
Math.random()*10
```

* Since Numbers can be **Floats** or **Integers** we often want to get rid of remaining decimal places, which can be done using `Math.floor`.

```js
// Remove the decimal
Math.floor(3.14)
=> 3
Math.floor(3.9999)
=> 3
```

## Variables

Having made some expressions it becomes evident we want to store these values.

```js
var myNumber = 1;
// or also

var myString = "Greetings y'all!"
```

The main note to make here is that these variables should always have the `var` keyword and use `camelCase`

### Exercise

Take a number, X. How would you force a second number, Y to have the same sign, (positive or negative) as X?


## Objects Everywhere

In Javascript we just discussed two types of values we can use. We call these values objects, which for now just means that in addition to storing some data you also get to use some helpful methods when you are working with them.

In JavaScript, almost everything is an object (primitive types are the exception).

* If you want to turn a number into a string you can use a helpful method called `toString`.

```js
myNumber.toString()
=> "1"
```

### Common String / Number methods

* Numbers
  * `.toString`, `.toFixed`, `parseInt`, `parseFloat`
* Strings
  * `.split`, `.indexOf`, `.toUpperCase`, `.toLowerCase`, `.replace`

Calling on an object vs. passing in an argument.

### Arrays

Unfortunately, strings and numbers are not enough for most programming purposes.
What is needed are collections of data that we can use efficiently, Arrays.

Arrays are great for:

* Storing data
* Enumerating data, i.e. using an index to find them.
* Quickly reordering data

```
var friends = ['Moe', 'Larry', 'Curly'];
=> ['Moe', 'Larry', 'Curly']
```

Items in an array are stored in sequential order, and indexed starting at `0` and ending at `length - 1`.

```
// First friend
var firstFriend = friends[0];
 => 'Moe'
// Get the last friend
var lastFriend = friends[2]
=> 'Curly'
```

### Group Exercise

Grab the person next to you. One person, create a variable that equals a comma delimited string with at least four of your favorite foods.

```js
var favorites = "noodles,bread,cheese,filet mignon";
```
Have the second person turn that string into an array, then the first person should ask the second what their third favorite food is.

### Array Methods

`.pop`, `.push`, `.shift`, `.unshift`, `.concat`, `.slice`, `splice`, `.reverse`, `.sort`, `.join`


### Objects

Why use objects to store `key` and `value` pairs? They are like arrays except that data is not stored in any sorted order and keys do not have to numbered indexes.


#### creating


```js
var friend = {firstName: "Jane", lastName: "Doe"}
```

#### accessing


```js
friend.firstName
friend.lastName

friend['firstName']
friend['lastName']
```

### Exercise


1.) How would you represent the following using an object? Then update John's address to `1234 Park ln`.

````js
John, Doe, 36, 1234 Park st.
````
**(Hint: think in terms of firstname, lastname, age, address)**


2.) Using a combination of Objects and Array, how would you represent the following:


```js
  Moe, Doe, 31, 1234 Park st.
  Larry, Doe, 36, 1234 Spark st.
  Curly, Doe, 36, 1239 Park st.
  Jane, Doe, 32, 1239 Spark st.
  Emma, Doe, 34, 1235 Spark st.
  Elizabeth, Doe, 36, 1234 Park st.
  Elinor, Doe, 35, 1230 Park st.
  Mary, Doe, 31, 1231 Park st.
  Darcy, Doe, 32, 1224 Park st.
  Grey, Doe, 34, 1214 Park st.
  Lydia, Doe, 30, 1294 Park st.
  Harriet, Doe, 32, 1324 Park st.

```

### Reference

[Values, variables, and literals](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Values,_variables,_and_literals)

[re-introduction to JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript)

[MDN JavaScript documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
