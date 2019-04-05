# Node Package Manager

There are three types of Node modules:
1. Core Modules (like ```fs```)
2. Local Modules (that you create)
3. Third Party Modules

Core modules are great for gaining quick access to commonly-needed functionality in your program, and local modules allow you the flexibility to build out whatever tools you might possibly need, but third party modules, which fall somewhere in between, are perhaps the most exciting modules of them all!

### Node Packages

Because developers are awesome, there are hundreds of thousands of already-written modules out there, ready for use! Each of these modules are encapsulated in a ***Node Package*** and made available via ***Node Package Manger*** or ***NPM***, for short. A node package is a folder that contains one or more modules, a ```package.json``` file, and any meta-info needed to make the modules work correctionly and play well with your node program.

### NPM

NPM is the largest open-source software registry in the world. It includes a website, a registry of Node Packages, and a command line interface that allows us to easily incorporate packages into our programs.

Check out this [NPM Intro Video](https://www.youtube.com/watch?v=x03fjb2VlGY)

The NPM CLI makes incorporating a node package into your program fairly easy, but you can refer to [this playlist](https://www.youtube.com/watch?v=pa4dc480Apo&list=PLQso55XhxkgBMeiYmFEHzz1axDUBjTLC6) if you ever get lost. It includes a whole series of videos that demonstrate the fundamentals of using NPM.

The NPM CLI installed automatically on your machine when you installed Node. Verify this now by checking the version in your terminal:
```npm -v```

### First Node Package: Nodemon

[Nodemon](https://www.npmjs.com/package/nodemon) is a package that makes developing node apps easier. It restarts the application everytime you save changes to your code.

We will use Nodemon quite a bit, so instead of installing it on each node app we build, we will install it globally. This will make it accessible to all of our node apps.

In the command line, type the following code:
```npm install -g nodemon```

Since we're installing it globally (that's where the ```-g``` flag comes in), it doesn't matter what directory we're in.

Let's see nodemon in action! Try running your ```my-first-node-app``` using nodemon. Simply ```cd``` into the directory, then run ```nodemon```. Nodemon knows to run the file that corresponds to ```main:``` in your ```package.json```.

Now open up ```my-first-node-app``` in sublime. Add the following code to ```index.js```:

```js
var i = 0

var myTimer = setInterval(count, 1000)

function count() {
	console.log(i)
	i++
}
```

Make sure to save the file and check out what's happening in your terminal!

Now change the ```count``` function to print ```i*2``` instead of just ```i``` and save. 

You can always restart nodemon by typing ```rs```.

To quit nodemon (and any program running in the terminal), press CTRL+C.

***Congratulations***, you've just installed and used your first third party node module!

We installed nodemon globally, but most node packages will only be useful for specific projects. In this case, when you run ```npm install [package name]``` you want to make sure you're inside the directory of the project you want to use the package in, and leave off the ```-g``` flag.
