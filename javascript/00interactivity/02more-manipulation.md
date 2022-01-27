# DOM Manipulation

So far we've only seen examples of how to change properties of the DOM and do things like:

* change the `textContent` of an element
* swap an existing image tag with another
* attach click listeners
* add/remove CSS classes
* modify CSS

We haven't seen the true power of DOM manipulation. The power to create and destroy DOM elements!!

## Creating DOM Elements

We can add to the DOM! One big part of DOM manipulation is creating and adding new HTML elements to our page.

To create any new element we follow three basic steps:

1. **create** a new element and save it to a variable
2. **modify** any properties of the element
3. **attach** the element to an existing element on the page

Let's look at an example of how to create a new element in JavaScript and add it to a page.

### Adding A New Link to the Bottom of a Page

```javascript
const a = document.createElement("a");
a.href = "http://hackertyper.com/";
a.textContent = "Hack!";

document.body.appendChild(a);
```

First, we use `document.createElement` and pass a string representing the tag we want to create. In this case we pass `"a"` to say we want to make a new link anchor tag. Save the result of the function into a variable.

`document.createElement` returns a new anchor tag. The element saved in our variable has properties like any other anchor tag on the page, except they're all empty because it was just created. We must manually add `href` and `textContent` to set the link and display text.

Finally, we add the new anchor tag to the `<body>` with `document.body.appendChild`. This adds the anchor to the bottom of the page.

#### .appendChild\(\)

The `appendChild()` function exists for all HTML elements. It's easy to show how to add things to the end of the body of the page because body is a property on the global document variable.

In order to append a new element to any other element, simply obtain a reference to it first. Here's an example showing how to add a new list item to an unordered list of my favorite movies.

```markup
<ul id="my-favorite-movies">
  <li>Rushmore</li>
  <li>Star Trek VI: Undiscovered Country</li>
  <li>Anchorman</li>
</ul>
```

```javascript
// obtain a reference to where we'll add it
const list = document.getElementById("my-favorite-movies");

// CREATE
const newMovie = document.createElement("li");

// MODIFY
newMovie.textContent = "Pirates of Silicon Valley";

// ATTACH
list.appendChild(newMovie);
```

And there you have it!

#### .insertBefore\(\)

It's easy to add things to the end of the body, at the bottom of a div, or at the end of a list. We have to do slightly more work if we want to add a new element at the beginning or in the middle of an existing element.

Use the following syntax:

```javascript
const insertedNode = parentNode.insertBefore(newNode, referenceNode);
```

* `parentNode` refers to the container \(like body, or a div, or a list\)
* `newNode` refers to the element we're adding
* `referenceNode` referes to an element that already exists in the `parentNode`

We can obtain a reference to all of the elements attached to a `parentNode` by accessing the `children` property.

Here's what it looks like all together:

```javascript
const list = document.getElementById("my-favorite-movies");

const newMovie = document.createElement("li");
newMovie.innerText = "Dr. Strangelove";

// get a reference to the second element inside the list
const second = list.children[1];

console.log(second);

// use insertBefore to add newMovie just before the second element.
list.insertBefore(newMovie, second);
```

Of course, you can choose any of the children of an element as a `referenceNode` for `insertBefore`. The new element will simply be added in the spot just before whatever you choose.

## The Case Against `.innerHTML`

It's true that instead of doing any of those fancy DOM manipulation we could just use set `.innerHTML` equal to strings.

**1. Safer** Using `innerHTML` may be a security concern. Someone can sneak malicious content on your page. Using `.textContent` guarantees strings will only appear as text.

Imagine if someone posted this as their status on Facebook and Facebook rendered it with `.innerHTML`. If status appeared in your page you would be redirected to an evil website!

```markup
  <script>
  window.location = "http://evil.com";
  </script>
```

**2. Easier** Using `innerHTML` requires string manipulation when it's mixed with functions and parameters. These lines get long, and it's easy to confuse when to use necessary single-quotes or double-quotes to make attributes in HTML tags render correctly.

As elements become more complex innerHTML becomes hairier to use and you'll find that creating elements as described here offers more modularity and fine-grain control over how things are added to the page.

It totally works, but it can get nasty!

**3. Faster** A final reason to prefer manual DOM manipulation over `.innerHTML` is that it's much faster. The browser is optimized to make changes to the DOM via the methods described here.

The browser spends more time manually computing how to interpret string content added via `.innerHTML`.

## Destroying DOM Elements

It's way easier to remove elements than it is to add them. Use this syntax:

```javascript
// straight up remove an element without remorse.
parent.removeChild(child);

// you may, if desired, save a reference to the element that was removed.
const oldChild = parent.removeChild(child);
```

`.removeChild()` allows you to remove any element you have reference to. If you save a removed element to a variable then you have access to it and can add it to somewhere else on the page.

### Exercise: Moving Elements

Practice saving the return value of `.removeChild()` and passing it to `.appendChild()` to move elements from one list to another.

Hook the functionality up to a button so you move one brunch item to the lunch list every time it is clicked. Prevent any errors from occuring if there's nothing left in the breakfast list.

```text
<button id="brunch">move to brunch</button>

<h1>Breakfast</h1>
<ul id="breakfast-foods">
  <li>Pancakes</li>
  <li>Waffles</li>
  <li>French Toast</li>
</ul>

<h1>Lunch</h1>
<ul id="lunch-foods">
  <li>Hamburger</li>
  <li>Sandwich</li>
</ul>
```
