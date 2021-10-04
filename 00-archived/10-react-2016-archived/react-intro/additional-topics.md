# Additional Topics

Two additional concepts that appear frequently in React are the **component life cycle** and the **Flux architecture.**

#### Component Life Cycle

There are some additional points in the component life cycle that you may want to take advantage of. Examples include when `props` change, or when we remove a component from the DOM. In order to perform different actions during the life cycle of a component, just define the following functions in the component.

* `componentWillMount` – Fired once **before** the initial component render
* `componentDidMount` – Fires once **after** the initial component render
* `componentWillReceiveProps` – Fires whenever there is a change to `props`
* `componentWillUnmount` – Fires before the component unmounts from the DOM

[Component documentation](https://facebook.github.io/react/docs/component-specs.html)

#### Flux

While you can incorporate a server with React through a RESTful API and AJAX \(jQuery\), generally React is used with a different type of architecture called Flux. Watch the video on the Flux Overview page below to understand some of the benefits behind this highly-scalable architecture.

[Flux Overview](http://facebook.github.io/flux/docs/overview.html)

![Flux Architecture](https://facebook.github.io/flux/img/flux-simple-f8-diagram-explained-1300w.png)

## Conclusion

React is substantially different from Angular because its main goal is to **render UI based on data.** We can keep track of static data using `props`, and keep track of dynamic data using `state`. By isolating data in `state`, we can keep track of when data is changed and re-render the UI accordingly.

Incorporating React with an API involves nothing special. In fact, you can use jQuery's `.ajax` function to make requests inside a React component, then call `setState` when the data is ready.

### More Resources

* [React with Gulp and Browserify](http://tylermcginnis.com/reactjs-tutorial-pt-2-building-react-applications-with-gulp-and-browserify/)
* [Flux Architecture](https://facebook.github.io/flux/)
* [React Examples](http://react.rocks/)
* [React Router](https://github.com/rackt/react-router)
* React Addons
  * [React Animations/Transitions](https://facebook.github.io/react/docs/animation.html)
  * [Two-way data binding](https://facebook.github.io/react/docs/two-way-binding-helpers.html)
* [React Authentication with Flux](https://auth0.com/blog/2015/04/09/adding-authentication-to-your-react-flux-app/)
* [React starter kit](https://github.com/kriasoft/react-starter-kit)

