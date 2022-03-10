# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) React State: Mood Points

## Learning Objectives

_By the end of this lesson, you will be able to:_

* Define what state means in relation to React components.
* Differentiate between `this.state` and `this.props`.
* Create an initial state in a component.
* Change the state of a component.

## Let's Talk About Props!

In React, we are able to handle data in one of two ways:

* Props **represent** data that is **immutable**, or read-only. Let's see what happens when you try to directly change `this.props.name` in the `Hello` component.
* But, what about when we need data that is dynamic and changes? That's where React's state comes in!

## So Many Questions!

* What is state anyway?
* What's the difference between state and props?
* How do we access state?

### States

* Values stored in a component's state are **mutable**, or changeable, attributes.
* State may appear similar to props, but there are quite a few important differences.
* Like props, which we access through the `this.props` object, we can access state using `this.state`.
* As state has the ability to be changed, it is not quite as straightforward as props. However, once you get the hang of it, you'll be able to build really interactive apps!

> Try it yourself alongside [this video](https://generalassembly.wistia.com/medias/3ldc3tnyv0) in [this codepen](https://codepen.io/susir/pen/GWONLp).

![](https://github.com/WDI-SEA/notes/tree/5537c491fcc61eb363b9c34cc82a02076abf9fc7/16-react/react-state/images/moodtracker-directories.png)

## MoodTracker

* Use `npx create-react-app` to create a new `mood-tracker` app.
* Create a `MoodTracker` component and render it inside `App`.


```jsx
// ...
import MoodTracker from "./MoodTracker";

class App extends Component {
  render() {
    // ...
    return (
      <div className="App">
        ...
        <MoodTracker />
      </div>
    );
  }
}

export default App;
```

## Initial State

`constructor`

When working with values that are dynamic and changing, you should always provide an initial value for the changing pieces of data. In React, you can do this in the class constructor. Constructors say, "When you create an instance of a class, do this." Without explicitly defining a constructor, our components will use the default constructor inherited from the `Component` class. That's why we didn't need a constructor before — we weren't doing anything differently than the normal default for every component.

## Initial State

```javascript
import React, { Component } from 'react';

class MoodTracker extends Component {
  // What should happen when the component is first created?
  constructor() {
    // Make call to parent class' (Component) constructor.
    super();
    this.state = {
    // Your info here
    };
  }

  // What should the component render?
  render() {
  //  ....
  }
}

export default MoodTracker;
```

The first thing we always put in a constructor is a call to `super()`, which says, "You should still do the default initialization for this class."

Finally, we will add `this.state = {}`. This sets the initial values for our data, which are changeable. Like props, state is an object that belongs to the class.

React has undergone a *lot* of updates. One of them is a simplified notation for setting initial state. Now, instead of writing out the whole constructor, you can simply assign a new object to state, like so:

## React Components \(in React v16+\)

```javascript
import React, { Component } from 'react';

class MoodTracker extends Component {
  // What should the state be when the component is created?
  state = {
    // Your info here
  };

  // What should the component render?
  render() {
    //  ....
  }
}

export default MoodTracker;
```

Much cleaner, right? Throughout the course, we're going to use this newer way to define state, but you may run into the `constructor` syntax during your own research as this was the way it was done prior to the release of React version 16.

### Initialize a moodPoints state

Now that we've built the skeleton for our component, let's define our state's initial values. We can do this by giving a value to the `state` object. Inside of that object, we can define any variables we'd like.

We'll start our state with just one key-value pair. The key or label will be `moodPoints`, and the initial value for the `moodPoints` key will be `1`.

```javascript
class MoodTracker extends Component {
  // Define an initial state.
  state = {
    moodPoints: 1 // initialize this.state.moodPoints to be 1
  };

  // What should the component render?
  render() {
    //  ....
  }
}
```

## MoodTracker

Add some JSX to your `MoodTracker` component so it displays the `moodPoints` state!

```javascript
return (
  <div>
    <p>On a scale of 1-10</p>
    <p>You are this happy: {this.state.moodPoints}</p>
  </div>
)
```

Note how similar this looks to using props. All React components include both `this.props` and `this.state`. All together, the code inside `render()` for our `MoodTracker.js` can now look as seen here:

```javascript
    // What should the component render?
    render() {
        return (
            <div>
            <p>On a scale of 1-10</p>
            <p>You are this happy: {this.state.moodPoints}</p>
            </div>
        )
    }
```

> Check it out! If you browse to `http://localhost:3000`, your state will be displayed.

## Changing State

#### Events in JavaScript

The whole point of **state** is to capture/represent states of the application. When would the state of an app change? Usually a change of state is how an app responds to a user interaction (or other browser event, like the arrival of data).

* Now that we have an initial value up on the page, let's learn how to change this value and make it more dynamic.
* Step 1 in this process is to trigger an **event** — when the user interacts with the page in any way.
* Think back to using regular JavaScript or jQuery. What is the purpose of an event listener? Can you show me how to create a click event in JavaScript?

## Synthetic Events

**Events** in React are not the same as the normal events we're used to!

From the [React Docs](https://reactjs.org/docs/events.html):

_Your event handlers will be passed instances of SyntheticEvent, a cross-browser wrapper around the browser’s native event. It has the same interface as the browser’s native event, including `stopPropagation()` and `preventDefault()`, except the events work identically across all browsers._

Take a look at some of the other supported synthetic events!

* Event listeners in React look very similar to adding events through HTML attributes. There are two main differences when working with React's synthetic events:
* 1. React events are named using camelCase instead of lowercase:
     * `onClick` \(React\) vs. `onclick` \(HTML\)
     * `onSubmit` \(React\) vs. `onsubmit` \(HTML\)
* 1. In JSX, you pass the actual function in as the handler, rather than a string:
     * `<button onClick={this.doSomething}>Click Me</button>` \(React\)
     * `<button onclick="doSomething()">Click Me</button>` \(HTML\)

### Pause to research: Synthetic Events

Check out the [React documentation](https://reactjs.org/docs/events.html#supported-events) on supported events.

Think about the following:

1. What events could you see yourself using often?
2. What sort of events sound niche but interesting to play around with?

## Code-Along, Continued: Button to Increase Mood

We will create a button that the user can click, which will increase their mood by `1`.

### Helper Method

First, we need to define a helper method that we will call when the button is clicked. Unless you have a good reason **not** to, _**always**_ use arrow functions within Reach components (otherwise, you may end up with a binding issue that requires additional code to rememdy).

Helper functions go above the render method and below the state object.

```jsx
    // helper methods
    increaseMood = () => {
        console.log('Increasing mood!')
    };
```

### Trigger the Synthetic Event

Now we need to add a button to our JSX that calls the helper method when it is clicked:

```javascript
render () {
  return (
    <div>
      <p>You are this happy: {this.state.moodPoints}</p>
      <button onClick={this.increaseMood}>Cheer up!</button>
    </div>
  )
}
```

Why did we write `onClick={this.increaseMood}` rather than `onClick={this.increaseMood()}`?

> More details on [function calls versus function references](https://stackoverflow.com/questions/15886272/what-is-the-difference-between-a-function-call-and-function-reference).

**Test it!** See if you get the correct message in the console when you click the button.

### Actually Change State

Changing the value of `this.state` isn't quite as straightforward as something like `this.state.moodPoints++`. Instead, when we want to update a value in React, we will use a method called `this.setState()`. This method helps React update only certain parts of the DOM, resulting in a much faster website!

`this.setState` works in two ways, if you need access to the previous that values, it will accapt a callback as a argument, if you just need to set the state without the previous state, it accapts an object. In this case, we need to use a callback. When using the callback, you must return an object, and that object will be set to the new state

```javascript
// supplying a callback gives access to two values -- the previous state and the current props, you don't have to use both of them
this.setState((previousState, currentProps) => {
  return {
    ...
    new state values
    ...
  }
})

// OR 
// using an implicit return arrow function with a multiline expersssion return
this.setState((previousState, currentProps) => (
  ...
  new state values
  ...
))

// this is setting state withoud access to the previous state
this.setState({
  ...
  new state values
  ...
})
```

```javascript
increaseMood = () => {
  this.setState({
    moodPoints: this.state.moodPoints + 1
  });
};
```

## Mood Tracker

All together, your `MoodTracker.js` file now looks like this:

```javascript
import React, { Component } from 'react'
 
class MoodTracker extends Component {
    // Define an initial state.
    state = {
        moodPoints: 1 // initialize this.state.moodPoints to be 1
    };

    // helper methods
    increaseMood = () => {
        this.setState({
          moodPoints: this.state.moodPoints + 1
        });
    };

    // What should the component render?
    render() {
        return (
            <div>
                <p>On a scale of 1-10</p>
                <p>You are this happy: {this.state.moodPoints}</p>
                <button onClick={this.increaseMood}>Cheer up!</button>
            </div>
        )
    }
}

export default MoodTracker
```

> Check it out! If you browse to `http://localhost:3000`, your button now changes the state whenever it is clicked.

## Using React, **We Only Change the Parts of the DOM That Need to Be Changed**

Whenever we run `.setState`, our component calculates the difference, or "diff," between the current DOM and the virtual DOM node. Then, it figures out how to update the state of the DOM in as few manipulations as possible; it only replaces the current DOM with parts that have changed.

This is super important! Using React, **we only change parts of the DOM that need to be changed**. This has implications for performance.

We do not re-render the entire application like we have been doing so far. **This is one of React's core advantages.**

## Challenge: Count to 10

After 10 clicks, the user should see the counter reset to `1`.

> If you're interested in reading more in depth about this, here is more on what [should & shouldn't go in state](https://facebook.github.io/react/docs/state-and-lifecycle.html). This link is also in the Further Reading page at the end of this lesson.

```javascript
increaseMood = () => {
  let newMoodPoints; // Create new variable.
  if (this.state.moodPoints >= 10) {
    // Check to see if current state is greater than or equal to 10.
    newMoodPoints = 0; // If true, set MoodPoints to 0.
  } else {
    newMoodPoints = this.state.moodPoints + 1; // If false, increase MoodPOints by 1.
  }
  this.setState({
    moodPoints: newMoodPoints // Set state using new variable.
  });
};
```

## Challenge: Count to 10

Or, using ternaries:

```javascript
increaseMood = () => {
  let newMoodPoints = this.state.moodPoints >= 10 ? 0 : this.state.moodPoints + 1;
  this.setState({
    moodPoints: newMoodPoints
  });
};
```

## Resources

* [React State vs. Props](http://lucybain.com/blog/2016/react-state-vs-pros/)
* [Understanding State in React](https://thinkster.io/tutorials/understanding-react-state)
* [Understanding `this.setState`](https://medium.com/@baphemot/understanding-reactjs-setstate-a4640451865b)
* [Understanding `setState`](https://css-tricks.com/understanding-react-setstate/)
* [React State FAQs](https://reactjs.org/docs/faq-state.html)
* [What should & shouldn't go in state_](https://facebook.github.io/react/docs/state-and-lifecycle.html). 
