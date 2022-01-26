# Arrays

Unfortunately, strings and numbers are not enough for most programming purposes. What is needed are collections of data that we can use efficiently, Arrays.

Arrays are great for:

* Storing data
* Enumerating data, i.e. using an index to find them.
* Quickly reordering data

```javascript
let friends = ['Moe', 'Larry', 'Curly']
// => ['Moe', 'Larry', 'Curly']
```

Items in an array are stored in sequential order, and indexed starting at `0` and ending at `length - 1`.

```javascript
// First friend
let firstFriend = friends[0]
// => 'Moe'

// Get the last friend
let lastFriend = friends[2]
// => 'Curly'
```

## Exercise

Grab the person next to you. One person, create a variable that equals a comma delimited string with at least four of your favorite foods.

```javascript
let favorites = "noodles,bread,cheese,filet mignon"
```

Have the second person turn that string into an array, then the first person should ask the second what their third favorite food is.

## Array Assignment Using Const

Arrays that have been created using `const` can be modified, but not overwritten:

```javascript
const fruits = ['orange', 'mango', 'banana', 'strawberry']
fruits.push('apple') // this is okay!
fruits[3] = 'blueberry' // so is this
fruits = [] // will throw an error!
```

## Iterating Over Arrays

Often we want to write code that interacts with everything in an array. Let's say we have a list of numbers representing sub-totals on a receipt.

For a moment, let's assume we have four items on our receipt. We could "hard-code" a program to manually add up all of the items:

```javascript
let subTotals = [2.99, 3.00, 2.75, 14.99]
let total = subTotals[0] + subTotals[1] + subTotals[2] + subTotals[3]
```

We say the above example is "hard-coded" because it's brittle. The code assumes there's exactly four items in the array. The code would cause an error if there were less than four items. The code would fail to add anything beyond the first four items in the list. Instead of hard-coding our program we can use a for loop to _iterate_ over the array and calculate a total no matter how many things are in the array!

```javascript
// Make a variable to keep track of the total. Start it at zero.
let total = 0

// Create a for loop that starts at i = 0, and increments i++
// as long as i is less than the length of the list.
for (let i = 0; i <= subTotals.length; i++) {
  // add the subtotal of each item to our total.
  total += subTotals[i]
}
```

Iterating over arrays is very common.

## Self Exercise

Use a loop to iterate over an array. Calculate the average value of all numbers in the array. Consider how your code would operate on empty arrays, arrays with one value, arrays with two values, and arrays of any length.

```javascript
let a1 = []
let a2 = [14]
let a3 = [29, 32]
let a4 = [16, 99, -40]
let a5 = [12, 28, 92, 23, 94, 23, 99, 99, 99, 92]
```

## Arrays as a Reference Type

In javascript are are two fundamental types: primitive and reference. Primitives are the fundamental datatypes, such as `Numbers` and `Strings`. When you assign a primitive to new variable, a copy is made:

```javascript
let num1 = 10
let num2 = num1
num2 += 10
console.log(num1, num2) // 10, 20
```

Okay, that makes sense that primitives work as expected, but reference types are a little different. Reference Types include `Arrays` and `Objects`, and when you assign a reference type to a new variable, the new variable only references the original, a copy is not made.

```javascript
let langauges = ['HTML', 'CSS' ]
let langaugesTwo = languages
langaguesTwo.push('JS')
console.log(langauges, languagesTwo) // oops! ['HTML', 'CSS', 'JS' ], ['HTML', 'CSS', 'JS' ]
```

#### Ah, jeez. 

Don't fret! There are numerous was to copy a reference type:

```javascript
let langauges = ['HTML', 'CSS' ]
// ... is the spread operator, 
// here we 'spead' the values of langauges into a new array
let langaugesTwo = [...languages]
// you can also make a new array and concatenate to it:
let langaugesThree = [].concat(langauges)
// or the old-school way this the Array constructor and the new keyword
// let langaugesThree = new Array().concat(langauges)
```

## Array Methods

Arrays come with special methods attached to themselves that allow you to perform common operations.

### Adding and Removing Single Items

* `.push('element')` - add an element to the end of an array
* `.pop()` - remove and return the last element in an array
* `.shift()` - remove an element off the front of the array
* `.unshift(3)` - add an element to the beginning of an array

  \#\#\# Reorder an array: \* \`.sort\(\)\` - sort the elements in an array \* \`.reverse\(\)\` - reverse the array

* `.concat([1, 2])` - concatenate two arrays together
* `.slice(1, 3)` - return a copy of a portion of an array
* `.splice()` - alter an array by adding or removing elements
  * [https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects/Array/splice](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/splice)
* `.join(' ')` - take an array and join the elements together as a string

## [Repl.it](https://repl.it/@tmdarneille/JSArrays#index.js) with the code from this lesson
