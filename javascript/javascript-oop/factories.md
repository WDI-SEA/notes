# Factories

## Lesson Objectives

1. Create a Factory
2. Bonus - static properties for a class

## Create a factory

* Sometimes we need to have a factory object that will generate other objects
* The purpose of the factory is so it can control the creation process in some way
* This is usually a single object that exists throughout the program that performs a set of functions

  * also called a singleton

  Let's start with a car

```javascript
class Car {
  constructor (maker, serialNumber) {
    this.serialNumber = serialNumber;
    this.maker = maker
  }
  drive () {
    console.log('Vroom Vroom');
  }
}

const newCar = new Car('Mazda', 12345);
console.log(newCar);
```

Now let's make a factory class that will make cars for us.

```javascript
class Factory {
  constructor (company) {
    this.company = company;
    this.cars = [];
  }
  generateCar () {
    const newCar = new Car(this.company, this.cars.length);
    this.cars.push(newCar);
  }
  findCar (index) {
    return this.cars[index];
  }
}
const tesla = new Factory('Tesla');
tesla.generateCar();
tesla.generateCar();
tesla.generateCar();
tesla.generateCar();
console.log(tesla);
console.log(tesla.findCar(0));
```

Now we can easily create another new factory that produces its own cars

```javascript
const porche = new Factory('Porche');
porche.generateCar();
porche.generateCar();
console.log(porche);
console.log(porche.findCar(0));
```

## Extra

### Create static properties for a class

Sometimes you want to define properties that pertain to the class as a whole, not the instance. This allows us to limit, somewhat, what the user of class can do.

```javascript
class Person {
  static eyeColors () {
    return ['blue', 'green', 'brown'];
  }
  // rest of class definition here...
}
// more code...
const superman = new SuperHero('Clark Kent', 30, Person.eyeColors()[0], 'black');
```

_Adapted from_ [_SEI-MAE_](https://git.generalassemb.ly/Software-Engineering-Immersive-Remote/SEIR-MAE-INSTRUCTORS/blob/master/unit_1/w04d3/instructor_notes/3.%20Factories.md)

