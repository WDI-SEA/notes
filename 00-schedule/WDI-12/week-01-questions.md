# Week 01 Questions 
Here are questions asked at the end of Week 1 after completing the
Tic-Tac-Toe assignment.

### What's the difference Between innerHTML and textContent?
`innerHTML` will allow you to enter a String with HTML elements and it
will render the content as actual HTML. If you set it to `"<h1>Welcome</h1>"`
then an actual big header will appear on the page.

`textContent` only accepts text... If you set it to `"<h1>Welcome</h1>"`
you will only see it as text on the page.

It is generally better to use `textContent`. If you want to add actual HTML
to the page there are other ways to do this.

### Sorting alphabetically objects in array by name
Sorting objects inside an array can be tricky. You can't use the default `.sort()`
method by itself because JavaScript doesn't know how you want the objects sorted.

Consider an array representing people with names and ages. If you call .sort()
should the array sort them alphabetically by their name, or should it sort them
by their age?

If it sorts them by their age should it sort them from youngest to oldest, or oldest
to youngest?

We can specify how exactly the array should be sorted by passing a function to the
sort method. The function accepts two parameters. The function represents how to
compare any two things in the list.

```js
var people = [{name: "Susan", age: 32}, {name: "Alice", age: 14}, {name: "Bob", age: 45}]

// sort the people by their names alphabetically
people.sort(function(a, b) {
  return a.name > b.name;
});

// sort the people by their ages from youngest to oldest
people.sort(function(a, b) {
  return a.age > b.age;
});

// sort the people by their ages from oldest to youngest
people.sort(function(a, b) {
  return a.age < b.age;
});
```

### Is there a function to return the id of a clicked div?
Yes! Whenever you add an event listener the function is passed
a parameter that represents the event.

The event has properties
on it that allow you to get the mouse position, information about
the keyboard and a reference to the HTML element you clicked on.

To get a reference to an element you clicked on, accept a parameter
in your event listener function (usually the parameter is called `e`
or `ev`) and access the `e.target` property. The `target` property has
a reference to the HTML element that was clicked on.

```html
<div id="first">The 1st div</div>
<div id="second">The 2nd div</div>
<div id="third">The 3rd div</div>
```

```js
var divs = document.getElementsByTagName("div");
for (var i = 0; i < divs.length; i++) {
  var div = divs[i];
  div.addEventListener("click", identifyDiv);
}

function identifyDiv(e) {
  var div = e.target;
  var id = div.id;

  if (id === "first") {
    console.log("you clicked on the 1st div");
  } else if (id === "second") {
    console.log("you clicked on the 2nd div");
  } else if (id === "third") {
    console.log("you clicked on the 3rd div");
  }
}
```

### Use of `this`
`this` is a special keywork in JavaScript that we haven't learned yet. Wait
until we learn about objects on Week 2 Day 2 to learn more.

### When should we use parenthesis when calling a function?
Always use parenthesis when executing a function. Write things between parenthesis
when you're passing parameters to the function.

This `displayWelcomeMessage` function is an example of a function without
parameters.  The function simply encapsulates the behavior of displaying a
welcome message. It makes it easy for us to display a welcome message without
having to rewrite this code all the time.

Even though the function doesn't have parameters, we still need to use the
parenethesis to show we're calling the function.

```js
function displayWelcomeMessage() {
  var banner = document.getElementById("banner");
  banner.textContent = "Welcome to my website!"
}

displayWelcomeMessage();
```

This `multiply` function needs parameters. We pass in numbers between the parenthesis
when calling the function.

```js
function multiply(a, b) {
  return a * b;
}

multiply(3, 4);
```

Don't use parenthesis when you're hooking a function up to an event Listener.
The event listener only need to know the name of the function. 

```
function logClick() {
  console.log("the document was clicked");
}

document.addEventListener("click", logClick);
```

### Why do some "built in" functions not work and show up as ___.function is
not a function?

This sounds like you're trying to treat a property like a function. Try accessing
the same property without parenthesis. Remember, parenthesis mean you're calling
a function!

```js
var h1 = document.getElementById("header");
h1.textContent("treating textContent like a function will cause the error!!");

// use the equals sign to set the textContent instead.
h1.textContent = "treating textContent like a function will cause the error!!";
```

### When should we use `return` instead of `console.log`?
`console.log` only prints things out to the console. `return` actually passes
a value back from a function.

`return` allows you to pass values back from a function, save them in a variable
and use them later throughout your program.

```js
function double(n) {
  return n * 2;
}

// this prints 4 because values were returned from the function and added together
console.log(double(1) + double(1))
```

### Why doesn't `getElementById`, `getElementsByClassName` doesn't work for all situations?
`getElementById` only gets one item. `getElementsByClassName` returns a list of all elements
with the given class.
