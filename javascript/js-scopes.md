# Scoping

## Objectives

* Describe the purpose and functionality of IIFEs
* Use namespaces to protect data and limit global impact of objects and variables.
* Use IIFEs to hide "private" data

As we saw with constructors and prototypes, JavaScript features design patterns attempt to organize and modularize code. Before we continue to inheritance with prototypes, let's take a look at a couple other **important** design patterns.

## Namespacing

When multiple files are being used, it can be a major issue when global variables start conflicting. To avoid this, we introduce namespaces, which are not a native concept to JavaScript. Namespaces are contianers used to organize data. They can help limit global impact of variables and provide data protection.

Since namespaces aren't a native concept to JavaScript, they are commonly implemented as objects. For example:

```javascript
var myNameSpace = {
  list: ["Brian", "Lenny", "Daniel", "Sarah"],
  printList: function() {
    this.list.forEach(function(item) {
      console.log(item);
    });
  }
};
```

Notice that we are using the `this` keyword to refer to our wrapper and namespace. Also, the namespace will now act as a barrier that protects our variables `list` and `printList`. This is very very useful for very large applications, where we may accidentally create another variable called `list` \(which would create a conflict\)

To make things even cooler, you can nest namespaces inside each other as well \(but you probably already knew that, since they're just objects\).

### Try It

Create a namespace and call it your first name. Then, add these four properties:

* name
* friends \(as an array\)
* age
* a function that says "Hello, \[your name\]"

## Closures

So far, our module has only public properties. This means that someone can access our namespace and it's properties - what if we don't want that? What if we want to protect values? First we decide which should be public and private. Let's look at this example.

```javascript
var bankAccount = {
  cash: 1000,
  pin: 1234
}
```

Let's say that I want the ability to retrieve cash from this bank account, but **only** if I have the right pin. Unfortunately, it's really easy to see the pin by typing the following code:

```javascript
console.log(bankAccount.pin);
```

It's also really easy to empty the account!

```javascript
bankAccount.cash = 0;
```

We need to make these variables private. To 'privatize' properties, we can use what's called a closure, which is a function inside a function.

#### Bank Account via Closure

```javascript
function bankAccount() {
  var cash = 1000;
  var pin = 1234;

  function withdraw(amount, enteredPin) {
    if (enteredPin === pin) {
      cash -= amount;
    }
  }

  function balance() {
    console.log(cash);
  }

  //returning functions in an object so we can access them
  return {
    withdraw: withdraw,
    balance: balance
  }
}

// create a new bank account and withdraw 30
var account = bankAccount();
account.withdraw(30, 1234);

// returns 970
account.balance();

// returns 970 again because the pin failed
account.withdraw(30);
account.balance();

// both return undefined
account.pin
account.cash
```

**Why does this work?**

* `cash` and `pin` only exist inside the `bankAccount` function.
* By creating closures, the inside functions `withdraw` and `balance` have access to `cash` and `pin`.
* By returning closures, we can access the inside functions without directly accessing `cash` and `pin`.

Note that most languages do not implement the idea of **private** data in this manner. JavaScript, again, is one of the few exceptions.

## IIFEs

Note that we had to **call** the `bankAccount` function before we started using it. An alternative is to create an **Immediately-Invoked Function Expression \(IIFE\)**. Yikes! That's a fancy term for a function that's executed immediately after it's created. We can make the `bankAccount` an IIFE by wrapping it in parentheses, then **calling the function** with two additional parentheses at the end.

```javascript
var account = (function bankAccount() {
  var cash = 1000;
  var pin = 1234;

  function withdraw(amount, enteredPin) {
    if (enteredPin === pin) {
      cash -= amount;
    }
  }

  function balance() {
    console.log(cash);
  }

  return {
    withdraw: withdraw,
    balance: balance
  }
})();
```

Note that this syntax does have a drawback. We can only create one instance! Therefore, IIFEs are generally used with **singletons**. Singleton, meaning that there's only one instance of the expression.

#### Try It

Create an IIFE by using the one above as a pattern. Call the function `people` and assign the expression to a variable \(you can name it whatever you like\). The IIFE should have the following variables \(as arrays\):

* friends
* siblings

And it should return the following public functions:

* addFriend - pushes a name to the friends array
* viewFriends - prints the friends array
* viewSiblings - prints the siblings array

Note that we'll be protecting the siblings array by not allowing siblings to be added.

### Why have IIFEs?

IIFEs provide another way to protect data and limit the global impact of variables inside the IIFE. Since IIFEs are singletons, they're often used when creating modules, such as libraries.

Take a look at the top of the jQuery source code. Guess what, jQuery is one big IIFE!

[https://code.jquery.com/jquery-2.2.0.js](https://code.jquery.com/jquery-2.2.0.js)

## IIFE Arguments

What happens if we have a global variable outside of our IIFE, and we want to use it? A good example would be the `bankAccount`. Maybe we'd like to initialize the account with our own value for `cash`.

Luckily, IIFEs are just functions that are called right away, so it's possible to define parameters if arguments need to be passed in. Here's our final modified `bankAccount` IIFE.

```javascript
var account = (function bankAccount(initialCash, initialPin) {
  var cash = initialCash;
  var pin = initialPin;

  function withdraw(amount, enteredPin) {
    if (enteredPin === pin) {
      cash -= amount;
    }
  }

  function balance() {
    console.log(cash);
  }

  return {
    withdraw: withdraw,
    balance: balance
  }
})(70000, 0000);
```

Not bad! Take another look at the jQuery source code. You'll see that importing global variables as arguments is also done in the source code.

## More Reading

If you would like to learn more about design patterns in JavaScript check out these sources, they are advanced but incredibly valuable.

[JavaScript Allonge](https://leanpub.com/javascript-allonge)

[Learning JavaScript Design Patterns](http://addyosmani.com/resources/essentialjsdesignpatterns/book/)

[Understanding Closures with Ease](http://javascriptissexy.com/understand-javascript-closures-with-ease/)

