# Callback Functions

* Define a callback function
* Demonstrate ability to pass a function as a parameter

Functions may seem very different than the other javascript items we've worked with before, but don't be fooled! Functions are still [_first-class_ values](http://wiki.c2.com/?FirstClass), which means you can
* store them in variables
* **pass them as arguments to other functions**
* create them within functions
* return them from functions

If this all seems very strange, you could think of a javascript function as a _javascript_ object that stores code to be run instead of key/value pairs. A **callback function** is just a regular function that we pass as an argument to another function!

Take a look at this example:

```js
function greeting() {
	console.log("Hello, World!");
}

function formalGreeting(informalGreeting) {
	informalGreeting();
	console.log("How are you?");
}

formalGreeting(greeting)
```

When we pass a function into another function as a paramenter, we are passing the _function definition_, so it can be called at a later time (hence the name _callback_). Notice the different outputs in the below example. First we print the function itself, then we _call_ the function and print the output.

```js
function returnRandom() {
	return (Math.random()*100).toFixed();
}

function yellRandom(randomNumGenerator) {
	console.log("GENERATOR DEFINITION: ", randomNumGenerator)
	console.log("YOUR RANDOM NUMBER IS: "+randomNumGenerator());
}

yellRandom(returnRandom)
```

## Examples: Timing Functions

Many built in javascript functions take callback functions. For example, `setInterval` and `setTimeout` both take a function and run it at a specific time.

## setTimeout & setInterval

`setTimeout` takes two arguments:
* the function to be run
* how long to wait (in milliseconds) before running that function

```js
function alarm() {
	console.log("Wake up!");
}

setTimeout(alarm, 10000)
```

`setInterval` also takes two arguments:
* the function to be run
* how often to run the function (in milliseconds)

```js
function annoy() {
  console.log('Are we there yet?');
}

setInterval(annoy, 1000);
```

You may want to have multiple instances of these timing events going, so you can differentiate between the instances by assigning the functions to variables.

```js
function alarm() {
	console.log("Wake up!");
}

var firstAlarm = setTimeout(alarm, 3000);
var secondAlarm = setTimeout(alarm, 6000);

```

```js
function annoy() {
	console.log('Are we there yet?');
}

function shutDown() {
	console.log('No!')
}

var kids = setInterval(annoy, 1000);
var parents = setInterval(shutDown, 3200);
```

You can disable an interval using `clearInterval`:

```js
function annoy() {
	console.log('Are we there yet?');
}
function hush() {
	clearInterval(kids);
}
var kids = setInterval(annoy, 1000);
setTimeout(hush, 10000)
```
And you can disable your `setTimeout` before the function fires using `clearTimeout`:

```js
function alarmRing() {
	console.log('RRRIIINNNGGGGG');
}

function turnOffSnooze() {
	console.log("turning snooze off now");
	clearTimeout(snoozeAlarm);
}

var snoozeAlarm = setTimeout(alarmRing, 5000);

var snoozeOff = setTimeout(turnOffSnooze, 3000)
```

### Exercises:

***1.*** Use `setInteral` and `setTimeout` to write a program that prints the following:

(This should mimic a countdown, so each line will print after a one second delay.)

```bash
10
9
8
7
6
5
4
3
2
1
Blast off!
``` 

***2.*** How could you mimic the `setInterval` functionality using `setTimeout`? Use `setTimeout` to recreate the `var kids = setInterval(annoy, 1000);` functionality.

