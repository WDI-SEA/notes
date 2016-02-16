#Sequelize - Many to Many

##Objectives

* Create a join table and utilize it in a many-to-many relationship
* Use Sequelize's helper methods to add relationships between two different models.

If we wanted to expand our models to include a many to many relationship, we can use a many to many relationship via a join table. We will be expanding our data model to include authors, posts, and tags.

**Very Important** Name - your models `singular`

```
sequelize model:create --name author --attributes name:string

sequelize model:create --name post --attributes title:string,body:string,authorId:integer

sequelize model:create --name tag --attributes name:string
```

**Very Important** Name your join tables as two plural models combined, such as `tacosBurritos`

`sequelize model:create --name postsTags --attributes postId:integer,tagId:integer`

##Update your Associations

In order to associate posts to tags in a many to many fashion, you will need to update the associations on the posts and tags (we'll update the author as well)

###author.js

```js
associate: function(models) {
  models.author.hasMany(models.post)
}
```

###post.js

```js
associate: function(models) {
 models.post.belongsTo(models.author)
 models.post.belongsToMany(models.tag, {through: "postsTags"})
}
```

###tags.js

```js
associate: function(models) {
  models.tag.belongsToMany(models.post, {through: "postsTags"})
}
```

##Examples

###Create a post attached to an author

There are some helper functions that get generated automatically when you want to create a related item:

```js
db.author.findOrCreate({where: {name: "Brian"}}).spread(function(author, created) {
  author.createPost({title: "taco", body: "burrito"}).then(function(post) {
  });
});
```

###Add a unique tag to a Post.

In order to add a unique tag to a post, we must first try to find or create a tag, in order to make sure it is in fact unique.

Secondly, we must attach a post to the tags, using some built in helpers.

Some ORM has capabilities to do a bulk create on an object associations, but that kind of logic is not built in Sequelize.

```js
db.author.findOrCreate({where: {name: "Brian"}}).spread(function(author,created){
  author.createPost({title: "newTaco", content: "burrito"}).then(function(post) {
    db.tag.findOrCreate({where: {name: "xyzasdf"}}).spread(function(tag, created) {
      post.addTag(tag).then(function() {
        console.log("Its over");
        // res.send("");
      });
    });
  });
});
```

### Get all posts that use a tag

Sequelize generates helper functions that allow you to get related items. For instance, if you wanted to find all posts that used a given tag:

```js
db.tag.find({where: {name: "xyzasdf"}}).then(function(tag) {
  tag.getPosts().then(function(posts) {
    console.log("These posts are tagged with " + tag.name + ":");
    posts.forEach(function(post) {
      console.log("Post title: " + post.title);
    });
  });
});
```
