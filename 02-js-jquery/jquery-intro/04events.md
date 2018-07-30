# jQuery - Events

Similar to vanilla JavaScript, we can add event handlers to different elements on the page using jQuery event handler functions like .click(), .submit(), etc, or using .on([insert event type here], [insert function here]).

More on jQuery events here: https://api.jquery.com/category/events/

```js
// click
$('.item').on('click', function() {
  console.log('clicked!');
});

// click (alternative form)
$('.item').click(function() {
  console.log('clicked!');
});

// form submission
$('.form').on('submit', function() {
  console.log('clicked!');
});

// form submission, preventing refresh of the page
$('.form').submit(function(e) {
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

Event delegation attaches an event to a single element which then *delegates* that event out to specified children. 

```js
// click with event delegation
$('.list').on('click', 'li', function() {
  console.log('clicked!');
});
```

Why not do this?

```js
$('.list li').on('click', function() {
  console.log('clicked!');
});
```

While this works for a static list, if we were to add another list item later, it would not have an event listener attached unless we ran this function again. Event delegation makes things easier by applying the event to the entire parent which in turn delegates the event to its children as they are born.

<p data-height="265" data-theme-id="0" data-slug-hash="wWwdxP" data-default-tab="js,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/wWwdxP/">Event Delegation</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>


## Event Propagation

This occurs when there is an element nested within another element and both of them have event handlers attached to them, so the firing of an event attached to the internal element triggers the firing of the event handler attached to its parent elemennt.

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


## Conclusion

* jQuery makes JavaScript super friendly and easy to write. a lot of websites are using jquery, soon you will too.  Remember that it's always good to know how to use what is called vanilla JavaScript, or JavaScript without a library.

* Please spend some time reviewing [the documentation](https://api.jquery.com/).
