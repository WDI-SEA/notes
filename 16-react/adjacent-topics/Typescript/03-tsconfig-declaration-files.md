# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) TS Config and Declaration Files

## tsconfig
Our TypeScript Compiler offers many options for configuration and customization to fit your specific use case. 

Let's navigate to our ts_sandbox and see what it can do:
```bash
$ tsc --init
message TS6071: Successfully created a tsconfig.json file.
```

Oof!--that's a bit overwhelming when we are first getting started. More information on these options are available in the docs [here](https://www.typescriptlang.org/docs/handbook/compiler-options.html).

For our codelalong today, let's use this pared down snippet.

```json
{
  "compilerOptions": {
    "module": "commonjs",
    "esModuleInterop": true,
    "target": "es6",
    "noImplicitAny": true,
    "moduleResolution": "node",
    "sourceMap": true,
    "outDir": "build",
    "baseUrl": ".",
    "paths": {
      "*": [
        "node_modules/*"
      ]
    }
  },
  "include": [
    "src/**/*"
  ]
}
```

___

## Declaration Files and @types from npm

### **.d.ts**

TypeScript allows us to declare the shape of our types, variables and functions in separate files (for globals and/or modules). By using, the extension `.d.ts` the TypeScript Compiler/Linter can use these declarations in your project.

If you happen to be writing a library or working on a large project, this might be a good option. Today we will declare our types inline and at the head of our file.

[More information on Declaration Files](https://www.typescriptlang.org/docs/handbook/declaration-files/introduction.html)

```typescript
// this function will return a string
declare function parseString(str: string): string;

// this var will be a number
declare var myNum: number;
// this var will be a string
declare var name: string;

// hey look an interface we can use of contact info
declare interface ContactInfo {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
}

// the shape of a Cat class
declare class Cat {
  // the constructor accepts these args
  contructor(
    name: string,
    breed: string,
    age: number,
  )

  // methods for collecting and destroying
  collect(name: string, breed: string, age: number): void
  destroy(id: number): boolean
}
```

### **@types**

When using third-party libraries like Express, Sequelize or Mongoose it can be annoying and frustrating trying to determine what our Types should be. 

```typescript
// note the imports used in node for typescript 
import express from 'express';
import dotenv from 'dotenv';

dotenv.config();

const app: express.Application = express();
const port: number | string = process.env.PORT || 3001

app.get('/', (req: express.Request, res: express.Response) => {
  res.send('Wow I just wrote so much more code to accomplish this than I would with JavaScript')
})

app.listen(port, ():void =>{
  console.log(`"Typing" too much on port: ${port}`)
})

```

Lucky for us the fine folks at [Definitely Typed](https://github.com/DefinitelyTyped/DefinitelyTyped) have created a repo of type declarations that can be installed via npm for most of the libraries that are widely used.

```bash
$ npm i --save-dev @types/express @types/dotenv
```

Once installed, we can basically write normal javascript while implementing the Type guards of TS... making the example above look like this:

```js
import express from 'express';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const port: number | string = process.env.PORT || 3001

app.get('/', (req, res) => {
  res.send('Wow I just wrote so much more code to accomplish this than I would with JavaScript')
})

app.listen(port, () => {
  console.log(`Feeling better about this on port: ${port}`)
})

```
