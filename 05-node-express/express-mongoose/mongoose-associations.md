# Data Modeling with Mongooose

## Learning Objectives

By the end of this lecture students should be able to:

* Understand the difference between **embedding** and **referencing** in MongoDB
* Know how to implement a one-to-many association in Mongoose using both embedding and referencing
* Know how to use the `populate()` method to access referenced documents

## Introduction

Now that we have Mongoose in the mix, we can see how to make one-to-many and many-to-many relationships with our data in MongoDB. We previously saw how to embed and reference other data from our documents in the MongoDB shell. This is the basis of data "relations" in MongoDB but we will now learn how Mongoose can help us make this process even easier.

## Background

### Normalized vs. Denormalized Data

What is data normalization? It is a set of rules that we use when creating and relating data so that we do not have orphaned or duplicate data. Putting it simply, a **normalized** data set should have no redundant data, while a **denormalized** data set can have some duplicate data.

### References vs. Embeds

#### Referenced Data

**References** create relationships between data by storing references to one document inside of another. Applications can resolve these references in `multiple` queries to access the related data.

Here we see an example of a couple of documents that each hold a reference to a separate document. You could say that these exhibit **normalization** because linked data is referenced, and not duplicated.

<img src="https://i.imgur.com/NNJEG7N.png" width="75%">

#### Embedded Data

**Embedded** documents create relationships between data by storing related data in a single document structure. MongoDB documents make it possible to embed document structures in an array field within a document. These **denormalized** data models allow applications to retrieve and manipulate related data in a `single` database operation, at the cost of some duplicated data.

![embeds](https://i.imgur.com/j8iJx7n.png)

## Modeling One-to-Many Relationships with Embedded Subdocuments

A document embedded inside of another document is called a **subdocument**. The easiest and probably most common way to create a one-to-many association using Mongoose is through embedding. 

Let's consider an example. With this approach we embed *schemas* within *schemas*. Let's consider a `BlogPost` schema that has many `Comment`s:

Emdedding documents using Mongoose:

```javascript
const commentSchema = new mongoose.Schema({
    header: String,
    content: String,
    date: Date
})

const blogPostSchema = mongoose.Schema({
    title: String,
    body: String,
    comments: [commentSchema],
})

module.exports = mongoose.model('BlogPost', blogPostSchema)
```

In our model file for `BlogPost` we would define both the `blogPostSchema` and the `commentSchema` which will be embedded into the `BlogPost`s. We only need to make the model for the Parent. We use square brackets `[<Schema Name>]` to denote that many `comments` are in a single `BlogPost`.

Below, is how you *add* an embedded document to an array:

```javascript
// Create a blog post using the model
const post = new BlogPost({ title: "Cat", body: "Yeehaw! Sandos!" })

// Create a comment by pushing a comment object
post.comments.push({ header: 'My comment', content: "What!?"  })

// Save the parent after pushing the child into the parent's array
post.save(err => {
    if (!err) console.log('Success!');
})
```

We can treat `post.comments` as an array and use the Mongoose `push` method to push an embedded document into its parent document. **We must save the *parent* document in order for the embedded document to be saved.**

### Subdocument IDs

Mongoose is super-nice and automatically adds IDs to each of our embedded subdocuments. This makes it very easy to find specific ones for showing, updating or deleting. Mongoose even provides a handy `id()` function built onto subdocuments that we can use to find one:

```javascript
BlogPost.findById(postId, (err, foundPost) => {
    if (!err) {
        foundPost.comments.id(commentId).remove()
        foundPost.save(err => {
            // do something
            if(!err) console.log('succes!')
        })
    }
})
```

The `remove` method removes child documents. Above, we are locating a `BlogPost` by whatever value is in `myId` and then we are finding its subdocument with the ID of `subId` and removing that subdocument.

#### Code-Along: Create Embedded Schemas

Code it!

## Modeling One-to-Many Relationships with Document References

Consider the following example that maps `Product` and `Order` relationships. The example illustrates the advantage of referencing over embedding to avoid repetition of the products information.

```js
const mongoose = require('mongoose');

const orderSchema = new mongoose.Schema({
    products: [{type: mongoose.Schema.Types.ObjectId, ref: 'Product'}]
});

module.exports = mongoose.model('Order', orderSchema)
```

```js
const productSchema = new mongoose.Schema({
    name: String,
    price: Number
});

module.exports = mongoose.model('Product', productSchema)
```

The `orderSchema` has an array of `products` but we include both a `type` and a `ref`. The type will be `mongoose.Schema.Types.ObjectId` since it will be storing another document's ID. The ref is the name of the referenced model which will be used to help gather data for us as we will soon see.

**Quiz**: What is our one? What is our many?

This is how we would use referencing:

```js
// This is the flow with all callbacks removed for ease of reading
const product = new Product({name: 'Wrench', price: 5});
product.save();
const order = new Order()
order.products.push(product)
order.save();
```

It's pretty much the same flow that we did with embedded documents but this time we use the child model to actually create a new child object. Instead of simply pushing values into the parent's array, we are pushing a whole saved database object. Mongoose reads this and inserts only the `_id` column of the referenced document into the parent's array. If we were to query for a single order we would get back the following:

```js
{
    _id: '57ec7d63f292421828791b8c',
    products: [ '57ec7d5cf292421828791b8b' ]
}
```

That's not very useful to a human. However, Mongoose knows how to get at the data with that ID very easily.

### Modeling One-to-Many Relationships with Document References

Orders to products could really be a many-to-many relationship, but they way we've coded above makes it on-to-many insofar as querying in mongoose goes. We can start with an order and pull all the products that were in that order, but what if we wanted to query the other direction? What if I wanted to see a list of all orders that contained a certain product? We'd need to make it many--to-many so we could query either direction. We can do that by simply adding an array of orders to the product schema:

```js
const productSchema = new mongoose.Schema({
    name: String,
    price: Number,
    orders: [{type: mongoose.Schema.Types.ObjectId, ref: 'Order'}]
})
```

*Tip: It's like adding associations in sequelize models! If it's a 1:M, you only add the association on one of the models, but if it's N:M you have to add it to both!)*

### Populate

In order to obtain the referenced documents we need to call `populate` on the query.

```js
Order.findById(orderId).populate('product').exec((err, foundOrder) => {
    console.log(foundOrder);
})
```

Let's look at this code. We start by finding an Order by its ID. Normally, there we would use a callback since `findById()` is an asynchronous function. However, we can't put the callback there if we want to use `populate()`. You pass in only the `id` to `findById()` and then immediately chain the `populate()` function. It takes the name of the field to populate as a string. Strangely, `populate()` doesn't take a callback argument and so we must chain `exec()` which let's us add a callback. But the `populate()` function does all the magic.

When we put this line in our `orderSchema` above...

```js
products: [{type: mongoose.Schema.Types.ObjectId, ref: 'Product'}]
```

...we told Mongoose that `'Product'` was the name of the model to use when populating.The `populate` function follows your reference to the linked data in the second document and retrieves all of the data in there that is related to your first document. Using `populate` we can save ourselves the additional queries needed to retrieve all referenced documents. Below we see our `products` have automatically been included as if they were embedded:

```js
{
    _id: '57ec800a3130441eb4b52e39',
    __v: 0,
    products:
        [ { _id: '57ec800a3130441eb4b52e38',
        name: 'Wrench',
        price: 5,
        __v: 0 } ]
}
```

#### Code-along / Lab: Create Referenced Schemas

Code it!

### When to Embed? When to Reference?

Here are some guidelines to consider when deciding on referencing vs embedding from the MongoDB docs:

- For performance and simplicity reasons, lean toward _embedding_ over _referencing_.
- Prefer the _reference_ approach when the amount of child data is unbounded and there is a danger of exceeding the 16MB size limit for a document - an uncommon situation however - the entire body of work of Shakespeare can be stored in 5 megabytes!
- Prefer the _reference_ approach when multiple parent documents access the same child document and that child's data changes frequently. This avoids having to update redundant data in multiple locations.
- Obtaining _referenced_ documents requires multiple queries by your application instead of a single query when using _embedding_ - this is why _embedding_ is much more performant.
- Mongoose simplifies the multi-query process for getting data from referenced documents with the populate() function.
- In the _references_ approach, depending upon your application's needs, you may choose to maintain links to the related document's *_id* in either document, or both.
