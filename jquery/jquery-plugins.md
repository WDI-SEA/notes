# Plugins

## Objectives

* Describe what jQuery plugins are used for
* Answer the question "Why aren't good or approved plugins included in the standard jQuery library?"
* Include and implement jQuery plugins on web pages
* Experiment with different plugins

## What is a Plugin?

Plugins are methods that extend jQuery's functionality. jQuery's [plugin docs](https://learn.jquery.com/plugins/) tell us to think of the methods that come with jQuery core \(eg. `.addClass()`\) as plugins too, but normally the term _plugin_ refers that other people have written. These plugins aren't included in basic jQuery so we'll have to pull them in by downloading the code or using a CDN.

## Why aren't plugins just included in the standard jQuery library?

* extra code that you don't use just bogs down your project
* unopinionated -&gt; customizable

## How to implement

jQuery plugins require jQuery in order to work, so the script tag that pulls in the plugin must come **after** the one that pulls in jQuery.

## jQueryUI

jQuery has it's own library of plugins for widgets and interactions called [jQueryUI](https://jqueryui.com/). You can find the CDNs for jQuery and jQueryUI [here](https://developers.google.com/speed/libraries/).

The [demos page](http://jqueryui.com/demos/) has examples of the plugins implemented.

jQuery UI also provides elements with 'themes' or styling. In order to use these styled elements \(dropdowns, accordions, etc.\), be sure to include the appropriate jQueryUI CSS stylesheet in the head tag as well.

### Example: Datepicker

* [Demo](https://jqueryui.com/datepicker/)
* [Docs](http://api.jqueryui.com/datepicker/#entry-examples)

### Exercise:

Use [jQueryUI accordion](http://api.jqueryui.com/accordion/) to make an accordion menu.

### Exercise:

Implement [sortable](http://jqueryui.com/sortable/) into your jQuery to-do list if you haven't already.

## Codepen Examples:

See the Pen [jQuery UI Examples](http://codepen.io/bhague1281/pen/YwLXMV/) by Brian Hague \([@bhague1281](http://codepen.io/bhague1281)\) on [CodePen](http://codepen.io).

