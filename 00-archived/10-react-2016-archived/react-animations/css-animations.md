# CSS Animations

## Starter Code

We'll be using this iTunes search example and add transitions to the search items. Follow the instructions to set up the project.

[https://github.com/WDI-SEA/react-itunes-search](https://github.com/WDI-SEA/react-itunes-search)

## Using ReactCSSTransitionGroup

In order to implement CSS animations, we'll first need to install the appropriate React addon. We can do this via `npm`.

```text
npm install --save-dev react-addons-css-transition-group
```

Excellent! Now let's take a look at the documentation. [https://facebook.github.io/react/docs/animation.html](https://facebook.github.io/react/docs/animation.html)

You'll notice that we need to `require()` the module in the file we want to use it on. Then, we can encapsulate the components we want to animate with the following component:

```javascript
<ReactCSSTransitionGroup />
```

We also need to provide a transition name, as well as enter and leave timeouts. The timeouts will let React know when to unmount the components from the DOM.

In `/src/components/MusicSearch.jsx`, let's include ReactCSSTransitionGroup at the top of the page.

```javascript
const ReactCSSTransitionGroup = require('react-addons-css-transition-group');
```

Then, we'll encapsulate the `{listings}` being rendered with the component we mentioned earlier, `ReactCSSTransitionGroup`. The `return` statement under `render` should look something like this:

```javascript
return (
  <div>
    <h1>iTunes Search</h1>
    <form onSubmit={this.search}>
      <div className="form-group">
        <input type="text"
               value={this.state.searchTerm}
               onChange={this.onChange}
               placeholder="Search for Music"
               className="form-control" />
        </div>
      <input type="submit" className="btn btn-primary" />
    </form>
    <ReactCSSTransitionGroup transitionName="listing" 
                             transitionEnterTimeout={500} 
                             transitionLeaveTimeout={500}>
      {listings}
    </ReactCSSTransitionGroup>
  </div>
);
```

Finally, we have to add the actual transitions to our CSS. Add the following to `sass/style.scss`.

```css
.listing-enter {
  opacity: 0.01;
}

.listing-enter.listing-enter-active {
  opacity: 1;
  transition: opacity 500ms ease-in;
}

.listing-leave {
  opacity: 1;
}

.listing-leave.listing-leave-active {
  opacity: 0.01;
  transition: opacity 300ms ease-in;
}
```

We should now have transitions for each `MusicListing` component! However, there may be an issue when searching two terms one after another. The enter transition works, but the leave transition doesn't work. We can solve this by setting the `state` in the `search` function, so that the array is cleared before we reassign the results.

In `/src/components/MusicSearch.jsx`, make the following change to the `search` function.

```javascript
search: function(e) {
  e.preventDefault();
  // adding setState to []
  this.setState({results: []});

  //...
}
```

Now, as we make multiple searches, the results will fade in **and** out.

**Try it:** In AngularJS, we used the [animate.css](https://daneden.github.io/animate.css/) library for more complicated transitions. Try importing animate.css and use it with ReactCSSTransitionGroup.

