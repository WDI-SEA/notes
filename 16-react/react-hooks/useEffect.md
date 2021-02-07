# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) useEffect Hook

### Learning Objectives

*After this code-along section, you will be able to:*

* Use the `useEffect` hook to handle post-render effects

## The `useEffect` hook

What is an *effect*? React uses this term to refer to "side effects" which is more or less anything outside the normal rendering process. Some common examples include fetching data from an API or other network requests, manually manipulating the DOM, or writing to log files. Previously, these kinds of actions were handled by the various component lifecycle methods so it is accurate to think of `useEffect` as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount` combined. That's a big change in the way we think about React components but, as you will see, it makes things easier and organizes our code in better ways.

### The problems with Lifecycle Methods

In React's short time in use, lifecycle methods have become a focal point for problems and pitfalls when troubleshooting components. Originally there were several more methods available in the API but these were soon marked dangerous and were later deprecated. Now there are only three or four commonly used lifecycle methods, but they still lead to confusion when thinking about React. Here are some of the issues:

* Related code needs to be split over multiple methods. For example, if you start an interval upon mounting, you must clear it on unmounting. Or code that must be run on every update including the initial render also needs to be in two different functions.
* `componentDidMount` and `componentDidUpdate` block browser updates. They are synchronous actions and must be completed before the browser can update the screen.
* One given lifecycle method can contain code from several unrelated operations leading to further breakdown in logical organization.

Hooks aims to solve these problems by providing a functional approach to side effects. The reasoning is simplified, the code is asynchronous, and related blocks are kept together.

## Using `useEffect`

There are two types of effects:

1. Those not requiring any cleanup like an API call or DOM manipulation.
2. Those requiring cleanup like an interval or a subscription.

### Effects Without Cleanup

Effects without cleanup are the ones we've used most in this course. The most common "effect" we run is the fetching of data from an external API when the component mounts. But we could also do something like change the title of the document, something that is inside the DOM but not really within the scope of any component render.

Let's take a look at how we might write an effect to change the document title. We need to import the `useEffect` function so we'll add that to our existing import line. Then, effects go inside your functional component generally after any state hooks you have:

```js
import React, { useEffect, useState } from 'react'

function App() {
  const [count, setCount] = useState(1)
  const [user, setUser] = useState({name: 'Taylor'})

  const increaseCount = () => {
    setCount(count+1)
  }

  useEffect(() => {
    document.title = `Hello, ${user.name}!`
  })

  return (
    <>
      <h1>The count is: {count}</h1>
      <button onClick={increaseCount}>Click Me</button>
      <h2>The user is: {user.name}</h2>
    </>
  )
}

export default App;
```

As you see, we call `useEffect()` and pass in a function to run. This function is our effect and it will run after every render. By using it inside the component, we have full access to our state variables as well and can use them freely.

Just as each render has its own props and state, a render has it own effects as well. Instead of thinking of all the stages in the component lifecycle, just think about an effect as happening *after* one given render. We will get into cleaning up an effect (what would normally be done during `componentWillUnmount`) later.

### Effects With Dependencies

The effect above is very simple and can safely run every time we render a component. However, an API request is often something that we *cannot* do potentially multiple times per second. You definitely do not want to trigger an infinite rendering loop that calls an API that you are paying for! To avoid this, we can give our effects dependencies that will prevent them from running unless a dependency has changed.

Say we have an app that views a user's repos in Github. We will store that user in state and then fetch the user's repo list using axios:

```js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Repos() {
  const [user, setUser] = useState({})
  const [repos, setRepos] = useState([])

  // runs on every render
  useEffect(() => {
    axios.get(`/api/${user.githubId}/repos`)
      .then((res) => {
        setRepos(res.data)
      })
  }, [user])

  return (
    <p>Yada yada yada</p>
  )
}
```
Nothing shocking inside the `useEffect` function but we are passing in an additional argument after the function: `[user]`. This is our dependency list and in it we are referencing our state variable `user`. This means that the effect will rely on changes in `user` to know when to run or not.

Let's add an example to our App! We're going to display a pokemon from the [PokeAPI](https://pokeapi.co/) - specifically the pokemon whose id corresponds to the current count:

* install and import `axios`
```js
import axios from 'axios'
```
* add a `pokeImg` state that initializes to `null`
```js
  const [pokeImg, setPokeImg] = useState(null)
```
* add a second `useEffect` hook that depends on `count`
```js
  useEffect(()=>{
      // get picture url from api
      // store picture url in state
  }, [count])
```
* use axios to get the information from the API about the pokemon whose id matches count, and save that poke's `front_default` sprite to state
```js
  // runs on first render, and every render after that IF
  // count has changed
  useEffect(()=>{
    axios.get(`https://pokeapi.co/api/v2/pokemon/${count}`)
    .then(response=>{
      setPokeImg(response.data.sprites.front_default)
    })
    .catch(err=>{
      console.log(err)
    })
  }, [count])
```
* render the current poke to the JSX
```js
    <>
      <h1>The count is: {count}</h1>
      <button onClick={increaseCount}>Click Me</button>
      <h2>The user is: {user.name}</h2>
      <img src={pokeImg} alt="poke"/>
    </>
```

Test it! It will always run once when it mounts but will then watch any dependencies in that list on subsequent renders. If it finds that any of them have changed from the last render, it will run the effect. Otherwise, it skips it, saving us time and resources.

Now put a console log inside both of the `useEffect` hooks and see when they fire to get familiar with the difference between these two formats. Notice how the first `useEffect` is firing twice each time the `count` button is clicked - why is that? *(Hint: how many states are being set when count increments?)*
```js
  // runs on every render
  useEffect(() => {
    console.log('useEffect 1 running')
    document.title = `Hello, ${user.name}!`
    console.log('useEffect 1 running')
  })

  // runs on first render, and every render after that IF
  // count has changed
  useEffect(()=>{
    console.log('useEffect 2 running')
    axios.get(`https://pokeapi.co/api/v2/pokemon/${count}`)
    .then(response=>{
      setPokeImg(response.data.sprites.front_default)
    })
    .catch(err=>{
      console.log(err)
    })
  }, [count])
```
Now let's do another experiment. We'll disconnect `pokeImg` and `count` by adding a `pokeId` state that starts at 1, and a button in the JSX that increments this state each time it is clicked:

```js
  const [pokeId, setPokeId] = useState(1)

  ...

  const nextPoke = () => {
    setPokeImg(poke+1)
  }

  <button onClick={nextPoke}>Next Poke</button>
```
Now change the axios call to run based on `pokeId` instead of `count`:

```js
  useEffect(()=>{
    console.log('useEffect 2 running')
    axios.get(`https://pokeapi.co/api/v2/pokemon/${pokeId}`)
    .then(response=>{
      setPokeImg(response.data.sprites.front_default)
    })
    .catch(err=>{
      console.log(err)
    })
  }, [pokeId])
```

Test it by clicking the 'click me' button that increments count. Notice how the second useEffect *doesn't run anymore* when we increment count. That's because we have that second argument that says *"please only run this if there is a change in pokeId"*!
But that first useEffect is *still* running, even though we really don't need it to because it simply changes the title of the document. This leads us to the question, "What if I don't want it to run past the first time? What if we want it to act like `componentDidMount`?" To achieve that, we simply use an empty dependency list:

```js
  useEffect(() => {
    console.log('useEffect 1 running')
    document.title = `Hello, ${user.name}!`
  }, [])
```

Notice how we are still using the second argument but we have nothing in the array. This will cause it to run once at mounting and then never again. Since it has no dependencies, it will never detect a change and will never run more than the first time.

---

### Effects With Cleanup

In the older lifecycle method paradigm, whenever we started an asynchronous operation in `componentDidMount` we would need to stop it or clean up after ourselves inside `componentWillUnmount`. This splitting up of logic into different functions leads to code that becomes more difficult to maintain as it grows and is one of the main problems that hooks were intended to solve. The `useEffect` hook gives us an incredibly simple way to deal with this: we return a function from our effect that does our clean-up.

```js
import React, { useState, useEffect } from 'react';

function IntervalTicker() {
  const [handle, setHandle] = useState(null)
  
  useEffect(() => {
    // This line starts an interval and stores the returned handle in state
    setHandle( setInterval(() => console.log('tick'), 1000) )
    // This line returns a function that clears the interval
    return () => {
      clearInterval(handle)
    }
  }, []) // Don't forget the empty dependency list

  return (
    <p>Yada yada yada</p>
  )
}
```

Our cleanup for our interval involves clearing that interval by using the handle in the `clearInterval` function. All we need to do to make this cleanup happen is to *return a function that does that* from our effect. This can be any sort of function, named or anonymous, and it just needs to do the cleanup steps. By returning that function from our effect, we are telling React that this function should be run when this component is unmounted. React will take care of the rest! We do, however, need to remember to pass in an empty dependency list so that we don't start a new interval on literally every render.

## What other Hooks are there?

Here are some of the more popular ones:

* `useContext` - Allows use of the Context API, useful for decoupling state from components
* `useReducer` - Used for more complex state manipulations. Works very similarly to Redux.
* `useRef` - Allows for the use of refs to DOM objects
* `useLayoutEffect` - A synchronous version of useEffect used for reading layout metrics and then re-rendering based on those.

There are a few more and more are being added all the time. You can also create your own custom hooks yourself using `useEffect`!

## Conclusion

Hooks represent an improvement in React code organization and reasonability. You don't have to use them since class-based components still exist and work but Facebook is recommending that you try them out since they lend themselves to a better development experience.

## Additional Resources

* [Hooks Documentation](https://reactjs.org/docs/hooks-intro.html)
* [A Complete Guide to useEffect](https://overreacted.io/a-complete-guide-to-useeffect/)
* [Fetching Data with React and Hooks](https://www.robinwieruch.de/react-hooks-fetch-data)
