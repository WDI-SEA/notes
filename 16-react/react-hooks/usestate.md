# useState

### Learning Objectives

_After this code-along section, you will be able to:_

* Use the `useState` hook to access and set state

### Getting started:

* Create a new react app called `hooks-practice`
* Leave the default `App` component as a function
* Remove all the default JSX and of `App` \(we will add some back in soon\)

## The `useState` hook

Lets begin by watching [Dan Abramov's](https://youtu.be/dpw9EHDh2bM?t=1062) introduction to the `useState` hook at ReactConf 2018 (Watch until the 28 min mark) Dan is the one the creators of React hooks, along with create-react-app, and React Redux.

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

Add the following JSX to the return and run `npm start` to see the initial value of count:

```jsx
<h1>The count is: {count}</h1>
```

### Multiple state values

If we decide that we want another piece of state, we can simply add another `useState` line for the new variable:

```jsx
const [count, setCount] = useState(1);
const [user, setUser] = useState({name: 'Taylor'});
```

This will return another variable for holding the piece of state and another setter function. As before, we can choose the name of our state variable \(`user`\) and then declare a `setUser` identifier to receive the setter function returned from `useState`.

Add the following JSX to your component to see this second state rendered:

```jsx
<h2>The user is: {user.name}</h2>
```

This approach of using a different state line for each variable is a preferred approach. The only time we might want to take a different approach is if our state values were always updated together at the same time. If this is the case, perhaps it makes more sense to combine the state variables into a single, more complex object that we can update with a single function call instead of two. Use your best judgement.

### Setting state

To give it a new value, we can call the setter function that React gave us:

```jsx
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

## Adding a Controlled Form

Lets increase the complexity of this example to illustrate more about the differences between `this.setState` and `useState` by adding a controlled from.

Update your user state object to also include the user's favorite food as a key/value pair:

```jsx
  const [user, setUser] = useState({ 
    name: 'Taylor',
    favFood: '🍕'
  })
```

And update the jsx in your component's return to render the user's favorite food:

```jsx
<h2>The user is: {user.name}, and their favorite food is {user.favFood}</h2>
```

Now, lets add a form that allows us to update hte `user.name` and `user.favFood` in state:

```jsx

<form>
	<label for="name">user name:</label>

	<input
	  id="name" 
	  type="text"
	  placeholder="name..."
	  // we don't need to write an onChange event handler, we can just define an arrow function inline to handle the user's input
	  onChange={e => setUser({ name: e.target.value})}
	/>

	<label for="fav-food">Fav Food:</label>

	<input
	  id="fav-food" 
	  type="text"
	  placeholder="food..."
	  onChange={e => setUser({ favFood: e.target.value})}
	/>
</form>
```

But wait! There is a bug! If you type in an input, the other value disappears! What is happening here?

This bug illustrates one the the fundamental differences between `useState` and `this.setState` -- that being `this.setState` merges the object you pass it in with current state, however `useState` does not. Instead, `useState` overwrites the value, and if we want to merge it with the previous state value, it is up to us to do so.

In order to do that, we need to update our `onChange` handlers:

```jsx
...
// update the user input, here we are spreading all of the values that live in our user state, before updating the value that corresponds to this input
onChange={e => setUser({ ...user, name: e.target.value})}
...
// update the favFood input in the same way
onChange={e => setUser({ ...user, favFood: e.target.value})}
...
```

Et voilà! It works as expected.

