## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png)  The Plan: Our Example Dentist Website

We're going to make an example dentist website that has:
- A `Home` page.
- A page that lists available `Procedures`.
- A page displaying `Contact` information.

Each of these pages of content will be built into their own regular React component; then we'll create a unique URL route that leads to each component.

Here's how we'll route our single-page application:

| **URL Route**  | **Component**  | **Content Description**                          |
|----------------|----------------|--------------------------------------------------|
| /              | `<Home>`       | A homepage with welcome text.                    |
| /procedures    | `<Procedures>` | A list of all dentist procedures.                |
| /contact       | `<Contact>`    | A page with an address, phone number, and email. |

Remember, the URL routes are paths off our main website. We could put our
website at any domain, like `www.ourdentistwebsite.com` or
`www.premiumdental.com`, and the URL route paths would behave the same. Paths
only care about what comes after the domain name.

Our routes say that if someone goes to `ourdomain.com/` they will see our home page with welcome text.
- The content of this page will all be defined in its own `Home` component in a file called `home.js`.
- If someone navigates to the URL `ourdomain.com/contact`, they will see content with the business address, a phone number, and an email. All of this content will be defined in a component called `Contact` in a file called `contact.js`.

In the below codealong, we will walk through building this out together.

You can see a live working copy of the site [here](https://react-router-dentist.herokuapp.com/).

You are going to follow along, so that you have a locally working React Router application! However, if you'd like at any point to refer to the finished code, you can see all of the final code [here](../../../react-router-simple-dentist-site).

## In Your Terminal

> Remember to stop the React project you currently have running!

Now let's make the dentist project. In your terminal, use `create-react-app` to make a new project called `dentist-website`:

```
$ create-react-app dentist-website
$ cd dentist-website
$ npm start
```

Your browser should open to <http://localhost:3000/> and you'll see the standard
"Welcome to React" message with a fancy rotating atomic icon. `create-react-app`
creates several files for us in a directory called `src`. Open the `App.js`
file in your editor.

Remember, `App.js` contains our main application (it's what's called by `index.js`). You should see the basic JSX structure
of the standard React starter page. Make sure the file is the same thing you're
looking at in the browser by finding the text `Welcome to React` inside an
`<h2>` element.

Change the text to say `Hello!`, save the file and make sure
you see the changes automatically appear in your browser.

> If it doesn't automatically refresh, then try to manually
  refresh the page. If you still don't see changes after a manual refresh then  something could be wrong. Make sure you're editing the right file.

**Pro tip:** It's a good idea to make simple, verifiable changes like this when you're first starting a project. It's a good sanity check.

Make sure you can do simple things first. Don't start with complex things; complex changes come with greater potential for error. Prove to yourself the small changes work, and you'll save yourself headaches debugging large complex changes.


# Installing React Router
Let's install **React Router**.

Hit `ctrl-c` to stop the running app, so that we can use the terminal!

Since React Router is a third-party library, we'll need to use to download React Router and save it as
a dependency in our project.

In your terminal, enter:

```sh
$ npm install --save react-router-dom
```

* `npm install` is the command used to install libraries to our project.
* The `--save` flag tells `npm install` to save the thing we're downloading to
  our `package.json` file as a dependency. Saving the library as a dependency
  makes it easy for us to copy our project to another machine and just run
  `npm install` to install all of the dependencies for our project.
* `react-router-dom` is the official name of **React Router**

So, in summary, we're telling `npm install` to find the library package called
`react-router-dom`, install the package, and save the name of our package to our
file that keeps track of all the packages for our project.

If you don't use the `--save` flag then `npm install` will still find the
package and download it. It just won't save the package to your `package.json`
file, which allows you to easily install all of your saved dependencies if you later move to another machine.

# Create Custom Homepage

Let's start the app again. Enter the command `npm start` in your terminal.

Let's get rid of the standard "Welcome to React" page and replace it with our
own dentist website home page. Continue editing `App.js`: take out most of the JSX contents, and delete the import statement for `logo.svg`, which we won't use.

The `App.js` file contains one component that our whole app will live inside
of. Remember that React components have a `render(){ ... }` function that
defines what the component will look like when it is rendered on the webpage.

> Reminder! The render function alway has to return *at most* one top-level element. It's common to wrap everything in your component in a `div` to make sure you
  satisfy this constraint.

**So...**

Let's add one `<h1>` that says `Dentist Website` and a paragraph with some short welcome text. Your `App.js` file should now look like the code below. Save the file and check your browser to make sure the changes show up.

**App.js**
```js
import React, { Component } from 'react';
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <h1>Dentist Website</h1>
        <p>
          Welcome to my dentist website.
        </p>
      </div>
    )
  }
}

export default App
```

Great! Now we have a simple homepage set up. Let's move on to getting the rest
of the content for our site set up.


# Creating Our Homepage Component

We've been editing `App.js`, which defines one component for our entire
application. So far our app manually shows just the homepage. Let's refactor
this so the content of the homepage is moved into its own component called
`Home`.

1. Create a new file called `Home.js`.
2. Copy and paste everything inside `App.js` into `Home.js` to use as a
  template for how to create a React component.
3. Delete the import statement for `./App.css`.
4. Find everywhere the file says `App` and replace these instances with `Home`. This code previously created a component called `App`. Now we're rewriting it to create a component called `Home`.
5. Nothing needs to change in the rest of the `Home` component. You can look at the `render() { ... }` function and verify that it's returning content that represents our home page.  It should just be the one top-level
  `<div>`, the `<h1>` and a `<p>` paragraph element (if you used the same
  content as we did). Great. Now you have your `Home` component.
6. Go back to the `App.js` file and delete the `<h1>` and `<p>` tags where we used to
  have content written directly inside our `App` component. We don't
  need that written inside `App` any longer, because we just moved it all to the
  new `Home` component.
7. Instead, we need to call our new component. Put `<Home></Home>` inside the `<div>` in the `App` component. This tells the
  `App` component to render the `Home` component right there inside the div.
  > Note: We have been using `<Home />` to call components. `<Home></Home>` is just a different syntax we're showing you so that if you see it elsewhere, you're familiar with it.

8. Let's try it out! Look at the browser and see if the homepage appears. Unfortunately, if you've been following along, it won't. You'll see an
  error, which should look like this:

![Home not defined](assets/home-not-defined-error.png)

It's not enough to simply create the `Home.js` file and create the `Home`
component. We must also remember to import the component into the `App.js` file. Any components you want to use in a file need to first be imported into that file.

Your `App.js` and `Home.js` files should look like this after you've properly
created and imported the `Home` component.

**App.js**
```js
import React, { Component } from 'react';
import './App.css';
import Home from './Home';

class App extends Component {
  render() {
    return (
      <div>
        <Home></Home>
      </div>
    )
  }
}
export default App
```

**Home.js**
```js
import React, { Component } from 'react';

class Home extends Component {
  render() {
    return (
      <div>
        <h1>Dentist Website</h1>
        <p>
          Welcome to my dentist website.
        </p>
      </div>
    )
  }
}

export default Home
```

# Create Components for Procedures and Contact
The purpose of our site is to create several components that we can swap out
as the main content of the main page of our application in order to create a
modern Single Page Application. We'll create two more components, and then
we'll start routing things up.

1. Create a new file called `Procedures.js`
2. Create a new file called `Contact.js`

To create these new files, follow the same procedure we used to create the `Home` component. Basically, we used the `App` component as a template: create each file, change the
name of the component to its new name, then replace the JSX in the
`render() { ... }` function with custom content. Be sure to import each new
component into `App.js` just like we did with the `Home` component.

You can put your own content to be rendered by each component if you'd like. Refer to these complete files in the finished repo to make sure you got
everything correct:

* [Procedures.js](../../../react-router-simple-dentist-site/blob/master/src/procedures.js)
* [Contact.js](../../../react-router-simple-dentist-site/blob/master/src/contact.js)

Now that we have our components made, there's nothing stopping us from importing multiple components into our App.js. So now, we have:

**App.js**
```js
import React, { Component } from 'react';
import './App.css';

import Home from './Home';
import Procedures from './Procedures';
import Contact from './Contact';

class App extends Component {
  render() {
    return (
      <div>
        <Home></Home>
        <Procedures></Procedures>
        <Contact></Contact>
      </div>
    )
  }
}

export default App
```


> Check yourself! You should see all of content for each of the pages all stacked on top of each
other on the homepage. If you don't see content from all three of your components, something is wrong. You must fix this before continuing. Always
do simple things before doing complex things!
