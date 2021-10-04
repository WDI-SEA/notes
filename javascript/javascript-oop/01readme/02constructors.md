# Constructors

Before we examine constructors, let's review. There are a few different ways to create objects.

**Object Literal Notation**

```javascript
// Object Literal notation uses `var` and `:`
var instructor = {
  name: "Elie",
  age: 26
};

// Or (notice the use of the keyword "new")
var instructor = new Object();

instructor.name = "Elie";
instructor.age = 26;
```

## Problems with Object Literal Notation

Imagine you're an architect and you're tasked with designing a blueprint for a house \(which will be used to build 25 similar looking houses\). If we assume that every house has a number of square feet, bathrooms and bedrooms we can model this with a few objects.

```javascript
var house1 = {
  sqFeet: 3000,
  bathrooms: 3
  bedrooms: 2
};
var house2 = {
  sqFeet: 4000,
  bathrooms: 3.5
  bedrooms: 2
};
var house3 = {
  sqFeet: 1000,
  bathrooms: 2
  bedrooms: 1
};
var house4 = {
  sqFeet: 13000,
  bathrooms: 3.5
  bedrooms: 7
};
```

Unfortunately, this is not very efficient. We've created 4 houses and already it's taken almost 20 lines of code. Fortunately we can create a constructor as our "blueprint" and then create objects based off of that. To create a constructor in JavaScript, we need to take advantage of **functions** and **this**.

## Constructor Notation

We can use a constructor function to create multiple objects that share the same properties.

Using our previous example, we can create a constructor function like this:

```javascript
function House(sqFeet, bathrooms, bedrooms) {
  this.sqFeet = sqFeet;
  this.bathrooms = bathrooms;
  this.bedrooms = bedrooms;
}
```

Notice our use of the keyword `this`. Since we don't know what the value for the parameters will be, we use `this` as a placeholder. When we call the `House` function, we add in our values. To create an object instance using a constructor function, we use the `new` keyword. Here is an example of how we would create our four houses using a constructor function and the `new` keyword:

```javascript
var house1 = new House(3000, 3, 2);
var house2 = new House(4000, 3.5, 2);
var house3 = new House(1000, 2, 1);
var house4 = new House(13000, 3.5, 7);
```

Let's look at another example and a different way to write a constructor function.

```javascript
var Person = function(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return ("Hello " + this.firstName + " " + this.lastName);
  }
}

// This can also be written as:

function Person(firstName, lastName) {
  this.firstName = firstName;
  this.lastName = lastName;
  this.fullName = function() {
    return ("Hello " + this.firstName + " " + this.lastName);
  }
}
```

**Think about it:** What would happen if we didn't use `this` inside the `.fullName` function above?

What's the difference between these two? In short, The difference is that `var Person = function() {}` is defined at run-time \(which means that if we were to call it before defining it we would get an error\), whereas `function Person() {}` is defined at parse-time \(which means that if we were to call it before defining it we would **not** get an error\).

You can read more about the difference [here](http://stackoverflow.com/questions/336859/var-functionname-function-vs-function-functionname)

Let's now take a closer look at the constructor function.

```javascript
var elie = new Person("Elie", "Schoppik");

console.log(elie.firstName);
console.log(elie.lastName);
console.log(elie.fullName());
```

Using the `new` keyword, Javascript does a few things.

* Creates a new object
* Sets the `constructor` property to the `Person` constructor function
  * You can use `elie.constructor` to get a direct reference to the constructor.

## Things to watch for

* When using the constructor, don't try to call a constructor without the `new` keyword.
  * Otherwise, you'll get the output of the constructor function, which is `undefined`. The `new` keyword will use the constructor to return a new object.
* Always make sure the keyword `this` is on the left hand side: `this.taco = taco`. Remember, you're assigning parameters to properties of the new object being created.
* `return` statements are usually unnecessary in constructors.

