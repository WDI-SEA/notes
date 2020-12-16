# COLOR PALETTE PICKER

## Using event listeners in a loop

We are going to start building a color palette picker.

## Lesson Objectives

1. Generate 150 divs (squares) each with their own random color.
1. Create a click handler on each square that will add a square with the same color as the clicked square to the right column.

## Generate 150 divs (squares) each with their own random color.

Create DOM elements:

```html
<button id="generate">GENERATE</button>
<div id="container">
	<div id="color-palette"></div>
	<div id="my-palette"></div>
</div>
```

```css

div {
    border: 1px solid white;
}

#container {
    width: 608px;
}

#color-palette, #my-palette {
    display: inline-block;
    width: 300px; height: 500px;
    overflow: hidden;
}

.square {
    display: inline-block;
    width: 28px; height: 28px;
    cursor: pointer;
}
```

Grab them with javascript:

```javascript
const colorPalette = document.querySelector('#color-palette')
const myPalette = document.querySelector('#my-palette')
const generate = document.querySelector('#generate')
```

Write a function `makePalette` that will generate 150 squares with the class 'square' and append them to the `color-palette` div

```javascript
const makePalette = () => {
    const colorPalette = document.querySelector('#color-palette')

    for(let i=0; i<150; i++){
        const square = document.createElement('div')
        square.classList.add('square')
        colorPalette.appendChild(square)
    } 
}

document.addEventListener('DOMContentLoaded', ()=>{ 
    makePalette()
})
```

Make it so each square will have a random color

```javascript
const red = Math.floor(Math.random() * 255)
const green = Math.floor(Math.random() * 255)
const blue = Math.floor(Math.random() * 255)
const color = 'rgb('+red+','+green+','+blue+')'
square.style.backgroundColor = color
```

Should look like this:

![](https://i.imgur.com/AX50GkX.png)

Add an event listener to the `generate` button that will run the `makePalette` function

```javascript
generate.addEventListener('click', makePalette)  
```

Make it so the `makePalette` function will empty the previous palette of squares

```javascript
const makePalette = () => {
    const colorPalette = document.querySelector('#color-palette')
    while (colorPalette.firstChild) {
        colorPalette.removeChild(colorPalette.firstChild);
    }
    //...
}
```

Give each square an event listener whose `addColor` handler will (eventually) add the chosen square to the right column:

```javascript
const makePalette = () => {
	//...
    square.addEventListener('click', addcolor)
}
```

- Make the `addColor` handler.
- First, it should console.log the background color of the square that was clicked:

```javascript
const addColor = (event) => {
    console.log(event.target.style.backgroundColor)

}
```

* The `addColor` function should:

	* Make a new square
	* Give it a class of 'square'
	* Give it the clicked square's background color
	* Append to the 'my palette' right div

```javascript
const addcolor = (event) => {
    const color = event.target.style.backgroundColor
    const newSquare = document.createElement('div')
    newSquare.classList.add('square')
    newSquare.style.backgroundColor = color
    document.querySelector('#my-palette').appendChild(newSquare)
}
```
