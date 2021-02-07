## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Introduction to React Hooks

## Learning Objectives

*After this lesson, you will be able to:*

* Define React Hooks and why they were introduced

---

## What are React Hooks?

So far we have learned about two ways to create React components: function-based and class-based. We know that if we make a component that extends the React.Component class, it will be able to use state, lifecycle methods, refs - the whole kit and kaboodle. In contrast, a function-based component has access to none of that. It is basically just a render function that draws some JSX.

Over time, React users and Facebook engineers realized that much of this functionality is not needed all the time. Moreover, the ways in which state interacted with the various lifecycle methods was confusing, which led to a lot of improper usage. The creation of Hooks was largely in response to these issues.

Hooks allow us to write a **function-based component** that can "opt-in" to using the various React features by inclusion of a "hook" for that feature. For example, if we want to have state in our component, we can write a functional component that uses the `useState` hook or if we need some action to occur after the render, what would normally be done with lifecycle methods, we can use the `useEffect` hook.

It is important to know that hooks **DO NOT** work inside class-based components.

There is a hook for every feature of React but the most common and important ones to learn are `useState` and `useEffect`.

## Are Class-based components obsolete?

No! This is very important - the advent of hooks does not make class-based components obsolete. Existing React code will continue to work even if you never use hooks. But Facebook is urging developers to start developing new apps using hooks as they make your React code cleaner, easier to read, and easier to and maintain. Additionally, your components will not have the overhead of class-based components and will minify more effectively.
