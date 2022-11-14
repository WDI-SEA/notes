# Conditionals

### `if`

The **if statement** executes some code if a specified condition is true.

```javascript
if (true) {
  console.log("this will be printed");
}

if (false) {
  console.log("this will not be printed");
}

let x = 4;
//let x = 5;
if (x === 5) {
  console.log("x equals 5");
}
```

### `if/else`

When we want code that executes when the **if statement** condition is false, we can use the **else** keyword as a shorthand.

```javascript
let isTasty;
let food = "vegetables";
//let food = "pizza";
if (food === "pizza") {
  isTasty = true;
} else {
  isTasty = false;
}
console.log("Is the food tasty?", isTasty);
```

### `if/else if/else`

```javascript
let course = "sei";
if (course === "uxdi") {
  console.log("Hello, User Experience Designer!");
} else if (course === "fewd") {
  console.log("Hello, Front-End Developer");
} else if (course === "sei") {
  console.log("Hello, Immersed Developer")
} else {
  console.log("Who are you?")
}
```

### `switch`

Sometimes, numerous **if/else** statements make code hard to read. There's an alternative called a **switch statement**. It accepts a value and compares the value against various **cases**.

Each case block must end with **break;**, otherwise the block will fall through to the next block. If none of the cases match the value, you can also implement a **default** case.

```javascript
let grade = "B";
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

### Exercise:

Rewrite the `if/else if/else` example above using a switch statement.

<!--

## Switch statements can evaluate inequalities too!

```javascript
let grade = "75";
switch(true) {
  case (90<=grade && grade<=100):
    console.log('You got an A! Great job!');
    break;
  case (80<=grade && grade<90):
    console.log('You got an B! Good job!');
    break;
  case (70<=grade && grade<80):
    console.log('You got an C! Fair job!');
    break;
  default:
    console.log('Try again next time!');
    break;
}
```

-->

## Truthy vs. Falsey

What happens if we put something other than a Boolean as the conditional in an if statement? Turns out, any value can be evaluated as true or false.

Most values are truthy. In fact, there are only 6 falsey values in Javascript - can you guess them all?

```javascript
let person = null;
if (person) {
  console.log("this will not be printed");
} else {
  console.log("this will be printed");
}
let num = 0;
if (num) {
  console.log("this will not be printed");
} else {
  console.log("this will be printed");
}
let num = 5;
if (num) {
  console.log("this will be printed");
}
```

More on this topic: [http://james.padolsey.com/javascript/truthy-falsey/](http://james.padolsey.com/javascript/truthy-falsey/)
