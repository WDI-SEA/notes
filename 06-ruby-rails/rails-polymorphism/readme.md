#Polymorphic Associations

##Objectives

* Understand the purpose of polymorphic associations
* Use the Rails model generator to generate a polymorphic model
* Implement polymorphic associations

Sometimes a model needs to be able to reference multiple models. For example, a model to hold a vote could belong to a post and a comment (like on Reddit). While we could organize our models to include an id for each model, like this:

| Vote       |
| :--------- |
| user_id    |
| value      |
| post_id    |
| comment_id |

...this model has a couple key issues.

1. A vote ideally only belongs to a post or comment. Therefore, if the vote belonged to a post, the comment attribute would be set to NULL. This is a waste of space!
2. If we wanted a vote to reference another model (such as a user), we'd have to add another column for the model. This results in having to create another migration, and now the problem we had in issue #1 is multiplied.

Polymorphism solves this problem by abstracting the the "multiple models" into two columns.

| Vote         |
| :----------- |
| user_id      |
| value        |
| votable_id   |
| votable_type |

Instead of giving the model attribute a specific name, we store the id and name of the model as attributes. Now, `votable_type` can be any model we choose, and `votable_id` will be the `id` of the `votable_type`. Here's some examples:

| Vote: 1       | Vote: 2  |
| :------------ | :----- |
| user_id: 3    | user_id: 9 |
| value: -1     | value: 1 |
| votable_id: 4 | votable_id: 8 |
| votable_type: 'Post' | votable_type: 'User' |

####Resources

* [Rails guide - Polymorphic Models](http://guides.rubyonrails.org/association_basics.html#polymorphic-associations)
* [Rails Advanced Generators](http://railsguides.net/advanced-rails-model-generators/)

Let's setup a vote model in order to implement this functionality in our Link Board.

##Setup models

**Create model** - Terminal

```
rails g model vote value:integer user:references votable:references{polymorphic}
```

Here, we're creating a model that has a value, a user that created the vote, and a polymorphic association called `votable`. We're going to use `votable` to associate a vote to posts and comments.

**Check the migration**

make sure it has `polymorphic:true`

```rb
t.references :votable, polymorphic:true, index: true
```

**run migration** - Terminal

```
rake db:migrate
```

Now that we're migrated, we'll be adding the associations to posts and users.

First thing's first, let's double-check that the vote model has a polymorphic association:

**models/vote.rb**

```rb
belongs_to :votable, polymorphic: true
```

Now, let's associate votes to posts. We're going to define the attribute name as the plural of vote, which is `votes`. We'll define the association through the polymorphic attributes set up in vote.

**models/post.rb**

* has many votes (votes for/against this post)

```rb
has_many :votes, as: :votable
```

Now for user, we need to define the association for two different attributes. First, the user will have many `ratings`, which refer to a regular 1:M association. This means that each user has many votes that they cast.

The second association will be polymorphic, and will refer to users voting for other users.

**models/user.rb**

* has many `ratings`
    * votes created by user
    * not polymorphic - regular one to many
* has many `votes`
    * votes for/against this user
    * polymorphic

```rb
has_many :ratings, class_name: 'Vote'
has_many :votes , as: :votable
```


##Try it out

in terminal

```rb
#list comments, posts, users
User.all
Vote.all
Post.all

#user up votes a post
User.first.ratings << Post.first.votes.create({value:1})

#user down votes a post
User.first.ratings << Post.last.votes.create({value:-1})

#user up votes a user
User.first.ratings << User.first.votes.create({value:1})

#list user ratings (votes cast by user)
User.first.ratings

#list user votes (votes about a user)
User.first.votes
```
