# MongoDB with Mongoose

## Objectives

* Update & destroy a model
* Initialize & create a new instance of a model
* Perform basic find queries
* Reference other documents in an instance of a model
* Work with embedded and referenced documents with Mongoose

## MongoDB + Mongoose

MongoDB is a document database for storing data. We can access MongoDB through Node by using an ORM called Mongoose. It's similar to other ORMs, but involves a little more setup.

## Setting up Mongoose in your app

Create a new Express app and install the relevant npm packages:

```bash
mkdir family-tree
cd family-tree

# setup npm
npm init -y

# install dependencies
npm install express 

# create index file
touch index.js
```

To use Mongoose in your Node app:

```bash
npm install mongoose
```

With the package installed, lets use it - open index.js and setup your app:

```js
var express = require('express');
var bodyParser = require('body-parser');
var app = express();

app.use(bodyParser.urlencoded({ extended: false }));

// Mongoose stuff
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/family-tree');

app.get('/', function(req, res) {
  res.send('Hi!');
});

app.listen(3000);
```

You can now execute all the mongoDB commands over the database `family-tree`, which will be created if it doesn't exist.

## Working with Models

#### Defining a Model

Like the ORMs we've worked with previously, Mongoose allows us to define models, complete with attributes, validations, and middleware (known as hooks in Sequelize, or callbacks in ActiveRecord). Let's make a model.

From within our family-tree app:

```bash
mkdir models
touch models/user.js
```

Now let's add:

```js
var mongoose = require('mongoose');

// create a schema
var userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  age: Number,
  website: String
});
```

MongoDB is schemaless, meaning: all the documents in a collection can have different fields, but for the purpose of a web app, often containing validations, we can still use a schema will cast and validate each type. Also note that we can have nested structures in a Mongoose model.

At the moment we only have the schema, representing the structure of the data we want to use. To save some data, we will need to make this file a Mongoose model and export it:

```js
//in users.js
var mongoose = require('mongoose');

var userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String
  }
});

var User = mongoose.model('User', userSchema);

// make this available to our other files
module.exports = User;
```

Notice that you can use objects and nested attributes inside an object.

Here's a look at the datatypes we can use in Mongoose documents:

- String
- Number
- Date
- Boolean
- Array
- Buffer (binary)
- Mixed (anything)
- ObjectId

Also, notice we create the Mongoose Model with `mongoose.model`. Remember, we can define custom methods here - this would be where we could write a method to encrypt a password.

#### Creating Custom Methods

When defining a schema, you can add custom methods and call these methods on the models. These are instance methods. Let's write a `sayHello` function under our schema:

```js
var userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String
  }
});

userSchema.methods.sayHello = function() {
  return "Hi " + this.name;
};

var User = mongoose.model('User', userSchema);

module.exports = User;
```

Now we can call it by requiring the User model in index.js:

```javascript
var User = require('./models/user');

// create a new user called Chris
var chris = new User({
  name: 'Chris',
  email: 'chris@gmail.com',
  meta: {
    age: 27,
    website: 'http://chris.me'
  }
});

app.get('/', function(req, res) {
  res.send(chris.sayHello());
});
```

Now run the app with `nodemon index.js` to see the result! You can define class methods in a similar manner by attaching the method to `.statics` instead of `.methods`

## Interacting with MongoDB's CRUD

Let's hope into an interactive shell and test out CRUD functionality. To do this, from our app directory, we'll have to type in `node` and then require our Models manually.

#### Create

We can create a User using the `.save` method in Mongoose. You can also call `.create` to combine creating and saving the instance.

```js
var newUser = User({
  name: 'bob',
  email: 'bob@gmail.com'
});

// save the user
newUser.save(function(err) {
  if (err) return console.log(err);
  console.log('User created!');
});

// create and save a user
User.create({ name: 'Emily', email: 'em@i.ly' }, function(err, user) {
  if (err) return console.log(err);
  console.log(user);
});
```

There is no "find or create" in Mongoose.

#### What about Read?

We can find multiple model instances by using the `.find` function, which accepts an object of conditions. There's also `.findOne` and `.findById` available.

```js
// Find All
User.find({}, function(err, users) {
  if (err) return res.send(err);
  res.send(users);
});

// Find only one user
User.findOne({}, function(err, users) {
  if (err) return res.send(err);
  res.send(users);
});

// Find by email
User.find({ email: req.params.email }, function(err, users) {
  if (err) return res.send(err);
  res.send(user);
});

// Find by id
User.findById(req.params.id, function(err, users) {
  if (err) return res.send(err);
  res.send(user);
});
```

Note that in the `.find` function, you can also use MongoDB queries such as `$gt`, `$lt`, `$in`, and others. Alternatively, there's a new `.where` syntax that can be used as well. [Documentation on Model.where can be found here](http://mongoosejs.com/docs/api.html#model_Model.where)

#### Update

Models can be updated in a few different ways - using `.update()`, `.findByIdAndUpdate()`, or `.findOneAndUpdate()`:

```js
// updates all matching documents
User.update({ name: 'brian' }, { meta: { age: 26 } }, function(err, user) {
  if (err) console.log(err);
  console.log(user);
});

// updates one match only
User.findOneAndUpdate({ name: 'brian' }, { meta: { age: 26 } }, function(err, user) {
  if (err) console.log(err);
  console.log(user);
});
```

#### Destroy

Models can be removed in a few different ways - using `.remove()`, `findByIdAndRemove()`, and `.findOneAndRemove()`.

```javascript
// find all users with the name Brian and remove them
User.remove({ name: 'brian' }, function(err) {
  if (err) console.log(err);
  console.log('Users deleted!');
});

// find the user with id 4 and remove it
User.findOneAndRemove({ name: 'brian' }, function(err) {
  if (err) console.log(err);
  console.log('User deleted!');
});
```

## Independent Practice

Using the code we just wrote and the [official Mongoose Models docs](http://mongoosejs.com/docs/models.html), add three routes to your Express app.

- `GET users/`, this will return all the documents
- `POST users/`, given some arguments in the url, this method will create a `user` record.
- `DELETE users/:id`, will remove the document corresponding to the collection
