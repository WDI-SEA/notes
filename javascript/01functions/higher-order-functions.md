# Higher Order Functions

## Lesson Objectives

* Explain what is a higher order function
* Explain what is the purpose of a higher order function
* Write a higher order function with a callback

A function that takes another function as an argument is called a `higher order` function. The function that is being passed in is called a `callback`.

Why would we use higher order functions and callbacks?

* We want control of when a function gets executed \(a callback happens after the higher order function hase been called\) - this is how we can have some control of the order of function execution in an asynchronous language like JavaScript
* We want to stack functionality. For example, we may want something to happen after a certain amount of time and thus use a built in function that sets time for us. Have you learned about array iterators yet? How do they stack functionality?

Let's think about a higher-order function we've already used: `setTimeout`. This funciton splits functionality apart into

* waiting 5 seconds
* then triggering some other function

### Code Along

Let's create some employees to do some important task for their boss.

```javascript
const socky = () => {
  console.log('I will happily iron your socks!')
}

const foodie = () => {
  console.log('I will sort your M&Ms so that you never encounter a green one!')
}

const pr = () => {
  console.log('I will make sure everyone knows you are the best boss ever')
}
```

Let's create a function called `boss`. `boss`'s role will be to call employees to do her bidding.

```javascript
const boss = employee => {
  console.log('I am the boss and you will do as I say!')
  employee()
}
```

Let's get or boss to boss our employees around

```javascript
boss(socky)
boss(foodie)
boss(pr)
```

Our boss can even summon an anonymous function

```javascript
boss(()=> {
  console.log("I'll still hand grind your coffee beans even though you never remember my name")
})
```

What is the higher order function in the boss/employee example? What is the callback?

### Another Example

Let's say we are going to manipulate a lot of words - we are working on a new text editor with a lot of custom editing. We can write a function that will capitalize every word:

```javascript
const capitalize = word => {
  return word[0].toUpperCase() + word.substring(1)
}
```

We also want to be able to put an exclamation point on the end of each word

```javascript
const excitedWords = word => {
  return word + '!'
}
```

```javascript
const handleWords = (str, cb) => {
  const arr = str.split(' ')
  const newArr = []
  for (let word of arr) {
    newArr.push(cb(word))
  }
  return newArr.join(' ')
}

handleWords('hello how are you?', capitalize)

handleWords('I am fine, how are you?', excitedWords)

// BONUS - what is going on here?
handleWords(handleWords('omg hi how are you', capitalize), excitedWords)
```

_This lesson was adaped from_ [_SEI-MAE_](https://git.generalassemb.ly/Software-Engineering-Immersive-Remote/SEIR-MAE-INSTRUCTORS/blob/master/unit_1/w04d1/instructor_notes/1.%20Callbacks.md)

