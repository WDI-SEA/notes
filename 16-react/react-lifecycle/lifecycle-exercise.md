## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lab: React Lifecycle Methods

Much like other things you've dealt with you may want to do certain actions based on events in the "life" of a React component. Perhaps you want to do something after a component is loaded for the first time or after it updates. 

Think about things like Sequelize hooks, JavaScript classes, or DOM events. For example, Sequelize's `beforeCreate` hook allows you to run some code before a new entry goes into your SQL table. In the same way, React components allow you to tap into their own lifecycle methods. They sometimes have long, intimidating sounding names, which you'll have to get used to!

## The Big Three (or Four)

React components have 3 overarching categories that the lifecycle methods fit into. Some lifecycle events may overlap multiple categories. These categories are `Mounting`, `Updating`, and `Unmounting`. Sometimes you will see `Mounting` broken out into `Initialization` and `Mounting` as it is in this [medium article](https://medium.freecodecamp.org/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630).

#### Mounting

This is the birth of a React component. Any lifecycle event that takes place around the component coming into existence fits here:

* constructor
* componentDidMount
* render

#### Updating

This is basically any change or event that happens to the component that doesn't have to do with its birth or death:

* getDerivedStateFromProps
* shouldComponentUpdate
* getSnapShotBeforeUpdate
* componentDidUpdate
* render

#### Unmounting

This is when your component is about to shuffle off its mortal coil. When it passes to the code beyond and pushes up binary daisies. Only one lifecycle method is generally used here:

* componentWillUnmount

The reason you might use this is to clean up any open connections or free any memory in use. In object-oriented languages this is normally done in a `destructor` method - i.e., the opposite of the `constructor`.

## Lifecycle Methods Chart

![](https://res.cloudinary.com/briezh/image/upload/v1556220396/React-Lifecycle_bwt2dv.png)

[Image credit to programmingwithmosh.com](https://programmingwithmosh.com/javascript/react-lifecycle-methods/)

## Directions

#### 1. Your instructor will assign you one or two lifecycle methods listed below. 

Note that these methods may be deprecated. If so, why was it deprecated and what replaced it?

#### 2. Study what your methods do in-depth and know what part of the lifecycle they happen in - mounting, updating, or unmounting

#### 3. Prepare a short presentation for your classmates regarding your assigned lifecycle methods.

Your presentation doesn't have to be long, but it should minimally include:

* A definition
* Which part of the 3 parts of the lifecycle does it occur in
* A code example or an explanation of a scenario when the lifecycle method would be used


## Lifecycle Methods List

* constructor
* componentDidMount
* getDerivedStateFromProps
* shouldComponentUpdate
* getSnapShotBeforeUpdate
* componentDidUpdate
* render
* componentWillUnmount
* componentWillReceiveProps ([deprecated - here's why](https://hackernoon.com/replacing-componentwillreceiveprops-with-getderivedstatefromprops-c3956f7ce607))

## Resources

* [Medium - Understanding Lifecycle Methods](https://medium.freecodecamp.org/how-to-understand-a-components-lifecycle-methods-in-reactjs-e1a609840630)
* [Why componentWillReceiveProps is Deprecated](https://hackernoon.com/replacing-componentwillreceiveprops-with-getderivedstatefromprops-c3956f7ce607)
