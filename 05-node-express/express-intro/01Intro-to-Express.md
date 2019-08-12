# Express

_Express is a light-weight, web application framework for writing RESTful APIs in Node.js._

We'll get to the _RESTFUL API_ part soon, but for now, think of Express as a Node Package that gives us some extra tools for creating a web application using Node.

Let's create our first Node/Express app!

## Our first Express App

### 1. Create a new directory for your project.
```bash
mkdir hello-express
```

### 2. Initialize Node
```bash
cd hello-express
npm init
```

### 3. Install Express
```bash
npm install express
```

***Pause!*** Open your project file tree in sublime and notice the new files that appear.

#### node_modules
Each time you use npm to install a new package, this folder will populate with the package you installed, _along with all the dependencies of that package_. That's why you'll see several files that look like they have nothing to do with the package you were trying to install. They are helper packages for the one you're going to use! More on this folder [here](https://docs.npmjs.com/files/folders).

#### package-lock.json
This file keeps track of your npm install history. As we just learned, when we use npm to install a package, there may be several other dependencies installing behind the scenes. Think of package-lock.json as the commit history for this activity. More on this file [here](https://docs.npmjs.com/files/package-lock.json).

_No need to mess with any of these automatically generated files! NPM takes care of the modifications/additions for you each time you install/uninstall a package._

### package.json:
Revisit the package.json file. Notice that express and the version number now shows up in the dependencies field. All third party modules will be listed here automatically when you use npm to install them (but the dependencies of _those_ files will not be listed here).

### 4. Create your entry point file.
```bash
touch index.js
```

### 5. Import the Express module

***index.js***
```js
var express = require('express');
```

### 6. Create an instance of an express app

***index.js***
```js
var express = require('express');
var app = express();
```

### 7. Create a Home Route

***index.js***
```js
var express = require('express');
var app = express();

app.get('/', function(req, res) {
	res.send('Hello, World!');
});

app.listen(8000);
```

We'll learn more about this code in the next lesson. For now, just copy it down.

### 8. Run nodemon
```bash
nodemon
```

Now visit localhost:8000 in your browser. ***Congratulations!*** You've just built your first express app!
