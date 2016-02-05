#Introduction to ReactJS

##Objectives

* Understand the concepts of React components, props, and state
* Understand the concepts of the virtual DOM and JSX
* Compare and contrast ReactJS to AngularJS
* Create your own React components

##How will you React?

React is a front end JavaScript framework used for creating user interfaces. It was originally engineered by Facebook, and it is now used by Facebook, Instagram, Airbnb, and many other companies.

###But what is it really?

React deals **specifically** with rendering data as HTML, so it involves a different mode of thinking when compared to Angular. In React, data flows in one direction (no two-way data binding), and data is modularized using **components.**

![React components](http://maketea.co.uk/images/2014-03-05-robust-web-apps-with-react-part-1/wireframe_deconstructed.png)

Here's an example of how React components would be created and rendered on a page. You'll see that there's a hierarchy where each components can contain additional components. The data is stored by each component, and a `render` function takes the data and renders it as HTML on the page.

###Terminology We'll Need

####One-Way Data Flow

Data is not bound in both directions in React. Meaning, if we want an input field to update the actual data in a component, we'll need to call a function to modify the value. Compare this to Angular, where we can change the value of an input field bound to `ng-model` and it'll automatically update the value in the controller.

####Virtual DOM

React uses what's called a **virtual DOM.** When React renders data to the page, the differences are computed by comparing the page to the virtual DOM. When a component needs to be re-rendered, only the component and its subcomponents are actually rendered. This ideally results in a more efficient rendering process.

####JSX

We keep mentioning data, and how each component is actually just storing data. But how is that data rendered? We'll be using a syntax called **JSX** to render our components. More to come!

##Setup our Workflow

In order to make our workflow smoother, we have provided some starter code for you to start with. Note that we'll only be creating a front end application with React.

Also note that the setup we have provided is for demonstration and hobby uses only. The setup contains a JSX/Babel compiler (`browser.min.js`) as well as jQuery. Note that jQuery is not necessary for React to work, and JSX/Babel compiling should not be done in the browser on production sites.

That said, let's make our first React component.

##Your First React Component

In `js/main.js`, write the following component:

```js
//creating a basic component with no data, just a render function
var MyApp = React.createClass({
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
      </div>
    );
  }
});

//insert the component into the DOM
ReactDOM.render(<MyApp />, document.getElementById('reactApp'));
```

Now run a local HTTP server in `reactapp` and take a look!

**Side note:** You'll notice in that browser console that a message may appear when the app is first loaded:

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
var ListItem = React.createClass({
  render: function() {
    return <li>Item</li>;
  }
});

var ToDoList = React.createClass({
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

Then, add `<ToDoList></ToDoList>` to the `render` function for `MyApp`. Our DOM structure should look like this:

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

Nice! These components are not only reusable, but they are semantic as well. But there's still no data associated with the elements, since we had to hardcode `Item` in each `ListItem` component.

##Using Data through `props`

In order to represent and change data in React, we will first introduce the concept of `props`. `props` is how we can access data through properties on a component. If we compare the JSX syntax to HTML, these properties are passed by using attributes on the components. We can access `props` like so:

```js
this.props
```

Let's modify the `ListItem` and `ToDoList` components to use `props`.

```js
var ListItem = React.createClass({
  render: function() {
    return <li>{this.props.item}</li>;
  }
});

var ToDoList = React.createClass({
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

If we want to make this a truly extensible list, we could create an array of items, then pass them into `props` through the `ToDoList` component, then render out each item.

**Try it:** Create a list of items and pass them into the `ToDoList` component as a property called `items`. Then, **iterate** through the items and render each item out as a `ListItem` component. Note that you'll need an **iterator** to iterate through `items` and return each `ListItem`. Also, any variables you'd like to render inside JSX will require template tags and no quotes (`{}`).

##Updating `props`

Ultimately, this current setup provides a static interface. So what would be the reasonable method for updating `props`? Something like this?

```js
//note: this won't work in React
var MyApp = React.createClass({
  toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI'],
  addToDo: function() {
    this.toDos.push('item');
    console.log(this.toDos);
    this.render();
  },
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
        <button onClick={this.addToDo}>Add</button>
        <ToDoList items={this.toDos}></ToDoList>
      </div>
    );
  }
});
```

Unfortunately, a setup like this will not work. Therefore, our last main topic in React will be how to **change the values, or state, of props**. Sure enough, we can use a separate, *private* object on each component called **state** in order to not only pass updatable properties, but also **re-render the component.**

##Adding items through `state`

In a React component, `state` is just another object, like `props`. The only difference is that it can only be changed through the method `setState`. The exception is setting the initial state, which is only done once when initializing a React component. Let's continue refactoring our `MyApp` component to assign `toDos` through `state`.

```js
var MyApp = React.createClass({
  getInitialState: function() {
    return {toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI']}
  },
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
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
var MyApp = React.createClass({
  getInitialState: function() {
    return {toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI']}
  },
  clear: function() {
    this.setState({toDos: []});
  },
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
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
var MyApp = React.createClass({
  getInitialState: function() {
    return {
      toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI'],
      newItem: ''
    }
  },
  clear: function() {
    this.setState({toDos: []});
  },
  newItemChange: function(e) {
    this.setState({newItem: e.target.value});
  },
  addItem: function(e) {
    e.preventDefault();
    var toDos = this.state.toDos;
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
```

**Notes**

* Since JSX functions are callbacks, we can assume that any function called via an event can accept a callback argument with the event. We pass this in as `e` to `newItemChange` and `addItem`
* We can use `onChange` on the `input` field to trigger an event when the text in the box is changed

##Keeping Modularity in Mind

So now we have a working list! But it could use some work. What if we want to use the `ToDoList` component again in our app? Since `ToDoList` now requires four functions in the `MyApp` component, we lost the modularity of the `ToDoList` component.

In order to fix this up, let's put these concepts all together and think of how we could redesign `MyApp` and `ToDoList` to make `ToDolist` a modular component.

###Workflow

* `MyApp` should be as simple as possible, defining the top level of the app
  * We should be able to create multiple `ToDoList` components, each one having its own set of `props` and `state`
  * Each `ToDoList` component should have the ability to receive an initial array or no initial array
* `ToDoList` will have items that change, so we need to initialize `state`
  * Initialize `state` with the value from `props`
  * Move the `form` and `button` elements to `ToDoList` so that they are rendered in the component
  * Move the functions that change state to `ToDoList`
  * Modify `ToDoList` so that the items altered are attached to `state` instead of `props`
    * this will make the items dynamic

###Final Solution

```js
var MyApp = React.createClass({
  toDos: ['Mow the lawn', 'Get groceries', 'Finish WDI'],
  render: function() {
    return (
      <div className="well">
        <h1>Hello</h1>
        <ToDoList items={this.toDos}></ToDoList>
        <ToDoList></ToDoList>
      </div>
    );
  }
});

var ListItem = React.createClass({
  render: function() {
    return <li>{this.props.item}</li>;
  }
});

var ToDoList = React.createClass({
  getInitialState: function() {
    return {
      toDos: this.props.items || [],
      newItem: ''
    }
  },
  clear: function() {
    this.setState({toDos: []});
  },
  newItemChange: function(e) {
    this.setState({newItem: e.target.value});
  },
  addItem: function(e) {
    e.preventDefault();
    var toDos = this.state.toDos;
    toDos.push(this.state.newItem);
    this.setState({toDos: toDos, newItem: ''});
  },
  render: function() {
    var listItems = this.state.toDos.map(function(item, idx) {
      return <ListItem key={idx} item={item}></ListItem>;
    });
    return (
      <div>
        <button onClick={this.clear}>Clear</button>
        <form onSubmit={this.addItem}>
          <input type="text"
           placeholder="Item goes here"
           onChange={this.newItemChange}
           value={this.state.newItem}
          />
        </form>
        <ul>
          {listItems}
        </ul>
      </div>
    );
  }
});

ReactDOM.render(<MyApp />, document.getElementById('reactApp'));
```

###Additonal Topics in React

Two additional concepts that appear frequently in React are the **component life cycle** and the **Flux architecture.**

####Component Life Cycle

There are some additional points in the component life cycle that you may want to take advantage of. Examples include when `props` change, or when we remove a component from the DOM. In order to perform different actions during the life cycle of a component, just define the following functions in the component.

* `componentWillMount` – Fired once **before** the initial component render
* `componentDidMount` – Fires once **after** the initial component render
* `componentWillReceiveProps` – Fires whenever there is a change to `props`
* `componentWillUnmount` – Fires before the component unmounts from the DOM

[Component documentation](https://facebook.github.io/react/docs/component-specs.html)

####Flux

While you can incorporate a server with React through a RESTful API and AJAX (jQuery), generally React is used with a different type of architecture called Flux. Watch the video on the Flux Overview page below to understand some of the benefits behind this highly-scalable architecture.

[Flux Overview](http://facebook.github.io/flux/docs/overview.html)

![Flux Architecture](https://facebook.github.io/flux/img/flux-simple-f8-diagram-explained-1300w.png)

##Conclusion

React is substantially different from Angular because its main goal is to **render UI based on data.** We can keep track of static data using `props`, and keep track of dynamic data using `state`. By isolating data in `state`, we can keep track of when data is changed and re-render the UI accordingly.

Incorporating React with an API involves nothing special. In fact, you can use jQuery's `.ajax` function to make requests inside a React component.

###More Resources
* [React with Gulp and Browserify](http://tylermcginnis.com/reactjs-tutorial-pt-2-building-react-applications-with-gulp-and-browserify/)
* [Flux Architecture](https://facebook.github.io/flux/)
* [React Examples](http://react.rocks/)
* [React Router](https://github.com/rackt/react-router)
* React Addons
  * [React Animations/Transitions](https://facebook.github.io/react/docs/animation.html)
  * [Two-way data binding](https://facebook.github.io/react/docs/two-way-binding-helpers.html)
* [React Authentication with Flux](https://auth0.com/blog/2015/04/09/adding-authentication-to-your-react-flux-app/)
* [React starter kit](https://github.com/kriasoft/react-starter-kit)
