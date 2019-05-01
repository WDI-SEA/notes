# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) React.js Frameworks/UI Components


## Let's Test it out!

### Getting started

First things first, use `create-react-app` to create a new project.

Next, let's use Material UI. In their 'Getting Started' section on their website, 
they give you the code to install it in your React project.
```
npm install @material-ui/core
```
The next thing they require is the Roboto font and—if you want to use the `<Icon>` component—Material 
icons which can be included in the head of your html
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" />
<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
```

Now let's render some stuff. Create a new component called `Header.js` and copy this block of code into it.

```jsx
import AppBar from '@material-ui/core/AppBar';
import Button from '@material-ui/core/Button';
import React, { Component } from 'react';

class Header extends Component {
  render() {
    return (
      <AppBar position="static">
        <div>
          <Button>
            <div>Button 1</div>
          </Button>
          <Button>
            <div>Button 2</div>
          </Button>
        </div>
      </AppBar>
    );
  }
}

export default Header
```

Now replace the App component in your `index.js` with your fancy new Header component et VOILA! 
You should have a header with two buttons. Very exciting.

The buttons have a lovely ripple effect and they are blue. Why? Because that is Material UI's default theme. 
You can see the full details of the [default styles](https://material-ui.com/customization/default-theme/#default-theme).

### Enter the Theme

The first thing that needs to be done is to add a `theme.js` file in your src folder. In this file, 
the first thing we want to do is import some things. The first thing we want to import is the theme!
```jsx
import { createMuiTheme } from '@material-ui/core/styles';
```
We're going to import the createMuiTheme, then export it again with the values we want. 

Let's change the color of our AppBar. We're going to import a couple of color values from 
`@material-ui/core/colors` and put them into the `palette` section.

```jsx
import { createMuiTheme } from '@material-ui/core/styles';
import indigo from '@material-ui/core/colors/indigo';
import pink from '@material-ui/core/colors/pink';

export default createMuiTheme({
  palette: {
    primary: pink,
    secondary: indigo
  }
});
```

So, we've customised our theme, now what? 
* First, we have to import the theme provider `MuiThemeProvider`. 
* Next, we'll have to import the our theme file.
* Finally, we'll have to encapsulate our app inside the provider and pass our theme in as a prop.

Rather than apply our theme to a modular component like a header, let's clear out our `App.js` 
and import our MuiThemeProvider and Header in there. 


Your `App.js` should now look like this:
```jsx
import React from 'react';
import Header from './Header';
import MuiThemeProvider from '@material-ui/core/styles/MuiThemeProvider';
import theme from './theme';

App() {
  return (
    <MuiThemeProvider theme={theme}>
      <Header />
    </MuiThemeProvider>
  );
}

export default App
```

And if you look at your page, your AppBar is now pink!

### The next step

This is super rad, but what if you want to customise all instances of a particular component, like a button or icon?

To do this, we'll need to head back to our `theme.js` file and add another section to our theme object.

You will need to provide the name and class of the component you want to customize. If you're not sure what this is, 
you can find it in the Material UI API documentation in the CSS section. You should be able to see all the 
customisable options. ([Here is the documentation for the Button component](https://material-ui.com/api/button/#css))

Let's override some button style shall we?

In your theme section, below the `palette` object, add an `overrides` object. 
Within your `overrides` object, add the name of the component to be overridden 
(in our case `MuiButton`) and open an object.
In your `MuiButton` object, give it a `root` object. This will be where we play around with the CSS properties.
We'll give the `root` object two values: 
    1. `color: white,` will change the color of the button text to be white
    2. `'&:hover': { backgroundColor: 'purple' }` will apply `background-color: 'purple'` styling when a cursor hovers over it.

Your `theme.js` should now look like this:

```jsx
import { createMuiTheme } from '@material-ui/core/styles';
import indigo from '@material-ui/core/colors/indigo';
import pink from '@material-ui/core/colors/pink';

export default createMuiTheme({
  palette: {
    primary: pink,
    secondary: indigo
  },
  overrides: {
    MuiButton: {
      root: {
        color: 'white',
        '&:hover': {
          backgroundColor: 'purple'
        }
      }
    }
  }
});
```

Save the file and go check out your swanky new AppBar!

## What Now?

With theming, you can easily change lots of components very quickly. Making a theme for your site 
can expedite the styling process and keep it simple and clean.

But there is more to theming than just changing colors on buttons! So test it out! 
Investigate the docs! Make the ugliest website you can imagine! Make the prettiest!

Research a different React Framework. Do they have themes? If so, how is their theming different? 
Is it easier or harder to use?
