#Intro to Test-Driven Development

##Objectives

* Identify the benefits and reasons for TDD.
* Write code based on preexisting `assert` tests.

###What is Test-Driven Development (or TDD)?

> Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: first the developer writes an (initially failing) automated test case that defines a desired improvement or new function, then produces the minimum amount of code to pass that test, and finally refactors the new code to acceptable standards. - [wiki](http://en.wikipedia.org/wiki/Test-driven_development)

In summary, test-driven development means writing tests, then writing code to pass the tests. Not only does this identify what you're coding, but it also results in more robust code.

### The Process
1. Create / receive feature specification
2. Create test
3. Run tests (new test should fail)
4. Write code to try to make the test pass
5. Run tests (if fail return to step 4)
6. Refactor code if needed

As an intro, we'll go over using the built-in `assert` module provided by Node. Later, we'll encounter more powerful testing frameworks.

### Assert

Assert is a Node module that has many functions. We'll be looking at the function `strictEqual` in this example. [See assert documentation](http://nodejs.org/api/assert.html) for more options.

To use the assert plugin we must first require it as follows.

```js
var assert = require('assert');
```

This loads `assert` and allows us to reference the methods attached to it. So to use the strictEqual method we simply call assert.strictEqual() which has 3 parameters.

* actual - the value you want to check
* expected - what we expect that value to be
* message - the message to output if it is not what we expect.

Here is an example to check a simple `sum` function.

```js
var sum = function(num1, num2) {};

assert.strictEqual(sum(1, 1) , 2, '1+1 should equal 2.');

// Output
// > AssertionError: 1+1 should equal 2.
```

Using the TDD process, we would start our code like this and execute it. Since we haven't implemented the `sum` function, we should get a message that the test failed.

Failing the test is a way to *test our test*. Now, we can work on implementing the `sum` function until the test passes.

```js
var sum = function(num1, num2) {
  return num1 + num2;
};

assert.strictEqual(sum(1, 1) , 2, '1+1 should equal 2.');

// Output
// > undefined
```

All the functions that belong to `assert` will return `undefined` if the test passes.

### Usage of Assert

In WDI, we'll start off writing assert tests for you. Later, you'll write your own tests.

Finally, when testing in Express, we'll work with more powerful testing frameworks.
