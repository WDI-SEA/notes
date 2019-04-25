## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  Displaying Pages Individually

Try manually deleting two of the three components so only one component is left
on the page at a time. You should see your webpage update with just that
component. This is effectively what **React Router** does. We can configure React Router
so that it's aware of which component we want to show on the screen, and React
Router will swap the components out so that only the correct one is shown at a time.

Now that we've proven to ourselves that we're able to show each of the
components on the main page, it's time to hook them up to Router.

## Creating Routes
Here's the general syntax for creating routes. React Router uses some of its own components to define how URLs are routed
to your components and to create links to those routes. You must have one `<Router>`
component that wraps itself around multiple `<Route>` components. Each `<Route>`
component has two pieces:
- `path` - defining the URL path that leads to the component.
- `component` - defining
what component users will see when they navigate to the path.

Delete what is currently returned in the `render` function of your `App.js`, and replace it with a Router component call with three routes, as shown below.

```js
class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route path="/procedures" component={Procedures} />
          <Route path="/contact" component={Contact} />
        </div>
      </Router>
    )
  }
}
```

There are three other important things to note here:

- This goes *in place of* your existing component calls of `<Home />` or `<Home></Home>` (depending on which syntax you went for).

- The first route for the homepage at the root URL path `/` uses a
special extra `exact` attribute before defining the path. The `exact` attribute
means the component associated with the route will only be shown if users are
at exactly that URL path. If you forget to include the `exact` keyword, when someone navigates to `/contact` they will actually see two components, because `/` is a partial match for `/contact`.

- Notice that all of the `<Route>` components are wrapped inside one `<div>`. Like `render`, the `<Router>` element can only have one direct child element. If you don't
wrap the routes with a `<div>`, the page will appear blank, and you'll have to
open your JavaScript console to see that there's an error being logged to the
console. Like so -

![A Router may only have one child element.](assets/router-requires-only-one-child.png)


**Pro tip:** It's a good habit to check the console for errors whenever your
app is not behaving as expected.


## Import Statements
In order to use the React Router components in `App.js`, you'll need to import them. This
import syntax allows us to grab several specific components out of the
`react-router-dom` library at once. So far we've used `Router` and `Route`.

The Router component is actually called `BrowserRouter`
inside the library package, but we'll use the `as` keyword to rename it to
`Router` so it's easier to remember.

While we're here, we'll also import a third component, `Link`, which we'll get to in a minute.

Put this code at the top of your `App.js`

```js
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';
```

## Fully Routed
Here's how the imports and all the components look like together for our dentist
website:

**App.js**
```js
import React, { Component } from 'react';
import './App.css';

import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';

import Home from './Home';
import Procedures from './Procedures';
import Contact from './Contact';


class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route path="/procedures" component={Procedures} />
          <Route path="/contact" component={Contact} />
        </div>
      </Router>
    )
  }
}

export default App
```

# Navigate to the Routes
Now that everything is hooked up you can manually enter different URLs and
see how your page appears. If you go to <http://localhost:3000/>, you should
see just the homepage. If you go to <http://localhost:3000/procedures>, you should
see just the procedures page. If you go to <http://localhost:3000/contact>,
then you should see just the contact page.

> Check it!
> * Make sure that React Router is routing from each URL to the proper component
correctly.
> * Double check to make sure that the home page doesn't display at the
same time as another component. If the homepage is shown while you're at the
path to `/procedures` or `/contact` then you probably did not write the `exact`
keyword when you defined the `/` Home route.

## Debugging Common Errors
Let's intentionally make an error. Delete the `exact` keyword off the Home
route. Navigate to the `/procedures` page and the `/contact` page again and
see how the components are displayed. You should see the content of the
homepage and the content for one of the other pages at the same time, with
the home page on top.

Now add the `exact` keyword back to the home route and notice that the pages
don't double up any more.

Two common errors:
1. If the page appears blank, open the JavaScript console to see if there are
  errors. Chances are you have a typo somewhere or forgot to make sure the
  `<Router>` only has one child element. Remember, wrap all of your `<Route>` components
  in one `<div>`.
2. If multiple components appear on the page at the same time there's
  something with how you've routed URLs. Make sure you use the `exact`
  keyword on the root path `/` and make sure there are no duplicate URL paths
  defined anywhere.

# Adding a Nav Section
Great, now our site is up and running! We can manually type in URLs and see the
different pages.

Although... users never really type URLs, do they? We should probably have links at the top of the page so we can just click on
things. We could build this ourselves, but we don't have to! Remember that `Link` component we imported from React Router?

Just like links in HTML, we can wrap `<Link>` tags around whatever text that we want to display to the user to click on. The pieces of this are:

* `<Link>` - creates `<a>` tags and automatically integrates
  modern HTML5 browser history mechanics for the Single Page Application. It
  has one attribute:
* `to` - what path to navigate to when the user clicks the link

We'll add one `<Link>`
  component that leads to each of our different content pages.

```html
<Link to="/">Go to Home Page</Link>
<Link to="/procedures">See Our Procedures</Link>
<Link to="/contact">Contact Us!</Link>
```

> Did you notice that we don't reference components here? We simply make links for users to click that connect to URLs, and the `Router` section in the code handles the actual component changes.

We can include those links in a `<nav>` element at the top of our page.
It will stay on the page permanently, and the different components will be
swapped between each other below it. There's actually nothing special about
the `<nav>` element. It behaves exactly like a `<div>`. `<nav>` Is just a
semantic element that gives your JSX more meaning when people read it.

In your `App.js`, inside the `<div>` (because we want it rendered!) and before the `Route` statements, put:

```html
<nav>
  <Link to="/">Home</Link>
  <Link to="/procedures">Procedures</Link>
  <Link to="/contact">Contact</Link>
</nav>
```

So, our web app now looks like the left image - but do you see a difference between the left and the right?


![Spaces must be inserted manually.](assets/manual-spaces-in-nav.png)


There's one slightly annoying thing about React here - React strips out whitespace (e.g., spaces, returns, tabs) between elements. If we write `<Link>` components next to each other, even if they're on new lines in our code, React strips all of the whitespace between them and squishes them all together.

We
must insert a space manually by writing `{' '}` in order to get spaces between
our links.

So instead of the code we used before, here is how we'll format the links. Nothing has changed except that we've added the space:

```html
<Link to="/">Go to Home Page</Link>{' '}
<Link to="/procedures">See Our Procedures</Link>{' '}
<Link to="/contact">Contact Us!</Link>
```

And now the nav bar will have spaces like it should.  Try it!


# Final Code
Here's what our final `App.js` looks like:

```js
class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <nav>
            <Link to="/">Go to Home Page</Link>{' '}
            <Link to="/procedures">See Our Procedures</Link>{' '}
            <Link to="/contact">Contact Us!</Link>
          </nav>
          <Route exact path="/" component={Home} />
          <Route path="/procedures" component={Procedures} />
          <Route path="/contact" component={Contact} />
        </div>
      </Router>
    )
  }
}

export default App
```

> Check it out! Does yours work?
