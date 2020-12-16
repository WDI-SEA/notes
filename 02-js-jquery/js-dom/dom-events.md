# DOM EVENTS

## LESSON OBJECTIVES

_after this lesson, students will be able to:_

1. Describe what a browser event is
1. Create a click event
1. Use a named, referenced function as the click handler for the listener

## Describe what a browser event is

Every kind of interactivity in the browser is an event: clicks, mouseovers, key presses, scrolling, resizing, loading the page, and more.

When you interact with the browser it checks to see if there is a _listener_ for that interaction.

If there is a _listener_ present, the browser will try to run any _handlers_ for those interactions.

A _handler_ is just a function that runs a desired procedure.

## Create a click event

How can we set up a _click_ event?

We need:

1. An element to set it on
2. A _listener_ that listens for the event: on _which element_ should the event take place
3. A _handler_ that runs the procedure we want to have happen when the event is triggered

Make a button in the html:

```html
    <button id='btn'>Click me</button>
```

Grab the button in the JS (DOM element):

```javascript
    const btn = document.querySelector('#btn')
```

### Event listener

Set an event listener:

We use the `addEventListener` [docs](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener) method: 

```javascript
    btn.addEventListener('click', ()=>{
        // what do you want to happen when the button is clicked?
    })
```

The event listener takes a string as the first argument. There are just a few strings that it will recognize as valid events, and 'click' is one of them.

[List of events](https://developer.mozilla.org/en-US/docs/Web/Events)

### Event handler

Add a _function_ that runs what we want to have happen. This function is what _handles_ the event and is called an _event handler_:

```javascript
    btn.addEventListener('click', ()=>{
        console.log('button was clicked!')
    })
```

Notice that we have supplied a function as an argument. The jargon for using a function as an argument to another function is `callback`.

pseudo code for an event listener

```javascript
elem.addEventListener(STRING, CALLBACK);
```

### Add Text to the Page on Click

```javascript
    btn.addEventListener('click', ()=>{
        const confirmation = document.createElement('p')
        confirmation.innerText = 'The button hath been smashed.'
        document.querySelector('body').appendChild(confirmation)
    })

```

## Use a named, referenced function as the click handler for the listener

The _handler_ that we used for our click was _anonymous_. It was a function that had no name. We just told the listener to run an _anonymous_ function. We can give our function a name and thereby reuse that function with other event listeners.

### Named Function

We can abstract the anonymous function out and give it a name:

Separate function, not inside the listener:

```javascript
const addText = () => {
const showConfirmation = () => {
    const confirmation = document.createElement('p')
    confirmation.innerText = 'The button hath been smashed.'
    document.querySelector('body').appendChild(confirmation)
}
```

We can then reference it in the event Listener:

```javascript
document.addEventListener('DOMContentLoaded', ()=>{
    const btn = document.querySelector('#btn')
    btn.addEventListener('click', showConfirmation)
})
```

With a named function, we can use the same handler for more than one DOM element.

### Referenced Function

Note that we do not invoke the function with parentheses. We do not want to invoke the function right away, we merely want to _reference_ it to be invoked when the listener runs it.

* The function should be defined before it is used in the event listener
* When the function is invoked inside the event listener **leave out the parentheses**. We do not want to invoke the function right away! We merely want to reference that function in the listener.

Here the function is invoked and will run immediately:

```javascript
    btn.addEventListener('click', showConfirmation())
```

We don't want this! We only want the function to run when the user has clicked on the button.

Complete code:

```javascript
const showConfirmation = () => {
    const confirmation = document.createElement('p')
    confirmation.innerText = 'The button hath been smashed.'
    document.querySelector('body').appendChild(confirmation)
}

document.addEventListener('DOMContentLoaded', ()=>{
    const btn = document.querySelector('#btn')
    btn.addEventListener('click', showConfirmation)
})
```

Let's do something fancier, and toggle the background-color of the page using `.toggleClass()`

```javascript
const changeClass = () => {
    const bodyClasses = document.querySelector('body').classList
    if (bodyClasses.length>0) {
        bodyClasses.remove('black')
    } else {
        bodyClasses.add('black')
    }
}
```

CSS:

```css
.black {
  background-color: black;
}
```

## Removing Event Listeners

There are times where you want a DOM element to _stop_ listening for an event.

Psuedo-code: `elem.removeEventListener(EVENT, CALLBACK)`

Let's set up the `changeClass` function to remove the event listener from the button after it is clicked once (so the background is stuck as black after it is changed once).

```javascript
const changeClass = () => {
    const bodyClasses = document.querySelector('body').classList
    if (bodyClasses.length>0) {
        bodyClasses.remove('black')
    } else {
        bodyClasses.add('black')
    }
    document.querySelector('#btn').removeEventListener('click', changeClass)
}
```

## Activity

* Add a div to your html that has some height, width, and a border so you can see it

* Set an event listener on the div that listens for the [mouseover](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseover_event#:~:text=The%20mouseover%20event%20is%20fired,one%20of%20its%20child%20elements.) event and changes the background color of the div to yellow when there is a pointer on it.
