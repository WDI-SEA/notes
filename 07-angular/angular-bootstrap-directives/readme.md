#Bootstrap Directives and Animation

##Objectives

* Use third-party directives in an Angular application
* Utilize the concepts of dependency injection and templates with Bootstrap

##Bootstrap JS in Angular

You may have noticed that we left out `bootstrap.js` and `jquery.js` when working with our Angular apps. The reason for this is that we haven't used jQuery, and AngularJS is designed to be a *replacement* for jQuery in most regards. Instead of manipulating the DOM with handlers to events, we're letting directives handle manipulation for us.

Our events are also **data-driven**, meaning actions like `ng-submit` and `ng-repeat` affect the DOM depending on the data we provide to it.

Therefore, we need a set of directives to use Bootstrap JS elements, such as carousels, modals, dropdowns, etc.

##Bootstrap Directives

We can use Angular UI's Bootstrap directives in order to use different Bootstrap components. All we need is the `bootstrap.css` file and the directives script.

In `<head></head>` of the starter code, add:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular-animate.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular-ui-bootstrap/1.2.4/ui-bootstrap-tpls.js"></script>
<script src="js/app.js"></script>
```

Then, create an Angular application in `js/app.js`. Make sure to add the directives to the HTML file to bootstrap the application. Also, add `ngAnimate`, because we'll also be utilizing some animations.

```js
var app = angular.module('BootstrapApp', ['ngAnimate']);

app.controller('BootstrapCtrl', ['$scope', function($scope) {

}]);
```

##Adding a Navbar using ng-include

Partials are a common concept in web frameworks, and Angular is no exception. We can create "partial" views and render them in our app using the `ng-include` directive. Let's do this as we create a navigation bar.

Create a folder for holding views.

```bash
mkdir views

touch views/navbar.html
```

Create a navbar in `navbar.html`.

Then, use `ng-include` to include the partial, using the absolute path of the partial inside single quotes (this treats the path as a string).

Inside `index.html`:

```html
<div ng-include="'/views/navbar.html'"></div>
```

Lastly, if we try to render this page, there will be a cross origin error. So make sure to run a local HTTP server to load the partial (you should have a `srv` alias setup for this).

If you don't have a `srv` alias set up, then run this command manually. Make sure
you're in the directory with `index.html` in it.

```
python -m SimpleHTTPServer 8000
```
Now navigate to http://localhost:8000 and you should see you site there.

### Utilizing Angular Directives

Playing around with the navigation bar, you may notice that the "hamburger icon" dropdown does not work in mobile view. In order to utilize this, we'll have to add directives to create the **collapse** effect.

All of the Bootstrap directives are contained in an Angular module, so let's inject the Bootstrap UI module as a dependency for the app.

In `app.js`

```js
var app = angular.module('BootstrapApp', ['ngAnimate', 'ui.bootstrap']);
```

####Practice

Implement the **collapse** effect so that the navigation bar correctly collapses in mobile view. The [Bootstrap UI documentation](https://angular-ui.github.io/bootstrap) should be very helpful.
