# Intro to DOM and Events

## Objectives
* Define what DOM stands for and what it refers to
* Select elements from the DOM using selectors
* Add events to elements in the DOM
* Manage scope and control logic on a page

## What is the DOM?

Document Object Model: A model of all the objects on a web page - usually represented by a tree of nodes -  that is created by the browser when a web page is loaded.

![DOM](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSew-BsBdRn9RadAFC2626myd4j66yaFIWzSd6nkdvN-rbg14NX)

[DOM on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

## DOM manipulation

**What**: Using Javascript we can read and/or change the DOM, i.e. make the webpage do something interesting.

Examples:
* Change or Remove HTML elements
* Create and Add HTML elements
* Change the CSS styles of HTML elements
* Read & Change attributes of HTML elements (href, src, alt, etc)
* Attach event listeners to HTML elements (click, keypress, submit, etc.)

**Why**: Without DOM manipulation, web pages would just be static visuals with no changes and no interaction with the user.

**How**: The *document* object represents the DOM.

**Select by tag id:**

```js
var navBar = document.getElementById("ac-globalnav");
```

Let's look at the styles?

```js
navBar.style;
```

Change the styling:

```js
navBar.style.backgroundColor = "blue";
navBar.style.height = "75px";
```

Let's look at the innerHTML:

```js
navBar.innerHTML
```

Let's change the innerHTML:

```js
navBar.innerHTML
```

**Select by class**

When we use classes to grab elements, we get an HTML collection, the contents of which we can access like an array.
```js
var unitLinks = document.getElementsByClassName("unit-link");
unitLinks
unitLinks[0].style.backgroundColor = "purple";
```

**Select by tag name**
Like above, getElementsByTagName also returns an HTML collection.

```js
var headerThrees = document.getElementsByTagName("h3");
```

What if I want to do something to each h3? Since this isn't technically an array (it's an HTML collection), array methods like forEach wont work.

```js
Array.isArray(headerThrees);
```

But we can MAKE it an array!!

```js
var h3array = Array.from(headerThrees);
Array.isArray(h3array);
h3array.forEach(function(h){h.style.backgroundColor="yellow";});
```

**Preferred: select using CSS selectors**

Get elements by tag name or class is very unspecific. You can go after specific CSS selectors, just like you would in stylesheets:

```js
document.querySelectorAll("li");
document.querySelectorAll("li.selected");
document.querySelectorAll("div#essentials > ul > li");
```

**Accessing and changing element attributes**

There are 2 ways to get and set attributes of a DOM element. You can access the properties directly or use use get/setAttribute methods. It's important that you know both exist, but generally accessing the properties directly is more consistent across browsers.

```js
//set using property
document.querySelector("img").src = './images/beer.jpeg';

//get using property
var imgSrc = document.querySelector("img").src;

//get using getAttribute method
var imgSrc = document.querySelector("img").getAttribute("src");

//set using setAttribute method
document.querySelector("img").setAttribute("src","./images/beer.jpeg")
```

##CSS Classes

Acessing, getting, setting CSS classes is slightly different than other properties.

##className

First you can directly access the class attribute by using the `className` property of a DOM element. This works fine, but since elements can have multiple classes (separated by spaces) this often leads to needing to do some string parsing.

##classList

To solve the problem of not wanting to do string parsing of the `className` property browsers support the `classList` attribute which gives us an array of classes.

Additionally, the classList attribute has some special methods attached to it.

* add - add a class
* remove - removes a class
* contains - checks if an item has a class

**Usage**

```js
//list classes
item.classList

//add a class
item.classList.add('my-new-class');

//remove a class
item.classList.remove('my-new-class');

//check if an item has a class (returns true or false)
item.classList.contains('my-new-class');
```

##Events

Now that we know how to select DOM elements, we can attach events to them:

- Common Events:
	- change
	- click
	- mouseover
	- mouseout
	- keydown
	- keyup

* [List of Event Types](https://developer.mozilla.org/en-US/docs/Web/Events)

#####addEventListener

We have different **events**, but now we need a way to attach these events to elements. The solution? Use the `addEventListener` function. This function is called on DOM elements and takes two parameters: an **event type** and a **function**. The event type refers to a "click", "mouseover", or other type of event. The function contains the code that runs when the event occurs.

Also this is the style you should use often.

```js
document.getElementById("myDiv").addEventListener("click", function() {
	//Your code here
}
```

Events can only be attached to specific elements. Therefore, when you return a collection such as the result of `document.querySelectorAll` you **CANNOT** simply do this:

```js
document.querySelectorAll(".li").addEventListener("click", function() {
	console.log("Click worked");
}
```

Instead you must loop through all of the elements and attach an event to each item individually.

```js
var listItems = document.querySelectorAll(".li");
for(var i = 0; i < listItems.length; i++){
    listItems[i].addEventListener("click", function() {
    	console.log("Click worked");
    }
}
```

### DOMContentLoaded

All of the selectors we've been using rely on the use of DOM elements. However, if the JavaScript loads before all the DOM elements load, the selectors won't recognize that some of them exist! To avoid this problem, there's an event called `DOMContentLoaded` that we can encapsulate our code inside. Then, we can guarantee that the DOM elements exist before manipulating them.

```js
document.addEventListener('DOMContentLoaded', function() {
  //code and events go here
});
```

### Compare and Contrast

Compare and contrast the following selectors. Why can't we use querySelector/querySelectorAll for everything?

* getElementById
* getElementsByClassName
* getElementsByTagName
* querySelector
* querySelectorAll
