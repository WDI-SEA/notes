# Intro to Express

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

### 3. Create the entry point file
```bash
touch index.js
```

### 4. Install Express

```bash
npm i express
```

_**Pause!**_ Open your project file tree in your text editor and notice the new files that appear.

#### package-lock.json

This file keeps track of your npm install history. As we just learned, when we use npm to install a package, there may be several other dependencies installing behind the scenes. Think of package-lock.json as the commit history for this activity. More on this file [here](https://docs.npmjs.com/files/package-lock.json).

_No need to mess with any of these automatically generated files! NPM takes care of the modifications/additions for you each time you install/uninstall a package._

### package.json:

Revisit the package.json file. Notice that express and the version number now shows up in the dependencies field. All third party modules will be listed here automatically when you use npm to install them \(but the dependencies of _those_ files will not be listed here\).

#### node\_modules

Each time you use npm to install a new package, this folder will populate with the package you installed, _along with all the dependencies of that package_. That's why you'll see several files that look like they have nothing to do with the package you were trying to install. They are helper packages for the one you're going to use! More on this folder [here](https://docs.npmjs.com/files/folders).

### 5. gitignore your node modules

It's not necessary to upload the whole `node_modules` folder to github, because anyone who forks/clones your code will be able to install all the necessary dependencies simply by running `npm i` inside the cloned folder. This will download all the dependencies indicated in the `package.json` file. To tell git to ignore the node modules folder, create a `.gitignore` file in the root directory, and add `node_modules` to it.

```bash
echo "node_modules" >> .gitignore
```
 
### 6. Import the Express module

_**index.js**_

```javascript
const express = require('express');
```

### 7. Create an instance of an express app

_**index.js**_

```javascript
const express = require('express');
const app = express();
```

### 8. Create a Home Route

_**index.js**_

```javascript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.send('Hello, World!');
});

app.listen(8000);
```

We'll learn more about this code in the next lesson. For now, just copy it down.

### 9. Run nodemon

```bash
nodemon
```

Now visit localhost:8000 in your browser. _**Congratulations!**_ You've just built your first express app!
