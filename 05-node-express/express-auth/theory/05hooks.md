# Sequelize Hooks

Hooks allow us to perform actions at different points throughout the life cycle of a model. For example, we could do something before an item is updated or after an item is created.

Sequelize supports many types of hooks. [Full list in documentation](http://sequelize.readthedocs.org/en/latest/docs/hooks/)


**Example: normalize tags using beforeCreate**

If we want all of our tags to be stored in all caps we could use a beforeCreate hook. This way if someone adds a tag `Taco` it will be stored as `TACO` and all of our tags will be the same.

```js
//in models/tag.js -- tag model

//... some other model code above
hooks: {
  beforeCreate: function(tag, options, cb) {
  
    //take the tag name and capitalize it
    tag.name = tag.name.toUpperCase();
    
    //pass the updated tag object back
    cb(null, tag);
  }
}
//... some other model code below

```

***Another way: addHook() method***

```javascript
  tag.addHook('beforeCreate', (pendingTag, options)=>{
    tag.name = tag.name.toUpperCase();
  })
```

We can use beforeCreate hook to automatically hash a users password before it is created (AKA before the data is inserted into the database).
