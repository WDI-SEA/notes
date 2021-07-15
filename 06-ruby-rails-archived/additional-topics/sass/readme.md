SASS
=======

Make CSS easier
-------

As we've been covering Ruby on Rails you may have noticed the files in your `app/assets/stylesheets` ending in a different file extension. Instead of our typical `.css` we get `.scss`!

`.scss` files are part of a larger piece of software called SASS, or **Syntactically Awesome Style Sheets**. SASS is something called a **CSS Preprocessor**.

A preprocessor's job is to take a more advanced syntax of CSS and **PROCESS** it **BEFORE** ( hence "pre" ) it is sent to the client as plain old CSS.

[Sass Website](http://sass-lang.com/)

SASS vs SCSS
-------

So if the software is called SASS, why are we using files ending in SCSS?

SCSS or **Sassy CSS** is just the file type that the SASS framework utilizes.

[SASS vs SCSS article](http://www.sitepoint.com/whats-difference-sass-scss/)

Installation
-------
When working with Ruby on Rails, SASS is inherently installed in our Gemfile so there's no need to install anything ourselves.

With Node and other back-end platforms you will typically have to install the SASS package manually.

Cool Stuff SASS gives us
-------

SASS is basically CSS with actual programming aspects incorporated which makes our lives much easier.

### **Variables** ###

With SASS we can actually utilize variables in our CSS code. These are typically prefaced with the "$" symbol.

```sass
$pad: 2em;
$color-primary: rgb(40, 40, 40);
$color-secondary: rgb(40, 170, 220);

body {
  background-color: $color-primary;
}

h1 {
  color: $color-secondary;
}

.container {
  padding: $pad;
}
```

Which will be processed and converted into CSS like this:

```css
body {
  background-color: #282828;
}

h1 {
  color: #28aadc;
}

.container {
  padding: 2em;
}
```

### **Nesting** ###

With Nesting in SASS we can declare inherited styles that would normally make us repeat the parent selector

```sass
nav {
  text-align: center;

  ul {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  li {
    display: inline-block;
  }

  a {
    display: block;
    padding: 5px 10px;
  }
}
```
Which will turn into this CSS:

```css
nav {
  text-align: center;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

nav li {
  display: inline-block;
}

nav a {
  display: block;
  padding: 5px 10px;
}
```

### **Extend** ###

Another useful feature is the ability to extend styles from predefined classes or id's. To do so we'll use the **@extend** keyword.

```sass
// columns
.col-1-3 {
  width: 33.33%;
}

.col-2-3 {
  width: 66.66%;
}

// colours
.blue {
  color: rgb(40, 170, 220);
}

// structure
.primary-content {
  @extend .col-2-3;
}

.secondary-content {
  @extend .col-2-3;
}

// text
p.highlight {
  font-size: 3em;
  @extend .blue;
}
```

The resulting CSS:

```css
.col-1-3, .secondary-content {
 width: 33.33%;
}

.col-2-3, .primary-content {
 width: 66.66%;
}

.blue, p.highlight {
 color: #28aadc;
}

p.highlight {
 font-size: 3em;
}
```

### **Import** ###

A great feature of SASS is the ability to import other stylesheets. This aspect allows us to utilize DRY principles even in our stylesheets!

** **Note!**
When you're creating `.scss` files that you know you'll be importing into a main stylesheet be sure to name them starting with and **underscore**

e.g: `_navbar.scss`

This will tell the SASS preprocessor to not convert those directly to CSS but instead pull them into a main file and then convert everything there into CSS.

```sass
@import 'reset';
@import 'grid';
@import 'text';

body {
}

h1 {
}
```

### **Mixins** ###

Mixins are an extremely powerful feature of SASS. Basically they allow us to define a function and pass parameters to that function in order to output a result. Typically this can be used to make a shortcut for extraneous CSS rules.

```sass
@mixin border-radius($radius) {
  -webkit-border-radius: $radius;
     -moz-border-radius: $radius;
      -ms-border-radius: $radius;
          border-radius: $radius;
}

.box {
  @include border-radius(10px);
}
```

And the CSS that comes from that:

```css
.box {
  -webkit-border-radius: 10px;
  -moz-border-radius: 10px;
  -ms-border-radius: 10px;
  border-radius: 10px;
}
```

Fin
-----------

As we can see SASS gives us many tools that make writing styles for our apps easier and more robust. Basically anything that can improve on CSS we should be all for!
