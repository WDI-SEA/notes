#Auth in Practice

##Objectives

* Understand different Node packages separately
* Incorporate multiple packages into a working authentication setup
* Use flash messages for one-time user notifications

###Note

This codealong relies heavily on an app that's been scaffolded with signup and login routes. Please fork and clone here: https://github.com/WDI-SEA/express-auth

##Getting Started

A basic application with no database has been provided to you, with the following routes:

* `GET /` - home page
* `GET /secret` - a page we should keep secret (but is currently visible)
* `GET /auth/login` - a login form
* `POST /auth/login` - the route where our login form data will be sent to
* `GET /auth/signup` - a user signup form
* `POST /auth/signup` - the route where our user signup data will be sent to

Currently, the POST routes send back the form data to the browser. We'll be modifying this application to provide full, secure authentication.

###Laundry List

1. Create a user model, to store the user's name, email, and password
2. Test the user model
3. Add functionality to the signup POST route (`POST /auth/signup`)
  * Check if e-mail already registered
    * Creates new user if not registered
  * HASH THE PASSWORD
    * We'll use `bcrypt` and a `beforeCreate` hook
    * We'll also add password validations
4. Set up sessions middleware, so we can remember that users are logged in
5. Add functionality to the login POST route (`POST /auth/login`)
  * Create a function to check if the password matches
  * Check e-mail / password against database
    * Log in the user if valid (create a session)
6. Create a GET /auth/logout route (clears the session)
7. Create getUser() method (as middleware)


**Before getting started, fork/clone the starter app, install packages, and make sure the app works**
