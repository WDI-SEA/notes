#jQuery Plugins

##Objectives

* Describe what jQuery plugins are used for
* Include and implement jQuery plugins on web pages
* Experiment with different plugins and making custom jQuery plugins

##Plugins

As you've come to seen, jQuery provides many useful functions to make DOM selection much easier. Instead of having to loop through arrays of DOM elements, we can perform complex selections in one line. Here's an example of using `.css()` to change all spans inside list items red.

```js
$('li span').css('color', 'red');
```

But as you've come to discover, programmers always want more. jQuery was designed with extensibility in mind, which means we can use plugins in order to extend jQuery's functionality. The most common plugin is jQuery UI.

##jQuery UI

[jQuery UI](https://jqueryui.com/)

jQuery UI provides an additional library of user interactions and elements not provided by jQuery. In order to use its features, include the following script **after** jQuery.

**NOTE:** jQuery UI requires jQuery in order to extend jQuery's features. This is common across jQuery plugins, so make sure to import plugins after jQuery.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>
```

jQuery UI also provides elements with 'themes' or styling. In order to use these styled elements (dropdowns, accordions, etc.), be sure to include the appropriate jQuery UI CSS file as well (in `<head>`)

```html
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/jqueryui/1.11.4/jquery-ui.theme.min.css">
```

Once jQuery UI is included on the page, jQuery is *extended*, meaning jQuery UI provides additional functions to jQuery. An example:

```js
$('.item').draggable();
```

<p data-height="665" data-theme-id="0" data-slug-hash="YwLXMV" data-default-tab="html,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/YwLXMV/">jQuery UI Examples</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>
