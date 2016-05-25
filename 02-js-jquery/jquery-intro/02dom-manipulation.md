# jQuery - DOM Manipulation

## Installation
jQuery is a client side library, which means we need to include it in our HTML. To do this, we have two options:

* Reference jQuery from a server on the internet. CDNs (content delivery network) like [CDNJS](https://cdnjs.com/) or [Google Hosted Libraries](https://developers.google.com/speed/libraries/)
* Download a copy of jQuery to host on your own server:

[CDNJS](http://www.cdnjs.com), [Google Hosted Libraries](https://developers.google.com/speed/libraries/), and the [jQuery site](http://www.jquery.com) will all allow you to download a copy of jQuery to include in your projects.

#### What's with the 'min.js' in the name of the jQuery file?

If you look carefully at the filenames of the jQuery versions you download, or just look at the URL in the "src" attribute for each script tag above, you'll notice something at the end of each file name --- namely, that they end in 'min.js'. This means the JavaScript code has been minified.

#### Minified? Did I read that right?

Yep. You did. Minification is the process of making a JavaScript file smaller by, among other things, removing all line breaks and whitespace, reducing the length of variable and function names, and stripping out all comments. Minification can significantly reduce the size of a JavaScript file, and in turn, significantly decrease the time it takes our browsers to load the file into memory.

Minified scripts can be difficult to read, so most servers that host jQuery and other libraries will also offer the original (non-minified) version of the code so developers can understand the code.

#### And one more thing: 1.x vs. 2.x jQuery

If you've visited code.jquery.com, you'll see that there are two major versions in development:
  * The 1.x branch is the most cross-browser-compatible version of the jQuery core
  * The 2.x branch, while offering some new features, is not compatible with older web browsers --- most notably, it's not compatible with Internet Explorer versions 8 and below


## DOM manipulation with jQuery

To select an element in the DOM, we use the global jQuery function:

```js
// This is the basic syntax for jQuery selections
$(' ')

// To select a particular element by tag, you do
$('h2') // selects all h2 elements

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

#### Selecting a DOM element and changing it's content

In this HTML:

```html
<div id="myDiv">Hello world!</div>
```

```js
// vanilla JavaScript, using the browser API
var divToManipulate = document.getElementById('myDiv');
divToManipulate.innerHTML = "Goodbye world!";
```

Now the code above isn't too hard to deal with, but even so, in jQuery, this is a one-liner.

```js
$('#myDiv').html("Goodbye world!");
```

If we wanted to **save our selection as a jQuery object**, the code would look like this instead:

- First we select the element we want and save it as a jQuery object

```js
var taco = $('#taco');
```

- Then we use our jQuery object to perform our task

```js
taco.html("Goodbye world!");
```

There are three things about the example above that make jQuery easier to use:
  1. jQuery is using the same syntax as CSS to select elements
  2. jQuery allows us to chain methods together to accomplish our goals (i.e., $().html(...) ), making code shorter and easier to understand
  3. jQuery deals with any cross-browser compatibility issues, which may not seem like a big deal in this example, but which quickly become difficult to deal with as things get more complex

#### Appending a DOM element to a web page

If we had the following HTML page...

```html
<html>
<body>

  <div id="container"></div>

</body>
</html>
```

If we want to add a new DIV that provides a nice greeting, our vanilla JavaScript would have to be:

```js
  var myDiv = document.getElementById('container');
  var newP = document.createElement('p');
  newP.innerHTML = "Hello complicated, multi-step world of adding an element to the DOM!";
  myDiv.appendChild(newP);
```

And in jQuery, it looks like this:

```js
  $('#container').append("<p>").append("Hello simple insertion using jQuery chaining");
```

In the jQuery code example above, we first select the DIV with `id="container"``, then we append a new paragraph element (automatically created using core jQuery selector function), and then we append the text we want to insert to the new paragraph element we just created. In effect, the new HTML looks like this after the jQuery is run:

```html
  <div id="container">
    <p>
      Hello simple insertion using jQuery chaining
    </p>
  </div>
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
