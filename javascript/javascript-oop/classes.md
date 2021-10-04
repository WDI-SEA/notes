# Classes

## Lesson Objectives

1. Explain why we need classes
2. Create a class to define the blueprint for creating objects
3. Add methods to a class
4. Set properties on an instance of a class
5. What is `this`? Why do we need it?
6. Make an instance of each class customizable
7. Create methods to alter the properties of an instance

## Explain why we need classes

Sometimes we need to repetitively create new objects with the same attributes. Imagine we wanted to create a bunch of hotels for a boutique travel agency.

We'd need at least:

* name
* location
* rating
* vacancies
* tags describing the hotel
* rooms \(an array of objects with details of the rooms\)

```javascript
{
  name: 'Hotel California',
  location: 'California',
  rating: 4,
  vacancies: true,
  tags: [
    'pink champagne',
    'wine',
    'lovely',
    'can\'t leave'
  ],
  rooms: [
    {
      'roomNumber': 102,
      'size': 'Queen Double',
      'price': 55,
      'booked': true
    },
    {
      'roomNumber': 202,
      'size': 'King Suite',
      'price': 68,
      'booked': false
    },
    {
      'roomNumber': 404,
      'size': 'Queen Double',
      'booked': false
    },
    {
      'roomNumber': 605,
      'size': 'King Suite',
      'price': 68,
      'booked': true
    },
    {
      'roomNumber': 777,
      'size': 'Penthouse',
      'price': 888,
      'booked': false
    }
  ]
};
```

Great! One object. How can we create another one? How about copy pasting, then changing all the details? Typing it all from scratch? What if someone makes a typo with a key? What if our boutique expands to 1000 hotels?

There is a better way! We can create a class, which will be a blueprint or template for similar objects. Not only can we add data, we can also include functionality.

## Create a class to define the blueprint for creating objects

When creating a class, it's custom to capitalize the first letter of the variable, so we know it's a `class`. This follows customs in other programming languages.

```javascript
class Person {

}
```

Now we can "instantiate" or create new objects using this class. We do this by adding the `new` keyword before calling the class name like a function.

```javascript
const me = new Person();
const you = new Person();
console.log(me);
console.log(you);
console.log(typeof me);
console.log(typeof you);
```

## Add methods to a class

Right now, our object doesn't do anything. Let's have it do some stuff;

```javascript
class Person {
  greet () {
    console.log('hi!');
  }
}

const me = new Person();
const you = new Person();

me.greet();
you.greet();
```

These methods can, of course, take parameters:

```javascript
class Person {
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
}
const me = new Person();
const you = new Person();
me.greet('you');
you.greet('me');
```

We only had to update our code in one place, and then every instance of the class now has the updated functionality. Sweet!

If we have multiple methods, don't put commas between them:

```javascript
class Person {
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}

const me = new Person();
const you = new Person();
me.greet('bob');
me.walk();
you.greet('bob');
you.walk();
```

## Set properties on an instance of a class

If we log the instances of our class, we'll see they don't have any properties:

```javascript
class Person {
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}

const me = new Person();
const you = new Person();
console.log(me);
console.log(you);
```

Let's add some properties with a `constructor` function. This is a function that gets called once, each time an object is created:

```javascript
class Person {
  constructor () {
    this.legs = 2;
    this.arms = 2;
    this.eyes = 'blue';
    this.hair = 'blonde';
  }
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}
const me = new Person();
console.log(me);
```

`constructor` is a special function. Try misspelling `constructor` \(ie `constr`\) and see if you still get the same results.

[**Reserved Words in Javascript**](http://www.javascripter.net/faq/reserved.htm)

## What is `this`?

What is `this`? Let's think back to our hw problem on making a vending machine and let's build it again together.

**Model a vending machine**

* a vending machine is an object
* it has an array of snacks \(make 3 snacks\)
* snacks are objects that have a name and a price
* a vending machine has a function vend that allows user to enter the array position \(a number\) of the snack and then that snack will be returned
* Be able to call vendingMachine.vend\(\) with a valid integer to return a snack

When we wanted to access snacks within our object we had to put the name of the object `vendingMachine` in it to access the snacks

```javascript
const vendingMachine = {
  snacks: [
    {
      name: 'kitkat',
      price: 6
    },
    {
      name: 'sun chips',
      price: 7
    },
    {
      name: 'apple',
      price: 12
    }
  ],
  vend (input) {
    console.log('vending', vendingMachine.snacks[input]);
  }
};

vendingMachine.vend(1);
```

This worked just fine, because we knew what the name of the object would be.

But now we are making new objects that can be named anything. So we need a way to say `this` object's snacks or `this` object's legs property - We need a pronoun, a generic term to refer to whatever the name of the object is.

JavaScript uses `this`. So we can access things within an object this way. We can update our vendingMachine to use `this` instead:

```javascript
const vendingMachine = {
  snacks: [
    {
      name: 'kitkat',
      price: 6
    },
    {
      name: 'sun chips',
      price: 7
    },
    {
      name: 'apple',
      price: 12
    }
  ],
  vend (input) {
    console.log('vending', this.snacks[input]);
  }
};

vendingMachine.vend(1);
```

## Make an instance of each class customizable

Our world is very boring and weird if all of our people are exactly the same! We need a way to customize each object: Our constructor function can take params which we can use to alter the properties of the object instantiated. This allows us to customize each instance:

```javascript
class Person {
  constructor (name, age, eyes, hair) {
    this.legs = 2;
    this.arms = 2;
    this.name = name;
    this.age = age;
    this.eyes = eyes;
    this.hair = hair;
  }
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}

const me = new Person('Karolin', 41, 'green', 'copper dark ash blonde');
console.log(me);
```

## Create default values

Sometimes, you want to create default values that can be overwritten.

There are two ways to write it, writing it in the constructor with an `=` is the newer way. Using `||` is the older way and does work. In both cases, values that have default parameters should go at the end \(why?\).

```javascript
class Person {
  constructor (name, age, eyes, hair, lovesCats = false, lovesDogs) {
    this.legs = 2;
    this.arms = 2;
    this.name = name;
    this.age = age;
    this.eyes = eyes;
    this.hair = hair;
    this.lovesCats = lovesCats;
    this.lovesDogs = lovesDogs || false;
  }
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}
const me = new Person('Karolin', 40, 'green', 'copper dark ash blonde', true, true);
const you = new Person('Matt', 36, 'blue', 'blonde');
console.log(me);
console.log(you);
```

## Create methods to alter the properties of an instance

We can of course, alter the properties of an instance, after it is created:

```javascript
me.hair = 'supernova red';
console.log(me);
```

But it's a nice practice to define a method that will alter that:

```javascript
class Person {
  constructor (name, age, eyes, hair, lovesCats = true, lovesDogs) {
    this.legs = 2;
    this.arms = 2;
    this.name = name;
    this.age = age;
    this.eyes = eyes;
    this.hair = hair;
    this.lovesCats = lovesCats;
    this.lovesDogs = lovesDogs || true;
  }
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  setHair (hairColor) {
    this.hair = hairColor;
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}

const you = new Person('Matt', 36, 'blue', 'blonde');
console.log(you);
you.setHair('red');
console.log(you);
```

* This way, everything is done with methods
* Other developers can quickly scan the class definition to determine what you'd like them to be able to do with the class

## Objects interacting with other objects

We can pass an object to another object to have them interact

```javascript
class Person {
  constructor (name, age, eyes, hair, lovesCats = false, lovesDogs) {
    this.legs = 2;
    this.arms = 2;
    this.name = name;
    this.age = age;
    this.eyes = eyes;
    this.hair = hair;
    this.lovesCats = lovesCats;
    this.lovesDogs = lovesDogs || false;
  }
  greet (otherPerson) {
    console.log('hi ' + otherPerson + '!');
  }
  classyGreeting (otherClassyPerson) {
    console.log('Greetings ' + otherClassyPerson.name + '!');
  }
  setHair (hairColor) {
    this.hair = hairColor;
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}
const me = new Person('Karolin', 41, 'green', 'copper dark ash blonde', true, true);
const you = new Person('Matt', 36, 'blue', 'blonde');

me.classyGreeting(you);
you.classyGreeting(me);
```

_Adapted from_ [_SEI-MAE_](https://git.generalassemb.ly/Software-Engineering-Immersive-Remote/SEIR-MAE-INSTRUCTORS/blob/master/unit_1/w04d3/instructor_notes/1.%20Classes.md)

