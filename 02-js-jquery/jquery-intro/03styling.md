# jQuery - Styles

You can do more than select elements and modify content. You can also create or update CSS style attributes in jQuery using the .css() method

```js
$("#myDiv").css("color", "red");
```

Or, if we have a bunch of elements that all have the same class (in this example, it's class="myClass"), we can use the class selector to modify the color of all of them at once:

```js
$(".myClass").css("color", "blue");
```

But that seems kind of boring. I mean, what if we want to do something with less hard-coding using jQuery.

```js
var randColorValue = function() {
  return Math.floor( Math.random() * 255 );
}

var randColor = function() {
  var red = randColorValue();
  var green = randColorValue();
  var blue = randColorValue();

  return "rgb(" + red + "," + green + "," + blue + ")";
}

$(".myClass").css("color", randColor());
```
