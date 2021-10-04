# Code-Along: Edit Dino Blog

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Blog Project: Implement State

## Let's implement state in our blog.

**Deliverable:**

Let's implement state in our blog by making the `body` or `content` a mutable value.

## Steps to Achieve

1. Set an initial state prop in your component that contains content or body for posts.
2. Add a button to somewhere in your page \(up to you which component to add to!\). This button should `onClick` open an alert that takes a value.
3. Take the user inputed value into the alert box and use that return value to update the state of the body or content of your post.

**Some things to note:**

1. Set an initial state for our `App` component. The `state` object should have an attribute called `body`. Remove the prop we set for `App` and put it into the initial state instead. The value of `this.state.body` should be `Check out this body property!`.
2. Modify `App`'s `render()` method so that it uses the `body` from state, not props.
3. Create a `changeBody()` method inside `App` that updates `body` based on a user's input.
   * You should use `setState` somewhere in this method.
   * How can you get user input? Keep it simple and start with `prompt`.
4. Add a button to `App`'s `render()` method that triggers `changeBody()`.

## Solution Image

![Solution for Project](https://res.cloudinary.com/briezh/image/upload/v1556560665/State_SOLUTION_qszfgv.png)

**This is what your solution should look like.**

