# jQuery - DOM Manipulation

## Installation
jQuery is a client side library, which means we need to include it in our HTML. To do this, we include the CDN (content delivery network) in a script tag, which we can copy/paste. One source: [Google Hosted Libraries](https://developers.google.com/speed/libraries/) 

## DOM manipulation with jQuery

To select an element in the DOM, we use the global jQuery function:

```js
// This is the basic syntax for jQuery selections
$(' ')

// To select a particular element by tag, you do
$('div') // selects all div elements

// To select by ID, you use the same syntax as CSS selectors
$('#someID') // Would select the element with ID="someID"

// To select all elements of a particular class, use CSS syntax again
$('.someClass') // Selects all elements of the class "someClass"

// And you can use more complicated CSS selectors as well
$('p.anotherClass') // Selects all <p> tags that also have the class "anotherClass" (<p class="anotherClass">)
```

If you use variable assignment when doing a selection, a "jQuery" object is returned

```js
var paragraphs = $('p'); // Returns a jQuery object containing all <p> tags on your web page.
```

Here is a demonstration of all the different types of jQuery selectors: https://www.w3schools.com/Jquery/trysel.asp

#### Selecting a DOM element and changing it's content

In this HTML:

```html
<div id="myDiv">Hello world!</div>
```
We can select and change html elements like so:

```js
// vanilla JavaScript
document.getElementById('myDiv').innerHTML = "Goodbye world!";

//jQuery
var myDiv = $('#myDiv')
myDiv.html("Goodbye world!");
```

#### Appending a DOM element to a web page

If we want to add a new DIV that provides an opinion, our vanilla JavaScript would have to be:

```js
var newDiv = document.createElement("div");
newDiv.innerHTML = "Indigo should not be included in ROYGBIV";
document.querySelector("body").appendChild(newDiv);
```

And in jQuery, it looks like this:

```js
$("body").append("<div>").append("Indigo should not be included in ROYGBIV");
```

#### Adding and Removing Elements Using jQuery

Sometimes in a dynamic web application, user-input is meant to trigger the addition or removal of content or functionality. Using jQuery, we can easily create new DOM elements and insert them into the DOM, or remove existing elements (and any content they contain) from the DOM.

So, let's imagine we have a web page with the following content on it:

```html
<body>
  <div id="outerContainer">
    <div class="innerItem innerItemHeader">Enjoy some hipster ipsum:</div>
    <div class="innerItem">
      Aesthetic migas paleo McSweeney's, pork belly Kickstarter Echo Park sriracha keytar disrupt viral drinking vinegar fanny pack typewriter.
    </div>
  </div>
</body>
```

Let's say we want to add some more hipster ipsum to the page. Something like:

```html
<div class="innerItem">
  Farm-to-table Godard roof party bespoke, fashion axe mustache vinyl.
</div>
```

To add this DIV, and our hipster ipsum content using jQuery, we'd do the following:

Define a new DIV and assign jQuery object to $newDiv

```js
var hipsterIsum = $('<div>');

// Add hipster ipsum content
hipsterIsum.html("Farm-to-table Godard roof party bespoke, fashion axe mustache vinyl.");

// Set it's class to innerItem
hipsterIsum.addClass("innerItem");

// Append our new element
$('#outerContainer').append(hipsterIsum);
```
