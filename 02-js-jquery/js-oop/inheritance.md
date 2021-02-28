# JavaScript - OOP Inheritance

## Lesson Objectives

1. Make a class inherit attributes from a "parent class"
1. Create static properties for a class
1. Create a factory


## Make a class inherit attributes from a "parent class"

Sometimes we want to have a "parent" class that will have some basic attributes that will be inherited by "child" classes. Here is our parent class. But what if we have a super hero amongst us that has all our human attributes and more?

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
  classyGreeting (otherClassyPerson) {
    console.log('Howdy ' + otherClassyPerson.name + '!');
  }
  setHair (hairColor) {
    this.hair = hairColor;
  }
  walk () {
    console.log('I hate when my Segway is in the shop.');
  }
}
const supermanPerson = new Person('Clark Kent', 30, 'blue', 'black')
console.log(supermanPerson);
```
We could just copy paste the above and add what we need, but that's not sticking to the principal of DRY. Instead we can `extend` our Person class for our superhero

We can now add additional functionality:

```javascript
class SuperHero extends Person {
  fly () {
    console.log('Up up and away!');
  }
}
const superman = new SuperHero('Clark Kent', 30, 'blue', 'black')
console.log(superman);
superman.walk();
superman.fly();
```

And we can override previous functionality:

```javascript
class SuperHero extends Person {
  fly () {
    console.log('Up up and away!');
  }
  greet (otherPerson) {
    console.log(`Greetings Earthl- Oops, I mean ${otherPerson}`);
  }
}
const superman = new SuperHero('Clark Kent', 30, 'blue', 'black')
superman.greet('Bob');
```

We can even reference the parent class' method and extend its original functionality:

```javascript
class SuperHero extends Person {
  fly () {
    console.log('Up up and away!');
  }
  greet (otherPerson) {
    console.log('Greetings ' + otherPerson);
  }
  walk () {
    super.walk();
    this.fly();
  }
}
const superman = new SuperHero('Clark Kent', 30, 'blue', 'black')
superman.walk();
```

This is most useful on the constructor:

```javascript
class SuperHero extends Person {
  constructor (name, age, eyes, hair) {
    super(name, age, eyes, hair);
    this.superPowers = ['flight', 'superhuman strength', 'x-ray vision', 'heat vision', 'cold breath', 'super-speed', 'enhanced hearing', 'nigh-invulnerability'];
  }
  fly () {
    console.log('Up up and away!');
  }
  greet (otherPerson) {
    console.log('Greetings ' + otherPerson);
  }
  walk () {
    super.walk();
    this.fly();
  }
}
const superman = new SuperHero('Clark Kent', 30, 'blue', 'black')
console.log(superman);
```

Try adding a constructor to `SuperHero` *without* calling the parent constructor first (`super`) and see what happens. 

`super` is another special keyword/function. Try mispelling it - and you'll see it won't have the same functionality.
