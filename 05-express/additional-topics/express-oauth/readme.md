#OAuth with Passport

##Objectives

* Describe OAuth and its purpose
* Use Passport strategies for authentication

## What is OAuth?

You see many sites with buttons that allow for users to sign up with their Facebook or Twitter credentials.  OAuth makes all this possible.  

[OAuth](https://en.wikipedia.org/wiki/OAuth) is an agreed-upon set of standards for logging in through a third party service. It involves:

1. Leaving a website
2. Authenticating with the third party
3. Then the third party will redirect the user back to the original website with, among other things, an authentication token that can be persisted and used to request more information later.

Since OAuth is a set of standards that are universally accepted, there's a whole bunch of libraries we can use to make this happen - like [Passport](http://passportjs.org/)

![facebook-login](https://cloud.githubusercontent.com/assets/40461/9360397/e49b15be-468d-11e5-8b88-3757ca6cbcac.png)


You probably know this as "Login with Facebook": you click on "Login with Facebook", you're redirected to Facebook's application, and then you get back to your site.  As a developer, one benefit is your application gets a whole bunch of information it can use - or persist - later on, from Facebook. A downside for the users is that in order to login, they're giving a lot of data to the requesting application. Developers and companies love this, though, because they can use all this data.

#### How it works

To make any of our apps work, we need to first declare our app as a Facebook application using Facebook's [developer interface](https://developers.facebook.com/). Ultimately, we'll be defining the set of permissions / information we are requesting from the user.

A visitor of our website clicks **Login with Facebook**, and leaves our original application and are brought to Facebook - as a developer, you lose everything you had (params from a form, for example).

As a Facebook user, when you login, you pass in two important pieces of information to Facebook: the **app ID** and the **app secret** that identifies the application requesting the information.

After our app is given the okay, Facebook sends back an **access token**. With that access token, Facebook can identify users of our application as real Facebook users. These access tokens only last so long, usually expiring after a week or so, but with this access token we can call out to Facebook, if we want, and get Facebook data associated with that Facebook user.

###Starting Point

For OAuth, we'll assume that you've gone through the authentication lecture, and are familiar with sessions, bcrypt, and flash messages in Express. The starter code is an application with signup/login routes and a page that can only be accessed when logged in. Take a look at the application and verify that it works (you'll have to go through the usual motions, like installing the npm modules, creating/migrating the database, etc.).

We'll be using the following modules as we add Passport and two strategies: Local and Facebook. Install the following modules:

* passport
  * a npm module for implementing OAuth using multiple different providers
* passport-local
  * a Passport strategy for local authentication (We'll modify our current application to use this. Note that this does not use OAuth)
* passport-facebook
  * a Passport strategy for Facebook authentication (using OAuth)

####Load/Initialize passport

add to the top of **index.js**

```js
var passport = require('passport');
```

Load middleware

```js
app.use(passport.initialize());
app.use(passport.session());
```

####Serialization functions

You need to define how passport should keep track of users. This will store the user id in the session and re-query the database for the other info as needed. It uses the sequelize `.get()` method to get a clean user object.

```js
passport.serializeUser(function(user, done) {
  done(null, user.id);
});

passport.deserializeUser(function(id, done) {
  db.user.findById(id).then(function(user) {
    done(null, user.get());
  }).catch(done);
});
```

**Note:** Since passport utilizes a lot of callback functions, we can organize these functions into a configuration file. If done, your code will look something like this:

**index.js**
```js
var strategies = require('./config/strategies');

passport.serializeUser(strategies.serializeUser);
passport.deserializeUser(strategies.deserializeUser);
```

**config/strategies.js**
```js
var db = require('../models');

module.exports = {
  serializeUser: function(user, done) {
    done(null, user.id);
  },
  deserializeUser: function(id, done) {
    db.user.find(id).then(function(user) {
      done(null, user.get());
    }).catch(done);
  }
};
```

##Local Authentication (email / password)

You can use passport for basic authentication (email / password). Usually, if you are allowing for login via oAuth you'll want to provide e-mail/password as an alternative unless your product hinges on the oAuth connection.

source: [passport docs](http://passportjs.org/guide/username-password/)

####Setup proccess

* install `passport-local` (already done in starter code)
* Setup user model (already done in starter code)
* Require strategy
* Setup middleware strategy

##Setup User Model

To prepare for using passport, the user model needs to be able to encrypt and check the password. This is done via a `beforeCreate` hook, which is already in the starter code.

####Check password

To check the password we will add an instance method to the model called `checkPassword()`. This method will be availble on every insance of a user. Note that this varies from the `authenticate` class method, which belongs specifically to the `user` model (no instance).

```js
instanceMethods: {
  checkPassword: function(password, callback) {
    if(password && this.password){
      bcrypt.compare(password, this.password, callback);
    } else {
      callback(null, false);
    }
  }
}
```

If you'd like, the other `authenticate` class method can be deleted once we implement the local strategy.

##Add LocalStrategy middleware

We already installed `passport-local` via npm, so now let's require it near the top of index.js

```js
var LocalStrategy = require('passport-local').Strategy;
```

Then the local strategy using needs to be set up as middleware and we have to add code inside of its callback to use Sequelize to check the e-mail/password.

The logic for this strategy:

* Specify the username field as the first parameter
* Specify the function needed to authenticate the user
  * Find the user and check its password
    * if valid with no errors, return the user in the callback
    * if invalid/errors, return the error in the callback

Note that this strategy can be separated into a config file like the serialize/unserialize functions.

```js
passport.use(new LocalStrategy({
    usernameField: 'email'
  },
  function(email, password, done) {
    db.user.find({where: {email: email}}).then(function(user) {
      if (user) {
        user.checkPassword(password, function(err, result) {
          if (err) return done(err);
          if (result) {
            done(null, user.get());
          } else {
            done(null, false, {message: 'Invalid password'});
          }
        });
      } else {
        done(null, false, {message: 'Unknown user'});
      }
    });
  }
));
```

Once the strategy is configured, we can use it in the controllers to authenticate users.

####Handling login action

Set up a login post route (replacing the old one) by requiring passport and using its `authenticate` function to authenticate the user

The logic we use:

* authenticate the user using the local strategy
  * if the user is successfully authenticated, login the user and redirect after success
  * if the user is not authenticated, redirect back to the login page

**controllers/auth.js**

```js
router.post('/login',function(req,res){
  passport.authenticate('local', function(err, user, info) {
    if (user) {
      req.login(user, function(err) {
        if (err) throw err;
        req.flash('success', 'You are now logged in.');
        res.redirect('/');
      });
    } else {
      req.flash('danger', 'Error');
      res.redirect('/auth/login');
    }
  })(req, res);
});
```

####Adding logout

To log users out you simply need to call `req.logout()` in your logout route and then redirect them to the home page. You may also want to add a flash message.

**controllers/auth.js**

```js
router.get('/logout', function(req, res) {
  req.logout();
  req.flash('info', 'You have been logged out.');
  res.redirect('/');
});
```

####Checking authentication

Passport adds a function `req.isAuthenticated()` to check if the user is logged in. It will return a boolean true or false.

Passport also adds `req.user` which will contain the user object created in the `deserializeUser` method (defined above). This will be the user object.

##Facebook oAuth

Setting up passport to handle OAuth login for any social network is roughly the same. As an example, we're going to walk through setting up Facebook login.

####Setup proccess

* Create Facebook app
* Add providers model
* Install passport-facebook
* Load strategy requirement
* Setup middleware strategy

####Create Facebook app

To get started we need to go to the facebook developer portal and create an app [https://developers.facebook.com/](https://developers.facebook.com/).

Once you get signed up add your tokens to your `.env` file.

####Add providers model

oAuth uses a token that is sent back from the provider (Facebook, etc) to authenticate the user. We need to store that token along with the user data. This COULD be done as a column in the user table, but generally it is done by creating another model so each user HAS MANY providers (Facebook, Twitter, etc.) which allows for flexibility in adding additional providers in the future and keeps access

```bash
sequelize model:create --name provider --attributes pid:string,token:string,type:string,userId:integer

sequelize db:migrate
```

Then create a one to many relationship between users and providers in the association section of the models.

```js
//provider model
models.provider.belongsTo(models.user);

//user model
models.user.hasMany(models.provider);
```

####Require facebook strategy

```js
var FacebookStrategy = require('passport-facebook').Strategy;
```

####Setup middleware strategy

OAuth requires an absolute callback url. To make this adapt between development and production environments we need to create an environment variable to store the base url for our app.

in **.env**

```
BASE_URL=http://localhost:3000
```

Then we can initlize our strategy (note that this is a lot of code!)

The logic behind this strategy:

* Specify configuration as the first parameter (API keys, callback URL, profile fields to access)
* Specify the function needed to signup the user with Facebook
  * see if a Facebook provider exists for the user
    * if a provider exists, save the new access token and exit
    * if a provider doesn't exist, create a new provider with the email from Facebook
      * if there's already a user with the email as a user, exit with an error message
      * if the user's email is unique, create a new provider for this new user, and exit

```js
passport.use(new FacebookStrategy({
    clientID: process.env.FACEBOOK_APP_ID,
    clientSecret: process.env.FACEBOOK_APP_SECRET,
    callbackURL: process.env.BASE_URL + '/auth/callback/facebook',
    profileFields: ['email', 'displayName']
  },
  function(accessToken, refreshToken, profile, done) {
    db.provider.find({
      where: {
        pid: profile.id,
        type: profile.provider
      },
      include: [db.user]
    }).then(function(provider) {
      if (provider && provider.user) {
        provider.token = accessToken;
        provider.save().then(function() {
          done(null, provider.user.get());
        });
      } else {
        var email = profile.emails[0].value;
        db.user.findOrCreate({
          where: {email: email},
          defaults: {name: profile.displayName}
        }).spread(function(user, created) {
          if (created) {
            user.createProvider({
              pid: profile.id,
              token: accessToken,
              type: profile.provider
            }).then(function() {
              done(null, user.get());
            })
          } else {
            done(null, false, {message: 'You already signed up with this email address. Please login'});
          }
        });
      }
    });
  }
));
```

[profileFields documentation](https://developers.facebook.com/docs/graph-api/reference/user)

####Setup login route

Using URL parameters, we can create a versatile login route that will work for facebook or any future oAuth strategies.

```js
router.get('/login/:provider', function(req, res) {
  passport.authenticate(
    req.params.provider,
    {scope: ['public_profile', 'email']}
  )(req, res);
});
```

This will trigger the passport facebook module which will redirect the user to facebook and get their permission. Once they agree to allow access they will be redirected back to our callback route which we will create next.

**Scope**

The scope is how we ask for additional access to the user's facebook account. To facilitate login we need "public_profile" and "email", but we can ask for any level of access depending on our needs including the ability to post to the user's wall or ask for info about their posts or friends.

More info: [Facebook scope documentation](https://developers.facebook.com/docs/facebook-login/permissions/v2.3)

####Setup callback route

We also need to create a callback route. This is where facebook will redirect the user after they have agreed to give our app permission to access their facebook account info.

Again, we will use URL parameters to make this work for any oAuth strategy.

```js
router.get('/callback/:provider', function(req, res) {
  passport.authenticate(req.params.provider, function(err, user, info) {
    if (err) throw err;
    if (user) {
      req.login(user, function(err) {
        if (err) throw err;
        req.flash('success', 'You are now logged in with ' + req.params.provider);
        res.redirect('/');
      });
    } else {
      req.flash('danger', 'Error');
      res.redirect('/auth/login');
    }
  })(req, res);
});
```

The majority of the code is identical to the LocalStrategy login code we added earlier. Again, this can be DRY'd up by separating these functions into a separate configuration file.

####Logout

Logout for oAuth uses the exact same code as LocalStrategy so no changes are needed. We just have to call `req.logout()` which will invalidate the user's session.
