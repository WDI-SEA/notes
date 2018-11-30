# Intro to DOM and Events

## Objectives
* Define what DOM stands for and what it refers to
* Select elements from the DOM using selectors
* Add events to elements in the DOM

## What is the DOM?

When the broswer loads a webpage, it takes in all the information about what needs to be displayed on the page, and creates a bunch of Javascript objects that represent the elements on the page. These objects mirror the html hierarchy, where the highest order parent is the _document_ object.

![DOM](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSew-BsBdRn9RadAFC2626myd4j66yaFIWzSd6nkdvN-rbg14NX)

**Document Object Model**: A model of all the html elements on a web page - usually represented by a tree of nodes -  that is created by the browser when a web page is loaded.

[DOM on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

### Exercise

Visit [these website](https://taylordarneille.github.io/finished-intro-demo/) and open up the dev tools. Look at the Elements tab. Try expanding the collapsed elements to explore the structure of the document more. Now go to the Console tab and run `document` to see the document object. Notice that this is the same hierarchy from the Elements tab. ***The Elements tab of the console shows us a vertical representation of the DOM***

Now draw out a diagram (tree of nodes) that represents the DOM that is loaded by this webpage.

## DOM manipulation

### What is DOM manipulation?

Using Javascript we can read and/or change the DOM, i.e. make the webpage do something interesting.

**Examples:**
* Change or Remove HTML elements
* Create and Add HTML elements
* Change the CSS styles of HTML elements
* Read & Change attributes of HTML elements (href, src, alt, etc)
* Attach event listeners to HTML elements (click, keypress, submit, etc.)

### Why would we want to manipulate the DOM?

Without DOM manipulation, web pages would just be static visuals with no changes and no interaction with the user.

**Example:**
* Clicking on buttons would do nothing
* You could never type into an input field
* You could never zoom into an image or stop/start a video

### How do we manipulate the dom?: 

The *document* object represents the DOM.

#### Selecting DOM Elements by HTML
* document.getElementById
* document.getElementsByClassName
* document.getElementsByTagName

***html***
```html
<div id="hello" class="square">
  Hello, world!
</div>

<div id="gb" class="square">
  Goodbye, world!
</div>
```

***css***
```css
#hello {
  background: yellow;
}

#gb {
  background: orange;
}

.square {
  height: 100px;
  width: 100px;
}
```

***js***
```js
var myDiv = document.getElementById('hello');

console.log(myDiv);

var theSquares = document.getElementsByClassName("square");

console.log(theSquares[0]);
console.log(theSquares[1]);

var theDivs = document.getElementsByTagName("div")

console.log(theDivs[0]);
console.log(theDivs[1]);

```

#### Selecting DOM Elements by CSS
* document.querySelector
* document.querySelectorAll

***js***
```js
var myDiv2 = document.querySelector('#gb');

console.log(myDiv2);

var mySquares2 = document.querySelectorAll('.square')
;

console.log(mySquares2[0])
console.log(mySquares2[1])

var myDivs2 = document.querySelectorAll('div');

console.log(myDivs2[0])
console.log(myDivs2[1])
```

#### Changing DOM Elements

***changing styles***
```js
myDiv.style.backgroundColor= 'chartreuse';
myDiv2.style.height="300px";
```

#### Changing Content

***single DOM element changes***
```js
myDiv.innerText = "I love WDI"
myDiv2.innerHTML = "<h2>I love GA</h2>"
```

#### Manipulating Multiple DOM Elements

What if I want to do something to both divs at once?

```js
// this wont work!
theSquares.style.border = "2px dashed black"

// but this will
for(var i = 0; i<theSquares.length; i++) {
  theSquares[i].style.border ="dashed 2px black"
}
```

** Be Careful! **
Multi-element selectors like `querySelectorAll`, `getElementsByTageName`, and `getElementsByClassName` don't actually return an array; they return something called an _HTML collection_. This means that many array methods (iterators, in particular, which we'll learn about later) wont work. If you run into this problem, you can use the [`Array.from`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from) method to convert it to an array.


**Accessing and changing element attributes**

What if I want to change an attribute, like the src on this img?

**html**
```html
<img src="http://www.placekitten.com/200/200">
```

There are 2 ways to get and set attributes of a DOM element. You can access the properties directly or use use get/setAttribute methods. It's important that you know both exist, but generally accessing the properties directly is more consistent across browsers.

```js
var photo = document.querySelector("img");

//get using property
console.log(photo.src);

//set using property
photo.src = "https://picsum.photos/200/200";

//get using getAttribute method
photo.getAttribute("src");

//set using setAttribute method
photo.setAttribute("src","https://placebear.com/200/200");
```

**Classes**

Acessing, getting, setting CSS classes is slightly different than other properties.

First you can directly access the class attribute by using the `className` property of a DOM element.

```js
console.log(document.querySelector('div').className);
```

This works fine, but since elements can have multiple classes (separated by spaces) this often leads to needing to do some string parsing, so intead, we often use the `classList` attribute, which gives us "a DOM token list".

```js
console.log(document.querySelector('div').classList);
```

And just like the HTML collection, we can access the values in the classList like an array.

```js
var helloDiv = document.querySelector('div');
console.log(helloDiv.classList[0]);
```
You can add to the classList:

```js
helloDiv.classList.add('yellow');
console.log(helloDiv.classList);
```

You can also check if an item has a class (returns true or false)

```js
console.log(helloDiv.classList.contains('square'))
```

You can remove a class from the classList:

```js
helloDiv.classList.remove('yellow');
console.log(helloDiv.classList.contains('yellow'))
```

**Events**

Now that we know how to select DOM elements, we can attach events to them:

- Common Events:
	- change
	- click
	- mouseover
	- mouseout
	- keydown
	- keyup

* [List of Event Types](https://developer.mozilla.org/en-US/docs/Web/Events)

***addEventListener([event type],[function that you want to run when the event fires])***

```js
helloDiv.addEventListener("click", function() {
	console.log("HOME ICON CLICKED");
});
```

#### Exercise:

Research a different event listener (not `click`) and apply it to the other div.

### DOMContentLoaded

All of the selectors we've been using rely on the use of DOM elements. However, if the JavaScript loads before all the DOM elements load, the selectors won't recognize that some of them exist! To avoid this problem, there's an event called `DOMContentLoaded` that we can encapsulate our code inside. Then, we can guarantee that the DOM elements exist before manipulating them.

```js
document.addEventListener('DOMContentLoaded', function() {
  //code and events go here
});
```
