# Box Model

Most HTML elements can be considered boxes, or is _living inside a box_.

The CSS box model describes this principal - a box wraps around all HTML elements, and it consists of: margins, borders, padding, and the actual content. This model allows us to place a border around elements and space elements in relation to other elements.

With CSS properties and values, it is possible to apply specific styles to each of these elements, and change the way they behave and/or display on the page.

The image below illustrates the box model and what you should have seen in your dev tools:

![box-model](https://s3.amazonaws.com/viking_education/web_development/web_app_eng/css_box_model_chrome.png)

_From_ [_viking codeschool_](https://www.vikingcodeschool.com/html5-and-css3/the-css-box-model)

But what do these different layers mean, and how are they relating to one another?

**Margin**

* _outside of the element_
* clears an area around the border
* does NOT have a background color \(transparent - shows the `background-color` of the container the element lives inside of\)

**Border**

* _inside the element_
* a border that goes around the padding and content
* it will use the `color` of the element unless you give it its own `border-color`

**Padding**

* _inside the element_
* clears an area between the content and the border
* transparent - shows the `background-color` of the element

**Content**

* _inside the element_
* where text and images appear
* the element's `color` property actually colors the content

## Layers of the Box Model

Let's get go into some more detail and practice with each of these elements of The Box Model.

#### Margin

The margin is the space around the element. The larger the margin, the more space between our element and the elements around it. We can adjust the margin to move our HTML elements closer to or farther from each other.

Let's start with our margins. Adjusting our margins not only moves our element relative to other elements on the page but also relative to the "walls" of the HTML document.

For instance, if we take an HTML element with a specific width \(such as our `<div>` in the editor\) and set its margin to `auto` - this tells the document to automatically put equal left and right margins on our element, centering it on the page.

If you want to specify a particular margin, to a particular side, you can do it like this:

```css
div {
  margin-top: 1px;
  margin-right: 2px;
  margin-bottom: 3px;
  margin-left: 4px;
}
```

You can also set an element's margins all at once: you just start from the top margin and go around clockwise \(going from top to right to bottom to left\). For instance,

```css
div {
  margin: 1px 2px 3px 4px;
}
```

You can do top-bottom and side side - let's add this to our css for now:

```css
div {
  margin: 0 auto;
}
```

#### Border

The border is the edge of the element. It's what we've been making visible every time we set the border property.

Borders can be set in two ways, just like your margins and just like we've talked about previously.

```css
div {
  border: 5px solid black;
}

/* OR */

div {
  border-width: 5px;
  border-style: solid;
  border-color: black;
}
```

#### Padding and Content

The padding is the spacing between the content and the border. We can adjust this value with CSS to move the border closer to or farther from the content.

Padding can be set in two ways, just like your margins.

```css
div {
  padding: 2px;
}

/* OR */

div {
  padding-top: 3px;
  padding-right: 1px;
  padding-bottom: 0px;
  padding-left: 9px;
}

/* OR */

div {
  padding: 3px 1px 0 9px;
}
```

Padding becomes more apparent when we have "stuff" inside the box.

#### Width, Height and `box-sizing`

So with all of these parts of an element that can have their own widths, what are we actually setting when we adjust the `width` and `height` CSS properties of an element?

It turns out that there are two ways that width and height can be interpretted and which one is used is determined by a third property called `box-sizing`. The CSS `box-sizing` prop gives you two main options:

1. `content-box` - this is the default behavior. When you put `box-sizing: content-box` on an element \(or don't specify it at all\), the `width` and `height` props only affect the **content**, meaning that padding, border, and margin are not included in these values. To calculate the full size of the element, you would add the width \(of the content\) to the width of the padding as well as the width of the border. Then the margin exists outside of that area.
2. `border-box` - this is a newer option that makes it so that your `width` and `height` props actually include **content, padding, and border** \(all three\) in their values. The only thing outside the width of the element would be its margin. Using this property setting can usually simplify layout calculations but it must be set on all elements.

Having `content-box` as the default may be a reason why you may have seen your HTML elements unexpectedly wrapping onto multiple lines - if you don't add the padding and border sizes into your width calculations, you can easily exceed the width of the browser and cause content to wrap to the next line. If you switch to using `border-box` then the only extra space outside of your element's width is the margin between elements.

### Resources

* [CSS Box Model on W3Schools](https://www.w3schools.com/css/css_boxmodel.asp)
* [CSS Box Sizing on W3Schools](https://www.w3schools.com/cssref/css3_pr_box-sizing.asp)

