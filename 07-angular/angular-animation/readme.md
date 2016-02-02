![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Animations with ngAnimate

##Objectives

* Use the ngAnimate module to add animations to an application.
* Understand the properties that ngAnimate adds to directives.

##Getting started

Angular supports animations on enter, leave, and move. This is achieved by loading the ngAnimate module, which will automatically add the ng-enter/ng-leave/ng-move classes to your object when it is added/removed.

Read the [ngAnimate Documentation](https://docs.angularjs.org/api/ngAnimate)

Load `angular-animate.min.js` from the [AngularJS CDN](https://cdnjs.com/libraries/angular.js/1.4.8) using a `<script>` tag. Place this in the `<head></head>` tags.

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.8/angular-animate.js"></script>
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

### Examples

These are CSS transitions. Documentation can be found [here](https://developer.mozilla.org/en-US/docs/Web/Guide/CSS/Using_CSS_transitions).

```css
.item.ng-enter, .item.ng-move {
  transition: 0.5s linear all;
  opacity: 0;
}

.item.ng-leave {
  transition: 0.5s linear all;
  opacity: 1;
}

.item.ng-enter.ng-enter-active,
.item.ng-move.ng-move-active {
  opacity: 1;
}

.item.ng-leave.ng-leave-active {
  opacity: 0;
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

