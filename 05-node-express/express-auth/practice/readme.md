# Auth in Practice

## Objectives

* Incorporate multiple packages into a working authentication setup
* Use flash messages for one-time user notifications
* Implement middleware to simplify and automate repetitive tasks

### Note

This codealong relies heavily on an app that's been scaffolded with signup and login routes. Once we're done, you should have a starting point for your project. Due to this, we'll be using Github template feature, to turn this express-authentication into a template.
When starting a new project, you'll want to create a new repo on github and choose `express-authentication` as your template. 
After this, you'll want to take a few steps to customise your new project.

* `git clone` your new project onto your local repo.
* `npm install` to install dependencies
* Customise your `layout.ejs`, `package.json`, and `README.md` to reflect your project.
* Create a new Database for your project
* Update your `config.json` file.
* Check the models and migrations for relevance to your project's needs
* Add a `.env` file with at least a `SESSION_SECRET`.

**Repo Link:** https://github.com/WDI-SEA/express-authentication

## Getting Started

We have provided a starting scaffold with the following routes.

* `GET /` - home page
* `GET /profile` - a page we should show only to logged in users (but is currently visible)
* `GET /auth/login` - a login form
* `GET /auth/signup` - a user signup form

Dependencies such as express, ejs, and sequelize are included in this app. Follow the instructions provided in order to setup the application.

## Test-Driven Development

This project is also setup with tests for the authentication functionality we'll be implementing. We'll go one step at a time and make all the tests pass.

* Run `npm test` to run all tests
* Run `NODE_ENV=test node_modules/mocha/bin/mocha tests/fileName.js` to run a specific file

### Laundry List

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
8. Add flash messages as partials
