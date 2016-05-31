# Vendor Prefixes

The number of CSS properties is fairly large, and it's likely that you won't use all of them.

The number of CSS properties is also **growing!** Experimental and nonstandard properties are constantly being added to browsers, but using them will require a special *prefix* until the properties are standardized.

In order to use experimental features, the MDN documentation for a property will usually be associated with **vendor prefixes**. Here's an example with CSS transitions.

```css
.button {
  -webkit-transition: background-color 1s ease-out 1s;
  -moz-transition: background-color 1s ease-out 1s;
  -o-transition: background-color 1s ease-out 1s;
  transition: background-color 1s ease-out 1s;
}
```

This example has three vendor prefixes, for Webkit browsers (Safari, Chrome), Mozilla (Firefox), and Opera. There are additional prefixes for Internet Explorer and Edge as well.

Note that if a browser finds a matching prefix, it will **ignore the other prefixes**. Therefore, using properties with vendor prefixes will require us to define the standard syntax last.
