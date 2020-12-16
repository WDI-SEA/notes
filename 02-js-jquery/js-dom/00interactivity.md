# Building an Interactive App In The Browser

## Lesson Objectives

### Thinking Programmatically

1. Pseudo code

### Interactivity

1. Why Javascript
1. Execute Javascript in a web page
1. View logged messages in the browser
1. Send a message to the user in the browser
1. Get user input in the browser

### Problem solving for a bigger program

1. Nested function invocations
1. Sequence of execution
1. Reset state

### More  on Functions

1. Basic Functions review
1. Loops and Functions
1. When/How to use a function in a program
1. Running a function from browser input

## Thinking Programmatically

### Pseudo Code

Pseudo code is the process of taking a larger solution and breaking it down into the programmable steps without actually writing any code.

1. Think about the larger solution as a whole, but as a series of steps that you would write out for a petulant child to follow
1. Write out the solution in plain English, breaking it down into as many tiny steps as possible.  Remember, this child doesn't want to do the task.  If there's any ambiguity, you're sunk
1. Create a flow chart
1. Try to separate each phrase/independent clause onto a different line
1. Identify the following:
    - Assertions
        - comments, probably
    - Conditionals
        - A question is asked.  This tells us a conditional is coming
        - Looks for words like "if, unless, otherwise"
        - Think of all the possible outcomes of the situation
            - Each outcome represents an `if`, `else if`, or `else` statement
    - Loops
        - Something is done multiple times
        - Look for words like "while, as long as, until"
        - Think of the child asking "am I done yet?"
            - Better to tell them "keep eating string beans until there are no more string beans" than to tell them to each individual string bean
    - Functions
        - We've oversimplified a step which could be broken out into multiple steps.
1. Identify data types
    - whenever you have a conditional, loop, or something you're keeping track of, identify its type
        - text (strings)
        - numbers (ints/floats)
        - true/false values (booleans)
        - collections of stuff (arrays)
1. (Optional) Try to convert each line into something that resembles code

```
Peeling an orange: First, do we have an orange?  If not, I'm going to take one out of the fridge.  We now have the orange.  Then I'm going to see if it has already been peeled.  If it is peeled, I'm going to eat it.  If it isn't peeled, I'm going to remove a chunk of the rind.  At this point, I'm going to see if it's peeled.  If it isn't I'm going to remove another chunk of the rind.  I'll keep doing this until the orange is peeled.

Do we have an orange? - conditional coming up
    We do not have the orange: - conditional (boolean test: does orange exist)
        Take out the orange - function
We now have the orange - comment
Is it peeled? - conditional coming up
    If it is peeled - conditional, situation 1 (number test: number of pieces of rind left === 0)
        You're done!  Eat it! - function
    If it is not peeled  - conditional, situation 2 (number test: number of pieces of rind left > 0)
        As long as it is not peeled - loop (number test: while(number of rind pieces > 0))
            Remove a chunk of rind - function
        The orange is now peeled - comment
        You're done!  Eat it! - function
```

### Activity (10 min) + review

Pseudo Code the process for creating a peanut butter and jelly sandwich

## Interactivity

### Why Javascript

Javascript is the language used to make web pages interactive

### Execute Javascript in a web page

1. Put your javascript in a `.js` file as normal
2. Reference the file inside a script tag inside the `<head>` tag of your html file

    ```javascript
    <head>
        <script src="js/yourfile.js"></script>
    </head>    
    ```
#### You do:
1. Create a new folder called `interactivity`
2. Add an `index.html` file, a `js` folder and a `script.js` file to this folder.
3. Connect the `script.js` to your `index.html` file and open the `index.html` file in your browser! 

### View logged messages in the browser

To see a message that you've created using `console.log()`:

1. Open up the dev tools in your browser
1. At the top of the pane that appears, choose "Console" ![](https://i.imgur.com/T51Jxtv.png)

Now any messages that you send using `console.log()` will appear here (next to the carrot)

### Send a message to the user in the browser

`alert()` is a global function that will open up a message box in the browser

```javascript
alert('oh hai!');
```

***Notes: You can use this for testing and playing with javascript, but it's usually not a good idea to use alerts in practice because it locks the whole browser and stops the flow of code execution. They can also be turned off by the browser user, and most users don't read them thoroughly before clicking a button to close them anyway.***

### Get user input in the browser

`prompt()` is like alert, but it opens up a window with a message AND a place to enter some text

```javascript
const yourAnswer = prompt('Some question', 'A default value goes here');
console.log(yourAnswer)
```

You can use the return value of `prompt` just like any other value

```javascript
const yourAnswer = prompt('Do you like apples?', 'Yes/No');

if(yourAnswer == 'Yes'){
  console.log('Excellent!');
} else if (yourAnswer == 'No'){
  console.log('What?!?!? How can you not like apples?!?!');
} else {
  console.log('Does not compute');
}
```

You can call a function based on some input from the browser prompt

```javascript
const greet = ()=>{
    alert('Hi!');
}
const sayBye = ()=>{
    alert('Bye!');
}
const answer = prompt('Are you arriving or leaving', 'Arriving or Leaving?');

if(answer === "Arriving"){
    greet();
} else if(answer === "Leaving") {
    sayBye();
}
```

You can keep getting input until a certain exists like so:

```javascript
let action = null

while(action !== "stop"){
    action = prompt("What do you want to do", "Your action");
}
```

## Problem solving for a bigger program

### Nested function invocations

You can have functions call other functions:

```javascript
const func1 = ()=>{
    console.log('hello');
}
const func2 = ()=>{
    console.log('oh hai');
    func1();
}
func2();
```

### Sequence of execution

Program execution happens in a branching structure.  List what the following logs.  See if you can diagram its execution:

```javascript
const func1 = ()=>{
    console.log(1);
    func2(); //why can I call this now, even though the definition is below?
    func3();
    console.log('Finished!');
}
const func2 = ()=>{
    console.log(2);
    func4();
    func6();
}
const func3 = ()=>{
    console.log(3);
    func5();
}
const func4 = ()=>{
    console.log(4);
}
const func5 = ()=>{
    console.log(5);
}
const func6 = ()=>{
    console.log(6);
}
func1();
```

### Reset state

- Sometimes you want to reset a situation to its original state
- This can be done with a start function that gets called at the beginning and restarting of situation.
    - It should reset all values and begin process again

```javascript
let apples;
let money;

const start = ()=>{
    apples = 0;
    money = 20;
    askForAction();
}
const showStatus = ()=>{
    alert("You have " + apples + " apples and $" + money);
}
const askForAction = ()=>{
    showStatus();
    const choice = prompt("What do you want to do?", "buy apple / eat apple / restart");
    if(choice === 'buy apple'){
        buyApple();
    } else if (choice === 'eat apple'){
        eatApple();
    } else if (choice === 'restart'){
        start();
    }
}
const buyApple = ()=>{
    apples++;
    money -= 1;
    askForAction();
}
const eatApple = ()=>{
    apples--;
    askForAction();
}

start();
```

## More on Functions

### Basic Functions review

Functions encapsulate (isolate) a set of commands pertaining to one set of functionality

1. Get a users name
1. Add an item to your cart
1. Shoot the lizard creature
1. etc

Try not to have a function that "does" multiple things

### Loops and Functions

#### When to use which?

- A loop is used whenever you do something repeatedly
- A function is used to simplify something more complex (e.g. Take the orange out of the fridge)

#### Functions in Loops

If executing a function multiple times, you don't need to define the function within the loop.  Instead put it at the top

**GOOD**

```javascript
const myFunc = ()=>{
    console.log('hi');
}

for(let i = 0; i < 10; i++){
    myFunc();
}
```

**BAD**

```javascript
for(let i = 0; i < 10; i++){
    const myFunc = ()=>{
        console.log('hi');
    }

    myFunc();
}
```

#### Loops in Functions

You can have loops within a function:

```javascript
const manyGreetings = ()=>{
    for(let i = 0; i < 10; i++){
        console.log('hi');
    }
}

manyGreetings();
```

### When/How to use a function in a program

- If you can try to have your functions defined at the top of the javascript file
- At the bare minimum, make sure you create your functions before calling them

Good:
```javascript
const func1 = ()=>{
    alert('hi');
}
const func2 = ()=>{
    alert('oh hai!!!!');
}

func1();
func2();
```

Meh:
```javascript
const func1 = ()=>{
    alert('hi');
}
func1();
//in the future might need to add func2() here before it's created

const func2 = ()=>{
    alert('oh hai!!!!');
}
func2();
```

Bad:
```javascript
const func1 = ()=>{
    alert('hi');
}
func1();
func2();
const func2 = ()=>{
    alert('oh hai!!!!');
}
```
