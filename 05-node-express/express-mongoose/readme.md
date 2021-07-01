# MongoDB with Mongoose

## Objectives

* Update & destroy a model
* Initialize & create a new instance of a model
* Perform basic find queries
* Reference other documents in an instance of a model
* Work with embedded and referenced documents with Mongoose

## MongoDB + Mongoose

_Mongoose_ is to MongoDB as Sequelize is to a SQL database. But, because it maps code to MongoDB _documents_, it is referred to as an **Object Document Mapper (ODM)** instead of an ORM. Mongoose is going to make it easier to perform CRUD using object-oriented JS instead of working directly MongoDB.

Using the Mongoose ODM is by far the most popular way to perform CRUD on a MongoDB. Mongoose's homepage says it best:

> "Mongoose provides a straight-forward, schema-based solution to model your application data"

Wait a second, what's with this "schema" business, isn't MongoDB schema-less? Well, yes it is, however, the vast majority of applications benefit when their data conforms to a defined structure (schema). Mongoose allows us to define schemas and ensures that documents conform.

Mongoose also provides lots of other useful functionality:
* Default property values
* Validation
* Automatic related model population via the `populate` method
* _Virtual properties_ - create properties like "fullName" that are not persisted in the database
* Custom _Instance methods_ which operate on the document
* _Static methods_ which operate on the entire collection 
* `pre` and `post` event lifecycle hooks (Mongoose "middleware")

## The Big Picture 

Here is the big picture overview of the components we'll be working with:

<img src="https://i.imgur.com/Q6A7KTQ.png" width="900">

### Big Picture Example 

This is the general flow of how we will use Mongoose...

#### Make a Schema

What is a schema? It is just the structure of our data model: essentially the field names and what data type they are. This is similar the the schema we could see of each of our data tables in postgres. Viewing the table schema showed each of the columns and their data types. Recall that colmuns in SQL translate into fields or attributes in MongoDB.

We define the structure of our model as a schema...

```js
const postSchema = new mongoose.Schema({
  content: String
}) 
```

This will make a single field named `content` and it will be a string.

Then we use this schema to build an actual model class...

```js
module.exports = mongoose.model('Post', postSchema) 
```

This creates a model called `Post` (**REMEMBER MODEL NAMES ARE ALWAYS SINGULAR**). This two-step process results in a usable model similar to the ones we saw in Sequelize. It can be required and used to perform CRUD on the `posts` collection in the MongoDB:

```js
const Post = require('./models/post') 
Post.create({content: 'Amazing post...'}) 
```

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
const express = require('express') 
const app = express() 

app.use(express.urlencoded({ extended: false })) 

// Mongoose stuff
const mongoose = require('mongoose') 
mongoose.connect('mongodb://localhost/familyTree') 

app.get('/', function(req, res) {
  res.send('Hi!') 
}) 

app.listen(3000) 
```

You can now execute all the mongoDB commands over the database `familyTree`, which will be created if it doesn't exist.

### Mongoose Event Handlers

Let's modify our index.js as follows:

	```js
	const mongoose = require('mongoose') 
	mongoose.connect('mongodb://localhost/familyTree') 
	
	// shortcut to mongoose.connection object
	const db = mongoose.connection 
	
	db.once('open', function() {
  		console.log(`Connected to MongoDB at ${db.host}:${db.port}`) 
	}) 
	
	db.on('error', function(err) {
  		console.error(`Database error:\n${err}`) 
	}) 
	```

We set up an event listener to fire once when the connection 'opens' to console log what host and port it is running on. It will also console log any errors whenever they occur.

## Working with Models

#### Defining a Model

Like the ORMs we've worked with previously, Mongoose allows us to define models, complete with attributes, validations, and middleware (known as hooks in Sequelize). Let's make a model.

From within our family-tree app:

```bash
mkdir models
touch models/user.js
```

Now let's add:

```js
const mongoose = require('mongoose') 

// create a schema
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  age: Number,
  website: String
}) 
```

MongoDB is schemaless, meaning: all the documents in a collection can have different fields, but for the purpose of a web app, often containing validations, we can still use a schema will cast and validate each type. Also note that we can have nested structures in a Mongoose model.

At the moment we only have the schema, representing the structure of the data we want to use. To save some data, we will need to make this file a Mongoose model and export it:

```js
//in users.js
const mongoose = require('mongoose') 

const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String
  }
}) 

// Here is where you actually name the model. NAME IT SINGULAR!
const = User = mongoose.model('User', userSchema) 

// make this available to our other files
module.exports = User 
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

#### Timestamps in Mongoose

Mongoose will add `createdAt` and add/update `updatedAt` fields if we set the `timestamps` option as follows in the schema:

	```js
	const userSchema = new mongoose.Schema({
    name: String,
    email: { type: String, required: true, unique: true },
    meta: {
      age: Number,
      website: String
    }
	}, {
	  timestamps: true
	}) 
	```

#### Creating Custom Methods

When defining a schema, you can add custom methods and call these methods on the models. These are instance methods. Let's write a `sayHello` function under our schema:

```js
const userSchema = new mongoose.Schema({
  name: String,
  email: { type: String, required: true, unique: true },
  meta: {
    age: Number,
    website: String
  }
}) 

userSchema.methods.sayHello = function() {
  return "Hi " + this.name 
} 

const User = mongoose.model('User', userSchema) 

module.exports = User 
```

Now we can call it by requiring the User model in index.js:

```js
const User = require('./models/user') 

// create a new user called Chris
const chris = new User({
  name: 'Chris',
  email: 'chris@gmail.com',
  meta: {
    age: 27,
    website: 'http://chris.me'
  }
}) 

app.get('/', function(req, res) {
  res.send(chris.sayHello()) 
}) 
```

Now run the app with `nodemon` to see the result! You can define class methods in a similar manner by attaching the method to `.statics` instead of `.methods`

## Interacting with MongoDB's CRUD

Let's hope into an interactive shell and test out CRUD functionality. To do this, from our app directory, we'll have to type in `node` and then require our Models manually.

## A Quick note about different versions of Mongoose

Up until Mongoose version 4 Database queries required callback functions to handle asynchronous database operations like so:

```js
// create and save a user
User.create({ name: 'Emily', email: 'em@i.ly' }, function(err, user) {
  if (err) return console.log(err) 
  console.log(user) 
}) 
```

But starting in version 4 Mongoose database queries all return promises so queries can now be handled with `.then()` syntax or `async/await`:

```js
// create and save a user with .then()
User.create({ name: 'Emily', email: 'em@i.ly' })
  .then(user => {
    console.log(user) 
  })
  .catch(err => {
    console.log(err)
  })

// create and save a user with async/await
try {
  const user = await User.create({ name: 'Emily', email: 'em@i.ly' })
  console.log(user)
} catch (err) {
  console.log(err)
}
```

According to the [Mongoose docs on writing queries](https://mongoosejs.com/docs/queries.html) using either callbacks or promises to handle async database operations are both still supported and equally valid choices, but mixing the two together will lead to bugs so you should decide on one way or the other.

#### Create

We can create a User using the `.save` method in Mongoose. You can also call `.create` to combine creating and saving the instance.

```js
const newUser = User({
  name: 'bob',
  email: 'bob@gmail.com'
}) 

// save the user
newUser.save(function(err) {
  if (err) return console.log(err) 
  console.log('User created!') 
}) 

// create and save a user
User.create({ name: 'Emily', email: 'em@i.ly' }, function(err, user) {
  if (err) return console.log(err) 
  console.log(user) 
}) 
```

There is no "find or create" in Mongoose.

#### What about Read?

We can find multiple model instances by using the `.find` function, which accepts an object of conditions. There's also `.findOne` and `.findById` available.

```js
// Find All
User.find({}, function(err, users) {
  if (err) return res.send(err) 
  res.send(users) 
}) 

// Find only one user
User.findOne({}, function(err, user) {
  if (err) return res.send(err) 
  res.send(user) 
}) 

// Find by email
User.find({ email: req.params.email }, function(err, user) {
  if (err) return res.send(err) 
  res.send(user) 
}) 

// Find by id
User.findById(req.params.id, function(err, user) {
  if (err) return res.send(err) 
  res.send(user) 
}) 
```

Note that in the `.find` function, you can also use MongoDB queries such as `$gt`, `$lt`, `$in`, and others. Alternatively, there's a new `.where` syntax that can be used as well. [Documentation on Model.where can be found here](http://mongoosejs.com/docs/api.html#model_Model.where)

#### Update

Models can be updated in a few different ways - using `.update()`, `.findByIdAndUpdate()`, or `.findOneAndUpdate()`:

```js
// updates all matching documents
User.update({ name: 'brian' }, { meta: { age: 26 } }, function(err, user) {
  if (err) console.log(err) 
  console.log(user) 
}) 

// updates one match only
User.findOneAndUpdate({ name: 'brian' }, { meta: { age: 26 } }, function(err, user) {
  if (err) console.log(err) 
  console.log(user) 
}) 
```

#### Destroy

Models can be removed in a few different ways - using `.remove()`, `findByIdAndRemove()`, and `.findOneAndRemove()`.

```js
// find all users with the name Brian and remove them
User.remove({ name: 'brian' }, function(err) {
  if (err) console.log(err) 
  console.log('Users deleted!') 
}) 

// find the user with id 4 and remove it
User.findOneAndRemove({ name: 'brian' }, function(err) {
  if (err) console.log(err) 
  console.log('User deleted!') 
}) 
```

## Independent Practice

Using the code we just wrote and the [official Mongoose Models docs](http://mongoosejs.com/docs/models.html), add three routes to your Express app.

- `GET users/`, this will return all the documents
- `POST users/`, given some arguments in the url, this method will create a `user` record
- `PUT users/:id`, update one document with at a a specific id
- `DELETE users/:id`, will remove the document corresponding to the collection
