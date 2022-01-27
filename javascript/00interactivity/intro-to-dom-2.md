# DOM Review

Title: Intro to the DOM   
 Creator: Karolin Rafalski  
 Appendix Author: Thom Page   
 Topics: Intro to the DOM, Intro to 'Vanilla' JS  


## Lesson Objectives

* Define the DOM
* Explain what role the DOM plays in a web page
* Relate HTML elements as Parents, Children and Siblings
* Identify common DOM manpipulation patterns:
  * query for an element
  * edit an element
  * add an element
  * remove an element
* Use DOM commands to interact with a page

## Part 1

1. Code along to create a little website for Hawkins, Indiana
2. Navigate to  your `student_examples` folder for today
3. `mkdir dom_intro`
4. `cd dom_intro`
5. `touch app.js`
6. `touch index.html`
7. `code .`

**`app.js`:**

1. `console.log('stranger things are coming!')`

**`index.html`**

1. `! tab` - to insert html boiler plate
2. set title to `Hawkins` inside the head

**`index.html` =&gt; `body`:**

1.`<h1>` - with the text 'Welcome to Hawkins' 1.`<div>` with a class of `container`

**`index.html` =&gt; `body` =&gt; `div.container`:**

1. `<img>` with a `src` of `https://londontheinside.com/wp-content/uploads/2017/11/StrangerThings2.png` and an `alt` of `Welcome to Hawkins` 
2. `<h2>` with text `Featuring`
3. `<ul>`

```markup
<ul>
  <li>Hawkins National Laboratory</li>
  <li>Hawkins Police Station</li>
  <li>Bradly's Big Guy Supermarket</li>
  <li>Melvad's General Store</li>
  <li>The Palace Arcade</li>
</ul>
```

1. In the body, just before the closing tag add `src tab` to add a `scriptsrc`

   link the `app.js`

`<script src="app.js" charset="utf-8"></script>`

1. Load `index.html` in the browser
2. `command option j` to open Chrome Developer Console
3. Our html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hawkins</title>
</head>
<body>
    <h1>Welcome to Hawkins</h1>
    <div class="container">
        <img src="https://londontheinside.com/wp-content/uploads/2017/11/StrangerThings2.png" alt="Welcom to Hawkins">
        <h2>Featuring</h2>
        <ul>
            <li>Hawkins National Laboratory</li>
            <li>Hawkins Police Station</li>
            <li>Bradly's Big Guy Supermarket</li>
            <li>Melvad's General Store</li>
            <li>The Palace Arcade</li>
        </ul>
    </div>
    <script src="app.js"></script>
</body>
</html>
```

* Expected appearance:

![hawkins site](https://i.imgur.com/AO2eyzc.png)

* We can also draw our HTML as a tree, with the `document` as the parent, and then have relations of parent and children relationships and sibling relationships

![tree](https://i.imgur.com/mnx7TLM.png)

* The `head` and `body` are children of the `document`
* The `body` is the parent element to `h1` and the `div` with a class of `container`
* The `h1` element and the `container` element are siblings
* Additionally the `li` elements are also siblings or each other
* what relationship does the image have with the `h3`? What about the image and the `div` with the class of `container`?

Being able to relate the different elements in this way is often referred to as 'traversal' and there are JavaScript methods that will help you access the element you want. Oftentimes you'll want to target the child elements or the parent element, rather than the element itself. This will become more apparent as you start to build more complex things.

## DOM

The DOM stands for Document Object Model. When we send HTML to a browser, like we did with our mini Hawkins site, the browser renders the HTML \(displays it in a window\) and it also creates a giant object that represents the web page.

As web developers, we can interact with this object \(DOM\) and we can make changes to the DOM, the browser will then redraw the web page to reflect the changes we made to the DOM.

Open the console in Chrome Developer Tools:

`Option Command J`

![Chrome console](https://i.imgur.com/p3y5hjr.png)

All web pages start with the root of `document`.

As we start to type `document` in the Chrome console, we see it can be autocompleted because it exists

![document autocomplete in chrome console](https://i.imgur.com/xRBmZGk.png)

We can go one deeper into the body \(don't forget to press the up key to get your previous line\)

![body autocomplete in chrome console](https://i.imgur.com/9HCZEeF.png)

And deeper

We can see that the children of the body are an h1, element, a div with a a class of container:

![children of body in chrome console](https://i.imgur.com/HqTQq4X.png)

We can keep going deeper and deeper...

![all the way to the text Featuring](https://i.imgur.com/q8jWVc6.png)

This way of accessing elements in the document requires a LOT of typing and always mapping out your web page. And if you change anything one around on your page, the route will likely break \(great example of fragile code\). So if you moved the h2 element above the image it would be

`document.body.children[1].children[0].innerText`

Instead of hard-coding our access to different elements, the browser has some built in methods to find the element we are looking for. It's called `querying`

So we can query the `document` for the `h1` element and change the text inside \(referred to as a key-value property of `innerText`\) this element. When we change it in the DOM it will also update the browser view.

* `document.querySelector('h1').innerText = 'Welcome to the Upside Down';`

![update the DOM](https://i.imgur.com/cFnMRAm.png)

As we can see as we've updated the DOM in the console, it has also updated our view in the web page.

Let's refresh our page \(remember: `command r` also, sometimes you need a `hard` \(clears some cached things\) refresh you can do that with `command shift r`\) and see that we've switched back to Hawkins. Whatever changes we make in the Chrome console, aren't permanent.

We can also manipulate the DOM from a `js` file

Let's grab that code from above and put us back in the upside down:

```javascript
console.log('stranger things are coming!')
document.querySelector('h1').innerText = 'Welcome to the Upside Down'
```

Refresh the page.

### script tag placement

Oftentimes, `script` tags will be placed in the `head` of a document. Try moving your script tag to the `head`, then refresh the page.

![inner Text error](https://i.imgur.com/WkpCyO8.png)

This is because the document is being read from top to bottom and our JavaScript is running before our h1 has loaded.

There are a couple ways to solve it.

* The first solution is to move our link to our `app.js` back to the bottom of the body
* Alternatively, you can tell the browser to wait to run the javascript code until the dom has fully loaded by wrapping the DOM manipulation code in a `DOMContentLoaded` **event listener**:

```javascript
console.log('stranger things are coming!')

document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelector('h1').innerText = 'Welcome to the Upside Down'  
})
```

Now, when we refresh our page, we should see our updated `h1`.

## DOM Manipulation

* JavaScript was built to manipulate the DOM
* Early JavaScript was challenging to use for complex projects, and although all the basic functionality was built in, creating solutions could be verbose and clunky
* jQuery is a JavaScript library that was created to make manipulating the DOM easier. It built a lot of useful functions and made JavaScript for the DOM easier to write.
* JavaScript has been changing and a lot of better functionality has been built in. Some people would argue that now 'vanilla' JavaScript is a superior solution over jQuery. In this course, we will be using vanilla javascript, not jQuery \(for the most part\).

### Querying and storing the queried element

It is a common pattern to query for an element and then store it in a variable for reuse. querySelector and querySelectorAll are great methods for grabbing DOM elements, because they use CSS selector syntax. That means, if you know how to write a CSS rule for the element, you know how to grab it from the DOM using querySelector!

* Let's query for the image

`const image = document.querySelector('img')`

Instead of querying over and over again, we now have our image stored in a variable. Let's console.log it!

`console.log(image)`

![our image element, console logged](https://i.imgur.com/ckCMrWB.png)

### Changing CSS with JavaScript

Sometimes you want to add or remove a class to change the appearance. Sometimes you want to do it inline with JavaScript - for now let's do it inline:

We can now manipulate our image:

Let's make it disappear!

`image.style.display = 'none'`

Let's make it reappear!

`image.style.display = 'block'`

Let's make it black and white

`image.style.filter = 'grayscale(100%)'`

Let's set the width to 95%

`image.style.width = '95%'`

Finally, let's make it color again

`image.style.filter = ''`

There are tons of different things you can do. The important thing to note is how easy it is to reuse a queried element and manipulate it when you store it to a variable.

#### Creating an element

We can create a new element

Let's create a new image

```javascript
const eggos = document.createElement('img')
```

Where is it?

In Chrome console: ![element without a place in the DOM](https://i.imgur.com/t4K9hjO.png)

Although we created the element, we haven't appended it anywhere to the DOM.

Let's add those eggos to the `div` with a class `container`.

`document.querySelector('.container').appendChild(eggos)`

Yeah, wait! Where is our image? We can see the tag is appended after the `ul` in Chrome console:

![appended image with no src](https://i.imgur.com/QWvbwLS.png)

But it has no attributes. We have to give it a `src` attribute with an image

#### Set an attribute

Many elements have attributes, you can add, edit and remove them using JavaScript as well.

`eggos.setAttribute('src', 'https://i.ytimg.com/vi/TgSmPqMGk2g/maxresdefault.jpg')`

Oh! They are huge! Let's shrink them down a bit

`eggos.style.width = '100%'` - you could also target this element and style it in a css file

#### Remove an element

Getting rid of an element is easy!

`eggos.remove()`

#### Working with a Collection

What if we have more than one element of the same kind?

We have a few list items let's grab them!

`document.querySelector('li')`

Oh snap! We only got our first element!

![first list item](https://i.imgur.com/t3ZeEmE.png)

To get all of our elements, we have to use a different method

`document.querySelectorAll('li')`

Now we get a `NodeList`

![NodeList of li elements](https://i.imgur.com/qITIojz.png)

This list is like an array - So we can access the first li \("Hawkins Laboratory"\) and change its text to be "Demo Dog Hangout"

`document.querySelectorAll('li')[0].innerText = 'Demo Dog Hangout'`

![change first list item](https://i.imgur.com/ndSkQEo.png)

Hopefully all those drills of accessing objects and things within the objects is helping us understand how we can access the DOM

Let's try a different one `document.querySelectorAll('li')[4].style.color = 'hotpink'`

What did we change there?

Last one: Let's remove Melvad's

When we remove it, will The Palace Arcade lose it's new color?

`document.querySelectorAll('li')[3].remove()`

### Appendix

#### Common 'Vanilla' JavaScript DOM Commands

DOM commands fall into a few broad categories:

* Search / retrieval of elements on the page
* Creating new elements
* Editing the DOM
* Traversal \(related to search\) - navigating the DOM

We will only need a small handful of these commands for now. Here is a sample:

* **Search**
  * document.querySelector\(\)
  * document.getElementById\(\)
  * document.getElementsByClassName\(\)
  * document.getElementsByName\(\)
* **Creation**
  * document.createElement\(\)
  * node.style
* **DOM editing**
  * node.appendChild\(\)
  * node.removeChild\(\)
  * node.innerText
  * node.setAttribute\(\)
  * node.innerHTML
  * node.id
  * node.classList
* **Traversal**
  * node.childNodes
  * node.children
  * node.firstChild

You might be asking: what is a **node**?

A node is the generic name for any type of object in the DOM hierarchy. A node could be one of the built-in DOM elements such as document or document.body, it could be an HTML tag specified in the HTML such as `<input>` or `<p>` or it could be a text node that is created by the system to hold a block of text inside another element. So, in a nutshell, a node is any DOM object.

Information about nodes was gathered from [here](https://stackoverflow.com/questions/9979172/difference-between-node-object-and-element-object)
