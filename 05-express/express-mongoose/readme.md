![General Assembly Logo](http://i.imgur.com/ke8USTq.png)

# MongoDB with Mongoose

## Objectives

* Update & destroy a model
* Initialize & create a new instance of a model
* Perform basic find queries
* Reference other documents in an instance of a model
* Work with embedded and referenced documents with Mongoose

## Using MongoDB with Node

NodeJS and MongoDB work really well together. To handle HTTP requests and read from or send data to MongoDB, Mongoose is the most common Node.js ORM to manipulate data using MongoDB: CRUD functionality is something that is necessary in almost most every application, as we still have to create, read, update, and delete data.

Since we'll be able to use JSON across our application - with Mongo and Node - using JavaScript in our application is much easier. The MEAN stack - Mongo, Express, Angular, and Node - is becoming increasingly popular because of this.

### What Is Mongoose?

Mongoose is an object modeling package - think ORM for Node; this gives us the MongoDB CRUD commands.

## Setting up Mongoose in your app

Create a new Express app and install the relevant npm packages:

```bash
mkdir family-tree
cd family-tree

# setup npm
npm init

# install dependencies
npm install --save express body-parser

# create index file
touch index.js
```

To use Mongoose in your Node app:

```bash
$ npm install --save mongoose
```

With the package installed, lets use it - open index.js and setup your app:

```javascript
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

You can now execute all the mongoDB commands over the database `family-tree`.


## Working with Models

#### Defining a Model

We must build a Mongoose Model before we can use any of our new CRUD operations; think of the models as constructors we define, documents we can persist to and request from our database. Just like a `schema.rb` file, our Mongoose Schema is what we'll use to define our document attributes. Think about it like this: a document is the equivalent of a record/row in a relational database; only here, our attributes - or columns - are flexible.

One large different from Rails/Sinatra: we can define methods in our Mongoose schema!

From within our family-tree app:

```bash
mkdir models
touch models/user.js
```

Now let's add:

```javascript
var mongoose = require('mongoose');

// create a schema
var userSchema = new mongoose.Schema({
  firstName: String,
  lastName: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String,
    address: String,
    country: String,
  }
});
```

MongoDB is schemaless, meaning: all the documents in a collection can have different fields, but for the purpose of a web app, often containing validations, it's better to use a schema that will cast and validate each type.

At the moment we only have the schema, representing the structure of the data we want to use. To save some data, we will need to make this file a Mongoose model and export it:

```javascript
//in users.js
var mongoose = require('mongoose');

var userSchema = new mongoose.Schema({
  firstName: String,
  lastName: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String,
    address: String,
    country: String,
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

When defining a schema, you can add custom methods and call these methods on the models.  You can even overwrite the default Mongoose document methods. Let's write a `sayHello` function under our schema:

```javascript
var userSchema = new mongoose.Schema({
  firstName: String,
  lastName: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String,
    address: String,
    country: String,
  }
});

userSchema.methods.sayHello = function() {
  return "Hi " + this.firstName;
};

var User = mongoose.model('User', userSchema);

module.exports = User;
```

Now we can call it by requiring the User model in index.js:

```javascript
var User = require('./models/user');

// create a new user called Chris
var chris = new User({
  firstName: 'Chris',
  meta:{
    age: 27
  }
});

app.get('/', function(req, res) {
  res.send(chris.sayHello());
});
```

Now run the app with `nodemon index.js` to see the result!

## Interacting with MongoDB's CRUD

Let's hope into an interactive shell and test out CRUD functionality. To do this, from our app directory, we'll have to type in `node` and then require our Models manually.

#### Create

We'll create two users using the User method from before, along with the default save method from Mongoose:

```javscript
// in index.js

var newUser = User({
  firstName: 'bob',
  email: 'bob@gmail.com'
});

// save the user
newUser.save(function(err) {
  if (err) console.log(err);
  console.log('User created!');
});

var newUser2 = User({
  first_name: 'brian',
  email: 'brian@gmail.com'
});

// save the user
newUser2.save(function(err) {
  if (err) console.log(err);
  console.log('User created!');
});
```

#### What about Read?

Just like ActiveRecord, we can use the JavaScript equivalent of `.all`, `.find_by_`, and `.find` to get a hold of what we're looking for.

Inside `index.js` let's add:

```javscript
// Find All
app.get('/users', function(req, res) {
  User.find({}, function(err, users) {
    if (err) return res.send(err);
    res.send(users);
  });
});
```

...and just like `.find_by_` in ActiveRecord, you'll get the first record that matches the attributes defined, but in Mongoose, it's `.find`:

```javascript
//Find One
app.get('/users/:fName', function(req, res) {
  User.find({ firstName: req.params.fName }, function(err, user) {
    if (err) return res.send(err);
    res.send(user);
  });
});
```

There's also `.findById`:

```javascript
// get a user with ID of 1
User.findById('5654c4f06d80d4d95c69654a', function(err, user) {
  if (err) console.log(err);
  console.log(user);
});
```

#### Update

For update, you can do it in one of two ways (that are super easy!) - using `.findByIdAndUpdate()` or `.findOneAndUpdate()`:

```javascript
User.findOneAndUpdate({ firstName: 'brian' }, { meta: { age: 26 } }, function(err, user) {
  if (err) console.log(err);
  console.log(user);
});
```

#### Destroy

Mongoose gives you two easy methods to delete documents - `findByIdAndRemove()`and `.findOneAndRemove()`.

```javascript
// find the user with id 4
User.findOneAndRemove({ firstName: 'brian' }, function(err) {
  if (err) console.log(err);
  console.log('User deleted!');
});
```

## Independent Practice

Using the code we just wrote and the [official Mongoose Models docs](http://mongoosejs.com/docs/models.html). Add three routes to your Express app.

- `GET users/`, this will return all the documents
- `POST users/`, given some arguments in the url, this method will create a `user` record.
- `DELETE users/:id`, will remove the document corresponding to the collection


## What are embedded documents?

Embedded documents are just what they sound like: documents with their own schemas nested in other documents. They take of the form of objects within an array.  You can think of this as a sort of `has_many` relationship - the context to use embedded documents is data entities need to be used/viewed in context of another.

The nested schema are equipped with all the same features as your models: defaults, validators, middleware, and even error handling, as they are tied to the save() error callback; and Mongoose can work with embedded documents by default.


Let's look at these two schemas below - we can embed `childSchema` into the property `children`:

```javascript
var childSchema = new Schema({ name: 'string' });

var parentSchema = new Schema({
  children: [childSchema]
})

var Parent = mongoose.model('Parent', parentSchema);
var parent = new Parent({ children: [{ name: 'Matt' }, { name: 'Sarah' }] })
parent.children[0].name = 'Matthew';
parent.save(function(err) {
  if (err) console.log(err);
  console.log('New Parent!');
});
```

Or from mongoDB official docs, we can look at this example with Patron and Address models:

```javascript
{
   _id: "joe",
   name: "Joe Bookreader"
}

{
   patron_id: "joe",
   street: "123 Fake Street",
   city: "Faketon",
   state: "MA",
   zip: "12345"
}

{
   patron_id: "joe",
   street: "1 Some Other Street",
   city: "Boston",
   state: "MA",
   zip: "12345"
}
```
The address documents make two references to the Joe Bookreader object, so instead we can:

```javascript
{
   _id: "joe",
   name: "Joe Bookreader",
   addresses: [
                {
                  street: "123 Fake Street",
                  city: "Faketon",
                  state: "MA",
                  zip: "12345"
                },
                {
                  street: "1 Some Other Street",
                  city: "Boston",
                  state: "MA",
                  zip: "12345"
                }
              ]
 }
 ```

Note that sub-documents do not save individually, only with the highest-level document; in this case, the addresses are saved with the Joe Bookreader Patron document.

#### Finding a sub-document

All documents in Mongoose have an  `_id`.  Look above at our Patron example.  Joe Bookreader has an `_id` of 'joe'. DocumentArrays have a special `id` method for looking up a document by its `_id`.

```javascript
// in our first example
var doc = parent.children.id(idYouAreLookingFor);

// in the second example
var doc = patron.addresses.id(idYouAreLookingFor)
```

#### Adding and Removing sub-docs

Remember Ruby methods like `pop`, `push`, or the `<<` operator?  We'll, Mongoose comes with MongooseArray methods like as `push`, `unshift`, `addToSet`, and others.  And just like adding them, we can remove them with `remove()`

Using code from the official docs, we can see how these are used:

```javascript
var Parent = mongoose.model('Parent');
var parent = new Parent;

// create a child
parent.children.push({ name: 'Liesl' });
var subdoc = parent.children[0];
console.log(subdoc) // { _id: '501d86090d371bab2c0341c5', name: 'Liesl' }
subdoc.isNew; // true

parent.save(function (err) {
  if (err) return handleError(err)
  console.log('Success!');
});

//remove

var doc = parent.children.id(idYouAreLookingFor).remove();
parent.save(function (err) {
  if (err) return handleError(err);
  console.log('the sub-doc was removed')
});

```

Sub-docs may also be created without adding them to the array by using the create method of MongooseArrays.

```javascript
var newdoc = parent.children.create({ name: 'Aaron' });
```

## Conclusion
Mongoose is just a bridge to use MongoDB inside a NodeJS environment. There are a lot of options when creating a schema with Mongoose, we've just seen a few for the moment.

- How does Mongoose compare to ActiveRecord?
- How does the schema in Mongoose/Mongo/Express compare to Rails?
