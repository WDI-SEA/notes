# Programmatic DOM

## Lesson objectives

_After this lesson students will be able to:_

1. Add to the DOM with a function
1. Execute code once the DOM has loaded
1. Edit the DOM with a function
1. Add to the DOM with a loop
1. Use data to populate the DOM

We can use JavaScript control flow patterns like **functions**, **loops**, and **conditionals** in our DOM manipulation patterns to create some interesting things.

## Set Up

* Make a new directory called `programmatic-dom-practice`
* Add three files, `index.html`, `main.css` and `app.js`, to this directory
* Add the html boilerplate to `index.html` and link your css and javascript files to your html
* Add a background color and a DOMContentLoaded event listener with a console log, then open your app up in the browser to check if the files are properly linked

## Add to the DOM with a function

Write a function that will add an `h2` with the text "Just getting started" to the body of the page.

```javascript
const addH2 = () => {
    let h2 = document.createElement('h2')
    document.getElementsByTagName('body')[0].append(h2)
}

document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
})
```

## Edit the DOM with a function

Write another function that will change the first existing `h2` in the DOM tree (on the page) to have the text "Getting warmed up"

```javascript
const addH2 = () => {
    let h2 = document.createElement('h2')
    document.getElementsByTagName('body')[0].append(h2)
}

const changeH2 = () => {
    document.getElementsByTagName('h2')[0].innerText = 'Getting warmed up!'
}

document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
    changeH2()
})
```

## Add to the DOM with a loop

Here is a nice quilt:

![](https://i.imgur.com/vBwqImN.png)

Let's build a digital quilt! It's not going to be too easy on the eyes. In fact, it's going to be a horrible quilt.

What we are aiming at is this:

![](https://i.imgur.com/QZjQHT3.png)

Eventually, we would like to invoke a function `generateQuilt()` that will build the quilt on the page. We would like to specify how many squares the quilt has: `generateQuilt(1000)` would build a quilt with 1000 randomly-colored squares.

First goal: add 1000 divs to the DOM

* Write a for loop that counts from 1 to 1000

```javascript

document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
    changeH2()
    for (let i=1; i<=1000; i++) {
        console.log(i)
    }
})
```

* Make a square on each iteration of the loop and append it to the body

```javascript
document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
    changeH2()
    for (let i=1; i<=1000; i++) {
        const square = document.createElement('div')
        document.querySelector('body').appendChild(square)
    }
})
```

* Add a class that gives it shape

```javascript
document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
    changeH2()
    for (let i=1; i<=1000; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        document.querySelector('body').appendChild(square)
    }
})
```

```css
.square {
  height: 50px;
  width: 50px;
  border: 1px solid grey;
  border-radius: 10px;
  display: inline-block;
}
```

This is a DRY way to make a grid of 1000 divs.

### Add to the DOM using a function that runs a loop

I would like a convenient way to generate more squares.

We can wrap this process in a function:

```javascript
const generateQuilt = () => {
    for (let i=1; i<=1000; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        document.querySelector('body').appendChild(square)
    }
}

document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
    changeH2()
    generateQuilt()
})
```

### Give the function an argument

* Provide the function with a parameter and argument, and run the loop that many times:

```javascript
const generateQuilt = (numOfSquares) => {
    for (let i=1; i<=numOfSquares; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        document.querySelector('body').appendChild(square)
    }
}

document.addEventListener('DOMContentLoaded', ()=>{
    addH2()
    changeH2()
    generateQuilt(1000)
})
```

### Color the squares

We can use rgb values for our colors

```css
.square {
	background-color: rgb(25, 241, 84);
}
```

`rgb` stands for **red**, **green**, and **blue**. Each number is between 0 and 255, and says how much red, how much, green, and how much blue to blend.

`rgb(0, 0, 0)` is **black**.

`rgb(255, 255, 255)` is **white**.

[rgb color values](https://www.w3schools.com/colors/colors_rgb.asp)

Let's use it in the loop to add background color to each square:

```javascript
const generateQuilt = (numOfSquares) => {
    for (let i=1; i<=numOfSquares; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        square.style.backgroundColor='rgb(25, 241, 84)'
        document.querySelector('body').appendChild(square)
    }
}
```

## Color each square with a random color

Let's make a function that will return a **string** with **random rgb values**.

We will generate random values for red, green, and blue, and concatenate them into a return string.

```javascript
const randColorRGB = () => {
	const red = Math.floor( Math.random() * 256 );
	const green = Math.floor( Math.random() * 256 );
	const blue = Math.floor( Math.random() * 256 );
	return "rgb(" + red + "," + green + "," + blue + ")";
}
```
Test it with a console log in the loop

```javascript
const generateQuilt = (numOfSquares) => {
    for (let i=1; i<=numOfSquares; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        square.style.backgroundColor='rgb(25, 241, 84)'
        document.querySelector('body').appendChild(square)
        console.log(randColorRGB())
    }
}
```
Since it is inside a loop, it will run each time the loop runs, giving us a random color each time.

Now we can use the return value of this function in our background color assignment:

```javascript
const generateQuilt = (numOfSquares) => {
    for (let i=1; i<=numOfSquares; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        square.style.backgroundColor=randColorRGB()
        document.querySelector('body').appendChild(square)
    }
}
```

### Add text to each square

The quilt is not quite ugly enough. Let's put some numbers in each square.

* Display the number in each square from 1 to numOfSquares with `innerText`

```javascript
const generateQuilt = (numOfSquares) => {
    for (let i=1; i<=numOfSquares; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        square.style.backgroundColor=randColorRGB()
        square.innerText = i
        document.querySelector('body').appendChild(square)
    }
}
```

### For fun, give each square an id, the same as its number

```javascript
const generateQuilt = (numOfSquares) => {
    for (let i=1; i<=numOfSquares; i++) {
        const square = document.createElement('div')
        square.classList.add('square')
        square.style.backgroundColor=randColorRGB()
        square.innerText = i
        square.setAttribute('id', i)
        document.querySelector('body').appendChild(square)
    }
}
```

---

*Adapted from [SEI-MAE](https://git.generalassemb.ly/Software-Engineering-Immersive-Remote/SEIR-MAE-INSTRUCTORS/blob/master/unit_1/w06d1/instructor_notes/1.%20Programmatic%20DOM.md) by Taylor Darneille*