# Callbacks & Timing Functions Lab

Title: Callbacks  
 Type: Lab   
 Duration: 45 mins   
 Creator: Matt Huntington  
 Adapted by:

* v1 Thom Page
* v2 Taylor Darneille

### Greetings!

1. Create a function that takes a parameter and logs it
2. Create a second function that logs 'hi'
3. Invoke the first function, passing in the second function as a parameter
4. You should see a function reference being logged
5. Alter the first function so that it invokes its parameter
6. If you did these steps correctly, you should get a log of 'hi'

### Foo Bar Baz

See if you can guess what this will log:

```javascript
const foo = (param, param2) => {
    param(param2);
}

const bar = (param) => {
    console.log(param);
}

foo(bar, 'hi');
```

Run the code and see what happens.

See if you can guess what this will log:

```javascript
const foo = (param, param2) => {
    param(param2, 'hello');
}

const bar = (param, param2) => {
    console.log(param2);
}

foo(bar, 'hi');
```

Run the code and see what happens.

Add this function

```javascript
const baz = (param) => {
    console.log(param.toUpperCase());
}
```

and now predict what you'll get when you run this:

```javascript
foo(baz, 'hello')
```

### Electric Mixer

![electric mixer](https://i.pinimg.com/originals/14/b5/75/14b575bb9e064631727c7c1b8a30f06f.jpg)

A callback is like an electric mixer attachment. A mixer attachment _does_ something. Each attachment does something different: slice, dice, spiralize, all sorts of fancy things depending on the attachment.

The electric mixer also _does_ something: it uses the mixer attachment.

1. Write a function `electricMixer` that takes one parameter named `attachment`. The `electricMixer` function should console log "This mixer is now: " plus the return value of the attachment.
2. Write a function called `whippingAttachment` that returns the string `whipping`. _"Add the whipping attachment to your electric mixer"_ by passing `whippingAttachment` as an argument to `electricMixer`.
3. Invoke `electricMixer` using an **anonymous function** as the argument. The return of the anonymous function should be a string that says: "spiralizing".
4. Write one more custom attachment for your electric mixer and try it out!

Solution Code \`\`\`js const electricMixer = \(attachment\) =&gt; { console.log\("This mixer is now: " + attachment\(\)\); } const whippingAttachment = \(\) =&gt; { return "whipping"; } electricMixer\(\(\) =&gt; { return "spiralizing"; }\); const slicerDicer = \(\) =&gt; { return "slicin' and dicin'"; } electricMixer\(slicerDicer\); \`\`\`

## setInterval and setTimeout

We can still provide multiple arguments to a function even if one of those arguments is a function.

Pseudocode for **setInterval** and **setTimeout**

```javascript
functionName(CALLBACK, MILLISECONDS)
```

```javascript
setTimeout(() => {
  console.log('hi');
}, 2000);
```

```javascript
setInterval(() => {
  console.log('hi');
}, 2000);
```

> Use SetInterval to display a number that increases by 1 each second \(it's a clock!\)

**Food for thought: Give a real world example of when you would use setTimeout or setInterval**

Follow the following steps:

1. Create a function called `wordReverse` that reverses a string.
2. Create a function called `toUpperCase` that capitalizes every letter in a string.
3. Write a function, called `repMaster`, that accepts two arguments, input and a function. Input should be able to be used with the function.  The function used as an argument must return a string.  `repMaster` should take the result of the string, passed as an argument to the argument function, and return this result with `' proves that I am the rep MASTER!'` concatenated to it.  

Expected Output:

```javascript
      repMaster("Never give your heart to a blockhead", wordReverse);
```

> "blockhead a to heart your give never proves that I am the rep MASTER!"

```javascript
      repMaster("I finished this practice", toUpperCase);
```

> "I FINISHED THIS PRACTICE proves that I am the rep MASTER!"

## Hungry for More?

Javascript is a great language but it can always be improved!

1. We need a `.count` method and we need you to write it! The method should take an array and count how many elements are the same in that array, returning that number. _hint: remember to make an array that has duplicate elements!!_
2. Write a `.unique` method that creates a new array out of all the unique values in an array.

