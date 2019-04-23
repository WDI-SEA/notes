#Additional Gulp Topics

To provide some additional features to your `gulpfile.js`, here are some additional modules that can be installed. Some of these examples can be found in different branches on the solution code:

https://github.com/WDI-SEA/react-starter-basic

###gulp.watch

If running `gulp` over and over again becomes annoying, you can create a `watch` task and run `gulp watch`, which will run task(s) whenever specified files change.

> Extra dev dependencies: none

**Example**

```js
var gulp = require('gulp');

gulp.task('build', function() {
  console.log('build');
});

gulp.task('watch', function() {
  gulp.watch('src/**/*.jsx', ['build']);
});

gulp.task('default', ['watch']);
```

###Gulp with ESLint

In order to control code quality, companies may use **code linters** in order to enforce style guidelines. [ESLint](http://eslint.org/) is being more common as developers make the switch to ES6. Here's an example setup that will **lint** your code and produce reports on code quality. By default, ESLint will use the Airbnb code guidelines, but you can configure as necessary.

> Extra dev dependencies: babel-eslint, eslint-config-airbnb, eslint-plugin-react, gulp-eslint

**Example**

In the root of your project, you'll need to create a file named `.eslintrc`, which looks something like this:

```js
{
  "extends": ["airbnb"]
}
```

and then your `gulpfile.js` should look something like this:


```js
var gulp = require('gulp');
var eslint = require('gulp-eslint');

gulp.task('lint', function() {
  return gulp.src(['src/**/*.jsx'])
    .pipe(eslint())
    .pipe(eslint.format())
    .pipe(eslint.failAfterError());
})

gulp.task('build', function() {
  console.log('build');
});

gulp.task('default', ['lint', 'build']);
```

eslint will give you a lot of errors, because `eslint-config-airbnb` wants you to write es6 code, rather than JavaScript.


###Gulp with SASS

Don't worry, SASS isn't limited to Rails. We can use the `gulp-sass` package to take SASS files and compile them to CSS.

> Extra dev dependencies: gulp-sass

**Example**

```js
var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('build', function() {
  console.log('build');
});

gulp.task('sass', function() {
  return gulp.src('sass/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('dist/css'));
});

gulp.task('default', ['sass', 'build']);
```
