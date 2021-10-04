# N:M RelationshipsWith Async/Await

_Updated for ECMAScript 2017 async/await and Sequelize 6_

## Objectives

* Create a join table and utilize it in a many-to-many relationship
* Use Sequelize's helper methods to add relationships between two different models.

## To Join the Many

When creating a many to many relationship, we need to have some way of creating that relationship. With a 1:M relationship, the id of the one is attached to the many \(`pets.userId` in the 1:M relationship in our `userapp`\). What do we do when there is no 1? When everything is many, we have to have some place to put the corrosponding ids.

Enter join tables! These tables have a one to many relationship with each of the relevant tables.

![An er diagram featuring a many to many relationship with students and classes and a join table called enrollments](https://fmhelp.filemaker.com/help/18/fmp/en/FMP_Help/images/relational.07.06.1.png)

Often, the naming convention is to have the join table have the names of both tables. For examples if you have products and orders, the join table will often be called `ProductOrders` or `product_orders`. \(More info on [associative tables](https://en.wikipedia.org/wiki/Associative_entity)\).

## Sequelize models

We will be expanding our data model in `userapp` to include toys for our pets.

```text
sequelize model:create --name toy --attributes type:string,color:string

sequelize model:create --name pets_toys --attributes petId:integer,toyId:integer
```

You may be noticing that this model is plural! Doesn't that break the cardinal rule that "Models are always singular!"? According to the Sequelize documentation when using a Junction Model \(a model represening an join table\), the model is pluralized.

Check out the [Sequelize N:M docs](https://sequelize.org/master/manual/assocs.html#many-to-many-relationships) and the [Sequelize BelongsToMany docs](https://sequelize.org/master/manual/creating-with-associations.html#hasmany---belongstomany-association) for more on all of the code and conventions covered in this lesson!

## Update your Associations

In order to associate pets to toys in a many to many fashion, you will need to update the associations on the pets and toys.

Many to many associations use the `belongsToMany` sequelize method, which takes a second options argument. Use the `through` option to indicate the name of the join model \(in this case, `pets_toys`\).

### pet.js

```javascript
 class pet extends Model {
   ...
   static associate(models) {
     // define association here
     models.pet.belongsTo(models.user)
     models.pet.belongsToMany(models.toy, { through: "pets_toys" })
   }
 }
```

### toys.js

```javascript
 class toy extends Model {
   ...
   static associate(models) {
     // define association here
     models.toy.belongsToMany(models.pet, { through: "pets_toys" })
   }
 }
```

Don't forget to migrate after adding your new associations!

## Examples

### Add a unique toy to a pet.

In order to add a unique toy to a pet, we need to first find \(or create\) a pet to associate the toy to.

Secondly, we must have a toy to attach to the pet, then we can associate them.

Some ORMs have functions to perform a bulk create on an object associations, but that kind of logic is not built in Sequelize. The list of special methods/mixins available on Sequelize N:M associations can be found in the [documentation here](https://sequelize.org/master/manual/assocs.html#-code-foo-belongstomany-bar----through--baz-----code-).

```javascript
async function createToy() {
  try {
    // First, get a reference to a pet.
    const [pet, petCreated] = await db.pet.findOrCreate({
      where: {
        name: "Silly May",
        species: "Mini Aussie",
        userId: 1
      }
    })

    // Second, get a reference to a toy.
    const [toy, toyCreated] = await db.toy.findOrCreate({
      where: { type: "stinky bear", color: "brown" }
    })

    // Finally, use the "addModel" method to attach one model to another model.
    await pet.addToy(toy)
    console.log(`${toy.type} added to ${pet.name}.`);

  } catch (error) {
    console.log(error)
  }
}

createToy()
```

Take some time to use these helper functions to add more toys and more pets! NOTE: If you are querying the pets\_toys table in a `psql` shell you will need to wrap the table name within quotations i.e. "pets\_toys".

An example of how you might use this in an express route:

```javascript
app.post('/pets/toys', async (req, res) => {
  try {
    // First, get a reference to a pet.
    const [pet, petCreated] = await db.pet.findOrCreate({
      where: {
        name: "Silly May",
        species: "Mini Aussie",
        userId: 1
      }
    })

    // Second, get a reference to a toy.
    const [toy, toyCreated] = await db.toy.findOrCreate({
      where: { type: "stinky bear", color: "brown" }
    })

    // Finally, use the "addModel" method to attach one model to another model.
    await pet.addToy(toy)

    // redirect to to show the created toy
    res.redirect(`/pets/${req.body.petId}`);
  } catch (error) {
    console.log(error)
  }
})
```

### Get all pets that use a toy

Sequelize generates helper functions that allow you to get related items. For instance, if you wanted to find all pets that used a given toy:

```javascript
async function readToy() {
  try {
    const toy = await db.toy.findOne({
      where: { type: "stinky bear" }
    })

    const pets = await toy.getPets()
    console.log(`${pets.length} pet(s) loves the ${toy.color, toy.type}.`);
  } catch (error) {
    console.log(error)
  }
}

readToy()
```

Because this is a Many to Many association, all the logic from before can be turned around to search for all the toys of a particular pet!

```javascript
async function readPet() {
  try {
    const pet = await db.pet.findOne({
      where: { name: "Silly May" }
    })

    const toys = await pet.getToys()

    toys.forEach(toy => {
      console.log(`${pet.name} loves their ${toy.color} ${toy.type}.`);
    })
  } catch (error) {
    console.log(error)
  }
}

readPet()
```

> NOTE: In the above code, if the pet doesn't have any toys, that `forEach` function will crash the nodemon server! Make sure you have error handling so your whole app doesn't shut down because one pet isn't materialistic!

### Get all the data!

Since we have a 1:M relationship between users and pets as well as a N:M relationship between pets and toys, we can get all our info through the Pet model. One of the easier ways of doing this is through the `include` keyword:

```javascript
async function eagerLoad() {
  try {
    const pet = await db.pet.findOne({
      where: {
        name: "Silly May"
      },
      include: [db.user, db.toy]
    })

    pet.toys.forEach(toy => {
      console.log(`${pet.user.firstName}'s pet ${pet.name} loves their ${toy.color} ${toy.type}.`);
    })
  } catch (error) {
    console.log(error)
  }
}

eagerLoad()
```

If you try to use eager loading includes between two models that aren't directly related, but are linked by an intermediate model \(such as finding a user and including all thier pet's toys\)

```javascript
...
const user = await db.user.findByPk(1, { 
  include: [db.pet, db.toy] 
})
```

you will see this error:

![user-toy-error](../../.gitbook/assets/user-toy-error.png)

Never Fear! you can nest includes to query complex relationships!

```javascript
async function readUser() {
  try {
    const user = await db.user.findByPk(1, { 
      include: [{
        model: db.pet,
        include: [db.toy]
      }]
    })

    user.pets.forEach(pet => {
        pet.toys.forEach(toy => {
          console.log(`${user.firstName}'s pet ${pet.name} loves their ${toy.color} ${toy.type}.`);
        })
      })

  } catch (error) {
    console.log(error)
  }
}

readUser()
```

