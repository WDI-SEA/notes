# Testing Node with Mocha/Chai

## Objectives

* Describe the importance of testing your code programmatically
* Use describe and assertion functions to test site functionality

## IMPORTANT NOTE

These concepts can be applied to any Express app. We'll be using our Taco app in this example, but feel free to use another.

https://github.com/WDI-SEA/tacoapp

## Mocha, Chai And Javascript Testing

We've now created several Express applications. All these apps cover a single topic, so most of the time, they are quite small. But with most apps, the codebase will become bigger and more complex every time you add some features. At some point, adding code in `file A` will break features in `file B`, and to avoid these "side-effects", we need to test our app.

To do so in Node, we will use two libraries: one to run the tests and a second one to run the assertions. Previously, we used the `assert` module to compare expected vs. actual results. However, we can use a different module called `chai` in order to create more readable assertions.

In addition to Chai, Mocha will be our testing framework. From the Mocha Website:

_"Mocha is a feature-rich JavaScript test framework running on Node.js and the browser, making asynchronous testing simple and fun. Mocha tests run serially, allowing for flexible and accurate reporting, while mapping uncaught exceptions to the correct test cases."_

To be able to make HTTP requests inside tests, we will use a framework called `supertest`.

## Let's Test!

### Setting up the app

Open the app provided and take a few minutes to explore the code and the routes being defined.

To test this app, we need to install a couple of dependencies.

First, let's install Mocha. We will install this globally only once, for convenience. Mocha is a command-line tool that can be run anywhere.

```bash
npm install -g mocha
```

Then we will install Chai, Supertest, and Mocha again using --save-dev

```bash
npm install chai supertest mocha --save-dev
```

**NOTE:** Saving Mocha as a development dependency does two things. First, we'll only have these tools in development environments. Second, we won't be relying on a user installing Mocha using the `-g` flag, thus guaranteeing that Mocha is installed. This will be handy for creating our own test scripts. Speaking of which...

#### Creating a test script

In order to run our tests by simply typing `npm test`, let's add a test script to `package.json`:

**package.json**

```
"scripts": {
  "test": "NODE_ENV=test node_modules/mocha/bin/mocha"
},
```

The script above will set the Node environment to `test`, which is very useful for handling test databases, as we'll see shortly. The next command runs Mocha from the project's `node_modules` folder. Super!

#### Files and Folders

Now that we're configured, let's set up our file and folder structure. All the tests will be written inside a folder `test` at the root of the app:

```bash
mkdir test
```

Then we will write the tests inside a file called `index.tests.js`:

```bash
touch test/index.tests.js
```

#### Let's write some tests

Open the file `index.tests.js`. We now need to require some dependencies at the top of this file:

```js
var expect = require('chai').expect;
var request = require('supertest');
var app = require('../index');
```

The code above imports Chai's `expect` assertions, as well as Supertest and our application.

All the tests need to be inside a `describe` function. `describe` functions are used to group tests. We can nest as many as we want. In our case, we'll use one `describe` block for our root route.

```js
describe('GET /', function() {
  //tests will be written inside this function
});
```

First, we will write a test to make sure that a request to `GET /` returns a HTTP status 200:

```js
describe('GET /', function() {
  it('should return a 200 response', function(done) {
    request(app).get('/')
    .expect(200, done);
  });
});
```

Now go in the command line and type `npm test`. You should get a message saying that you have 1 test passing.

Congrats, your test is passing!

> Note: You may see an error saying "Address already in use. This means nodemon is running your server somewhere else when your
tests also try to start the server. Either kill your nodemon server, or add this code around `app.listen()` to prevent your server
from starting twice:

```js
// prevent the app from starting twice if tests are running.
if (!module.parent) {
  app.listen(3000);
}
```

> If you see an error saying "TypeError: app.address is not a function", the following line needs to be added at the end of your main javascript file:

```js
 module.exports = app;
```

Every block of code that starts with `it()` represents a test.

The callback represents a function that Mocha will pass to the code so that the next test will be executed only when the current is finished and the `done` function is called - this allows tests to be executed once at a time.

## Verifying Tacos

Next, let's test the `tacos.js` controller. This presents a challenge due to Sequelize. However, as long as we have a test database, setting the `NODE_ENV` to `test` will use the test databse instead of the development database.

#### Setting up the database

The taco app should have a test database defined in `config/config.json`. Double-check that this is the case.

The test database is used when the `NODE_ENV` environment variable is set to `test`. This is done in our test script, now all we need is a test database. Let's create it (disregard migrations for now).

```bash
createdb tacos_test
```

#### before() and Sequelize

In order to ensure our test environment is consistent every time, we need to recreate and remigrate the database every time our tests are run. Mocha provides a couple handy functions that allow code to be executed before all or each-and-every test. These functions are `before()` and `beforeEach()`. We'll use `beforeEach()` to "sync" the test database before running all the tests.

Let's create these tests in a separate file called **tacos.tests.js**

```js
var expect = require('chai').expect;
var request = require('supertest');
var app = require('../index');
var db = require('../models');

before(function(done) {
  db.sequelize.sync({ force: true }).then(function() {
    done();
  });
});
```

We're importing Chai, Supertest, our application, as well as the models. Before all the tests, we want to run a function attached to `db.sequelize` called `sync`, and set the `force` property. This will take care of database setup and migrations for our tests.

#### GET /tacos

Testing `GET /tacos` will be similar as before.

```js
describe('GET /tacos', function() {
  it('should return a 200 response', function(done) {
    request(app).get('/tacos')
    .expect(200, done);
  });
});
```

#### POST /tacos

Testing `POST /tacos` will require sending form data, as well as verifying that a redirect occurred after the data was saved. We'll use the following functions to check these behaviors:

* `.type()` - sets the type of data we can send to the app
* `.send()` - accepts the data to send to the app

Additionally, we can check if `Location` in the response is set to `/tacos`, which is the route that the redirect should take us to.

```js
describe('POST /tacos', function() {
  it('should create and redirect to /tacos after posting a valid taco', function(done) {
    request(app).post('/tacos')
    .type('form')
    .send({
      name: 'Cheesy Gordita Crunch',
      amount: 6000
    })
    .expect('Location', '/tacos')
    .expect(302, done);
  });
});
```

#### DELETE /tacos/:id

Testing `DELETE /tacos/:id` will not only require checking the status code, but also checking if the response has a message property with a value of "success". This will involve direct access to the response, which can be accessed through `supertest` using the `.end()` function.

```js
describe('DELETE /tacos/:id', function() {
  it('should return a 200 response on deleting a valid taco', function(done) {
    request(app).delete('/tacos/1')
    .end(function(err, response) {
      expect(response.statusCode).to.equal(200);
      expect(response.body).to.have.property('msg');
      expect(response.body.msg).to.equal('success');
      done();
    });
  });
});
```

Note how the `expect` assertions have additional functions that can be called, which make the lines read as if written in plain English. These types of tests fall under **Behavior-Driven Development**. BDD is an extension of TDD, and it's a testing process that revolves around testing and debugging specific behaviors. Many frameworks can be used to implement BDD. [Here's a great post with more information about TDD vs. BDD](https://www.toptal.com/freelance/your-boss-won-t-appreciate-tdd-try-bdd)

## Independent Practice

Add tests to the suite:

1. Write an additional test for `DELETE /tacos/:id` to test deleting a taco that does not exist. Remember to think about the results you should *expect*, then write the tests to reflect those behaviors.
2. Write a set of tests for `PUT /tacos/:id`
3. Write tests for the remaining routes:
  * `GET /tacos/new`
  * `GET /tacos/:id/edit`
  * `GET /tacos/:id`

## Conclusion

We've covered the principles of testing in JavaScript, but Chai offers a lot of different expectations syntaxes. Check the [Chai Documentation](http://chaijs.com/api/)

- How does Mocha work with Chai to write tests in your JavaScript application?
- Describe how to configure your app to use Mocha and Chai.
