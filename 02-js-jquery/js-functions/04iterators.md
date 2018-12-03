# Iterators

Iterators are built-in Array functions. They iterate through  an array and use a callback to do something to, or with, the the values in that array.

_Couldn't we just use `for`-loops?_ Totall! But writing `for` loops is error prone and tiring, which is why Javascript provides these iterators to perform common operations for us.

* run some piece of logic on each item
* create a new array with each item being slightly transformed
* filter the array to contain only a subset of items
* combine all the items in some fashion

The iterators for these operations are, respectively:

* [forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)
* [map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)
* [filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter)
* [reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce)

### General Practice

1. Declare an array
2. Call an iterator on the array
3. Pass a function to the iterator
4. Get results


## forEach

### What

`forEach` is the basic replacement for your standard `for` loop. 

### How

Take the body from your `for` loop, wrap it in a function, and pass that as the callback argument to `forEach`. This iterator will take each array value and one-by-one pass these values into your callback function. 

### Examples:

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


## map

### What:

Use the values from an array to build a new array. In other words: Map the values from one array into another new array and return that new array.

### How:

Like `forEach`, map will one-by-one pass the values from the array into your callback function. You must return a value in your callback function, and this will be the value that appears in the new array.

### Examples:

**Create a new array where all the values from the old array are capitalized.**

```js
var names = ["tim thompson", "ilias iliad", "elie ellison", "markus mourning"];

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
// > ['TIM THOMPSON', 'ILIAS ILIAD', 'ELIE ELLISON', 'MARKUS MOURNING']
// > ['TIM THOMPSON', 'ILIAS ILIAD', 'ELIE ELLISON', 'MARKUS MOURNING']
```

**Use `map` to create an array of objects with a `firstName` property and a `lastName` property**
```js
var names = ["tim thompson", "ilias iliad", "elie ellison", "markus mourning"];

function splitName(fullName) {
  return {
    firstName: fullName.split(" ")[0], 
    lastName: fullName.split(" ")[1]
  }
}

var objNames = names.map(splitName);

console.log(objNames);

// Should output
// > [ { firstName: 'tim', lastName: 'thompson' },
  { firstName: 'ilias', lastName: 'iliad' },
  { firstName: 'elie', lastName: 'ellison' },
  { firstName: 'markus', lastName: 'mourning' } ]
```

**Challenge: Modify `splitName` to account for the possibility of a middle name that will store as a `middleName` property.**
```js
var names = ["tim toby thompson", "ilias iliad", "elie ellison", "markus mary mourning"];

function splitName(fullName) {
  var nameArr = fullName.split(" ")
  var nameObj = {firstName: nameArr[0]};
  if(nameArr.length===3) {
    nameObj.middleName = nameArr[1];
    nameObj.lastName = nameArr[2];
  } else {
    nameObj.lastName= nameArr[1];
  }
  return nameObj;
}

var objNames = names.map(splitName);

// Should output
// > [ { firstName: 'tim', middleName: 'toby', lastName: 'thompson' },
  { firstName: 'ilias', lastName: 'iliad' },
  { firstName: 'elie', lastName: 'ellison' },
  { firstName: 'markus', middleName: 'mary', lastName: 'mourning' } ]

```

**Use `map` to create a new array `strNums` that holds the same values as `intNums` but as strings instead of integers**
```js
var intNums = [0, 1, 2, 3, 4, 5]

var strNums = intNums.map(function(elem){
  return elem.toString();
  });

console.log(strNums);
```

[more on map](https://codeburst.io/learn-understand-javascripts-map-function-ffc059264783)

## filter

### What:

Returns a subset of the original array by iterating through the original array and filtering out values.

### How:

Your callback must return a boolean. `filter` will one-by-one pass the values from the array into your callback. If the callback returns `true`, that element is included in the returned new array, otherwise it is excluded.

### Examples:

**Use `filter` to get 2 new arrays - one that contains names of even length only and one that contains names of odd length only**

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

**Use `filter` to return an array of dogs.**

```js
var pets = [ {name: "fluffy", age: 2, type: "cat"}, {name: "fido", age: 1, type: "dog"}, {name: "nelly", age: 64, type: "parrot"}, {name: "benedict", age: 1, type: "sea cucumber"}, {name: "spot", age: 10, type: "dog"}, {name: "magic", age: 9, type: "cat"}]

var dogs = pets.filter(function(pet){
  if (pet.type === "dog") {
    return pet
  }
})

console.log(dogs);
```

## reduce

### What:

Iterates over an array and turns it into one, accumulated
value. In other words, you _reduce_ a collection of values into one value. _(In some other languages it is called `fold`.)_

### How:

Your callback must take _two_ arguments: (1) accumulated value/total (2) new/original array value. The value that your callback returns will be the new `total`.

By default, `total` will start out as the 0th element in the array and `new` will be the element at index 1. 

**Example**

```js
var nums = [1,2,3,4];
var add = function (total, new) {
  return total + new;
};

var sum = nums.reduce(add);
console.log(sum);

// Should output:
// > 10
// which is, 1 + 2 + 3 + 4
```

**Alternative Initial Value**

If you want to start with a different `total` than 0th element, you can pass a second argument into `filter`, and it will start by passing _this_ value in as `total`, and the 0th element as `new`.

```js
var nums = [1,2,3,4];
var add = function (total, new) {
  return total + new;
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