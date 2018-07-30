# jQuery - Events

Similar to vanilla JavaScript, we can add event handlers to different elements on the page. There are two ways to do this: using the event functions themselves (.click(), .sumbit(), etc.), or using .on([insert event type here], function(){});

```js
// click
$('div').on('click', function() {
  console.log('clicked!');
});

// click (alternative form)
$('div').click(function() {
  console.log('clicked!');
});

// hover, which needs 2 functions for hovering over and out
$('div').hover(function() {
  console.log('hovered over!');
}, function() {
  console.log('hovered out!');
});

```

see full list of event-related jQuery functions here: https://api.jquery.com/category/events/

## Event Delegation

Event delegation attaches an event to a single element and *delegates* the events out to specified children.

```js
// click with event delegation
$('ul').on('click', 'li', function() {
  console.log('clicked!');
});
```

But why not do this?

```js
// click without event delegation
$('ul li').on('click', function() {
  console.log('clicked!');
});
```

While this works for a static list, if we were to add another list item later, it would not have an event listener attached unless we ran this function again. 

```html
<ul>
  <li>#1</li>
  <li>#2</li>
  <li>#3</li>
</ul>
```

```js
// click without event delegation
$('ul li').on('click', function() {
  console.log('clicked!');
});

//add a new list item
var newListItem = $("<li></li>");
newListItem.text("#4");
$("ul").append(newListItem);
```
In the above code, the 4th list item wouldn't have an event handler attached to it!

Event delegation makes things easier by applying the event to the entire parent for delegation to all children as they are born.

<p data-height="265" data-theme-id="0" data-slug-hash="wWwdxP" data-default-tab="js,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/wWwdxP/">Event Delegation</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>

## Effects and Animations

* `hide()`
* `show()`
* `fadeIn()`
* `fadeOut()`
* `slideToggle()`
* `animate()`

And of course, there are more in jQuery's documentation.

## Event Propagation

<p data-height="465" data-theme-id="0" data-slug-hash="XKrRYQ" data-default-tab="js,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/XKrRYQ/">Event Propagation</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>

## Making sure the DOM has loaded

Using vanilla JS, we used:

```js
document.addEventListener('DOMContentLoaded', function() {
  // your code here
});
```

But using jQuery, we can use:

```js
$(document).ready(function() {
  // your code here
});

//or

$(function() {
  // your code here
});
```
