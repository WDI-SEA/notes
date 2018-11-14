# Node Modules

### Importing and Exporting Modules with Node

Node's module system allows code written in one file to be exported, and then imported into other files. By importing a module (i.e. a specified section of code), we can then use that code as if it actually were written in the file we imported it to. 

Let's try an example!

1. Create your module.

Inside the ```my-first-node-project``` folder, create a javascript file called ```myModule.js```.

In Node, ```module.exports``` is an object that will hold the code to be exported. We can use dot-notation to add the code we want to export to this object.

Add the following code to your ```myModule.js``` file:

```js
module.exports.beBasic = function() {
	return "That's so fetch.";
}
```

Now, our module.exports object has a key-value pair where the key is ```beBasic``` and the value is a function.

2. Import your module in ```index.js```.

This is where the ```require``` function, specific to Node, comes into play. This function takes one argument: the path to the file that contains the module you are exporting.

In the ```index.js``` file, write the following code:

```js
var myModule = require('./myModule.js');

console.log(myModule.beBasic());
```

Run ```index.js``` via the command line:

```node index.js```

Voila! You've successfully created and imported a module!

Let's add some more code to our module. In ```myModule.js```, add the following code:

```js
module.exports.beBasic = function() {
	console.log("That's so fetch.");
}

var count = function() {
	for (var i = 0; i <= 10; i++) {
		console.log(i);
	}
}
```

Now call this new count function from ```index.js```:

```js
var myModule = require('./myModule.js');

myModule.beBasic();
myModule.count();
```

Try running this code in the command line:
```node index.js```

What happened? Why didn't this work?

_The exported module will only contain the code that is encapsulated in the_ ```module.exports``` _object!_

How do we get our ```count``` function to run? Make this happen.

Functions aren't the only things we can export! Try adding some other types of data to your module.

To view a practical example of importing and exporting modules, read
[this article](http://www.sitepoint.com/understanding-module-exports-exports-node-js/). You'll see that we can export multiple functions by assigning `module.exports` to an object. This is a pattern that we'll see frequently in Node.
