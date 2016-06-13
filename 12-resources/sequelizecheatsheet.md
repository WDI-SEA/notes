#Sequelize Cheat Sheet

Sequelize documentation is horrendous, so here's a handy cheat sheet.

##Sequelize/PostgreSQL commands

###Create a database
```
createdb database_name
```

###Initialize Sequelize
```
sequelize init
```

###Create a Sequelize Model

**NOTE:** The model name will be **singular**

**NOTE 2:** Any foreign keys will be **modelNameId**
  * example: a foreign key to an `author` model will be `authorId`

```
sequelize model:create --name comment --attributes author:string,content:text,favoriteId:integer
```

###Create a Sequelize Migration (empty by default)
```
sequelize migration:create --name migrationName
```

###Run all Sequelize migrations
```
sequelize db:migrate
```

###Undo latest Sequelize migration
```
sequelize db:migrate:undo
```

---

##Sequelize Querying (using a `comment` model)

###Create
```js
db.favorite.create({
  author: 'Brian',
  content: 'A comment'
}).then(function(favorite) {
  //code here
});
```

###Find or Create
```js
//returns the instance if exists, otherwise creates it

db.favorite.findOrCreate({
  where: {
    author: 'Brian'
  },
  defaults: {
    content: 'A comment'
  }
}).spread(function(favorite, created) {
  //code here
});
```

###Find
```js
//returns only one instance; the first one that matches the where clause

db.favorite.find({
  where: {
    author: 'Brian'
  }
}).then(function(favorite) {
  //code here
});
```

###Find + Eager Load
```js
//returns only one instance, and loads all the comments associated with the favorite

db.favorite.find({
  where: {
    author: 'Brian'
  },
  include: [db.comment]
}).then(function(favorite) {
  // favorite.comments will exist, allowing access to the comments
});
```

###Find All
```js
//returns all instances that match the where clause

db.favorite.findAll({
  where: {
    author: 'Brian'
  }
}).then(function(favorite) {
  //code here
});
```

###Find By Id
```js
db.favorite.findById(1).then(function(favorite) {
  //code here
});
```

###Find One
```js
//returns only one instance

db.favorite.findOne().then(function(favorite) {
  //code here
});
```

###Update
```js
db.favorite.update({
  name: 'Josh'
  }, {
  where: {
    author: 'Brian'
  }
}).then(function(favorite){
  // do something after update
});
```

###Destroy
```js
db.favorite.destroy({
  where: {
    author: 'Brian'
  }
}).then(function() {
  // do something after destruction
});
```

---

##Associations

###1:M

Adding associations (using `author` and `post` models)

**author.js**

*Authors should have many posts*
```js
associate: function(models) {
  models.author.hasMany(models.post);
}
```

**post.js**

*A post should belong to an author*
```js
associate: function(models) {
  models.post.belongsTo(models.author);
}
```


###M:M

Adding associations (using `post` and `tag` models, with a join table called `postsTags`)

**post.js**

*A post should belong to many tags*
```js
associate: function(models) {
  models.post.belongsToMany(models.tag, {through: 'postsTags'});
}
```

**tag.js**

*A tag should belong to many posts*
```js
associate: function(models) {
  models.tag.belongsToMany(models.post, {through: 'postsTags'})
}
```

###Helper Functions (using a `post` model)

* `createPost()` - should create a post when called on a model related to post. Takes attributes as parameters
* `getPosts()` - should get posts when called on a model related to post
* `addPost(post)` - should add an existing post when called on a model related to post
* `setPost([post1, post2])` - should delete all existing associations and add the array of posts when called on a model related to post

---

##Promises

###`then`

This is the default promise called when a query is completed.

###`spread`

This is used to spread an array of values to parameters. This is only used for `findOrCreate`, where the callback has two parameters.

###`catch`

This is triggered if something goes wrong (an error).

###`finally`

This is triggered after all other callbacks (including `then`, `spread`, and `catch`). Can be used for cleanup.
