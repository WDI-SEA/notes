# Intro to Node

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

We'll see that there are functions and patterns unique to Node (for example, the `require` function in Node, which is not available in the browser).

### Setting up a Node Project

1. Create a new folder for your first node project.
```mkdir my-first-node-proj```

Open the folder in your favorite text editor.

2. Initialize Node inside the project folder.

(check the command line prompt to make sure you're actually inside the project folder)
```
npm init
```

You will be prompted to enter values for a number of fields to set up the node project. You can just press enter to accept the default value, or enter specific values if you'd like.

To skip this step in the future (and accept all default values at once), type ```npm init -y```.

What do you notice?

