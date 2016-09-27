#Meteor Auth

##Objectives

* Discuss user accounts in Meteor
* Install Meteor packages for accounts
* Implement accounts in Meteor app

##Meteor User Accounts

As we've seen, Meteor comes coupled with a ton of features from the get-go. Implementing a real-time web app takes no time at all and in true Meteor form, neither does implementing user accounts.

Meteor comes coupled with a robust built-in accounts system that takes very little to get up and running.

###Users and DDP

A cool thing that Meteor does with our user accounts is store the **userId** field on the DDP connection itself. What this means for us is that when a user is logged in, that user's unique ID is always available no matter where we are in the app code.

####Implementation
We're going to be implementing user accounts with our image-board app from before. The process is pretty straight-forward with Meteor. The first thing we'll need to do is install a couple Meteor packages to allow logging in and signing up.

In the terminal inside our app directory run this command first:

```bash
meteor add accounts-ui accounts-password
```

This will add two packages, **accounts-ui** for a drop-in auth template and **accounts-password** that will allow us to login/signup users with a username and password.

Next we need to configure our auth template to include the correct fields. We'll be doing this in a new **imports/startup** folder.

```bash
mkdir imports/startup
touch imports/startup/accounts-config.js
```

Then in the newly created **accounts-config.js** file:

```javascript
import { Accounts } from 'meteor/accounts-base';
 
Accounts.ui.config({
  passwordSignupFields: 'USERNAME_ONLY',
});
```

Then finally we'll import that config into our client code in **main.js**

```javascript
import '../imports/startup/accounts-config.js';
```

Now lets go checkout our new Auth functionality!

####Accessing Auth Helpers

Now that we've got full autherization in our app we can start utilizing Meteor user helper methods to display certain parts of the page as well as access user data in our code.

First we'll add a new field to our image objects that are getting added to the DB in the **body.js** file. We'll also be importing the main Meteor library to access data:

```javascript
import { Meteor } from 'meteor/meteor';
```

```javascript
Images.insert({
  url,
  createdAt: new Date(),
  owner: Meteor.userId(),
  username: Meteor.user().username
});
```

The two helper methods we're utilizing here are the ```Meteor.userId()```, which allows us to access the unique id of the currently logged in user. And the ```Meteor.user()```, which gives us the ability to interact with the user data object itself, notice the chained on ```username``` property.

Using these in our JS code allows us to write user specific data. These values can be accessed anywhere you import the core Meteor library.

Next we'll setup our view to only allow logged-in users to see the add image form. To do this we'll be using another user accounts helper.

In **body.html** we'll be adding these lines around our form:

```html
{{#if currentUser}}
  <form id="new-cat">
    <input type="text" name="text" placeholder="Enter Cat URL">
  </form>
{{/if}}
```

*{{currentUser}}* is another feature that Meteor auth gives us. When we have auth wired up, we can access **currentUser** in any template to drive UI logic and obscure aspects of our page.

####Oauth

Just like the main Meteor accounts, adding Oauth to our app is as easy as installing a package and adding some configuration. Let's add Facebook Oauth.

First we need to add another accounts package:

```bash
meteor add accounts-facebook
```

Currently there are a few different packages for other Oauth providers:
* Google
* Github
* Twitter
* Meteor

with more on the way!

Once we've installed the necessary package we'll see that our accounts UI has changed to include logging in with Facebook along with instructions on how to get our Oauth setup!
