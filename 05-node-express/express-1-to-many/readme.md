# Sequelize - 1 to Many Relationships

## Objectives

* utilize table relationships in a database
* add a 1:M association using Sequelize
* use helper methods to add and access a related model
* understand the purpose of eager loading when accessing a model's associations

Today we're going to cover how to setup a one to many relationship, using more than one table. This will allow data in one table to be associated with data in another.

## Getting Started

Creating a blog.

```
npm init -y

npm install express ejs pg sequelize

createdb blog

sequelize init
```

Make sure to setup `config.json` with postgres settings.

## Creating A Model

There are a few things to remember when creating models. Models shall be lowercase and singular. Sequlize will automatically create plural tables when any migrations are run. Also id, createdAt, and updatedAt fields are given for you.

```
sequelize model:create --name author --attributes name:string
```

When creating a table that will reference another table, use the following format, `parentId`, when adding the foreign key to the table. This format is necessary for some of built in methods of Sequelize.

```
sequelize model:create --name post --attributes title:string,content:text,authorId:integer
```

### Adding the Associations

The following lines need to be inserted into the author and post models respectively in the `associate` function. The comment line is where you will insert it.

Insert into **models/author.js**, inside the `associate` function

```js
associate: function(models) {
  models.author.hasMany(models.post);
}
```

Insert into **models/post.js**, inside the `associate` function

```js
associate: function(models) {
  models.post.belongsTo(models.author);
}
```

Finally, let's run create all the necessary tables from our models by migrating the database.

```
sequelize db:migrate
```

Read more: [Seqeulize docs - One to Many](http://docs.sequelizejs.com/en/latest/docs/associations/#one-to-many-associations)

## Using the association

Once the association is set up, we can use the `createModel`, `getModels`, `setModel`, and `addModel` helper methods. "Model" in each of these is replaced with the model name you create.

### Creating an associated item with `createModel`

We can use the `createPost` method to create a new post associated with an author. Remeber to use the `.then` promise.

```js
db.author.findOne().then(function(author) {
  author.createPost({
    title: 'Post title',
    content: 'this is the post content'
  }).then(function(post) {
    console.log(post.get());
  });
});
```

### Loading associated items using `getModels`

We can manually get all posts of an author by calling `.getPosts()` on an author instance. Remember this query is asynchronous and takes time, so we have to  use a `.then()` promise too.

```js
db.author.findOne().then(function(author) {
  //load posts for this author
  author.getPosts().then(function(posts) {
    //do something with posts here
  });
});
```

### Other methods

`setModel` and `addModel` are used to associate an existing record. If you created a post and later wanted to add an association to an author this is how you'd do it.

```js
db.author.findOne().then(function(author) {
  //associate previously loaded post instance
  author.addPost(post);
});
```

## Using `include`

Sequeize supports "eager loading", meaning it can load all of the posts for us in advance if we know we need them. We let it know what we need by using `include`.

```js
db.author.findAll({
  include: [db.post]
}).then(function(authors){
  // authors will have a .posts key with an array of posts
  console.log(author.posts);
});
```
