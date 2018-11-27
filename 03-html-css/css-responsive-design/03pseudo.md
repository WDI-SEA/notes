# Pseudo-Classes and Pseudo-Elements

There will be cases where you'll want to apply styling to certain *states* of your elements. For example:

* Hovering over an element
* Checking a checkbox
* Highlighting the first or last element
* Highlighting every other element


### Pseudo-Classes

For these specific *states*, we can use **pseudo-classes**, which have a format like this:

```css
.button:hover {
  background-color: red;
}
```

Notice that the CSS selectors is followed by a single colon, then the name of the pseudo-class. These selectors can be handy when compared to the alternative (using JavaScript). Here are some examples:

<p data-height="400" data-theme-id="0" data-slug-hash="bpXVvX" data-default-tab="css,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/bpXVvX/">Pseudo Classes</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>

### Pseudo-Elements

Similar to pseudo-classes, we can also use **pseudo-elements**. These selectors have two big differences from pseudo-classes.

* Instead of styling *element state*, pseudo-elements style *parts of a document*
* Instead of a single colon, pseudo-elements are defined with two colons.

Specifically, pseudo-elements can style first lines, first letters, as well as things you wouldn't normally think of, like the color of selected text.

<p data-height="400" data-theme-id="0" data-slug-hash="BzyKVL" data-default-tab="css,result" data-user="bhague1281" data-embed-version="2" class="codepen">See the Pen <a href="http://codepen.io/bhague1281/pen/BzyKVL/">Pseudo-Elements</a> by Brian Hague (<a href="http://codepen.io/bhague1281">@bhague1281</a>) on <a href="http://codepen.io">CodePen</a>.</p>

For more pseudo-classes and pseudo-elements, see the Additional Topics links.
