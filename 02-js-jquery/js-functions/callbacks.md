# Callback Functions

Functions may seem very different than the other javascript items we've worked with before, but don't be fooled! Functions are still _first-class_ values, which means you can
* store them in variables
* **pass them as arguments to other functions**
* create them within functions
* return them from functions

If this all seems very strange, you could think of a javascript function as a _javascript_ object that stores code to be run instead of key/value pairs. A **callback function** is just a regular function that we pass as an argument to another function! Let's look at an example.