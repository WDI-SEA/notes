# Python Functions

## Objectives

After this lesson students will be able to

* Write a Python function using the `def` keyword
* Include parameters and return statements in a Python function
* Describe the use of the `global` keyword
* Use named arguments and default values for arguments to a function

## The Basics

A function in Python has the same purpose as a function in other languages: To write reusable code that can be run at any time after the function as been written. If you're hopping over to Python after using JavaScript, you'll be relieved to hear that there is only really one way in Python to write functions!

### `def` keyword

The `def` keyword is used much like the `function` keyword in JavaScript. It's used to declare or _define_ the function. A function that prints "Hello world" in Python looks like this:

```python
def greeting():
  print('Hello world')
```

Notice the parts of the function:

* `def`: Keyword that indicates this is a function definition
* `greeting`: The name of the function \(can be alphanumeric + underscores - see details below\)
* `()`: An empty set of parentheses indicates that no data is expected to be passed into this function. Any parameters we want to define would go here
* `:`: The colon here is important. It indicated the end of the function signature and the start of the function's code
* `print('Hello world')`: This is the actual code that the function contains. 

#### Aside: Naming a Python function

Naming conventions for functions in Python follow many of the same guidelines as naming variables. Your function in Python should:

* Start with a letter or underscore
* Contain alphanumeric characters and underscores
* Be lowercase \(use snake case: `like_this` instead of camel case or title case: `notLikeThis`\)
* Not be a reserved keyword in Python \(for example, no function can be named `def` or `if`\)
* Be concise. Python functions can be any length within reason, but try to keep the names short and to the point. Try to make the function name informative about what it does. 

You can look into [more details here](https://www.dummies.com/programming/python/how-to-name-functions-in-python/) for more info about naming conventions in Python. Also, need a keyword list? [Check this out](https://www.programiz.com/python-programming/keyword-list).

#### Aside: Stubbing a function

In JavaScript or another language, you may have done a process called "stubbing". This is a practice where you'd define functions, classes, routes, etc., with the intention of writing the actual code inside them later. It can be a useful practice when you want to plan out the overall structure of your program before getting into the line-by-line details of your code.

```javascript
function greeting() {
  // TODO: Write this code later
}
```

However, if you try to run this code in Python, you will get an error:

```python
def greeting():
  # TODO: This is a job for future me!
```

The error you get looks like this:

![Syntax Error](https://res.cloudinary.com/briezh/image/upload/c_scale,w_364/v1590000037/Screen_Shot_2020-05-20_at_11.39.42_AM_omq2ji.png)

In order to make a stub in Python what we want to use is the [pass keyword](https://res.cloudinary.com/briezh/image/upload/c_scale,w_364/v1590000037/Screen_Shot_2020-05-20_at_11.39.42_AM_omq2ji.png). As you might have expected given the name, the `pass` keyword does nothing. It's a placeholder, exactly what we want! Let's modify our Python stub above with the `pass` keyword to make the code functional again.

```python
def greeting():
  # TODO: This is a job for future me!
  pass # This let's the function have one line of code that just does nothing
```

## Parameters and Arguments

Parameters and arguments both describe data that goes into a function. Generally the subtle difference is that arguments are the bits of data you pass in, and parameters are the names that the function uses to understand the data that was passed in to it.

### A function with one parameter

Here's a function with one parameter - let's modify our greeting function from above to allow a person's name to be passed in.

```python
def greeting(name):
  print('Hello', name)

greeting('Erin')
greeting('Paolo')
greeting('Tanya')
```

We've called \(executed\) the function 3 times with different names. Expected Output:

```text
Hello Erin
Hello Paolo
Hello Tanya
```

In the above example, `name` is the parameter. It's the data as defined within the function. Arguments on the other hand are the data that is passed in when the function is called. In this case, 'Erin', 'Paolo', and 'Tanya' are all arguments being passed into the greeting function.

### Multiple Parameters

Creating a function with multiple parameters in Python is a lot like creating a function with only one parameter. It's important to note that unless otherwise specified \(see named arguments\) the arguments are understood to be in order. Consider the following code:

```python
def about_me(fave_food, fave_animal, fave_place):
  print('I love to eat', fave_food, 'while petting my', fave_animal, 'at', fave_place)

about_me('sushi', 'cat', 'the beach')
```

The expected output is `"I love to eat sushi while petting my cat at the beach"`. This is because "sushi", "cat", and "the beach" are provided in order corresponding to the parameters fave\_food, fave\_animal, and fave\_place. Therefore, the values are assigned like this:

* fave\_food = "sushi"
* fave\_animal = "cat"
* fave\_place = "the beach"

What happens if we mess up the order? For example, what is the output when the function is called like this:

```python
about_me("the beach", "sushi", "cat")
```

The output is a goofy non-sensical sentence because the parameters have been assigned like this:

* fave\_food = "the beach"
* fave\_animal = "sushi"
* fave\_place = "cat"

What if we want or need to provide them out of order? What we need is named arguments!

### Named Arguments

Consider the above example code. When we tried to call the function with the arguments out of order, we got a mess:

```python
about_me("the beach", "sushi", "cat")
```

However, Python allows us to specify the names of the parameters if we wish. Try running this code:

```python
about_me(fave_place="the beach", fave_food="sushi", fave_animal="cat")
```

### Default Values

Typically in Python, if we pass a wrong number of arguments in, we'll get an error - unlike JavaScript which just allows undefined arguments! However sometimes having a default value or an optional argument can be useful. For example, perhaps if a user does not provide a piece of information, we can make an assumption about what it is. If we have a function that stores user information and they don't provide whether their phone number is a work, home, or cell number, we can infer that it's a cell number.

```python
def accept_phone(number, phone_type):
  print('The phone number', number, 'is a', phone_type, 'phone')
```

We can pass arguments as normal:

```python
accept_phone('555-1234', 'home')
accept_phone('555-5678', 'cell')
accept_phone('555-8765', 'work')
```

But what if we'd like to pass arguments like this and just assume that the type of phone is a cell?

```python
accept_phone('555-1122')
```

As the function is currently written we'll get an error telling us we've passed the wrong number of arguments. We can modify the function to accept a default of "cell" for the second argument.

```python
def accept_phone(number, phone_type="cell"):
  print('The phone number', number, 'is a', phone_type, 'phone')
```

With this modification, test out the following functions. What do they print? Do they behave as expected?

```python
accept_phone('555-1234', 'home')
accept_phone('555-5678', 'cell')
accept_phone('555-8765', 'work')
accept_phone('555-1122')
```

## Global vs Local Variables

Python functions have their own scope, which can house separate variabled from the parent scope. If you want to use a global variable within your function, it will typically work as expected, however it is a good practice to indicate which values are global and in certain cases you will need to use it to disambiguate when there is a global and local variable with the same name.

### Activity

Run each of the following code snippets. What prints out? Was it what you expected? Why or why not?

**Scenario 1: Only a global variable**

```python
def greeting():
  print('Hello', name)

name = 'Marco'
greeting()
```

**Scenario 2: A global variable and a local variable**

```python
def greeting():
  name = 'Maria'
  print('Hello', name)

name = 'Marco'
greeting()
```

**Scenario 3: Using both variables**

```python
def greeting():
  print('Hello', name)
  name = 'Maria'
  print('Hello', name)

name = 'Marco'
greeting()
```

**Scenario 4: Is this allowed?**

```python
def greeting():
  global name
  print('Hello', name)
  name = 'Maria'
  print('Hello', name)

name = 'Marco'
greeting()
```

You can [read more on it here](https://www.geeksforgeeks.org/global-local-variables-python/).

