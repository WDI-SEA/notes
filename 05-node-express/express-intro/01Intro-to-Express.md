# Express

_Express is a light-weight, web application framework for writing RESTful APIs in Node.js._

We'll get to the _RESTFUL API_ part soon, but for now, think of Express as a Node Package that gives us some extra tools for creating a web application using Node.

Let's create our first Node/Express app!

## Our first Express App

### 1. Create a new directory for your project.
```bash
mkdir express-hello-world
```

### 2. Initialize Node
```bash
cd express-hello-world
npm init
```

### 3. Install Express
```bash
npm install express
```

***Pause!*** Open your project file tree in sublime and notice the new files that appear. This happens when you use npm to install a package locally, but only once! These files are only needed to run third party modules so they appear when you install one but wont duplicate if you install more than one.

* node_modules folder
* package-log.json

Also take a look at the package.json file. Notice that express now shows up in the dependencies field. All third party modules will be listed here automatically when you use npm to install them.

### 4. Create your entry point file.
```bash
touch index.js
```

### 5. Import the Express module

***index.js***
```js
var express require('express');
```

### 6. Create an instance of an express app

***index.js***
```js
var express require('express');
var app = express();
```