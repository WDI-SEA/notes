# Custom Properties

## Custom Properties - EXPERIMENTAL!

Speaking of experimental CSS properties, here is one coming down the pipeline: CSS Custom Properties add the ability to define and access variables inside your CSS. But what does it mean that it is experimental? It means that it is not actually part of the standard yet and, as a result, it will not have perfect support in all browsers. It is also subject to change as it is not finalized yet.

We must be careful about building websites that use non-standard or experimental features because we won't be able to guarantee that they work for all users. However, it is in our very best interest to be familiar with upcoming features so that when they are mainstream we can begin using them ASAP. It is also a good thing to mention to employers during interviews when they ask what new things you are learning about. With that in mind, let's see how they are proposed to work:

```css
:root {
  --maincolor: red;
  --subcolor: blue;
}
```

This block creates two custom properties which we can use like variables. The proposed place to initialize them is in the `:root` pseudo-class which is the same as selecting the `html` element but it has higher specificity. Putting them in there makes them visible, or in-scope, for every other element in our page.

Now to use these new values in our CSS, we can refer to them with the `var()` function:

```css
header {
  background-color: var(--maincolor);
}
header p {
  color: var(--subcolor);
}
```

This is one of the most useful features of Sass, the popular CSS preprocessor. It is very exciting that it will soon be a part of standard CSS. You can imagine the time savings involved in changing a single variable in our code versus changing every place its value is used!

## Additional Topics

### CSS Custom Properties

* [Custom Properties \(MDN\)](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)
* [Using Custom Properties to Modify Components](https://css-tricks.com/using-custom-properties-modify-components/)
* [It's Time to Start Using CSS Custom Properties](https://www.smashingmagazine.com/2017/04/start-using-css-custom-properties/)

