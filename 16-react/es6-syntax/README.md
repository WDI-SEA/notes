# ES6+/ESNext

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) ES6+

### Learning Objectives

_After this lesson, you will be able to:_

* Define ES6/ESNext

## What is ES6?

Let's buckle in for some solid terminology. We'll try to make it fun and easy.

At the core, ES6 is a set of JavaScript features that were added in 2015. We'll go through the main ones here. You've actually already been seeing some ES6. As you go through this lesson, see what you recognize!

ES6, also called ES2015, refers to a set of language features that were added to the ECMAScript standard in 2015.

**Cool, what's ECMASript?** It's a standard that JavaScript tracks. For our purposes, it _is_ JavaScript.

**2015?** Yes, that was a while ago now, but it was the last major paradigm shift in the JavaScript language. There were more additions to JavaScript in 2016, also known as ES7. These changes weren't as drastic or exciting as those of ES6, which is why you don't hear much about it. Updates happen each year, for example ES8/ES2017 added more features. The entire set of modern features from ES6 onward is sometimes referred to as `ESNext`.

## Why do I care?

The language features of ESNext are _awesome_. They enable you to write more concise, easier-to-read, and easier-to-maintain code. They also make your code _more fun to write!_ \(For example, there's some syntax that looks like a rocket ship, and using that rocket ship, you have much less you actually have to write out\).

**That sounds great, but can we just do React for now?** If you look at the [React docs](https://facebook.github.io/react/docs/installation.html#enabling-es6-and-jsx), you'll see they are written with the assumption that the reader is familiar with ES6. Modern JavaScript language features \(ES6, ES7, and beyond\) are widely used in the React development community. Whether you're reading blog posts, studying source code, or browsing questions on Stack Overflow, you're going to see them in use frequently. So, it's very helpful to have an understanding of them.

**If some browsers don't support ES6, why does anyone use it? How can we use ES6 universally?** Great question with a simple answer: [Babel](https://babeljs.io/). Babel takes your ES6 \(and beyond\) code and transpiles it into browser-friendly ES5. If you use Create React App to start a project, Babel is built in, so your production build is ready for deployment. And support for new language features _is_ coming to browsers. All of the JavaScript features we'll talk about in this lesson except "module imports" can be used _right now_ in Chrome - try them out in the DevTools console!

**Is JSX the same as ES6?** No. JSX is the XML/HTML-like syntax you can use _in your JavaScript_ when creating React components \(and there are other frameworks that use JSX as well\).

Within React, you can remember this as ES6 is the JavaScript that you write, whereas JSX is just what your components will render to the actual screen.

For example:

* JSX: `<h1>{this.props.name} this will be rendered in the browser</h1>`
* ES6: `const x = 1; var addTwo = num => { return num + 2; }`

Babel _can_ transpile JSX to plain JavaScript, though - just like it transpiles ES6 JavaScript to ES5.

## ESNext features we'll cover here:

* `const` and `let`
* Arrow functions
* Object literal shorthand
* Template literals
* Imports and modules

Note that in this lesson, we're talking about JavaScript and nothing React-specific \(you can use ES6 in your day-to-day JavaScript\).

Also note that semicolons are optional in ES6. However, whether or not to use them is under constant debate in the wider programming community. We've included them in this lesson for clarity.

## Some of the features from ES6 and beyond we will _not_ cover:

* [Promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
* [Async](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function)/[Await](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await)
* [Generators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Iterators_and_Generators)
* [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
* [Array spread](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_operator)
* [Array and Object destructuring assignment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)
* [Object rest spread](https://babeljs.io/docs/plugins/transform-object-rest-spread/)

