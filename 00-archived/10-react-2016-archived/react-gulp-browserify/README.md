# React with Gulp and Browserify

## Objectives

* Identify the purpose and uses for a front-end build tool
* Explain why **browserify** is needed and beneficial for front-end modules
* Use Gulp to set up a build system for a ReactJS project

When working with ReactJS in Codepen, there was little setup due to a built-in Babel/JSX transpiler and including React and ReactDOM via CDN links. In production setups, we'll need to find another way to transpile ES6/JSX -&gt; ES5, as well as another way to require the modules we need.

Specifically, we'll be using **Gulp**, a front-end build tool that allows us to create **tasks** to copy and transpile files for us. We'll also take advantage of **browserify**, which will allow us to use `require` in front-end files. Previously, this was only available within Node.

**Note:** There's another package manager specifically for front-end dependencies called **Bower.** However, many of the React components we'll be using can be installed through `npm`. If you're interested in learning more about Bower, read more on their website [here](http://bower.io/)

