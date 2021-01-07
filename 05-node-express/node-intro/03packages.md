# Node Package Manager \(NPM\)

There are three types of Node modules: 
* 1. Core Modules \(like `fs`\) 
* 2. Local Modules \(that you create\) 
* 3. Third Party Modules

Core modules are great for gaining quick access to commonly-needed functionality in your program, and local modules allow you the flexibility to build out whatever tools you might possibly need, but third party modules, which fall somewhere in between, are perhaps the most exciting modules of them all!

### Node Packages

Because developers are awesome, there are hundreds of thousands of already-written modules out there, ready for use! Each of these modules are encapsulated in a _**Node Package**_ and made available via _**Node Package Manger**_ or _**NPM**_, for short. A node package is a folder that contains one or more modules, a `package.json` file, and any meta-info needed to make the modules work correctionly and play well with your node program.

### NPM

NPM is the largest open-source software registry in the world. It includes a website, a registry of Node Packages, and a command line interface that allows us to easily incorporate packages into our programs.

Check out this [NPM Intro Video](https://www.youtube.com/watch?v=x03fjb2VlGY)

The NPM CLI makes incorporating a node package into your program fairly easy, but you can refer to [this playlist](https://www.youtube.com/watch?v=pa4dc480Apo&list=PLQso55XhxkgBMeiYmFEHzz1axDUBjTLC6) if you ever get lost. It includes a whole series of videos that demonstrate the fundamentals of using NPM.

The NPM CLI installed automatically on your machine when you installed Node. Verify this now by checking the version in your terminal: `npm -v`

### First Node Package: Nodemon

[Nodemon](https://www.npmjs.com/package/nodemon) is a package that makes developing node apps easier. It restarts the application everytime you save changes to your code.

We will use Nodemon quite a bit, so instead of installing it on each node app we build, we will install it globally. This will make it accessible to all of our node apps.

In the command line, type the following code: `npm i -g nodemon`

Since we're installing it globally \(that's where the `-g` flag comes in\), it doesn't matter what directory we're in.

Let's see nodemon in action! Try running your `my-first-node-app` using nodemon. Simply `cd` into the directory, then run `nodemon`. Nodemon knows to run the file that corresponds to `main:` in your `package.json`.

Now open up `my-first-node-app` in your text editor. Add the following code to `index.js`:

```javascript
let i = 0

const count = () => {
    console.log(i)
    i++
}

const myTimer = setInterval(count, 1000)
```

Make sure to save the file and check out what's happening in your terminal!

Now change the `count` function to print `i*2` instead of just `i` and save.

You can always restart nodemon by typing `rs`.

To quit nodemon \(and any program running in the terminal\), press CTRL+C.

_**Congratulations**_, you've just installed and used your first third party node module!

We installed nodemon globally, but most node packages will only be useful for specific projects. In this case, when you run `npm i [package name]` you want to make sure you're inside the directory of the project you want to use the package in, and leave off the `-g` flag.

## Using a Third Party Module

#### Introducing Moment: A Date/Time Format Module

Moment is a date formatting module. Instead of the mess of text that comes out when you create a regular date with JavaScript using the date class, we can pretty-print the date in a human readable way.

```javascript
console.log(new Date())
// Prints: Fri Apr 05 2019 09:58:38 GMT-0700 (Pacific Daylight Time)
```

#### Install Moment

1. Go to your terminal
2. Make sure you're in the top level of your `my-first-node-app` folder
3. Type the command `npm i moment`
4. When the command is finished, go back to your text editor
5. Make sure there is a folder called `node_modules` in the top level of your `my-first-node-app` folder

#### Use Moment in a Node App

* Open `index.js` in your text editor
* Require the moment library at the top of `index.js` and assign it to a variable called `moment`
* Take a look at [Moment's Docs](http://momentjs.com/). There are a lot of things you can do with this module!
* Let's use the moment module to print a date! Add the following code to your `index.js` file:

```javascript
console.log(moment().format("MMM Do YYYY"))
```

* What does this print? You should have seen whatever today's date was in the format: 3-letter month, numerical day plus ordinal, and 4-digit year. For example: 

```text
Apr 15th, 2020
```

* Next challenge: Use moment to pretty-print your birthday. Use the fully spelled out month, day of the week, escaped text for words such as `the` and `of`, and 4-digit year. For example:

```text
Wednesday the 11th of September in the year 1985
```

* BONUS: Use moment's `.fromNow()` function to print just how many years ago that birthday was!

<details>
    <summary>SOLUTION</summary>
    
<p>

```js
 const moment = require('moment')  
  
 // Prints today's date  
 console.log(moment().format("MMM Do YYYY"))  
  
 // Prints my birthday  
 console.log(moment('09-11-1985', 'MM DD YYYY').format("dddd [the] Do [of] MMMM [in the year] YYYY"))  
  
 // Prints how long ago my birthday was  
 console.log('Oh boy, that was', moment('09-11-1985', 'MM DD YYYY').fromNow(), 'years ago!')
```

</p>
</details>


#### Git Ignore File

Before we get too much further, **WAIT**!

Take a look at the `node_modules` folder that got generated when you used the `npm install` command. How big is this folder? How many files are in it? What's going on?

In general, we keep track of the version of the module that we are using in a file called `package.json`. This means we can just redownload the modules based on the version number on any new computer we want to put our code on - be that a fellow developer's computer or a production server. A package.json file might look something like this:

```javascript
{
  "name": "node-introl",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "moment": "^2.24.0"
  }
}
```

> Notice there is a "dependencies" section which lists our 3rd party dependencies. Right now we just have one, but others we install will go here, along with their version numbers in alphabetical order.

So, because we can just re-install the appropriate packages, we actually don't _need_ to have the `node_modules` folder to be tracked by git at all! In fact, the node\_modules folder can get so huge and unweildy that it's greatly preferred that you **DO NOT** push them up to github nor track them with version control! In fact, this can also cause serious errors during deployment!

**How can we avoid this?!**

We can specify directions to git about which files it should ignore by creating a file called `.gitignore`. Yes, the `.` at the front is necessary!

A `.gitignore` file will contain a list of files and folders that git should NOT be tracking. Go ahead and make a `.gitignore` file now and put `node_modules` into it as the first line.

_.gitignore_

```text
node_modules
```

Congrats - now when you add git tracking to this folder, it will not track the node\_modules folder and will not push it to github!

Other common things to ignore for git are things like `.env` files which contain localized settings and possibly sensitive data like secret keys, salts, or API keys. Thus leading to this pro-tip:

> Life Pro Tip: .gitignore should be one of the first files you create in a project! Create it before you do a single check-in. Always. Don't be the developer who oopsed and put an API key in public.

