# Node Modules

### Importing and Exporting Modules with Node

Node's module system allows code written in one file to be exported, and then imported into other files. By importing a module (i.e. a specified section of code), we can then use that code as if it actually were written in the file we imported it to. 

Let's try an example!

1. Inside the ```my-first-node-project``` folder, create a javascript file called ```myModule.js```.

2. 
**Person.js**
```js
var Person = function(name) {
  this.name = name;
};

module.exports = Person;
```

**app.js**
```js
var Person = require('./Person.js');

var brian = new Person('Brian');
```

To view a practical example of importing and exporting modules, read
[this article](http://www.sitepoint.com/understanding-module-exports-exports-node-js/). You'll see that we can export multiple functions by assigning `module.exports` to an object. This is a pattern that we'll see frequently in Node.
