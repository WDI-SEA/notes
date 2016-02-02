![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#JavaScript Control Flow

##Objectives

* Understand the benefits of altering control flow in JavaScript
* Use boolean statements to return true and false values
* Utilize if/else statements in order to skip blocks of code
* Utilize for, for...in, and while loops to loop through data structures and repeat code
* Identify truthy and falsey values

##Control Flow

A program can be read from top to bottom, but eventually we'll need ways to **skip** over code or **repeat** code. In other words, we need to alter the control flow of the program. Here are some of the statements we'll be using.

1. [if](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)
2. [switch](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)
3. [while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
4. [for](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
5. [for...in](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...in)

But before that, let's create the expressions needed for these statements.

##Boolean Expressions

### Equality Operator

The equality operator aka double equal (`==`) is used to compare two values.

```js
3 == 3
//true

4 == 3
//false
```

The equality operator allows type cohersion which means that if you compare two values of different types you might get unexpected results.

```js
3 == "3"
//true

0 == false
//true

1 == true
//true
```

### Identity Operator (recommended)

The identity operator aka triple quotes (`===`) works exactly like the equality operator (`==`) except it is a strict comparison operator. It does not convert types so it is more predictable and therfore the prefered method for comparision.

```js
3 === 3
//true

4 === 3
//false

3 === "3"
//false

0 === false
//false

1 === true
//false
```

### Additional Boolean Operators

There are also ways to check if a value is greater than, less than, or not equal to another value.

```js
4 > 5
//false

4 < 5
//true

4 >= 5
//false

5 <= 5
//true

4 != 5
//true

5 !== "5"
//true
```

### Logical Operators

Lastly, we can combine different boolean expressions by using logic operators.

* `&&` - and
* `||` - or
* `!` - not

```js
(4 > 5) && (5 == 5)
//false, the "and" operator requires both statements to be true

(4 > 5) || (5 == 5)
//true, the "or" operator requires at least one of the statements to be true

!(4 > 5) && (5 == 5)
//true, the "not" operator negates the first expression (!false ends up being true)
```

We'll be using these expressions throughout the course.

####Exercise

What are the results of these statements?

```js
//1
!(5 === "5") && (6 > 5) && (1 >= 0)

//2
(5 < 4) || !(3 == 3) && true
```


###If

The **if statement** executes some code if a specified condition is true.

```js
if (true) {
  console.log("this will be printed");
}

if (false) {
  console.log("this will not be printed");
}

var x = 4;
//var x = 5;
if (x === 5) {
  console.log("x equals 5");
}
```

**If / Else**

When we want code that executes when the **if statement** condition is false, we can use the **else** keyword as a shorthand.

```js
var isTasty;
var food = "vegetables";
//var food = "pizza";
if (food === "pizza") {
  isTasty = true;
} else {
  isTasty = false;
}
console.log("Is the food tasty?", isTasty);
```

**If / Else If / Else**

```js
var course = "wdi";
if (course === "uxdi") {
  console.log("Hello, User Experience Designer!");
} else if (course === "fewd") {
  console.log("Hello, Front-End Developer");
} else if (course === "wdi") {
  console.log("Hello, Immersed Student")
} else {
  console.log("Who are you?")
}
```

###Switch

Sometimes, numerous **if/else** statements make code hard to read. There's an alternative called a **switch statement**. It accepts a value and compares the value against various **cases**.

Each case block must end with **break;**, otherwise the block will fall through to the next block. If none of the cases match the value, you can also implement a **default** case.

```js
var grade = "B";
switch(grade) {
  case "A":
    console.log('You got an A! Great job!');
    break;
  case "B":
    console.log('You got an B! Good job!');
    break;
  default:
    console.log('Try again next time!');
    break;
}
```

###While

A **while loop** repeatedly executes a code block as long as a specified condition is true.

```js
var i = 0;
while (i < 5) {
  console.log("i is " + i);
   i++;
}

// Will print out:
// >i is 0
// >i is 1
// >i is 2
// >i is 3
// >i is 4
```

**The parts of a while loop**

```
while (CONDITION) {
  //CODE
}
```

###For

A **for loop** is a fancy **while loop**.

```js
for (var i = 0; i < 5; i++) {
  console.log("i is " + i);
}

// Will _also_ print out:
// >i is 0
// >i is 1
// >i is 2
// >i is 3
// >i is 4
```

**The parts of a for loop**

```
for (VARIABLE DECLARATION; CONDITION; UPDATE) {
  //CODE
}
```

In other words, you declare a variable and test to see if that variable passes a condition in order to run the code block. The update statement runs after the code block is executed.

Very commonly, you will use it to loop through an array.

```js
var foods = ["pizza", "tacos", "ice cream"];
for (var i = 0; i < foods.length; i++) {
  console.log("i like " + foods[i]);
}

// Will print out:
// >i like pizza
// >i like tacos
// >i like ice cream
```

###For...in

A **for...in** loop is similar to a **for loop**, but good for looping
through all the key-value pairs in an Object.

```js
var car = {
  wheels: 4,
  doors: 2,
  seats: 5
};
for (var thing in car) {
  console.log("my car has " + car[thing] + " " + thing);
}

// Will print out:
// > my car has 4 wheels
// > my car has 2 doors
// > my car has 5 seats
```

###Exercises

1. Implement [Fizz Buzz](http://en.wikipedia.org/wiki/Fizz_buzz). Loop
   from 1 to 100.  If the number is divible by both 3 and 5, print
   "fizzbuzz". Otherwise, if the number if divisible by 3, print
   "fizz", or, if the number is divisible by 5, print "buzz". If none
   of the above are true, print the number. This is a very common
   interview question!

2. Use a `for...in` loop to examine the `phoneBook` Object below and print
   out the names of all the people who share the phone number "333-333-3333".

```js
var phoneBook = {
  "Abe": "111-111-1111",
  "Bob": "222-222-2222",
  "Cam": "333-333-3333",
  "Dan": "444-444-4444",
  "Ern": "555-555-5555",
  "Fry": "111-111-1111",
  "Gil": "222-222-2222",
  "Hal": "333-333-3333",
  "Ike": "444-444-4444",
  "Jim": "555-555-5555",
  "Kip": "111-111-1111",
  "Liv": "222-222-2222",
  "Mia": "333-333-3333",
  "Nik": "444-444-4444",
  "Oli": "555-555-5555",
  "Pam": "111-111-1111",
  "Qiq": "222-222-2222",
  "Rob": "333-333-3333",
  "Stu": "444-444-4444",
  "Tad": "555-555-5555",
  "Uwe": "111-111-1111",
  "Val": "222-222-2222",
  "Wil": "333-333-3333",
  "Xiu": "444-444-4444",
  "Yam": "555-555-5555",
  "Zed": "111-111-1111"
};
```

###Truthy vs. Falsey

What happens if we put something other than a Boolean as the conditional
in an **if statement**?

[http://james.padolsey.com/javascript/truthy-falsey/](http://james.padolsey.com/javascript/truthy-falsey/)

```js
var person = null;
if (person) {
  console.log("this will not be printed");
} else {
  console.log("this will be printed");
}
```

```js
var num = 0;
if (num) {
  console.log("this will not be printed");
} else {
  console.log("this will be printed");
}
```

```js
var num = 5;
if (num) {
  console.log("this will be printed");
}
```

###Common Mistakes

1. Using the assignment operator(=) instead of the equality operator(===)
2. Infinite loops!
