#Introduction to ReactJS

##Objectives

* Describe the concepts of React components, props, and state
* Explain the concepts of the virtual DOM and JSX
* Compare and contrast ReactJS to AngularJS
* use `create-react-app` to start a React App
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
