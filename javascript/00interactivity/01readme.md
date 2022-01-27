# DOM and Events

## Objectives

* Define what DOM stands for and what it refers to
* Select elements from the DOM using selectors
* Add events to elements in the DOM

## What is the DOM?

When the browser loads a webpage, it takes in all the information about what needs to be displayed on the page, and creates a bunch of Javascript objects that represent the elements on the page. These objects mirror the html hierarchy, where the highest order parent is the _document_ object.

![DOM](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSew-BsBdRn9RadAFC2626myd4j66yaFIWzSd6nkdvN-rbg14NX)

**Document Object Model**: A model of all the html elements on a web page - usually represented by a tree of nodes - that is created by the browser when a web page is loaded.

[DOM on MDN](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)

### Exercise

Visit [these website](https://taylordarneille.github.io/finished-intro-demo/) and open up the dev tools. Look at the Elements tab. Try expanding the collapsed elements to explore the structure of the document more. Now go to the Console tab and run `document` to see the document object. Notice that this is the same hierarchy from the Elements tab. _**The Elements tab of the console shows us a vertical representation of the DOM**_

Now draw out a diagram \(tree of nodes\) that represents the DOM that is loaded by this webpage.

## DOM manipulation

### What is DOM manipulation?

Using Javascript we can read and/or change the DOM, i.e. make the webpage do something interesting.

**Examples:**

* Change or Remove HTML elements
* Create and Add HTML elements
* Change the CSS styles of HTML elements
* Read & Change attributes of HTML elements \(href, src, alt, etc\)
* Attach event listeners to HTML elements \(click, keypress, submit, etc.\)

### Why would we want to manipulate the DOM?

Without DOM manipulation, web pages would just be static visuals with no changes and no interaction with the user.

**Example:**

* Clicking on buttons would do nothing
* You could never type into an input field
* You could never zoom into an image or stop/start a video

### How do we manipulate the dom?:

The _document_ object represents the DOM.

#### Selecting DOM Elements by HTML

* document.getElementById
* document.getElementsByClassName
* document.getElementsByTagName

_**html**_

```markup
<div id="hello" class="square">
  Hello, world!
</div>

<div id="gb" class="square">
  Goodbye, world!
</div>
```

_**css**_

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

_**js**_

```javascript
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

_**js**_

```javascript
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

_**changing styles**_

```javascript
myDiv.style.backgroundColor= 'chartreuse';
myDiv2.style.height="300px";
```

#### Changing Content

_**single DOM element changes**_

```javascript
myDiv.innerText = "I love WDI"
myDiv2.innerHTML = "<h2>I love GA</h2>"
```

#### Manipulating Multiple DOM Elements

What if I want to do something to both divs at once?

```javascript
// this wont work!
theSquares.style.border = "2px dashed black"

// but this will
for(var i = 0; i<theSquares.length; i++) {
  theSquares[i].style.border ="dashed 2px black"
}
```

 **Be Careful!**  Multi-element selectors like `querySelectorAll`, `getElementsByTagName`, and `getElementsByClassName` don't actually return an array; they return something called an _HTML collection_. This means that many array methods \(iterators, in particular, which we'll learn about later\) wont work. If you run into this problem, you can use the [`Array.from`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/from) method to convert it to an array.

**Accessing and changing element attributes**

What if I want to change an attribute, like the src on this img?

**html**

```markup
<img src="http://www.placekitten.com/200/200">
```

There are 2 ways to get and set attributes of a DOM element. You can access the properties directly or use use get/setAttribute methods. It's important that you know both exist, but generally accessing the properties directly is more consistent across browsers.

```javascript
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

```javascript
console.log(document.querySelector('div').className);
```

This works fine, but since elements can have multiple classes \(separated by spaces\) this often leads to needing to do some string parsing, so intead, we often use the `classList` attribute, which gives us "a DOM token list".

```javascript
console.log(document.querySelector('div').classList);
```

And just like the HTML collection, we can access the values in the classList like an array.

```javascript
var helloDiv = document.querySelector('div');
console.log(helloDiv.classList[0]);
```

You can add to the classList:

```javascript
helloDiv.classList.add('yellow');
console.log(helloDiv.classList);
```

You can also check if an item has a class \(returns true or false\)

```javascript
console.log(helloDiv.classList.contains('square'))
```

You can remove a class from the classList:

```javascript
helloDiv.classList.remove('yellow');
console.log(helloDiv.classList.contains('yellow'))
```

**DOM Events**

DOM events are the bedrock of interactivity on web pages. They enable us as developers to implement _event-driven programming_. This programming paradigm is such that much of our code, written as _event listeners_, runs in response to events being triggered during run-time.

Lots of events are generated within the browser, for example, when:

* a user moves or clicks the mouse
* a user presses a key
* when a form is submitted
* when the page has finished loading or has been resized
* etc.

Take a gander [here](https://developer.mozilla.org/en-US/docs/Web/Events) at the type and sheer number of events.

#### Event Listeners

An _event listener_ is a function, more specifically, a _callback_ function, that is called when an event fires. You may also hear them referred to as _event handlers_ \(depending upon how they are "registered" with the browser\).

There are three different approaches for attaching event listeners to elements:

1. In the HTML \(inline\) - `<button id="reset-btn" onclick="reset()">` - this isn't great because it embeds JavaScript code into our HTML, violating our separation of concerns.
2. Assigning to DOM elements' properties - `resetBtn.onclick = reset;` - this is a better choice but it is limited to adding single event listeners. 
3. Calling `addEventListener` on a DOM element - this is the preferred way to do it since it is functional and supports adding multiple listeners at a time.

#### Event Listener Syntax

_**addEventListener\(\[event type\],\[function that you want to run when the event fires\]\)**_

```javascript
helloDiv.addEventListener("click", function(event) {
    console.log("HOME ICON CLICKED");
});
```

#### The Callback and the Event Object

The first parameter to `addEventListener` is the name of the event that we are listening for \(e.g. click, change, keydown, etc.\). The second parameter is the **callback function** that we pass in to tell the browser what to do when this event occurs. This callback is allowed to use a very special parameter: the event object \(shown above as the parameter `event` but is frequently abbreviated to `evt` or `e`\).

This event object is passed into our event listener callback by the JavaScript engine in the browser. It contains may useful details about the event. Of special note are:

* `event.target` - this contains a reference to the actual DOM element that generated the event. In the case of a 'click' event, `event.target` would be the element that was clicked on.
* Several _...X_ and _...Y_ properties that tell where the click occurred.
* `event.preventDefault()` - a function to immediately disable the default action of this event for the given element. Useful for preventing unwanted form submissions or link navigation.
* `event.stopPropagation()` - a function for disabling the "bubbling" of this event up the DOM. More on this below...

_Note:_ JavaScript's `this` keyword within the listener function will also be set to the DOM element that `addEventListener` was called on, so you can use it instead of `event.target` if you like.

#### Event Bubbling

When an event occurs on an element, that event, whether it is listened to on that element or not, _bubbles_ up through the DOM, all the way up to the `document` object.

![](https://i.imgur.com/B7f5PAZ.png)

All event listeners registered for the same event, such as `click`, will be invoked along the path to the `document` element - unless one of those listeners calls the _event object_'s `stopPropagation()` method.

This passing of the event up the DOM tree allows for a very nice feature called Event Delegation.

#### Event Delegation

Imagine an unordered list with many list items inside it. Each list item in our app needs to have a click event that allows it to perform some unique action. We could probably add an event listener to each list item and if there weren't too many, it woudn't be too bad. But imagine that this unordered list can grow and add hundreds of additional list items programmatically while the app is running. We can't add them to each element manually. Instead, because of the bubbling of events, we can delegate the parent of the list items to handle the event.

Event delegation allows us to register a **single** event listener that can respond to events triggered by any of its **descendants**. Much more efficient!

All we would need to do is view the `event.target` property of the event object to see what element was referenced there. This would be the child element that generated the event.

#### Removing Event Listeners

It's possible to remove an added event listener, however, only if a named function was used as the callback:

```javascript
btn.removeEventListener('click', handleClick);
```

This would remove the 'click' event listener \(`handleClick`\) that was registered on the `btn` element like this:

```javascript
btn.addEventListener('click', handleClick);
```

#### Exercise:

Research a different event listener \(not `click`\) and explain what it does to your partner.

#### DOMContentLoaded Event

All of the selectors we've been using rely on the use of DOM elements. However, if the JavaScript loads before all the DOM elements load, the selectors won't recognize that some of them exist! To avoid this problem, there's an event called `DOMContentLoaded` that we can encapsulate our code inside. Then, we can guarantee that the DOM elements exist before manipulating them.

```javascript
document.addEventListener('DOMContentLoaded', function() {
  //code and events go here
});
```

### References

* [Event Developer Guide on MDN](https://developer.mozilla.org/en-US/docs/Web/Guide/Events)
