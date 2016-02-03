![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

#Scoping with Namespaces and IIFEs

##Objectives

* Use namespaces to protect data and limit global impact of objects and variables.
* Understand the purpose and functionality of IIFEs
* Use IIFEs to hide "private" data

## Namespacing

When multiple files are being used, it can be a major issue when global variables start
conflicting. To avoid this, we introduce namespaces, which are not a native concept to
JavaScript. Their purpose is to limit global impact and provide data protection.

To start, create an object around your namespace. All of our variables and functions
will now be properties of this object. For example:

```js
var MYNAMESPACE = {
    list: ["Brian", "Lenny", "Daniel", "Sarah"],
    count: function() {
      for (var i = 0; i < this.list.length; i++) {
      console.log(this.list[i])
      };
    }
}
```

Notice that we are using the `this` keyword to refer to our wrapper and namespace.
All of our native variables and methods will use `this`. The namespace will now act as a
barrier in the global scope. This is very very useful for very large applications.

To make things even cooler, you can nest namespaces inside each other - which is very common
in the module pattern.

**TL;DR:** Namespaces limit the scope of our data. Since they're not native to JavaScript,
we use JavaScript objects.

### Try It

Create a namespace and call it your first name. Then, add these four properties:
* name
* friends (as an array)
* age
* a function that says "Hello, [your name]"


## Closures

So far, our module has only public properties. This means that someone can access our
namespace and it's properties - what if we don't want that? What if we want some privacy?
First we decide which should be public and private. Let's look at this example.

```js
var MYNAMESPACE = {

  // This can be public, I don't mind other people messing with this
  friends:["Lenny", "Daniel"],

  // This array should be private!
  siblings: ["Jackie", "James"],

  // a function manipulate my friends array - let's make that public
  addFriends: function(){},

  // a function to add siblings... let's make that public as well
  addSiblings: function(){}
}
```

To 'privatize' properties we can use a closure! First, let's introduce some terminology and
syntax.

To 'privatize' properties, we use something called a **Immediately-Invoked Function
Expression (IIFE)**. Yikes! That's a fancy term for a function that's executed immediately
after it's created.

IIFEs are important because we can create a function that contains private variables, but
only returns public variables. The public variables belong to the namespace, but the private
variables belong to the IIFE. Here's the syntax:

```js
(function(){
    // all your private attributes here
    var privateKey = '...';
    var secretPassword = '...';

    // all your public attributes here, which are returned as an object for your use
    return {
      publicKey: 'asdfjkl;',
      message: "Hi!"
    }

})();
```

So let's go back to MYNAMESPACE. First, we wrap our code in an IIFE and create some
local variables that will be closed up into the namespace - so now it looks like this:

```js
var MYNAMESPACE = (function(){

  // PUT OUR PRIVATE METHODS ON THE TOP

  // This array should be private! This property will only belong to the function instead of directly to the namespace
  var siblings = ["Jackie", "James"];


  // PUT OUR PUBLIC METHODS HERE IN AN OBJECT WHICH BECOMES THE NAMESPACE

  return {

  // This can be public, I don't mind other people messing with this
  friends: ["Lenny", "Daniel"],

  // a function to see my siblings array - let's make that public
  seeSiblings: function(){
    console.log(siblings);
  },

  // a function to add a sibling
  addSibling: function(name) {
    siblings.push(name);
  }
 };
})();
```

Our sensitive data is private by closure and our public properties are accessible through
the namespace!

### Try It

Create a namespace similar to the one above, where siblings are private and friends are
public. In addition, there should be two functions: seeSiblings and addSibling. Once finished,
try to see if you can access siblings directly (without calling seeSiblings).

## Global Imports

What happens if we have a global variable outside of our namespace? If we have multiple
nested variables, this becomes very tricky and expensive to search up all the way to the
global namespace! So how can we import global variables to our namespace? It's also
essential for other people working on your code, to see in what scope your variables are
located in.

For clearer faster global modules we use imports. For every global variable that you import,
add it as a parameter in your IIFE and then in the function invocation - pass in the global
variable! You can now modify the value without touching the global namespace!

```js
var taco = "I love tacos";

var MYNAMESPACE = (function(foo){

  var siblings = ["Jackie", "James"];
  siblings.push(foo);

return {

  friends: ["Lenny", "Sarah"],

  addFriends: function(){
    console.log(siblings);
  }
 };
})(taco);
```

## More Reading

If you would like to learn more about design patterns in JavaScript check out these sources, they are advanced but incredibly valuable.

[JavaScript Allonge](https://leanpub.com/javascript-allonge)

[Learning JavaScript Design Patterns](http://addyosmani.com/resources/essentialjsdesignpatterns/book/)
