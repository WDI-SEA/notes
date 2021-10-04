# Props

### Learning Objectives

_After this lesson, you will be able to:_

* Describe props
* Create a component that renders props

## Component Data with Props

The React framework was built to handle data that changes over time.

So far, we have defined a `Hello` component in `App.js`. The component's `render` method returns a div with a few headings, written in JSX.

In `index.js`, we are importing this component, appending what the `Hello` component `render` method returns to the virtual DOM, and rendering that.

This is great, but it doesn't involve any data yet, let alone data that changes over time! Let's make it more interesting.

Rather than simply display "Hello world", let's display a greeting to the user. We'll make the greeting change dynamically based on the user's name.

The question is, how do we add a name to our `Hello` component without hardcoding it into the component's `render` method?

Find out! Try it yourself alongside [this video](https://generalassembly.wistia.com/medias/gchiu63slo) in [this codepen](https://codepen.io/susir/pen/vxWypq) _\(note: right click both for new tab!\)_

### Hello World exercise - You do!

#### Code along: Adding props to our component

Let's use **props** to make our "Hello World" app more flexible.

**First, a single prop**

We want to make a greeting that's reusable for many different users, so we'll have a `name` prop for the name of the user.

In your `src/index.js`, we'll change the line that renders the `Hello` component to include this `name` prop. The new line will be:

`<Hello name={"Nick"} />`

> We pass in data wherever we are rendering our component. In rendering the `Hello` component above, we pass in a prop called "name" with a value of "Nick".

Your `index.js` should now look like this:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Hello from './App.js';

ReactDOM.render(
  <Hello name={"Nick"} />,
  document.getElementById('root')
)
```

Now, every time we render our component, we will pass in data.

* When the `Hello` component renders, we pass the `Hello` component a prop called `name` with a value of `Nick`.

If you check your application now, nothing has changed. We're passing the `name` prop into the component, but the component isn't _using_ it yet.

In our component definition, we will change the `<h1>Hello World!</h1>` to `<h1>Hello {this.props.name}!</h1>`. The portion `{this.props.name}` deserves a closer look:

* `this` refers to the specific component instance
* `this.props` will collect all the props for this component instance
* `this.props.name` pulls out the name property from `this.props`.

> The `{}` syntax in JSX renders the result of any expression inside it. It works even without props. If you wrote `{2+2}` in your JSX, `4` would be rendered.

In `App.js`, your `Hello` class should now look like this:

```jsx
class Hello extends Component {
  render () {
    return (
      <div>
        <h1>Hello {this.props.name}!</h1>
        <h3>It is time for tea.</h3>
      </div>
    )
  }
}
```

In the above example, we replaced "world" with `{this.props.name}`.

> Check it out! You should be able to browse to [http://localhost:3000](http://localhost:3000) to view this change!

## What about... multiple props?

Of course, we often want components to display more complex information. To do so, we can pass multiple properties to our component! We'll use the same two steps we took to add the first prop.

First, add another prop to the component call: `<Hello name={"Nick"} />,` changes to `<Hello name={"Nick"} age={24} />`.

Update your `index.js` file to reflect this:

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import Hello from './App.js';

ReactDOM.render(
  <Hello name={"Nick"} age={24} />,
  document.getElementById('root')
)
```

Now, in our component definition we have access to both values. The second step is to change the `Hello` component class in `App.js` to use the age information!

```javascript
class Hello extends Component {
  render () {
    return (
      <div>
        <h1>Hello {this.props.name}!</h1>
        <p>You are {this.props.age} years old.</p>
      </div>
    )
  }
}
```

> Check it out! You should be able to browse to [http://localhost:3000](http://localhost:3000) to view this change!

## What about... multiple props passed from an object?

If we have many props, it might get difficult to keep track when we're passing everything in to render a component. A better practice is to organize values in some kind of object and then pass props to the component from that object. Let's see this strategy.

Currently, in `index.js`, we put Nick's name and age directly into the `ReactDOM.render` call. Instead, we'll create an object that holds Nick's name and age, making it clearer for other developers and easier to change in the future. In your `index.js file`, below the `import` statements, add this object definition:

```javascript
const person = {
  personName: "Nick",
  personAge: 24
}
```

Next, we'll update what's passed into the component. Near the bottom of your `index.js`, modify the `ReactDOM.render()` call:

```javascript
ReactDOM.render(
  <Hello
    name={person.personName}
    age={person.personAge}
  />,
  document.getElementById('root')
)
```

We don't have to change anything in `App.js`, because it's still receiving exactly the same values for exactly the same two props - `name` and `age`. We're just sending it those values in a slightly different way.

> Check it out! If you browse to [http://localhost:3000](http://localhost:3000) nothing should have changed.
>
> Try changing the values inside the `person` object without changing the `ReactDOM.render()` call. See how the page updates.

#### Multiple props from a more complex object

Since we're just pulling props out of an object, we can use any object we want. For example, we can nest an array inside it.

Let's say our user has some favorite animals. Update your object to include an array:

```javascript
const person = {
  personName: "Nick",
  personAge: 24,
  favorites: [
    "Capybaras",
    "Tigers",
    "Dinosaurs count!"
  ]
}
```

Now we can use this new information as a prop, just like normal. You could choose to pass a single element \(`favorites[0]`\) or the entire array. We'll use the entire array so that the component can display _all_ a person's favorite animals. First, update your `ReactDOM.render()` call in `index.js`:

```javascript
ReactDOM.render(
  <Hello
    name={person.personName}
    age={person.personAge}
    animals={person.favorites}
  />,
  document.getElementById('root')
)
```

If you check your application now, nothing has changed. Remember, a component class will just ignore any props it receives that it doesn't use. But, we want to use the favorite animals! So, second, update your `Hello` class `render` method in `App.js`:

```markup
<div>
  <h1>Hello {this.props.name}!</h1>
  <p>You are {this.props.age} years old.</p>
  <p>You love: {this.props.animals}</p>
</div>
```

If you check the page now, you'll see React prints the entire array, as that's what was passed in. If we wanted to include all the animals clearly, we could fix the spacing. Instead, to review some syntax, let's just modify the code to render the first value.

```markup
<div>
  <h1>Hello {this.props.name}!</h1>
  <p>You are {this.props.age} years old.</p>
  <p>You love: {this.props.animals[0]}</p>
</div>
```

Check it out!

[_Read more about using props in JSX, if you'd like!_](https://facebook.github.io/react/docs/jsx-in-depth.html) _This link is also in the Further Reading page at the end of the React module, under the Facebook documentation._

