#OAuth with Passport

##Objectives

* Describe OAuth and its purpose
* Explain how OAuth and Auth are different
* Use Passport strategies for oAuth authorization

## What is OAuth?

You see many sites with buttons that allow for users to sign up with their Facebook or Twitter credentials. OAuth makes all this possible.  

[OAuth](https://en.wikipedia.org/wiki/OAuth) is an agreed-upon set of standards for authorization with a third party service. It involves:

1. Leaving a website
2. Authenticating with the third party
3. Then the third party will redirect the user back to the original website with, among other things, an access token that can be persisted and used to request more information later.

Since OAuth is a set of standards that are universally accepted, there's a whole bunch of libraries we can use to make this happen - like [Passport](http://passportjs.org/)

![facebook-login](https://cloud.githubusercontent.com/assets/40461/9360397/e49b15be-468d-11e5-8b88-3757ca6cbcac.png)

You probably know this as "Login with Facebook": you click on "Login with Facebook", you're redirected to Facebook's application, and then you get back to your site. As a developer, one benefit is your application gets a whole bunch of information it can use - or persist - later on, from Facebook. A downside for the users is that in order to login, they're giving a lot of data to the requesting application. Developers and companies love this, though, because they can use all this data.

#### How it works

To make any of our apps work, we need to first declare our app as a Facebook application using Facebook's [developer interface](https://developers.facebook.com/). Ultimately, we'll be defining the set of permissions / information we are requesting from the user.

A visitor of our website clicks **Login with Facebook**, and leaves our original application and are brought to Facebook - as a developer, you lose everything you had (params from a form, for example).

As a Facebook user, when you login, you pass in two important pieces of information to Facebook: the **app ID** and the **app secret** that identifies the application requesting the information.

After our app is given the OK, Facebook sends back an **access token**. With that access token, Facebook can identify users of our application as real Facebook users. These access tokens only last so long, usually expiring after a week or so, but with this access token we can call out to Facebook, if we want, and get Facebook data associated with that Facebook user.

**IMPORTANT NOTE:** OAuth is an *authorization standard*, which is not the same as authentication. Authentication occurs when you're redirected to Facebook. Authorization occurs when you receive the access token *after* authentication.

###Starting Point

We'll be working off a functioning Express authentication example, which you can find finished here:

https://github.com/WDI-SEA/express-authentication/tree/brian-finished

For OAuth, we'll assume that you've gone through the authentication lecture, and are familiar with sessions, bcrypt, and flash messages in Express.

####Create Facebook app

To get started we need to go to the Facebook developer portal and create an app [https://developers.facebook.com/](https://developers.facebook.com/). Follow the instructions to create an app, and ensure you enable the following configurations:

* Add the **Facebook Login** product
  * Enable **Client OAuth Login**
  * Add `http://localhost:3000/auth/callback/facebook` to **Valid OAuth redirect URIs**

Once you get signed up, add your app id and secret to your `.env` file. We'll also add a variable for our site URL, which will be used in the Passport configuration.

```
FACEBOOK_APP_ID=insertkeyhere
FACEBOOK_APP_SECRET=insertkeyhere
BASE_URL=http://localhost:3000
```

####Add Facebook attributes

OAuth uses an access token that is sent back from the provider to authorize the user. We need to store that token along with the user's identifier from Facebook. We'll need to create a migration to our existing user in order to add these additional columns.

```bash
sequelize migration:create --name addFacebookIdAndToken
```

Add the following to your migration in **migrations/*-addFacebookIdAndToken.js**

```js
'use strict';

module.exports = {
  up: function (queryInterface, Sequelize) {
    // add facebookId and facebookToken as columns
    return queryInterface.addColumn('users', 'facebookId', Sequelize.STRING).then(function() {
      return queryInterface.addColumn('users', 'facebookToken', Sequelize.STRING);
    });
  },

  down: function (queryInterface, Sequelize) {
    // remove facebookToken and facebookId as columns
    return queryInterface.removeColumn('users', 'facebookToken').then(function() {
      return queryInterface.removeColumn('users', 'facebookId');
    });
  }
};
```

Lastly, run this migration.

```bash
sequelize db:migrate
```

####Setup Passport Facebook

To setup the passport middleware, install the following module.

```bash
npm install passport-facebook
```

####Configuring passport-facebook

You'll want to configure your Passport Facebook module within **config/ppConfig.js**. This is a lot of code, so we'll explain the logic using comments.

```js
// at the very top, require the passport-facebook strategy
var FacebookStrategy = require('passport-facebook').Strategy;

/*
 * Below the LocalStrategy, setup passport to use the FacebookStrategy.
 * We'll need to pass along the app id, app secret, and callback URL from
 * environment variables. We'll also want to define the fields we're
 * getting from Facebook, and enabling proof, which tells Facebook to
 * check the client secret in order to verify our server
 */
passport.use(new FacebookStrategy({
  clientID: process.env.FACEBOOK_APP_ID,
  clientSecret: process.env.FACEBOOK_APP_SECRET,
  callbackURL: process.env.APP_URL + '/auth/facebook/callback',
  profileFields: ['id', 'email', 'displayName'],
  enableProof: true
}, function(accessToken, refreshToken, profile, cb) {
  /*
   * This function we're inside will be called once our user is authenticated
   * by Facebook. We can access our token and profile, as well as run a callback
   * function that accepts an error and a user
   */

  // pull the email from the user's Facebook profile, if it exists
  var email = profile.emails ? profile.emails[0].value : null;

  // see if the user exists in the database by email
  db.user.find({
    where: { email: email },
  }).then(function(existingUser) {
    // if the user with a valid email exists already, link their existing account with their Facebook.
    if (existingUser && email) {
      existingUser.update({
        facebookId: profile.id,
        facebookToken: accessToken
      }).then(function(updatedUser) {
        cb(null, existingUser);
      }).catch(cb);
    } else {
      // if the user doesn't exist, findOrCreate the user on the user's Facebook id
      db.user.findOrCreate({
        where: { facebookId: profile.id },
        defaults: {
          facebookToken: accessToken,
          name: profile.displayName,
          email: email
        }
      }).spread(function(user, created) {
        // if the user is created, we're done
        if (created) {
          return cb(null, user);
        } else {
          // if the user wasn't created, they exist. Update their access token
          user.facebookToken = accessToken;
          user.save().then(function() {
            cb(null, user);
          }).catch(cb);
        }
      }).catch(cb);
    }
  }).catch(cb)
}));
```

[profileFields documentation](https://developers.facebook.com/docs/graph-api/reference/user)

####Setup authentication routes

In **controllers/auth.js**, we can use `passport.authenticate` to setup two Facebook authentication routes. The first route will redirect the user to Facebook for authentication (`GET /auth/facebook`). The second route is the *callback route* that will be called by Facebook, once the user is authenticated.

```js
router.get('/facebook', passport.authenticate('facebook', {
  scope: ['public_profile', 'email']
}));

router.get('/facebook/callback', passport.authenticate('facebook', {
  successRedirect: '/',
  failureRedirect: '/auth/login',
  failureFlash: 'An error occurred, please try later',
  successFlash: 'You have logged in with Facebook'
}));
```

**Scope**

The scope is how we ask for additional access to the user's facebook account. To facilitate login we need "public_profile" and "email", but we can ask for any level of access depending on our needs including the ability to post to the user's wall or ask for info about their posts or friends.

More info: [Facebook scope documentation](https://developers.facebook.com/docs/facebook-login/permissions/v2.3)

####Adding Facebook Login Functionality

In order to login via Facebook, the last piece in the puzzle is a button to access `GET /auth/facebook`.

Add the following to the bottom of **auth/login.ejs**, outside the form.

```html
<a href="/auth/facebook" class="btn btn-primary">
  Login via Facebook
</a>
```

## Notes when testing

* Ensure that your app is running using `foreman`.
* Try testing login under various conditions.
* For more security, you can choose to delete the `facebookToken` when converting the user to JSON.
* You may run into issues with Facebook authentication. Be patient and debug if encountered.
