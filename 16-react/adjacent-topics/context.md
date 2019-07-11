# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Context API

### Learning Objectives
*After this lesson, you will be able to:*
- Define Context and distinguish a `Context.Provider` from a `Context.Consumer`
- Use the React Context API to pass data and functions across the Component Tree
- Identify appropriate use cases for React Context

## What is Context in React

From the [React Docs](https://reactjs.org/docs/context.html):
>Context provides a way to pass data through the component tree without having to pass props down manually at every level.

In short, the Context API gives as a method to work around prop-drilling in certain situations.

We have learned that React has a uni-directonal flow of data, only passing data or functions from parent to child via props. Using `Context` allows us to use data or functions that we would consider _global_ within our Component tree without passing them through each level of a branch.


A `Context` is composed of three parts: the definition, the Provider and the Consumer. Aptly named, the Provider will provide access to the data that we want to make available, and the Consumer will be used where we want to use the data provided. 

You may have already been using Context whether you knew it or not. React Router is an example of the Context API in use! Behind the scenes, React Router has created a Context that includes `location`, `history`, `match` and helper functions to deal with navigation. It grants access via the`<BrowserRouter />` and `<Link />` components.
```js
/* App.js */
<BrowserRouter> // Context Provider
  <Router exact path='/' component={Home} />
  <Router ... />   
  <Router ... />  
</BrowserRouter>


/* NavComponent.jsx */
<Link to='/'>Home</Link> // Context Consumers 
<Link to='/issues'>Issues</Link>
<Link to='/pullrequests'>Pull Requests</Link>
```
## Appropriate Use Cases
- Authenticated User Data
- Theming
- Localization data

>Context is primarily used when some data needs to be accessible by many components at different nesting levels. Apply it sparingly because it makes component reuse more difficult.

___
## Using Context

### Create a Context
Touch a new file in `src` to house your Context code. You can define and export data and function stubs to be used by Context. When creating your context make sure that the shape of your Context data matches what you will use be using in your Context Providers and Consumers

```js
// ColorContext.js
import React from 'react';

// global array of colors that we will use
export const colors = ['black', 'blue', 'green', 'rebeccapurple', 'red', 'whitesmoke'];

//make sure that the Context matches the signature that your Consumer will expect later
export const ColorContext = React.createContext({
  color: '',
  changeColor: () => {} // emtpy function <= we will apply a function to in our Provider
});
```

### Context Providers

Import the Context (and any data) into the Component that you intend to provide data from.

```js
/* App.js */
...
import { ColorContext, colors } from './ColorContext';
...
```
Wrap the portion of your Component tree in which you intend to use the data with a Context Provider and pass the data to it as a `value` prop.

```js
class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      color: colors[0],
      changeColor: this.changeColor // wait, whattttt?! methods in state?! you better believe it
    }
  }

  changeColor = () => {
    // color change logic goes here
  }

  render() {
    return(
      <ColorContext.Provider value={this.state}>
        {/* Child Components */}
      </ColorContext.Provider>
    )
  }
}
```

### Context Consumers
Within the child component where data should be displayed, import the Context and wrap the portion of the component with a `Context.Consumer`. Your context data will be accessible through an anonymous function.

### Accessing Context in Function Components
```js
/* ColorPane.jsx */
export function ColorPane(props) {
  return(
    <ColorContext.Consumer>
      { // open a block
        ({color}) => { // Anonymous function with destructuring syntax to access `color` from the Context
          let style = {
            background: color, // this is our Context color!
            height: "200px", 
            width: "200px"
          }
          return (
            <div style={style}></div>
          )
        }
      }
    </ColorContext.Consumer>
  )
}
```
```js
/* ColorButton.jsx */
export function Colorbutton(props) {
  return(
    {
      ({changeColor}) => <button onClick={changeColor}>CHANGE THE COLOR</button> // yup, just like that
    }
  )
}

```
### Accessing Context in Class Components
Class Components offer another method of accessing Context data by assigning a context to the `Component.contextType` property. This method only works when access to a single Context is required.
```js
import React from 'react';
import { ColorContext } from './ColorContext'

class ColorPane extends React.Component {
  render() {
    let style = {
      background: this.context.color, // We can access data in the this.context object
      height: "200px", 
      width: "200px"
    }

    return (
      <div style={style}></div>
    )
  }
}

ColorPane.contextType = ColorContext; // Assign context after class is defined

export default ColorPane;
```

### Accessing Multiple Contexts
You can use data from multiple Contexts in the following manner
```js
...
<ColorContext.Consumer>
  { ({color}) => (
      <UserContext.Consumer>
      { user => (
          <MyComponent user={user} themeColor={color} />
        ) 
      }
      </UserContext.Consumer>
    )
  }
</ColorContext.Consumer>

...

```

### Note on Hooks

The [new Hooks API*](https://reactjs.org/docs/hooks-reference.html#usecontext) has provided a `useContext` hook to allow access to your Contexts within function components.

___
## Alternatives to Context
- [Component Composition Patterns](https://reactjs.org/docs/composition-vs-inheritance.html)

Containment
```js
// ParentContainer.jsx
export const ParentContainer = props => {
  return(
    <div>
      {props.children}
    </div>
  )
}


// App.jsx 
...
render() {
  return(
    <ParentContainer some={someProps}> 
        <ChildComponent diffe={rentProps} /> 
        <AnotherChild someOth={erProps} /> 
    </ParentContainer>`
  )
}
...
 ```
Passed 
```js
//Parent.jsx
import React from 'react';
import { ChildOne } from './ChildOne'

export function Parent(props) {
  return (
    <ChildOne {...props} />
  )
}

// ChildOne.jsx
import React from 'react';

export function ChildOne(props) {
  return (
    <div>
      {props.usedDownTheTree}
    </div>
    )
}

// UsedDownTheTree.jsx
import React from 'react';

export function UsedDownTheTree(props) {
  return(
    <>
      <h1>Hello, {props.name ? props.name : 'World!'}</h1>
      <h3>{props.message ? props.message : '' }</h3>
    </>
  )
}

//App.js
import React, { Component } from 'react';
import {Parent} from './Parent'
import {UsedDownTheTree} from './UsedDownTheTree';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      user: 'GLaDOS',
      message: "I don't like lemonade"
    }
  }


  render() {
    let usedDownTheTree = <UsedDownTheTree name={this.state.user} message={this.state.message}/>
    return (
      <div className="App">
          <Parent usedDownTheTree={usedDownTheTree}/>
      </div>
    );
  }
}

export default App;


```

## Extra Resources

* Redux - [Docs](https://redux.js.org/basics/usage-with-react)
* [Hackernoon - how to use Context API](https://hackernoon.com/how-do-i-use-react-context-3eeb879169a2)
