#Auth in Practice

##Objectives

* Understand different Node packages separately
* Incorporate multiple packages into a working authentication setup
* Use flash messages for one-time user notifications

###Note

This codealong relies heavily on an app that's been scaffolded with signup and login routes. Once we're done, you should have a starting point for your project. Due to this, we won't be forking the repo, but instead cloning the repo and performing the following:

* Removing the `.git` folder
* Reinitializing your git repo by running `git init` and adding your project's remote to the repo
* Renaming the databases from `express_auth` to `yourprojectname`
* Renaming the `package.json` file to include your project name
* Changing the `README.md` to reflect your project

**Repo Link:** https://github.com/WDI-SEA/express-authentication

##Getting Started

We have provided a starting scaffold with the following routes.

* `GET /` - home page
* `GET /profile` - a page we should show only to logged in users (but is currently visible)
* `GET /auth/login` - a login form
* `GET /auth/signup` - a user signup form

Dependencies such as express, ejs, and sequelize are included in this app. Follow the instructions provided in order to setup the application.

##Test-Driven Development

This project is also setup with tests for the authentication functionality we'll be implementing. We'll go one step at a time and make all the tests pass.

* Run `npm test` to run all tests
* Run `NODE_ENV=test node_modules/mocha/bin/mocha tests/fileName.js` to run a specific file

###Laundry List

1. Create a user model to store the user's name, email, and password, complete with validations
2. Create functions to hash the user's password, validate the password, and protect the password
3. Add functionality to have users sign up for an account
  * Check if e-mail already registered
    * Creates new user if not registered
  * Redirects back to the signup page if errors occur
4. Set up sessions middleware, so we can remember that users are logged in
5. Add functionality to have users log in
  * Setup Passport configuration
    * Retrieving and saving users
    * Verifying if a user's email and password are correct
6. Add functionality to have users log out
7. Create middleware for protecting pages
8. Add flash messages as Bootstrap alerts
