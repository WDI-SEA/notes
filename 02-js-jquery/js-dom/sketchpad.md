# Sketchpad

## LESSON OBJECTIVES

_after this lesson, students will be able to:_

1. Generate DOM elements in a _for_ loop
1. Set a single click listener on each element generated inside the _for_ loop
1. Write a single click handler outside the loop
1. Use `currentTarget` to target an element within the handler

## Generate DOM elements in a _for_ loop

Let's say we want to have **ONE THOUSAND** square divs on our page. We _could_ write out or copy/paste 1000 divs, **or** we could use a _for_ loop and do it once. Keepin' it DRY.

We are going to make 1000 square divs for our sketchpad. Each div will have the same event handler.

The goal is to generate 1000 divs in a _for_ loop and append them to the body

* Write a loop that counts up to 1000
* Inside the loop, create a div
* Give the div a class of `square` (just for display purposes)
* Append the div to the `body`
* Check in the Elements tab in your console to see if you have 1000 divs with class 'square'

```javascript
document.addEventListener('DOMContentLoaded', ()=>{
    for (let i = 0; i < 1000; i++) {
		let div = document.createElement('div')
		div.className = 'square'
		document.querySelector('body').appendChild(div)
	}
})
```

### Change the Square Color on MouseOver

Now, we can add an eventListener to the div within the loop. For our sketchpad, we don't want a 'click'. Instead, we can use a 'mouseover'.

* set an event listener one time within the loop. The first argument for the listener should be `mouseover` instead of `click`. For the second argument, use a named handler function called `changeColor`
* Write the `changeColor` function above and outside the loop.
* The handler function will add a class `pink` that will make the _target_ element pink. To locate the target element, use `event.target`.

```javascript
const changeColor = (e) => {
    e.target.classList.add('pink')
} 

document.addEventListener('DOMContentLoaded', ()=>{
    for (let i = 0; i < 1000; i++) {
		let div = document.createElement('div')
        div.classList.add('square')
        div.addEventListener('mouseover', changeColor)
		document.querySelector('body').appendChild(div)
	}
})
```

## SKETCHPAD ACTIVITY

### Activity in groups (20 mins)

FIGURE IT OUT

* Using an input field, make it so that the user can decide how many divs there are!

* There will be an input box and a button. When the button is clicked, it will grab the user's input from the input box.

* The value from the input box can be used in the control panel of your for-loop

STEPS:

Add an input box and a button to the html:

```html
<input id="inputBox" type="text" placeholder="grid size"/>
<button id="inputButton">SUBMIT</button>
```

* Above your for loop (NOT inside the loop) Grab both the input box and button in your js
* Set an event listener on the button.
* When it is clicked, inside the handler capture the input with `inputBox.value`. `console.log(inputBox.value`

Where should the code that generates your divs reside? Inside the button's click handler? What is the sequence of events?

How can you change your for loop to generate the number of divs that you grabbed from the input box?

### SUPER FIGURE IT OUT

* Make it so that when the user mouses over a square, a _random_ color will appear, not just pink. There are many different ways to solve this problem. The important thing is that you try to tackle it rather than solve it.

### SUPER FIGURE IT OUT

* Make it so that the square divs are contained inside a container div of fixed height and width. Depending on how many divs the user decides to make, the divs should alter their _size_ to fit the container!

### [Reference example](https://taylordarneille.github.io/sketchpad/)

---

*Adapted from [SEI-MAE](https://git.generalassemb.ly/Software-Engineering-Immersive-Remote/SEIR-MAE-INSTRUCTORS/blob/master/unit_1/w07d2/instructor_notes/sketchpad.md)*
