## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Blog Project: Implement State


## Let's implement state in our blog.

**Goals:**

Let's implement state in our blog by making the `body` a mutable value. 

> Note: mutable means editable  or changeable!


---

## But First: What Would Happen to State if You Refreshed the Page?

- In React, state just represents the state of data on our page.

- Something saved to state in React is not automatically saved to a database or to local storage.

- State is just what's currently on the page. If you refresh the page, then all state is lost and refreshed with the page.

---

## Steps

#### 1. Set an initial state for our `App` component.

#### 2. Modify `App`'s `render()` method so that it uses the `body` from state, not props.

#### 3. Create a `changeBody()` method inside `App` that updates `body` based on a user's input.

#### 4. Add a button to `App`'s `render()` method that triggers `changeBody()`.


**Some things to note:**

1. Set an initial state for our `App` component. The `state` object should have an attribute called `body`. Remove the prop we set for `App` and put it into the initial state instead. The value of `this.state.body` should be `Check out this body property!`.

2. Modify `App`'s `render()` method so that it uses the `body` from state, not props.

3. Create a `changeBody()` method inside `App` that updates `body` based on a user's input.
  - You should use `setState` somewhere in this method.
  - How can you get user input? Keep it simple and start with `prompt`.

4. Add a button to `App`'s `render()` method that triggers `changeBody()`.

---

## Solution

![Solution for Project](https://res.cloudinary.com/briezh/image/upload/v1556560665/State_SOLUTION_qszfgv.png)

<aside class="notes">

**This is what your solution should look like.**

---

## Bonus

Use a form to take in user input.

> Helpful documentation is available [here](https://reactjs.org/docs/forms.html).


**Talking Points:**

- The blog post's `body` should be updated dynamically when the user types in an input field.
- One option is to keep track of what the new input is going to be by triggering a method using `onChange` on the `<input>`.
- Another option is to pass an `event` object to the `onSubmit()` method and traverse the DOM from the event's target (for example, `e.target`) to find the `<input>` value.
- Note: You can leave the button from above to give the user options!

---

## Bonus Solution

![Solution for Bonus](https://res.cloudinary.com/briezh/image/upload/v1556560666/state_BONUS_SOLUTION_mjqchw.png)

<aside class="notes">

**This is what your solution should look like.**

