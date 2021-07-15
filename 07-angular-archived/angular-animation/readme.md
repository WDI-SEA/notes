#Animations with ngAnimate

##Objectives

* Use the ngAnimate module to add animations to an application.
* Describe the properties that ngAnimate adds to directives.

##Getting started

Angular supports animations on enter, leave, and move. This is achieved by loading the ngAnimate module, which will automatically add the ng-enter/ng-leave/ng-move classes to your object when it is added/removed.

Animations are only attached to elements that have the following directives:

| Directive       | Supported Animations                                                       |
|-----------------|----------------------------------------------------------------------------|
| ngRepeat        | enter, leave and move                                                      |
| ngView          | enter and leave                                                            |
| ngInclude       | enter and leave                                                            |
| ngSwitch        | enter and leave                                                            |
| ngIf            | enter and leave                                                            |
| ngClass         | add and remove (the CSS class(es) present)                                 |
| ngShow & ngHide | add and remove (the ng-hide class value)                                   |
| form & ngModel  | add and remove (dirty, pristine, valid, invalid & all other validations)   |
| ngMessages      | add and remove (ng-active & ng-inactive)                                   |
| ngMessage       | enter and leave                                                            |

Read the [ngAnimate Documentation](https://docs.angularjs.org/api/ngAnimate)

Load `angular-animate.js` using a `<script>` tag. Place this in the `<head></head>` tags.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.5.0/angular-animate.js"></script>
```

Inject the `ngAnimate` dependency into your module.

```javascript
var app = angular.module('AnimationsApp', ['ngAnimate']);
```

##Defining an animation class

To add an animation to an item simply add a class to that item and define a css animation that requires the item to have both your custom class and ng-enter/ng-leave/ng-move. There are also two additional classes with the `-active` postfix that you'll need to define, to represent the final state of the animation.

```css
.myclass.ng-enter, .myclass.ng-move {
  //animation here
}

.myclass.ng-leave {
  //animation here
}

.myclass.ng-enter.ng-enter-active,
.myclass.ng-move.ng-move-active {
  //final animation state
}

.myclass.ng-leave.ng-leave-active {
  //final animation state
}
```

Documentation can be found [here](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Using_CSS_transitions).

### Examples

Here's an example of a div that has the ng-if directive. The div will only appear if `$scope.bool` is `true`.
This div has the class `fade` so it will fade in and out as the ng-if directive adds and removes the div
from the page.

```html
<div ng-if="bool" class="fade">
   Fade me in out
</div>
<button ng-click="bool=true">Fade In!</button>
<button ng-click="bool=false">Fade Out!</button>
```

```css
/* The starting CSS styles for the enter animation */
.fade.ng-enter {
    transition:0.5s linear all;
      opacity:0;
}

/* The finishing CSS styles for the enter animation */
.fade.ng-enter.ng-enter-active {
    opacity:1;
}

/* now the element will fade out before it is removed from the DOM */
.fade.ng-leave {
    transition:0.5s linear all;
      opacity:1;
}
.fade.ng-leave.ng-leave-active {
    opacity:0;
}
```

We can also use animation libraries, such as [animate.css](https://daneden.github.io/animate.css/). Add the CDN link.

```html
<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/3.4.0/animate.min.css">
```

Then add these animations via the `animate` CSS property. Note that we're using `ng-hide` and `ng-hide-remove` for the `ng-show` directive. These are the animation directives associated with this particular directive.

```css
.container.ng-hide-remove {
  animation: bounceIn 1s;
  opacity: 0;
}

.container.ng-hide {
  animation: bounceOut 1s;
  opacity: 1;
}

.container.ng-hide-remove.ng-hide-remove-active {
  opacity: 1;
}

.container.ng-hide.ng-hide-active {
  opacity: 0;
}
```

These CSS-Tricks articles are also great resources when playing with transitions and animations.
* [CSS Transitions](https://css-tricks.com/almanac/properties/t/transition/)
* [CSS Animations (uses keyframes)](https://css-tricks.com/almanac/properties/a/animation/)

**Note:** Animation classes will only be added to items as they are manipulated using supported directives, like ng-repeat, ng-show, ng-hide, ng-if, etc...

## But what about JavaScript?

We can define JavaScript animations as well, similar to how we implemented custom filters.

```js
app.animation('.myclass', [function() {
	return {
		enter: function(element, doneFn) {
			// code goes here, then callback
			doneFn();
		},
		leave: function(element, doneFn) {
			// code goes here, then callback
			doneFn();
		}
	}
}]);
```

This block of code attaches an animation to a class and returns an object with the animations we want to run on enter and leave.

For simplicity, we can use jQuery for animations (this isn't *too* terrible, since we're strictly using jQuery for its animation capabilities). There's also other alternatives for JavaScript animations, like [Velocity.js](http://julian.com/research/velocity/).

