![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# Testing Node with Mocha/Chai

## Objectives

* Describe the importance of testing your code programmatically
* Use describe and assertion functions to do basic testing

## IMPORTANT NOTE

This lesson includes starter code. Fork and clone here to follow along:

https://github.com/WDI-SEA/mocha-chai-starter

## Mocha, Chai And Javascript Testing

We've now created several Express applications. All these apps cover a single topic, so most of the time, they are quite small. But when you create a larger application, the codebase will become bigger and more complex every time you add some features. At some point, adding code in file A will break features in file B, and to avoid these "side-effects", we need to test our app.

To do so in Node, we will use two libraries: one to run the tests and a second one to run the assertions.

Mocha will be our testing framework. From the Mocha Website:

_"Mocha is a feature-rich JavaScript test framework running on Node.js and the browser, making asynchronous testing simple and fun. Mocha tests run serially, allowing for flexible and accurate reporting, while mapping uncaught exceptions to the correct test cases."_


For assertions, we will use Chai. From the Chai website:

_"Chai is a BDD / TDD assertion library for node and the browser that can be delightfully paired with any javascript testing framework."_


To be able to make HTTP requests inside tests, we will use a framework called `supertest`.

## Let's Test! Codealong

### Setting up the app

Open the starter code provided and take a few minutes to explore the code and the routes being defined.

To test this app, we need to install a couple of dependencies.

First, let's install mocha, and we will install this package globally using `-g`:

```bash
npm install -g mocha
```

Then we will install chai and supertest using --save-dev

```bash
npm install chai supertest --save-dev
```

#### Files and Folders

Now that we're configured, let's set up our file and folder structure. All the tests will be written inside a folder `test` at the root of the app:

```bash
mkdir test
```

Then we will write the tests inside a file called `candiesTests.js`:

```bash
touch test/candiesTests.js
```

> Note: Explain that because our tests will request the application through HTTP, students have to make sure they are running the app while running the tests

#### Let's write some tests

Open the file `candies_tests.js`. We now need to require some dependencies at the top of this file:

```js
var should = require("chai").should();
var expect = require("chai").expect;
var request = require("supertest");
var app = require("../index");
```

All the tests need to be inside a `describe` function.  We will use one describe block per route:

```js
describe("GET /candies", function() {
  //tests will be written inside this function
});
```

First, we will write a test to make sure that a request to the index path `/candies` returns a http status 200:

```js
describe("Candies", function() {
  it("should return a 200 response", function(done) {
    request(app).get("/candies")
    .expect(200, done);
  });
});
```

Now go in the command line and type `mocha` from the root of the project. You should get a message saying that you have 1 test passing.

Congrats, your test is passing!

Every block of code that starts with `it()` represents a test.

The `callback` represents a function that Mocha will pass to the code so that the next test will be executed only when the current is finished and the `done` function is called - this allows tests to be executed once at a time.

Now, let's verify the content of the response by looking at the data sent back by hitting the `/candies` endpoint:

```js
[
  {
    id: 1,
    name: "Chewing Gum",
    color: "Red"
  },
  {
    id: 2,
    name: "Pez",
    color: "Green"
  },
  {
    id: 3,
    name: "Marshmallow",
    color: "Pink"
  },
  {
    id: 4,
    name: "Candy Stick",
    color: "Blue"
  },
  {
    id: 5,
    name: "test",
    color: "brown"
  }
]

```

We can write a test that verifies the response is an array:

```js
it("should return an array", function(done) {
  request(app).get("/candies")
  .end(function(error, response) {
    expect(response.body).to.be.an('array');
    done();
  });
});
```

We can write another test that verifies the presence of a field in the response:

```js
it("should return an object that have a field called 'name' ", function(done) {
  request(app).get("/candies")
  .end(function(error, response) {
    expect(response.body[0]).to.have.property('name');
    done();
  });
});
```


We can also send data to the server and test the behavior - in our case, we want to make sure that when we post some JSON to `/candies`, a new object is added to the array candies.

Because we are going to test another route, lets add another describe block:

```js
describe("POST /candies", function() {

});
```

For this test, we need to:

1. Create a new object by sending a `POST` request
2. Verify that a new object has been "saved" by requesting the index route

For this, we will use `before` blocks. A `before` block will be executed for every `it` function is called inside a `describe` block.

Add this inside the new `describe` block:

```js
before(function(done) {
  request(app).post("/candies")
  .send({
    id: 5,
    name: "Lollipop",
    color: "Red"
  }).end(done);
});
```

This code will be called for every test we will add into the current `describe` block.

Now, we can verify that calling "POST" will add an object to candies:

```js
it("should add a candy object to the collection candies and return it", function(done) {
  request(app).get("/candies")
  .end(function(error, response) {
    expect(response.body.length).to.equal(5);
    done();
  });
});
```

Run the `mocha` command in the terminal, you should now have four passing tests!


## Independent Practice

Add tests to the suite:

1. Write a test that make sure the object returned when you call show with a specific ID contains the right fields.
2. Write a test that ensure an object is deleted from the array candies when you call delete.
3. Write a test that ensure a property is updated when you call `PUT /candies/:id/edit`


## Conclusion

We've covered the principles of testing in JavaScript, but Chai offers a lot of different expectations syntaxes. Check the [Chai Documentation](http://chaijs.com/api/)

- How does Mocha work with Chai to write tests in your JavaScript application?
- Describe how to configure your app to use Mocha and Chai.
