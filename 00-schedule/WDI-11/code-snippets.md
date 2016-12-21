# Code Snippets From Lecture

### Common Postgres / Sequelize Mistakes

Watch out. When you run the `sequelize model:create` command to create a model
you must provide the command with a singular 

If you're trying to create something to keep track of Users for a site then
sequelize will make two things:

- Sequelize makes *models*: These represent one user. They're singular. A model defines all
of the different properties that make up the thing you're trying to represent.
- Sequelize makes a *table*: Table names are plural. A Table is where all Users
will be stored in the database. The column names and column data types in the
database are derived from the model definition.

Models are singular. User, Book, Movie.
Tables are plural. Users, Books, Movies.

```
sequelize model:create --name user
  --attributes firstName:string,lastName:string,age:integer,email:string
```



### Parsing miniJSON
<script src="//repl.it/embed/Et7o/65.js"></script>

<https://repl.it/Et7o/2>

```js
// In our miniature version of JSON we have these rules:
// 1. must be one object starting and ending with {}
// 2. keys are surrounded in double quotes.
// 3. values are ONLY integers.
// 4. each key-value pair is separated by a comma.
// 5. keys and values are separated by a colon.
// 6. no whitespace.
var data = '{"page_loads":49,"students":11}';

// This function accepts a string that follows the rule specification
// of miniJSON defined above, and it returns a JavaScript object.
function parseMiniJSON(json) {
  var obj = {};
  
  // snip off first and last curly braces.
  json = json.substr(1, json.length - 2);
  
  var keyValuePairs = json.split(',');
  for (var i = 0; i < keyValuePairs.length; i++) {
    var key = keyValuePairs[i].split(":")[0];
    var val = keyValuePairs[i].split(":")[1];
    
    // snip off first and last double-qoutes
    key = key.substr(1, key.length - 2);
    
    // convert val to actual integer.
    val = parseInt(val, 10);
    
    obj[key] = val;
  }
  
  return obj;
}

var result = parseMiniJSON(data);
console.log("page loads:", result.page_loads);
console.log("students:", result.students);
console.log("loads per student:", result.page_loads / result.students);
```

### Classes
- Simple House class example <https://repl.it/EjiB/0>
- Point class with distanceTo method <https://repl.it/EjiG/2>

### How to Reset DOM
Here's a repo that shows you several things:
- how to detect which elements are clicked on.
- how to build a function that resets and initializes a page
- how to attach click handlers to newly created elements
- how to reset variables and manipulate the DOM back into
  some starting state.

Be sure to look at the [commit history](https://github.com/ga-students/how-to-reset-dom/commits/master)
to see how each step was completed.

<https://github.com/ga-students/how-to-reset-dom>

### Arrays and For Loops
- printing and array with fencepost commas: <https://repl.it/Eegy/10>
- get maximum value: <https://repl.it/Eehp/1>
- getEvenNumbers: <https://repl.it/Ee6k/41>
- isAscending: <https://repl.it/Eeqy/22>
- isUnique: <https://repl.it/Eer8/3>

### Function Declarations
- Two function syntaxes: <https://repl.it/Ed0a/4>
- Stomping on function names: <https://repl.it/Ed0b/2>

### Intervals and Timeouts
- a simple interval, timeout counter: <https://repl.it/CqVJ>
- counting up with an interval: <https://repl.it/CqVJ>
- clearInterval with setTimeout: <https://repl.it/CqV8/2>

- ding, and stop ding: <https://repl.it/CqV8/2>
- cat meowing, dog barking: <https://repl.it/CqV8/3>

### Scopes and Closures
- scope example: <https://repl.it/CqS4/4>
- bank account closure: <https://repl.it/CqTA/2>
- bad vs good scope/closure examples: <https://repl.it/CqVY/2>

### Iterators
- .reduce() example: <https://repl.it/CqZD>
- .filter() .map() .reduce() in one breath: <https://repl.it/CqZH/0>
