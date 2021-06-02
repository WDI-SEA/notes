# N:M Relationships

## Objectives

* Create a join table and utilize it in a many-to-many relationship
* Use Sequelize's helper methods to add relationships between two different models.

## To Join the Many

When creating a many to many relationship, we need to have some way of creating that relationship. With a 1:M relationship, the id of the one is attached to the many \(`pets.userId` in the 1:M relationship in our `userapp`\). What do we do when there is no 1? When everything is many, we have to have some place to put the corrosponding ids.

Enter join tables! These tables have a one to many relationship with each of the relevant tables.

![An er diagram featuring a many to many relationship with students and classes and a join table called enrollments](https://fmhelp.filemaker.com/help/18/fmp/en/FMP_Help/images/relational.07.06.1.png)

Often, the naming convention is to have the join table have the names of both tables. For examples if you have products and orders, the join table will often be called `ProductOrders` or `product_orders`. (More info on [associative tables](https://en.wikipedia.org/wiki/Associative_entity)).

## Sequelize models

We will be expanding our data model in `userapp` to include toys for our pets.

```text
sequelize model:create --name toy --attributes type:string,color:string

sequelize model:create --name pets_toys --attributes petId:integer,toyId:integer
```

You may be noticing that this model is plural! Doesn't that break the cardinal rule that "Models are always singular!"? According to the Sequelize documentation when using a Junction Model (a model represening an join table), the model is pluralized.

Check out the [Sequelize N:M docs](https://sequelize.org/master/manual/assocs.html#many-to-many-relationships) and the [Sequelize BelongsToMany docs](https://sequelize.org/master/manual/creating-with-associations.html#hasmany---belongstomany-association) for more on all of the code and conventions covered in this lesson!

## Update your Associations

In order to associate pets to toys in a many to many fashion, you will need to update the associations on the pets and toys.

Many to many associations use the `belongsToMany` sequelize method, which takes a second options argument. Use the `through` option to indicate the name of the join model (in this case, `pets_toys`).

### pet.js

```javascript
 class pet extends Model {
   ...
   static associate(models) {
     // define association here
     models.pet.belongsTo(models.user)
     models.pet.belongsToMany(models.toy, {through: "pets_toys"})
   }
 }
```

### toys.js

```javascript
 class toy extends Model {
   ...
   static associate(models) {
     // define association here
     models.toy.belongsToMany(models.pet, {through: "pets_toys"})
   }
 }
```

Don't forget to migrate after adding your new associations!

## Examples

### Add a unique toy to a pet.

In order to add a unique toy to a pet, we need to first find (or create) a pet to associate the toy to. 

Secondly, we must have a toy to attach to the pet, then we can associate them.

Some ORMs have functions to perform a bulk create on an object associations, but that kind of logic is not built in Sequelize. The list of special methods/mixins available on Sequelize N:M associations can be found in the [documentation here](https://sequelize.org/master/manual/assocs.html#-code-foo-belongstomany-bar----through--baz-----code-).

```javascript
// First, get a reference to a pet.
db.pet.findOrCreate({
  where: {
    name: "Silly May",
    species: "Mini Aussie",
    userId: 1
  }
}).then(([pet, created]) => {
  // Second, get a reference to a toy.
  db.toy.findOrCreate({
    where: {type: "stinky bear", color: "brown"}
  }).then(([toy, created]) => {
    // Finally, use the "addModel" method to attach one model to another model.
    pet.addToy(toy).then(relationInfo => {
      console.log(`${toy.type} added to ${pet.name}.`);
    });
  });
});
```

Take some time to use these helper functions to add more toys and more pets! NOTE: If you are querying the pets_toys table in a `psql` shell you will need to wrap the table name within quotations i.e. "pets_toys".

An example of how you might use this in an express route:

```js
app.post('/pets/toys', (req, res) => {
  // First get a reference to the pet
  db.pet.findByPk(req.body.petId)
  .then(pet => {
    db.toy.findByPk(req.body.petId)
    .then(toy => {
      pet.addToy(toy);
      res.redirect(`/pets/${req.body.petId}`);
    })
  })
})

```

### Get all pets that use a toy

Sequelize generates helper functions that allow you to get related items. For instance, if you wanted to find all pets that used a given toy:

```javascript
db.toy.findOne({
  where: {type: "stinky bear"}
}).then(toy => {
  toy.getPets().then(pets => {
    console.log(`${pets.length} pet(s) loves the ${toy.color, toy.type}.`);
  });
});
```

You can use the `addModel()` helper function to add a pet association on a toy if there are no pet associations yet.

```javascript
db.toy.findOrCreate({
  where: {type: "ball", color: "green"}
}).then(([toy, created]) => {
  toy.getPets().then(pets => {
    // Check if their are any pets associated with this toy
    if (pets.length > 0) {
      pets.forEach(pet => {
        console.log(`${pet.name} loves their ${toy.color} ${toy.type}.`);
      });
    } else {
      // findOrCreate a Pet and add it to the toy
      db.pet.findOrCreate({
        where: {
          name: "Ruby Tuesday",
          species: "Toy Aussie"
        }
      }).then(([pet, created]) => {
        toy.addPet(pet).then(relationInfo => {
          console.log(`${pet.name} has faved the ${toy.color} ${toy.type} toy.`);
        })
      });
    } // end of if statement
  });
});
```



Because this is a Many to Many association, all the logic from before can be turned around to search for all the toys of a particular pet!

```javascript
db.pet.findOne({
  where: {name: "Ruby Tuesday"}
}).then(pet => {
  pet.getToys().then(toys => {
    toys.forEach(toy => {
      console.log(`${pet.name} loves their ${toy.color} ${toy.type}.`);
    });
  });
});
```

> NOTE: In the above code, if Ruby Tuesday doesn't have any toys, that `forEach` function will crash the nodemon server! Make sure you have error handling so your whole app doesn't shut down because one pet isn't materialistic!

### Get all the data!

Since we have a 1:M relationship between users and pets as well as a N:M relationship between pets and toys, we can get all our info through the Pet model. One of the easier ways of doing this is through the `include` keyword:

```javascript
db.pet.findOne({
  where: {
    name: "Silly May"
  },
  include: [db.user, db.toy]
}).then(pet => {
  pet.toys.forEach(toy => {
    console.log(`${pet.user.firstName}'s pet ${pet.name} loves their ${toy.color} ${toy.type}.`);
  })
})
```

Or we can use a mix of `include` and helper functions to get all the toys of all the pets of a certain user!

```javascript
db.user.findByPk(1, { include: [db.pet] })
.then(user => {
  user.pets.forEach(pet => {
    pet.getToys().then(toys => {
      toys.forEach(toy => {
        console.log(`${user.firstName}'s pet ${pet.name} loves their ${toy.color} ${toy.type}.`);
      });
    });
  });
});
```

As you can see, there are MANY \(to\) MANY ways to get associated data when it is needed. It's also easy to see how easy it can be to get lost in nesting heck. One way to help keep things clean is to comment the end of each section. If we take the last block of code as an example:

```javascript
db.user.findByPk(1, { include: [db.pet] })
.then(user => {
  user.pets.forEach(pet => {
    pet.getToys().then(toys => {
      toys.forEach(toy =>  {
        console.log(`${user.firstName}'s pet ${pet.name} loves their ${toy.color} ${toy.type}.`);
      }); // toys.forEach end
    }); // getToys end
  }); // pets.forEach end
}); // user.findByPk end
```

