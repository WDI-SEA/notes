## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) React State


### Learning Objectives
*After this code-along section, you will be able to:*
* Define what state means in relation to React components.
* Differentiate between `this.state` and `this.props`.
* Create an initial state in a component
* Change the state of a component

## Intro

At this point, we know about React properties and how they relate to our component's data.

* The thing is, `props` represent data that will be the same every time our component is rendered. What about data in our application that may change depending on user action?
* That's where `state` comes in.

What's state?
> Try it yourself alongside [this video](https://generalassembly.wistia.com/medias/3ldc3tnyv0) in [this codepen](https://codepen.io/susir/pen/GWONLp).

Values stored in a component's `state` are mutable attributes.
* `State` is similar to `props`, but *is meant to be changed*.
* Like props, which we access with `this.props.val`, we can access state values using `this.state.val`
* Setting up and modifying `state` is not as straightforward as working with props. Instead, it requires multiple methods - explicitly declaring the mutation and then defining methods to define how to update our state.

Let's switch gears back to our `hello_world` project.

> Be sure to switch which app is running locally!

Let's modify our earlier Hello World example to include a new `MoodTracker` component. There will be a mood displayed, and eventually a user will click a button to indicate on a scale of 1-10 how much of that mood they are feeling.

### Initial State (Old School Way)

First, now that we're going to have a state, we're going to have an initial value. When working with classes, a good way to make initial values is by creating a constructor: `constructor (props) {}`. Constructors say, "When you create an instance of this class, do this." Without a constructor explicitly defined by us, our components will use the default constructor inherited from the `Component` class. That's why we didn't need a constructor before - we weren't doing anything differently than the normal default for every component.


```js
class Hello extends Component {
  // what should happen when the component is first created
  constructor (props) {
  }

  // what should the component render
  render () {
    //  ....
  }
}
```

The first thing we always put in a constructor is a call to `super()`, which says "You should still do the default initialization for this class."

```js
class Hello extends Component {
  // what should happen when the component is first created
  constructor (props) {
    // make call to parent class' (Component) constructor
    super()
  }

  // what should the component render
  render () {
    //  ....
  }
}
```

After this, we can define what's new. What's new for us right now is that when the class first gets called, we want to set an initial state. We can do this by giving a value to `this.state`, the component's special state object. Inside of that object, we can define any state variables we'd like.

We'll start our state with just one key-value pair inside.  The key or label will be `moodPoints`, and the initial value for the `moodPoints` key will be 1.

At the top of the `Hello` class in your `src/App.js` file, add the `constructor` function.

```js
class Hello extends Component {
  // what should happen when the component is first created
  constructor (props) {
    // make call to parent class' (Component) constructor
    super()
    // define an initial state
    this.state = {
      moodPoints: 1 // initialize this.state.moodPoints to be 1
    }
  }

  // what should the component render
  render () {
    //  ....
  }
}
```

### State Initialization in React v16+

```js
import React, { Component } from 'react';

class MoodTracker extends Component {
  // What should the state be when the component is created?
  state = {
    // Your info here
  };
  
  // What should the component render?
  render() {
    // ...
  }
}

export default MoodTracker;
```

Even though you may see the `constructor` syntax used in some online resources, the best practices for how to write the initial state for components has changed in recent years. Instead, we can create a component and directly define the starting state without ever having to use a constructor as of React 16.

Much cleaner, right? Throughout the course, we're going to use this newer way to define state, but you may run into the constructor syntax during your own research as this was the way it was done prior to the release of React version 16.

### Displaying State

Now let's make sure we display that information to the user. Still in `App.js`, in your `render` method, we'll let the user know how many mood points they are at by adding in a line:

```html
// note how similar this looks to accessing props
<p>You are this happy: {this.state.moodPoints}</p>
```

All together, the code inside `render` for our `App.js` can now look like this:

```html
return (
  <div>
    <h1>Hello {this.props.name}!</h1>
    <p>You are {this.props.age} years old.</p>
    <p>You love: {this.props.animals[0]}</p>
    <p>On a scale of 1-10</p>
    <p>You are this happy: {this.state.moodPoints}</p>
  </div>
)
```

> Check it out! If you browse to http://localhost:3000, your state will be displayed.


### Changing State

Ok, we set an initial state. But how do we go about changing it?

Changing the value of `this.state` isn't quite as straightforward as something like `this.state.moodPoints++`. Instead, when we want to update a value in React, we will use a method called `this.setState()`. This method helps React update only certain parts of the DOM, resulting in a much faster website!

First, we will create a method to increase the mood.  Under the `Hello` constructor, above the `render` method, add this method:

```js
increaseMood = () => {
  this.setState({
    moodPoints: this.state.moodPoints + 1
  })
}
```

Note that we call `this.setState` to change the state.

Now we'll create the button to trigger calling this function. The button will be displayed to the user, so we'll add it to the `render` function. When the user clicks it, we'll call the `increaseMood` function.

```js
  render () {
    // remember: can only return one top-level element

    return (
      <div>
        <h1>Hello {this.props.name}</h1>
        <p>You are {this.props.age} years old</p>
        <p>On a scale of 1-10</p>
        <p>You are this happy: {this.state.moodPoints}</p>
        <button onClick={this.increaseMood}>Cheer up!</button>
      </div>
    )
  }
}
```

### Synthetic Events

**Events** in React are not the same as the normal events we're used to!

From the [React Docs](https://reactjs.org/docs/events.html):

*Your event handlers will be passed instances of SyntheticEvent, a cross-browser wrapper around the browser’s native event. It has the same interface as the browser’s native event, including `stopPropagation()` and `preventDefault()`, except the events work identically across all browsers.*

Take a look at some of the other supported synthetic events!

**Event listeners** in React look very similar to adding events through HTML attributes. There are two main differences when working with React's synthetic events:

- React events are named using camelCase instead of lowercase:
-- onClick (React) vs. onclick (HTML)
-- onSubmit (React) vs. onsubmit (HTML)
- In JSX, you pass the actual function in as the handler, rather than a string:
-- <button onClick={this.doSomething}>Click Me</button> (React)
-- <button onclick="doSomething()">Click Me</button> (HTML)

Altogether, your `App.js` file now looks like this:

```js
// bring in React and Component from React

import React, {Component} from 'react';

// define our Hello component
class Hello extends Component {

  constructor (props) {

    // make call to parent class' (Component) constructor
    super()
    // define an initial state
    this.state = {
      moodPoints: 1 // initialize this.state.counter to be 0
    }
  }

  // increase moodPoints by 1 in this.state
  increaseMood(e) {
    this.setState({
      moodPoints: this.state.moodPoints + 1
    })
  }

  // what should the component render
  render () {
    // make sure to return some UI

    return (
      <div>
        <h1>Hello {this.props.name}</h1>
        <p>You are {this.props.age} years old</p>
        <p>You love {this.props.animals[0]}</p>
        <p>On a scale of 1-10</p>
        <p>You are this happy: {this.state.moodPoints}</p>
        <button onClick={(e) => this.increaseMood(e)}>Cheer up!</button>
      </div>
    )
  }
}

export default Hello
```

> Check it out! If you browse to http://localhost:3000, your button now changes the state.

Whenever we run `.setState`, our component calculates the difference or "diff" between the current DOM and the virtual DOM node. Then, it figures out how to update the state of the DOM in as few manipulations as possible; it only replaces the current DOM with parts that have changed.

This is super important! Using React, **we only change parts of the DOM that need to be changed.**

* This has implications for performance.
* We do not re-render the entire component like we have been so far.
* This is one of React's core advantages.


#### Challenge: Count to 10

After 10 clicks, the user should see the counter reset to 1.

*If you're interested in reading more in depth about this, here is more on what [should & shouldn't go in state](https://facebook.github.io/react/docs/state-and-lifecycle.html). This link is also in the Further Reading page at the end of the React module.*
