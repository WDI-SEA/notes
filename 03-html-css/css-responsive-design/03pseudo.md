# Pseudo-Classes/Elements

There will be cases where you'll want to apply styling to certain _states_ of your elements. For example:

* Hovering over an element
* Checking a checkbox
* Highlighting the first or last element
* Highlighting every other element

## Pseudo-Classes

For these specific _states_, we can use **pseudo-classes**, which have a format like this:

```css
.button:hover {
  background-color: red;
}
```

Notice that the CSS selectors is followed by a single colon, then the name of the pseudo-class. These selectors can be handy when compared to the alternative \(using JavaScript\). Here are some examples:

See the Pen [Pseudo Classes](http://codepen.io/bhague1281/pen/bpXVvX/) by Brian Hague \([@bhague1281](http://codepen.io/bhague1281)\) on [CodePen](http://codepen.io).

## Pseudo-Elements

Similar to pseudo-classes, we can also use **pseudo-elements**. These selectors have two big differences from pseudo-classes.

* Instead of styling _element state_, pseudo-elements style _parts of a document_
* Instead of a single colon, pseudo-elements are defined with two colons.

Specifically, pseudo-elements can style first lines, first letters, as well as things you wouldn't normally think of, like the color of selected text.

See the Pen [Pseudo-Elements](http://codepen.io/bhague1281/pen/BzyKVL/) by Brian Hague \([@bhague1281](http://codepen.io/bhague1281)\) on [CodePen](http://codepen.io).

For more reading on pseudo classes and elements, see [this smashing magazine article](https://www.smashingmagazine.com/2016/05/an-ultimate-guide-to-css-pseudo-classes-and-pseudo-elements/).

For more pseudo-classes and pseudo-elements, see the Additional Topics links.

