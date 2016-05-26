# jQuery - Events

Similar to vanilla JavaScript, we can add event handlers to different elements on the page.

```js
// click
$('.item').on('click', function() {
  console.log('clicked!');
});

// click (alternative form)
$('.item').click(function() {
  console.log('clicked!');
});

// click with event delegation
$('.list').on('click', 'li', function() {
  console.log('clicked!');
});

// form submission
$('.form').on('submit', function() {
  console.log('clicked!');
});

// form submission, preventing refresh of the page
$('.form').on('submit', function(e) {
  e.preventDefault();
  console.log('clicked!');
});

// hover, which needs 2 functions for hovering over and out
$('.form').hover(function() {
  console.log('hovered over!');
}, function() {
  console.log('hovered out!');
});

```

## Event Delegation

Note that one of our examples used something called **event delegation**. Event delegation attaches an event to a single element and *delegates* the events out to specified children. But why not do this?

```js
$('.list li').on('click', function() {
  console.log('clicked!');
});
```

While this works for a static list, if we were to add another list item later, it would not have an event listener attached unless we ran this function again. Event delegation makes things easier by applying the event to the entire parent.

<p data-height="265" data-theme-id="0" data-slug-hash="wWwdxP" data-default-tab="js,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/wWwdxP/">Event Delegation</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

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
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

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


## Conclusion

* jQuery makes JavaScript super friendly and easy to write. a lot of websites are using jquery, soon you will too.  Remember that it's always good to know how to use what is called vanilla JavaScript, or JavaScript without a library.

* Please spend some time reviewing [the documentation](https://api.jquery.com/).
