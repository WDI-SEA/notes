#Intro to DOM and Events

## Objectives
* Select elements from the DOM using selectors
* Add events to elements in the DOM
* Manage scope and control logic on a page

##DOM Manipulation with JavaScript

**Review:** What is the DOM?

Go to Developer Console. Look at DOM in *Elements*, then look at the DOM in *Console*. The object 'document' represents the DOM in JavaScript. We can change the DOM, i.e. the page, by changing the **document object**.

Review [DOM on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

Now, inspect a few properties, for example:

```js
document.URL
document.head
document.links (what does it return?)
```

How to change the DOM? Select elements and manipulate them.

**Select by tag id:**

```js
var greeting_div = document.getElementById("greeting");
```

What's the greeting?

```js
greeting_div.innerHTML;
```

Change it:

```js
greeting_div.innerHTML = "Wow, something changed.";
```

Also, try `textContent` too! (you may also see this as `innerText`, but this is not supported by all browsers)

Change styling:

```js
greeting_div.style.backgroundColor = "yellow";
greeting_div.style.color = "red";
greeting_div.style.height = "100px";
```

Properties can be a getter and setter. What does this mean?

**Select by class**

```js
var content_div = document.getElementsByClassName("content");
```

Change it:
```js
content_div.innerHTML = "I can change , too";
```

**Select by tag name**
```js
var allListElements = document.getElementsByTagName("li")
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
