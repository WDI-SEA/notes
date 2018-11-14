#Introduction to Node.js and Express

## Objectives
* Use the node package manager to install and save modules
* Describe what data is found in package.json
* Create Express routes that utilize parameters and form middleware
* Contrast and implement different HTTP verbs through Express routes
* Implement and explain the components of a basic Express app

## Review: Client-Server

* What's the front-end (client side)?
  * Broswer
  * User interface
  * Html, CSS, Javascript
* What's the back-end (server-side)?
  * what's going on behind the scenes
  * data transactions/business logic
    * C - sign up for a facebook account
    * R - display all of your facebook friends
    * U - change your facebook password
    * D - delete your facebook account
* Why do we need a back-end?
  * efficiency and security
    * lighten up front end load
    * manage data securely

## Node
Node is a platform that uses JavaScript for creating network applications.

But wait! Isn't Javascript is a _front-end_ language written for browsers? Yes! This is the beauty of Node. It gives us a server-side environment that can handle logic written in Javascript. It allows JavaScript to be run on a server.

We'll see that there are functions and patterns unique to Node (for example, the `require` function in Node, which is not available in the browser). Let's go over some unique aspects of Node before we get started with Express.
