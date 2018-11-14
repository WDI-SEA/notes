#Node Modules

### Importing and Exporting Modules with Node

Node's module system allows code written in a partiuclar file (or folder) to be exported, and then imported into other files. Here's an example of a module called `Person.js` being imported into a file.

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
