# jQuery - Styles

jQuery allows us to change the style of DOM elements with .css([property],[value]);

```js
$("#myDiv").css("color", "red");
```

We can change several elements at once too:

```js
$("div").css("background", "yellow");
```

But that seems kind of boring. I mean, what if we want to do something with less hard-coding using jQuery.

```js
//returns a random value 0-255;
var randColorValue = function() {
  return Math.floor( Math.random() * 255 );
}

//assigns a random color value to three different variables and returns a proper rgb value
var randColor = function() {
  var red = randColorValue();
  var green = randColorValue();
  var blue = randColorValue();

  return "rgb(" + red + "," + green + "," + blue + ")";
}

$("#myDiv").css("color", randColor());
```
