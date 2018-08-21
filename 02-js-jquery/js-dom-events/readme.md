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
document.querySelectorAll("h3");
document.querySelectorAll("h3").forEach(function(h3){h3.style.backgroundColor = "white"});
```

You can just grab the first element with that selector by dropping the "All".

```js
var learnMore = document.querySelector("#section-1-hero-position-1 > div > div.links.cta > a:nth-child(1)");
learnMore
```

While we're at it, let's mess with the text:

```js
learnMore.innerHTML
learnMore.textContent
learnMore.innerText
learnMore.innerHTML = "Learn NOTHINGS"
learnMore.textContent = "Learn Latin"
learnMore.innerText = "Learn ALL THE THINGS"
```

**Accessing and changing element attributes**

What if I want to change an attribute, like the href on this a tag?

There are 2 ways to get and set attributes of a DOM element. You can access the properties directly or use use get/setAttribute methods. It's important that you know both exist, but generally accessing the properties directly is more consistent across browsers.

```js
var homeIcon = document.querySelector("#ac-gn-firstfocus-small"); //this is the apple logo at the top

//get using property
homeIcon.href;

//set using property
homeIcon.href = "https://google.com";

//get using getAttribute method
homeIcon.getAttribute("href");

//set using setAttribute method
homeIcon.setAttribute("href","https://google.com");
```

**Classes**

Acessing, getting, setting CSS classes is slightly different than other properties.

First you can directly access the class attribute by using the `className` property of a DOM element.

```js
homeIcon.className
```

This works fine, but since elements can have multiple classes (separated by spaces) this often leads to needing to do some string parsing, so intead, we often use the `classList` attribute, which gives us "a DOM token list".

```js
homeIcon.classList
```

And just like the HTML collection, we can access the values in the classList like an array.

```js
homeIcon.classList
```
You can add to the classList:

```js
homeIcon.classList.add('my-new-class');
homeIcon.classList
```

You can also check if an item has a class (returns true or false)

```js
homeIcon.classList.contains('my-new-class');
```

You can remove a class from the classList:

```js
homeIcon.classList.remove('my-new-class');
homeIcon.classList.contains('my-new-class');
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
homeIcon.addEventListener("click", function() {
	console.log("HOME ICON CLICKED");
}
```

### DOMContentLoaded

All of the selectors we've been using rely on the use of DOM elements. However, if the JavaScript loads before all the DOM elements load, the selectors won't recognize that some of them exist! To avoid this problem, there's an event called `DOMContentLoaded` that we can encapsulate our code inside. Then, we can guarantee that the DOM elements exist before manipulating them.

```js
document.addEventListener('DOMContentLoaded', function() {
  //code and events go here
});
```
