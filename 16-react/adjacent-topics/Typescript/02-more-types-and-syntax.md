# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) More Types and TypeScript Syntax

## Unions
We can enforce types of multiple values with a type declaration on a union
```typescript
type Color = 'Green' | 'Red' | 'Blue'

let colorChoice: Color = 'Green' 
colorChoice: Color = 'Purple' // Throws an error

let colorOrNum: Color | number = 10 // OK!
```
___
## Interfaces
What if we would like to enforce typings on the shape of an `object`?

**Enter the interface!**

Typescript offers us the ability to do this with `interfaces`:

```typescript

interface DogObject {
    name: string;
    age: number;
    isGood: boolean;
    wagsTail?: boolean; // the '?' means that wagsTail is optional
}

function isGoodDog(dog: DogObject): boolean {
    let {name, age, isGood} = dog; // Object destructuring is neat!
    let message = `${name} is ${age} and is very good!${dog.wagsTail ? ' wag, wag, wag' : ''}`
    if (!isGood) {
        console.log('How dare you! All dogs are good dogs!!')
        dog.isGood = true
    }
    console.log(message)
    return true
}

let oneGoodBoy: DogObject = {
    name: 'Harley Muffinhead',
    age: 7,
    isGood: true,
    wagsTail: true 
}

let barnCat: object = {
    name: 'Scar Tatteredear',
    age: Infinity,
    clawedKiller: true,
    isGood: false
}

isGoodDog(oneGoodBoy) 
// Works!
isGoodDog(barnCat) 
// Error, barnCat is not 'DogObject' type. Argument of type 'object' is not assignable 
// to parameter of type 'DogObject'. Type '{}' is missing the following properties 
// from type 'DogObject':name, age, isGood

// If we removed the Explicit type from barnCat, isGoodDog(barnCat) would work 
// because barnCat has all the necessary values of the DogObject type


```


___

## Tuples
>Tuple types allow you to express an array where the type of a fixed number of elements is known, but need not be the same. 

```typescript
let myStringNumTuple: [string, number] = ["Hello", 42];
myStringNumTuple = [42, "Hello"] // ☠️ will throw an error at compile time
```

When accessing an element with a known index, the correct type is retrieved:
```typescript
console.log(myStringNumTuple[0].substr(1)); // OK
console.log(myStringNumTuple[1].substr(1)); // Error, 'number' does not have 'substr'
```
When accessing an element outside the set of known indices, an error will be thrown:
```typescript
myStringNumTuple[3] = "world"; 
// error, Type '"world"' is not assignable to type 'undefined'
```
So can I tack more onto a tuple and just assign it a new type?
```typescript
myStringNumTuple[3] = string; 
// TWO errors!
// Tuple type '[string, number]' of length '2' has no element at index '3'
// 'string' only refers to a type, but is being used as a value here
```

Tuples can be as long as you want; think of them like interfaces without the name. Think back to our `DogObject` example, you could create a tuple with those constraints, but instead of accessing those values via their keys, they're accessed by their index.
```typescript
let tupleDog: [string, number, boolean, boolean
```
___
## Enum
According to the TypeScript docs, Enums allow us to 'give friendly names to a set of numeric values'.

```typescript
enum Color {Green, Red, Blue}
let colorChoice: Color = Color.Green
let colorString: string = Color[0]
```
While this does enforce a `Color` Type that only has the values `"Green"`, `"Red"`, `"Blue"`... this little bit of TS compiles to this mess of JavaScript:
```js
var Color;
(function (Color) {
    Color[Color["Green"] = 0] = "Green";
    Color[Color["Red"] = 1] = "Red";
    Color[Color["Blue"] = 2] = "Blue";
})(Color || (Color = {}));

var colorChoice = Color.Green; // evaluates to 0
var colorString = Color[0] // evaluates to "Green"
```

![WTF](https://media.giphy.com/media/ukGm72ZLZvYfS/giphy.gif)


Typescript can now support Enums with strings, so you could assign certain values to certain strings
```typescript
enum Color {
    Red = ff0000,
    Green = 00ff00,
    Blue = 0000ff
}
```

If you want to know a bit more about this bizarre type and it's usage, check out [this medium article](https://medium.com/@KevinBGreene/typescript-enums-and-polymorphism-with-type-matching-fc3dc74b031c) and [this stack-overflow question](https://stackoverflow.com/questions/40275832/typescript-has-unions-so-are-enums-redundant). 

The tl;dr for most devs is that Enums can be iterated over, can be used as bit flags, and have some specific use cases, but you will mostly be using Union types.

___
## `Generics<T>`

What should we do if we want to enforce typings further down the scope of our function or class but don't want to explicity declare a type?

Well, TS humbly offers up the Generic type. 

We can use variables between angle brackets in our type declarations to enforce consistent use of a type! Classically, you will see `<T>` used to represent Type however, you can name them anything you want as long as they are not reserved words or types. We can even use multiple generics in the same construct by separating them with commas: `Construct<T, U, ThirdType>`.

Check out this example of a simple Queue:

```typescript
class Queue<T> {
    constructor(data: T[]){
        this.data = []
    }

    enqueue(payload: T): void {
        this.data.push(payload)
    }

    dequeue(): T {
        return this.data.unshift()
    }

}
```

We can also use complex datatypes:

```typescript
type BadMessage = 'Warning' | 'Error'
type GoodMessage = 'All is Well' | 'There is a fresh pot of coffee in the kitchen' 

function shout<T>(arg: T): string {

    return arg.toString().toUpperCase()
}

console.log(shout<BadMessage>('Warning'));
console.log(shout<BadMessage>('All is Well')); // Argument of type '"All is Well"' is not assignable to parameter of type 'BadMessage'.
console.log(shout<GoodMessage>('There is a fresh pot of coffee in the kitchen'));
```

_Prepare yourself... we are about to put it to work!_
___
