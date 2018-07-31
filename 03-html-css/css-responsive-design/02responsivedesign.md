# Responsive Design

> "Responsive Design" is the strategy of making a site that "responds" to the browser and device that it is being shown on... by looking awesome no matter what.

You can also check out this visual explanation:
http://johnpolacek.github.io/scrolldeck.js/decks/responsive/

## Background

PUT STUFF HERE

### Examples of responsive sites:

- [Boston Globe](http://www.bostonglobe.com/)  
- [GA](https://generalassemb.ly/)

#### Non-responsive sites

You'll be hard-pressed to find a major website that doesn't deal with mobile
devices somehow. Reddit isn't specifically responsive, but you do have the
option of switching to a mobile-optimized site.

If you look at the Reddit site on your phone, try hitting the hamburger menu in
the top right corner, and selecting desktop site. How does this change your
experience?

### The Web has always been responsive

From the beginning, the web has been meant to be shown on a variety of
different screens. Text wraps, floats automatically position themselves based
on screen size, and we've had percentage sizing in CSS basically forever.

If we go to this simple example, we see that floats reflow, depending on screen
width:

<p data-height="400" data-theme-id="0" data-slug-hash="ZOYWQJ" data-default-tab="html,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/ZOYWQJ/">Float demo</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

Likewise, the paragraphs remain at 50% of screen width, no matter what this screen width is.

This works to an extent, but we'd really like a few more tools for changing
layout based on screen size.

## Making Responsive Webpages

### The Viewport

When web developers started creating sites for mobile, they had problems with
displaying pages that were initially created for desktops. They were too large!
The quick fix was to scale pages to fit the screen, but we ended up getting
results like this:

![No Viewport Meta Tag](https://developers.google.com/speed/docs/insights/images/viewport/iphone_no_viewport.jpg)

Yikes, that's hard to read on a small device. The solution is that we need to
control the width and the zoom level of the page.

When creating sites for mobile (which you should almost always do), we want to
control the page width and zoom level of the browser using the viewport tag:

```html
<meta name="viewport" content="width=device-width, initial-scale=1">
```

Doing so will give us something like this:

![Viewport Meta Tag](https://developers.google.com/speed/docs/insights/images/viewport/iphone_viewport.jpg)

Much better! Pictures courtesy of [Google Developers](https://developers.google.com)

### Media Queries

Media queries are simply a way to conditionally apply styles based on the
device the page is being displayed on.

We already know that if we do something like this:

```css
p {
  color: red;
}

p.blue_text {
  color: blue;
}
```

By default, all p tags will have red text, unless they have the class
blue_text, in which case, the text will be blue. We can do a similar thing with
media queries.

```css
p {
  color: blue;
}

@media (min-width: 600px) {
  p {
    color: red;
  }
}
```

Now, all p tags will be red, until the screen size reaches 600px, when they'll turn blue.

A potentially more useful example would be to float all list items left until a
certain screen size, then revert the list items to block, causing them to
stack.

```css
li {
  display: block;
  color: blue;
}

@media (min-width: 600px) {
  li {
    display: inline-block;
    color: red;
  }
}
```

Along with `min-width`, you can also provide `max-width` to a media query, as
well as combine different device orientations and resolutions. For example,
here's a media query that will apply to the list elements between 600-1000px.

```css
@media (min-width: 600px) and (max-width: 1000px) {
  li {
    display: inline-block;
    color: black;
  }
}
```

Most of the time, `min-width` and `max-width` will be your bread and butter.
You can read more about media queries at MDN's website. See Additional Topics
for more links.

### Columns Example

<p data-height="400" data-theme-id="0" data-slug-hash="zBxqda" data-default-tab="html,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/zBxqda/">Media Queries</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>
