# Functions with Python

## Objectives

After this lesson students will be able to

* Write a Python function using the `def` keyword
* Include parameters and return statements in a Python function
* Describe the use of the `global` keyword
* Use named parameters and default values for arguments to a function

## The Basics

A function in Python has the same purpose as a function in other languages: To write reusable code that can be run at any time after the function as been written. If you're hopping over to Python after using JavaScript, you'll be relieved to hear that there is only really one way in Python to write functions! 

### `def` keyword

The `def` keyword is used much like the `function` keyword in JavaScript. It's used to declare or *define* the function. A function that prints "Hello world" in Python looks like this:

```py
def greeting():
  print('Hello world')
```

Notice the parts of the function:

* `def`: Keyword that indicates this is a function definition
* `greeting`: The name of the function (can be alphanumeric + underscores - see details below)
* `()`: An empty set of parentheses indicates that no data is expected to be passed into this function. Any parameters we want to define would go here
* `:`: The colon here is important. It indicated the end of the function signature and the start of the function's code

#### Aside - how should you name a Python function?

Naming conventions for functions in Python follow many of the same guidelines as naming variables. Your function in Python should:

* Start with a letter or underscore
* Contain alphanumeric characters and underscores
* Be lowercase (use snake case: `like_this` instead of camel case or title case: `notLikeThis`)
* Not be a reserved keyword in Python (for example, no function can be named `def` or `if`)
* Be concise. Python functions can be any length within reason, but try to keep the names short and to the point. Try to make the function name informative about what it does. 

You can look into [more details here](https://www.dummies.com/programming/python/how-to-name-functions-in-python/) for more info about naming conventions in Python.
