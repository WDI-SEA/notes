# Floats and Clears

The float property specifies whether or not a box \(or an element\) should float; essentially, it determines whether text will be wrapped around the element.

![](https://cloud.githubusercontent.com/assets/40461/8234489/3b61ef02-15d4-11e5-8864-435fb6e0c3cc.png)

Note that "absolutely positioned" elements ignore the float property as they are removed from the normal document flow.

Floated elements remain a part of the flow of the web page. This is distinctly different than page elements that use absolute positioning.

There are four valid values for the float property. `left` and `right` float elements those directions, respectively. `none` \(the default\) ensures the element will not float and `inherit` which will assume the float value from that element's parent element.

## Clear

All elements will float next to floated items until they are specifically cleared. Think about the text on the page.

![](https://cloud.githubusercontent.com/assets/40461/8234478/287c1156-15d4-11e5-9901-ba9090a5bf70.png)

## Floats to create multicolumn layouts

If our element sizes are variable or dynamic, we can use floats to allow text/other elements to wrap around the floated element. This can be done by creating containers and having them all float to the left. See the example below.

See the Pen [Floats and Clears](http://codepen.io/bhague1281/pen/vGoajr/) by Brian Hague \([@bhague1281](http://codepen.io/bhague1281)\) on [CodePen](http://codepen.io).

Note that our text is aware that our div wants to be as left as possible and kindly wraps it in a nice text hug.

## Floats with clears

While floats make other elements aware of their location and get text hugs, clears make other elements aware and are told not to touch.

`clear` is saying "I'm not sure how much space I'm going to take but whatever it is clear off my right side" so our text respects its wishes and drops to the line below.

