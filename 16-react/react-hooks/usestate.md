# useState

### Learning Objectives

_After this code-along section, you will be able to:_

* Use the `useState` hook to access and set state

### Getting started:

* Create a new react app called `hooks-practice`
* Leave the default `App` component as a function
* Remove all the default JSX and of `App` \(we will add some back in soon\)

## The `useState` hook

The first hook we will learn is the one that allows us to add state to a component. It is called `useState` and it gives us the ability to declare initial state, update it, and access it all from a function-based component.

We can import this hook from the react node module by modifying our standard React import line:

```javascript
import React, { useState } from 'react';
```

Now, the way we use this is different than how we used state in a class-based component. Let's say, for example, that we want to store a simple integer counter in state. This is how we create that variable and the corresponding setter function. This line goes inside the body of our function component:

```javascript
const [count, setCount] = useState(1);
```

Let's examine this line. The `useState()` function returns two items for us: a named variable which will hold our state value and a function for setting its value. We are free to choose the name of the variable \(in this case, `count`\) but the setter function must be named `setName` where `Name` is what you chose for the variable name, respecting camelCase. These are unpacked using array destructuring into two identifiers. The value passed into useState\(\) is the initial value of the variable. You can imagine the above code to be equivalent to the following:

```javascript
state = {
  count: 1
}

setCount = (newCount) => {
  this.setState({
    count: newCount
  })
}
```

### Using state

Now here are the cool things: the variable holding the value is accessible simply by using its name! You do not need to type out `this.state.count` every time you want to get at the value. Also, the `setCount()` function that it makes for you is always bound to this component. There is no need to bind the method or use arrow functions - it will always work just like this!

Add the following JSX to the return and run `npm start` to see the inital value of count:

```javascript
<h1>The count is: {count}</h1>
```

### Multiple state values

If we decide that we want another piece of state, we can simply add another `useState` line for the new variable:

```javascript
const [count, setCount] = useState(1);
const [user, setUser] = useState({name: 'Taylor'});
```

This will return another variable for holding the piece of state and another setter function. As before, we can choose the name of our state variable \(`user`\) and then declare a `setUser` identifier to receive the setter function returned from `useState`.

Add the following JSX to your component to see this second state rendered:

```javascript
<h2>The user is: {user.name}</h2>
```

This approach of using a different state line for each variable is a preferred approach. The only time we might want to take a different approach is if our state values were always updated together at the same time. If this is the case, perhaps it makes more sense to combine the state variables into a single, more complex object that we can update with a single function call instead of two. Use your best judgement.

### Setting state

To give it a new value, we can call the setter function that React gave us:

```javascript
function App() {
  const [count, setCount] = useState(1)
  const [user, setUser] = useState({name: 'Taylor'})

  const increaseCount = () => {
    setCount(count+1)
  }

  return (
    <>
      <h1>The count is: {count}</h1>
      <button onClick={increaseCount}>Click Me</button>
      <h2>The user is: {user.name}</h2>
    </>
  )
}
```

**Note:** It is important to realize, when using hooks, that a value in state will have _only that value_ for the total duration of that render cycle. Lifecycle methods could change this behavior but you can rely on a value in state if using hooks. But make sure you notice that when we declare the state variable and setter, we are making them constants which means that nothing can reassign to our state variable. This constant-ness lasts until the next render when React replaces the value.

