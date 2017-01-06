# Code Snippets From Lecture

## Testing Models and Using Istanbul for Code Coverage

```
npm install -g istanbul
istanbul cover _mocha -- -R nyan
open coverage/lcov-report/index.html
```

```js
var expect = require('chai').expect;
var db = require('../models');

before(function(done) {
  db.sequelize.sync({ force: true }).then(function() {
    done();
  });
});

describe('User Model', function() {
  describe('Creating new users', function() {
    it('should be able to create new users', function(done) {
      db.user.findOrCreate({
        where: { email: 'user@gmail.com' },
        defaults: {
          name: 'User Userton',
          password: 'regularoldpassword'
        }
      }).spread(function(user, created) {
        expect(created).to.equal(true);
        expect(user.email).to.equal('user@gmail.com');
        expect(user.name).to.equal('User Userton');
        done();
      });
    });

    it('should reject invalid emails', function(done) {
      db.user.findOrCreate({
        where: { email: 'nopenopenope' },
        defaults: {
          name: 'User Userton',
          password: 'regularoldpassword'
        }
      }).spread(function(user, created) {
        expect(true).to.equal(false);
      }).catch(function(error) {
        expect(error.message).to.equal('Validation error: Invalid email address');
        done();
      });
    });

    it('should prevent duplicate accounts from being created', function(done) {
      db.user.findOrCreate({
        where: { email: 'dupe@dupe.com' },
        defaults: {
          name: 'dupe',
          password: 'dupedupe'
        }
      }).spread(function(user, created) {
        expect(created).to.equal(true);
        db.user.findOrCreate({
          where: { email: 'dupe@dupe.com' },
          defaults: {
            name: 'dupe',
            password: 'dupedupe'
          }
        }).spread(function(user, created) {
          expect(created).to.equal(false);
          done();
        });
      });
    });
  });
});
```

## Merge Two Sorted Arrays

<https://repl.it/FCY0/67>

## Security Vulnerabilities Based On Measuring Time
Here's a function that checks whether two passwords are identical. It compares
an actual password to a login attempt character by character. There's a problem!
This function returns false too soon. A malicious user can time how long it takes
to run this function and detect how far along the function got before it returned
true or false. By running the function several times with different input a user
can determine how much of their password was correct. The longer the function takes
to run, the more correct the first letters in the password were, because the function
took more time to check more letters in the attempt.

See the attached GitHub repo to check out the code and run the experiment yourself.

```
function passwordCheck(attempt) {
  var password = "SUPERSECRET";
  for (var i = 0; i < password.length && i < attempt.length; i++) {
    if (password[i] !== attempt[i]) {
      return false;
    }
  }

  return true;
}
```
Repl.it: <https://repl.it/FBt4/0>
GitHub: <https://github.com/geluso/time-attack-password-demo>

<script src="//repl.it/embed/FBt4/0.js"></script>

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
