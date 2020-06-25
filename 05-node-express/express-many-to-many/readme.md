# Sequelize - Many to Many

## Objectives

* Create a join table and utilize it in a many-to-many relationship
* Use Sequelize's helper methods to add relationships between two different models.

## To Join the Many

When creating a many to many relationship, we need to have some way of creating that relationship. With a 1:M relationship, the id of the one is attached to the many (`pets.userId` in the 1:M relationship in our `userapp`). What do we do when there is no 1? When everything is many, we have to have some place to put the corrosponding ids.

Enter join tables! These tables have a one to many relationship with each of the relevant tables. 

![An er diagram featuring a many to many relationship with students and classes and a join table called enrollments](https://fmhelp.filemaker.com/help/18/fmp/en/FMP_Help/images/relational.07.06.1.png)

Often, the naming convention is to have the join table have the names of both tables. For examples if you have products and orders, the join table will often be called `products_orders`.

## Sequelize models

We will be expanding our data model in `userapp` to include toys for our pets.

> **Very Important** Name - your models `singular`, but your join model will be plural.


```
sequelize model:create --name toys --attributes type:string,color:string

sequelize model:create --name petsToys --attributes petId:integer,toysId:integer
```

## Update your Associations

In order to associate pets to toys in a many to many fashion, you will need to update the associations on the pets and toys.

### pet.js

```js
 pet.associate = function(models) {
   // associations can be defined here
   models.pet.belongsTo(models.user);
   models.pet.belongsToMany(models.toy, {through: "petsToys"})
 };
```

### toys.js

```js
toys.associate = function(models) {
   models.toy.belongsToMany(models.pet, {through: "petsToys"})
 };
```

## Examples

### Create a pet

```js
db.pet.findOrCreate({
  where: {
    name: "Ruby Tuesday",
    species: "Toy Aussie"
  }
}).then(function([pet, created]) {
  console.log(pet.get());
});
```

### Add a unique toy to a pet.

In order to add a unique toy to a pet, we must first try to find or create a toy, in order to make sure it is in fact unique.

Secondly, we must attach a pet to the toys, using some built in helpers.

Some ORM has capabilities to do a bulk create on an object associations, but that kind of logic is not built in Sequelize.

```js
// First, get a reference to a pet.
db.pet.findOrCreate({
  where: {
    name: "Ruby Tuesday",
    species: "Toy Aussie"
  }
}).then(function([pet, created]) {
  // Second, get a reference to a toy.
  db.toy.findOrCreate({
    where: {type: "ball", color: "green"}
  }).then(function([toy, created]) {
    // Finally, use the "addModel" method to attach one model to another model.
    pet.addToy(toy).then(function(toy) {
      console.log(toy.type, "added to", pet.name);
    });
  });
});
```

### Get all pets that use a toy

Sequelize generates helper functions that allow you to get related items. For instance, if you wanted to find all pets that used a given toy:

```js
db.toy.find({
  where: {type: "ball"}
}).then(function(toy) {
  toy.getPets().then(function(pets) {
    pets.forEach(function(pet) {
      console.log(pet.name, 'loves the', toy.type);
    });
  });
});
```
