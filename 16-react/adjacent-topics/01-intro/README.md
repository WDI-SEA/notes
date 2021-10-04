# Typescript

## ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) TypeScript

#### Learning Objectives

* Describe advantages and disadvantages to using TypeScript
* Identify and use basic types, interfaces and additional TypeScript stuff
* Understand type inference and declaration
* Configure and use the typescript compiler

## Why TypeScript?

* Identifying bugs at compile time is better than finding them at runtime
* Type enforcement in large code bases reduces bugs across the organization/teams/time
* TypeScript allows ESNext syntax -- though many of the features highlighted by TS folks have been introduced with ES6 and 7
* Lowish barrier to entry
  * can use it sparingly to start \(your JS is probably fine, just add some typings or `any`\)
  * implicit and explicit typing 

[TypeScript Docs / Handbook](https://www.typescriptlang.org/docs)

This is a pretty great resource put together by some benevolent dev:

[TypeScript Deep Dive by @basarat](https://basarat.gitbooks.io/typescript/)

## Disadvantages

* Adds complexity to your project
  * directory structure needs source and build
  * setup compiler or babel and/or webpack and build step
* TS compiler will yell at you for things that you have perceived as legal for the entirety of your JS career
* Advanced techniques can be a little confusing

### Let's get started!

Install TypeScript and its compiler on your local machine!

```bash
$ npm install -g typescript
$ tsc -v 
Version 3.3.X
```

We're all set!

Let's test it out

```bash
$ mkdir ts_sandbox && cd ts_sandbox
$ touch type_fun.ts
```

**type\_fun.ts**

```typescript
let hello: string = "Hello, World!"
```

Save your `type_fun.ts` and run this bash command:

```bash
$ tsc type_fun.ts
$ ls
```

You should now see two files, `type_fun.ts` and `type_fun.js`! The `tsc` command compiles our typescript file into javascript!

```bash
$ cat type_fun.js

var hello = "Hello, World!"
```

## Basic Types

We can get started with TypeScript by adding just a little extra cruft to the JS syntax we know and love. By now, you are all very familiar with the javascript primitives: `string`, `number`, `boolean`. TypeScript makes use of these primitives... and then adds to it!

### Applying Type constraints to variables

In order to apply type constraints to our variables with TypeScript, all we need to do is declare a `type` after the variable name, separated by a colon

```typescript
let myVariable: type = "my value"
```

| Basic Types | &lt;= according to the TS Docs 🎉 |
| :---: | :--- |
| String | Your run of the mill string type |
| Number | Can be used with decimal integers and floats as well as hex, octal and binary numbers |
| Boolean | our old friends `true` and `false` |
| Any | oh my! you're telling me I don't actually have to plan ahead? |
| Array | lets add primitive typings to arrays \(syntax may vary!\) |
| void | used for functions that do not return a value |
| null | `null`, this is one of Typescript's two _subtypes_ |
| undefined | `undefined`, Typescript's other _subtype_ |
| Object | anything that is not `number`, `string`, `boolean`, `null`, or `undefined` |
| never | represents the type of values that never occur |
| Tuple | enforced typings on a specified number elements |
| Enum | Enforce a set of values -- we can use custom `Type`s in many cases |

#### `string`

```typescript
let myString: string = "Hello, World!"
let myTemplateLiteral: string = `"${myString}" is the phrase we always use when learning a new language.`
```

#### `number`

```typescript
let myInt: number = 3;
let myFloat: number = 6.4;
let myHex: number = 0xf00d;
let myOct: number = 0o744;
let myBin: number = 0b1010;
```

#### `boolean`

```typescript
let myBool: boolean = true;
myBool = false;
```

#### `any`

When a data type is not known or required ahead of time, `any` can be used.

```typescript
let myAny: any = 'what should we throw in here?'
myAny = 7
myAny = true

// all ok!
```

However, if we know that a variable can accept both strings or numbers, TypeScript allows us to plan for this scenario with the `|` operator. \(This is called a "Union" type and can be a more advanced technique\)

```typescript
let myIndecisiveVar: string | number = 'This is ok!'
myIndecisiveVar = 5 // also ok!
myIndecisiveVar = false // Throws an error
```

#### The Subtypes

Typescript gives us two _subtypes_, `null` and `undefined`. These are used when we've defined the type of a variable, but we don't know what that value is yet.

```typescript
let futureVar: number = undefined
// OR
let futureVar: number = null
// may require use of the `as` keyword
let futureVar = null as number;
```

#### Arrays

TypeScript offers 2 options for enforcing type constraints on an array. 1. Adding `[]` after a type declaration 2. Using angle brackets and the `Array` generic type

```typescript
let myStrings: string[] = ['Hello','World'];
let myStringArray: Array<string> = ['Hello','Squirrel'];

let myNums: number[] = [9,3,6,12];
let myNumArr: Array<number> = [3,3,3,3,3,3];

let arrayOfAny: any[] = ['what','is','purpose','of','this','array','?!', 2, true, {gross: "yup"}]
```

Be careful when using the angle bracket notation as it can cause conflicts when working with TSX, the TypeScript equivalent of JSX.

### Typing Functions

The format we used to add type constraints to our functions and methods is as follows:

```typescript
// function identifier(arg: type): returnType {}
function myFunc(arg: string, arg2: number): string {
    // myFunc logic
    return 'The string';
}

const myArrowFunc = (arg:string, arg2: number): string[] => {
    // logic
    return ['','',''];
}
```

If our function will not be returning anything, we can assign the return type `void`.

```typescript
function myVoidFunc(data: string[]): void {
    data.forEach( (datum: string): void => {
        console.log(datum)
    })
}
```

#### Explicit vs Implicit Typing

All this extra syntax making your headspin?

The typescript compiler can infer some of your typings from the initial definition!

```typescript
let str: string = 'I am explicitly defined as a string type'
let otherStr = 'I am implicitly defined as a string type'

function printMsg(message: string): void {
    console.log(message)
}

printMsg(str) // Works!
printMsg(otherStr) // Also Works!
```

In essence, typescript looks at a variable that isn't typed \(in this case `otherStr`\) and says, "This looks like a string, follows the sytax of a string, must be a string!"

![Must be gelfling](https://66.media.tumblr.com/tumblr_m32hrruhGr1qdj4i3o1_r1_500.gif)

This will be more apparent and relevant when we get into interfaces and enforcing object type structures in the next section.

The rules that govern these type inferences can vary and/or be configured by the compiler. In general, if the data type is not primitive, it is unlikely that implicit typping will work.

For more information: [Rules of Type Inference](https://www.typescriptlang.org/docs/handbook/type-inference.html)

