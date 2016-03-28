#Your First React Component

##Setup our Workflow

http://codepen.io/bhague1281/pen/JXEaeK

In order to make our workflow smoother, we'll be using a starter template in Codepen, which provides React and an in-browser JSX/Babel compiler. Note that we'll only be creating a front end application with React.

Also note that the setup we have provided is for demonstration and hobby uses only. The setup contains a JSX/Babel compiler as well as jQuery. Note that jQuery is not necessary for React to work, and JSX/Babel compiling should not be done in the browser on production sites. We will address using front-end build tools later on.

Make sure to fork the starter template, then write the following component:

```js
//creating a basic component with no data, just a render function
const MyApp = React.createClass({
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
      </div>
    );
  }
});

//insert the component into the DOM
ReactDOM.render(<MyApp />, document.getElementById('container'));
```

**Side note:** You may notice when going into Codepen's debug mode that a message may appear when the app is first loaded:

```
Download the React DevTools for a better development experience: https://fb.me/react-devtools
```

It's highly recommended that you download the React DevTools. It'll make debugging components **much** easier. https://fb.me/react-devtools

###About our First Component

Here are some notes about our first component:

* We used `React` to create the component by calling `createClass`
* We used `ReactDOM` to attach the component to the DOM, by defining the component as JSX and the element we wanted to attach the component to.
* JSX syntax != HTML syntax. Note that in order to get the `well` class to appear, we needed to use the attribute `className`. Here are some [more details on JSX syntax](https://facebook.github.io/react/docs/jsx-in-depth.html)
* The `render` function is what renders the component to the screen.

##Nesting Components

Once components are created, we can use them as subcomponents. Let's try doing this by creating a list with list items inside.

```js
const ListItem = React.createClass({
  render: function() {
    return <li>Item</li>;
  }
});

const ToDoList = React.createClass({
  render: function() {
    return (
      <ul>
        <ListItem></ListItem>
        <ListItem></ListItem>
      </ul>
    );
  }
});
```

Then, add `<ToDoList></ToDoList>` to the `render` function for `MyApp`.

```js
const MyApp = React.createClass({
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
        <ToDoList></ToDoList>
      </div>
    );
  }
});
```

Our DOM structure should look like this:

```html
<div className="well">
  <h1>Hello</h1>
  <ToDoList>
    <ul>
      <ListItem>Item</ListItem>
      <ListItem>Item</ListItem>
    </ul>
  </ToDoList>
</div>
```

Nice! These components are not only reusable, but they are semantic as well. But there's still no dynamic data associated with the elements, since we had to hardcode `Item` in each `ListItem` component.

##Using Data through `props`

In order to represent and change data in React, we will first introduce the concept of `props`. `props` is how we can access data through properties on a component. If we compare the JSX syntax to HTML, these properties are passed by using attributes on the components. We can access `props` like so:

```js
this.props
```

Let's modify the `ListItem` and `ToDoList` components to use `props`.

```js
const ListItem = React.createClass({
  render: function() {
    return <li>{this.props.item}</li>;
  }
});

const ToDoList = React.createClass({
  render: function() {
    return (
      <ul>
        <ListItem item="Item 1"></ListItem>
        <ListItem item="Item 2"></ListItem>
      </ul>
    );
  }
});
```

Note that we now pass `{this.props.item}` into the `render` function of `ListItem`. This means that the property `item` will be placed into the `<li></li>` tags if we pass the property into `ListItem`.

If we want to make this a truly extensible list, we could create an array of items, then pass them into `props` through the `ToDoList` component, then render out each item. Let's do that now.

```js
const ToDoList = React.createClass({
  render: function() {
    const todoItems = this.props.items.map(item => {
      return <ListItem item={item}></ListItem>
    });

    return (
      <ul>{todoItems}</ul>
    );
  }
});
```

##Updating `props` through `state`

In a React component, `state` is just another object, like `props`. The only difference is that it can only be changed through the method `setState`. The exception is setting the initial state, which is only done once when initializing a React component. In order to pass items to the `ToDoList` component and make them mutable, we'll need to set the state of `MyApp`. Let's continue refactoring our `MyApp` component to assign `toDos` through `state`.

```js
const MyApp = React.createClass({
  getInitialState: function() {
    return {
      toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI']
    };
  },
  render: function() {
    return (
      <div className="well">
        <h1>To Do List</h1>
        <ToDoList items={this.state.toDos}></ToDoList>
      </div>
    );
  }
});
```

All we changed was adding a new function called `getInitialState`, which returns the initial value of the `state` object. We also altered the `ToDoList` in `MyApp` by passing `this.state.toDos` into the `items` property, which will then be accessed in the `ToDoList` component through `props` as usual.

###Updating `state`

Updating state will involve calling `setState`. Let's use a simple example with a clear button in `MyApp`

```js
const MyApp = React.createClass({
  getInitialState: function() {
    return {
      toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI']
    };
  },
  clear: function() {
    this.setState({toDos: []});
  },
  render: function() {
    return (
      <div className="well">
        <h1>To Do List</h1>
        <button onClick={this.clear}>Clear</button>
        <ToDoList items={this.state.toDos}></ToDoList>
      </div>
    );
  }
});
```

Now when we click on the button, the following will occur:

* `this.state` will be set to `{toDos: []}`
* The `render` function for `MyApp` will be called, and re-render the component

Let's add one more thing to our app, an input field for more items. In order to do so, we'll need the following variable to represent the **new item** we'll be entering:

* `newItem`

We'll also need **two** additional functions to represent the following changes in state:

* `newItemChange`, for when we type characters into an input field and change the value of `newItem`
  * We'll need to get the current value of the input field and set `state` accordingly
* `addItem`, for when we submit the form
  * We'll need to make a copy of the `toDos` array, push the `newItem`, set `state` and clear `newItem`

Like so:

```js
const MyApp = React.createClass({
  getInitialState: function() {
    return {
      toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI'],
      newItem: ''
    };
  },
  clear: function() {
    this.setState({toDos: []});
  },
  newItemChange: function(e) {
    this.setState({newItem: e.target.value});
  },
  addItem: function(e) {
    e.preventDefault();
    const toDos = this.state.toDos;
    toDos.push(this.state.newItem);
    this.setState({toDos: toDos, newItem: ''});
  },
  render: function() {
    return (
      <div className="well">
        <h1>To Do List</h1>
        <button onClick={this.clear}>Clear</button>
        <form onSubmit={this.addItem}>
          <input type="text"
           placeholder="Item goes here"
           onChange={this.newItemChange}
           value={this.state.newItem}
          />
        </form>
        <ToDoList items={this.state.toDos}></ToDoList>
      </div>
    );
  }
});
```

**Notes**

* Since JSX functions are callbacks, we can assume that any function called via an event can accept a callback argument with the event. We pass this in as `e` to `newItemChange` and `addItem`
* We can use `onChange` on the `input` field to trigger an event when the text in the box is changed

##Keeping Modularity in Mind

So now we have a working list! But it could use some work. What if we want to use the `MyApp` component again in our app? Since our actual list now requires four functions in the `MyApp` component, we need to make sure that the list can stand on its own.

In order to fix this up, let's rename `MyApp` to `ToDoApp` and create a new `MyApp` component so we can render multiple lists.

###Final Solution

```js
//creating a basic component with no data, just a render function
const ToDoApp = React.createClass({
  getInitialState: function() {
    return {
      toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI'],
      newItem: ''
    };
  },
  clear: function() {
    this.setState({toDos: []});
  },
  newItemChange: function(e) {
    this.setState({newItem: e.target.value});
  },
  addItem: function(e) {
    e.preventDefault();
    const toDos = this.state.toDos;
    toDos.push(this.state.newItem);
    this.setState({toDos: toDos, newItem: ''});
  },
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
        <button onClick={this.clear}>Clear</button>
        <form onSubmit={this.addItem}>
          <input type="text"
           placeholder="Item goes here"
           onChange={this.newItemChange}
           value={this.state.newItem}
          />
        </form>
        <ToDoList items={this.state.toDos}></ToDoList>
      </div>
    );
  }
});

const ListItem = React.createClass({
  render: function() {
    return <li>{this.props.item}</li>;
  }
});

const ToDoList = React.createClass({
  render: function() {
    const todoItems = this.props.items.map(item => {
      return <ListItem item={item}></ListItem>
    });

    return (
      <ul>{todoItems}</ul>
    );
  }
});

const MyApp = React.createClass({
  render: function() {
    return (
      <div>
        <ToDoApp></ToDoApp>
        <ToDoApp></ToDoApp>
      </div>
    );
  }
});

//insert the component into the DOM
ReactDOM.render(<MyApp />, document.getElementById('container'));
```
