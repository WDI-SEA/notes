# jQuery Plugins

## Objectives

* Describe what jQuery plugins are used for
* Answer the question "Why aren't good or approved plugins included in the standard jQuery library?"
* Include and implement jQuery plugins on web pages
* Experiment with different plugins

## What is a Plugin?

Plugins are pieces of code that someone else has written to extend jQuery's functionality. The most common plugin is jQuery UI.

## Why aren't plugins just included in the standard jQuery library?
* extra code that you don't use just bogs down your project
* unopinionated -> customizable

## How to implement
jQuery plugins require jQuery in order to work, so the script tag that pulls in the plugin must come **after** the one that pulls in jQuery.

## jQuery UI

jQueryUI provides an additional library of user interactions and elements not provided by jQuery. You can find the CDNs for jQuery and jQueryUI [here](https://developers.google.com/speed/libraries/)

jQuery UI also provides elements with 'themes' or styling. In order to use these styled elements (dropdowns, accordions, etc.), be sure to include the appropriate jQuery UI CSS stylesheet in the head tag as well.

### Example: sortable 

Let's go over implementing sortable in a jQuery to-do list.

* jQuery UI accordion lab
http://api.jqueryui.com/accordion/
* build up loading example
https://gasparesganga.com/labs/jquery-loading-overlay/#comments-and-ideas

<p data-height="665" data-theme-id="0" data-slug-hash="YwLXMV" data-default-tab="html,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/YwLXMV/">jQuery UI Examples</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>
