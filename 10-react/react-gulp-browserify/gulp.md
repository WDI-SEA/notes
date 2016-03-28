#Setting up Gulp

We're going to create a React starter repo that will allow you to setup full-stack React applications with Gulp, Browserify, and ES6.

##Getting Started

Create a new repository in Github and clone it to your computer. You can call it `react-starter-basic`. The link to the finished version is below, but we'll be building it from scratch.

https://github.com/WDI-SEA/react-starter-basic

###Installing gulp

Install the `gulp` command line tool:

```
npm install -g gulp-cli
```

###Setting up dependencies

After cloning your repo to your local computer, setup `npm` by running:

```
npm init
```

Then, install some dependencies we'll need for our workflow.

```
npm install --save-dev gulp browserify babelify babel-preset-react vinyl-source-stream react react-dom
```

* `--save-dev` will save these dependencies, but only install them on development environments
* `gulp` will allow us to run tasks needed to copy and transpile code
* `browserify` will allow us to use `require()` in front-end files. [Browserify](http://browserify.org/)
* `babelify` and `babel-preset-react` will allow us to transpile ES6/JSX to ES5
* `vinyl-source-stream` will allow us to convert the stream coming from `browserify` so we can use it with `gulp`
* `react` and `react-dom` are the dependencies needed to create React apps

Once these dependencies are set up, we'll also want to create a configuration file so Babel knows to use the preset for React.

###Creating a .babelrc file

Create a file called `.babelrc` in the root of the project directory, and create the following preset in the file:

**babel.rc**

```
{
  "presets": ["react"]
}
```

This preset will tell Babel to transpile using the React preset. Note that this is **IMPORTANT** when working with Babel, and the presets may vary depending on the type of application being developed.

##Creating a Gulpfile

In order to use `gulp`, we need to create a file called a **gulpfile**. This file will contain **tasks** that can take care of importing modules, transpiling code, and copying files. Specifically, we'll be doing the following in our gulpfile.

* Setting up `browserify` to import modules
* Transform code using `babelify`
* Copying JS files to a different directory (separating our source React files from the transpiled file)

While beyond the scope of this lesson, Gulp can also be setup to minify code, lint code, and utilize additional preprocessors like SASS and LESS. See the resources for more information on setting up these tasks.

###Gulp Tasks

A **task** in gulp is essentially a named function that can be invoked via the `gulp` command line tool. In the root of the project, let's make a gulpfile. Gulp will look for a file called `gulpfile.js`, so we'll name the file `gulpfile.js`.

In **gulpfile.js**:

```js
// require gulp
var gulp = require('gulp');

// creating a task, with a name and function
gulp.task('build', function() {
  console.log('Building the JS!');
});
```

This is a file with one task called `build`. It can be run in the command line by running `gulp build`.

By default, Gulp looks for a task called `default` and runs it automatically if no task if specified. Let's change the file to run the `build` task automatically.

```js
var gulp = require('gulp');

gulp.task('build', function() {
  console.log('Building the JS!');
});

// a task called 'default', which takes an array of tasks and runs them
gulp.task('default', ['build']);
```

Now we can type `gulp` in the command line and Gulp will automatically run the `build` task. Awesome!

###Fleshing out gulpfile.js

Let's make a few more modifications to the `gulpfile` in order to make it take care of our React files.

In **gulpfile.js**:

```js
var gulp = require('gulp');
var browserify = require('browserify');
var babelify = require('babelify');
var source = require('vinyl-source-stream');

gulp.task('build', function() {
  browserify({
    entries: 'src/app.jsx',
    extensions: ['.jsx'],
    debug: true
  })
  .transform(babelify, {presets: "react"})
  .bundle()
  .pipe(source('app.js'))
  .pipe(gulp.dest('dist'));
});

gulp.task('default', ['build']);
```

Yikes, what did we just do?! Let's break it down.

* At the top of the file, we required the additional modules needed to process our React files
* The `build` task is setup to do the following
  * Incorporate `browserify` so we can use `require()` in front-end files
    * Everything needed should belong in `src/app.jsx`
  * Transform ES6/JSX into ES5 code
  * Bundle the files together and create a new file called `app.js`
  * Write the file to a new location (`dist/app.js`)

###Testing the Gulpfile with a React app

In order to test this `gulpfile.js`, let's make sure that we have a sample React app that exists. Create the following folder structure in the project:

```
- react-starter-basic
  - src
    - app.jsx
```

Now, let's create a React application inside of `src/app.jsx`

In **src/app.jsx**:

```js
var React = require('react');
var ReactDOM = require('react-dom');

var App = React.createClass({
  render: function() {
    return <h1>Hello!</h1>;
  }
});

ReactDOM.render(<App />, document.body);
```

Now, try running the `gulpfile` by running in the command line:

```
gulp
```

If successful, the `build` task should run and create a file called `dist/app.js` in your project. This is the final file that can be included in a project. To test, try making a HTML file and include `dist/app.js` on the page. See if your React project works.

##Using Browserify

Browserify allowed us to require `react` and `react-dom` into our `src/app.jsx` file. Let's take this a step further by organizing all of our components into a separate file, then using `require()` to use them.

###Creating a components folder

Inside of the `src` folder, create a new folder called `components`. Also, create a file called `header.jsx` inside the `components` folder. Your folder structure should look like this:

```
- react-starter-basic
  - src
    - components
      - header.jsx
    - app.jsx
```

###Creating a header component

Inside of `src/components/header.jsx`, create a new React component. We'll make this Header component display `name` from `props`.

```js
var React = require('react');

var Header = React.createClass({
  render: function() {
    return <h1>{this.props.name}</h1>;
  }
});

module.exports = Header;
```

###Using the Header component in App

Now in order to use the Header component in `src/app.jsx`, let's use `require()` and render the component.

In **src/app.jsx**:

```js
var React = require('react');
var ReactDOM = require('react-dom');
var Header = require('./components/header');

var App = React.createClass({
  render: function() {
    return <Header name="Josh" />;
  }
});

ReactDOM.render(<App />, document.body);
```

Try testing this file by running `gulp` and opening the HTML created previously. Congrats, you've just used `gulp` and `browserify` to create a React app!
