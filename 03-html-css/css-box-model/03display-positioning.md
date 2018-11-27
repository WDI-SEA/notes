# Taking Up Space using Display

Cool, right? Each HTML element gets its own box to live in.

As you saw, the outermost box of each element went all the way across the page. This is why, until now, your HTML elements have been sitting on top of one another: by default, they take up the full width of the page.

We can change all this with the first positioning property we'll learn, the `display` property and the four values we can use: inline, block, inline-block, and none.

--

**Block Elements**
* by default, takes up the full width of the page
* line break before and after
* box model applies
* examples:
  * Semantic block containers: `<div>`, `<main>`, `<section>`, `<header>`, `<footer>`, `<article>`, `<nav>`, `<aside>`, etc.
  * Text wrappers: `<p>`, `<h1>`,...,`<h6>`, `<blockquote>`, `<li>`
  * List containers: `<ul>`, `<ol>`

**Inline Elements**
* only takes up as much width as it needs
* no line break before or after it
* no box model
* examples:
  * `<img>`
  * `<a>`
  * `<span>`
  * `<em>`, `<strong>`, etc.

**Inline-Block Elements**
* only takes up as much width as it needs
* no line break before or after it
* box model!!!

* If you assign **none** as the value of the display, this will make the element and its content disappear from the page entirely!

Here are a few examples in CSS, written as classes:

```css
.inline {
  display: inline;
}

.block {
  display: block;
}

.inline-block {
  display: inline-block;
}
```

We would end up with something like this:

![display](https://i.imgur.com/zeD1f2m.png)


## Positioning

Another CSS property, "position", can take `relative` or `absolute` values, among others.

A page element with "relative positioning" gives you the control to "absolutely position" children elements inside of it. This might not be obvious to everyone - that's probably because this isn't intuitive, at all. Let's look at an example.


![css position relative](https://i.imgur.com/LRd7lBy.png)

The relative positioning on the parent is what matters here. This what would happen if we forgot that:

![](https://i.imgur.com/0vGcPFL.png)

In this small example, it doesn't seem to matter much, but it really is a significant change.

⇒ The "absolutely positioned" elements are positioning themselves in relation to the body element, instead of their direct parent. So if the browser window grows, that element in the bottom left is going to stick with the browser window, not hang back inside, like it was the case in the previous example.

#### Relative Positioning

Declaring `position:relative` allows you to position the element top, bottom, left, or right relative to where it would normally occur.

```css
.relative-item {
  position: relative;
  top: 0;
  left: 40px;
}
```

#### Static Positioning

HTML elements are positioned static by default. A "static positioned" element is always positioned according to the normal flow of the page and are not affected by the top, bottom, left, and right properties.

Again, the default positioning for all elements is static. This means that no positioning has been applied and the elements occurs where they normally would in the document.

```css
.static-item {
  position: static;
}
```

You rarely explicitly declare `position:static` like this because it is the default.

#### Fixed Positioning

An element with fixed position is positioned relative to the browser window.  It will not move even if the window is scrolled, so a fixed positioned element will stay right where it is.

```css
.fixed-item {
  position: fixed;
  top: 0;
  left: 0;
}
```

#### Absolute Positioning

Specifying `position: absolute` _removes the element from the document flow_ and places it exactly where you tell it to be.

```css
.absolute-item {
  position: absolute;
  top: 0;
  right: 0;
}
```

#### Using Absolute + Relative Together

There are many cases where you'll want to use `absolute`, but position an element _exactly relative to another element_. In that case, you can use `absolute` inside a `relative` element. See this Codepen for an example.

<p data-height="665" data-theme-id="0" data-slug-hash="WwVKMq" data-default-tab="css,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/WwVKMq/">Relative + Absolute</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>
