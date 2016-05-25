#Additional Topics

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
