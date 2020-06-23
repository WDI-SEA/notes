# Sequelize - 1 to Many Relationships

## Objectives

* utilize table relationships in a database
* add a 1:M association using Sequelize
* use helper methods to add and access a related model
* understand the purpose of eager loading when accessing a model's associations

Today we're going to cover how to setup a one to many relationship, using more than one table. This will allow data in one table to be associated with data in another.

## Getting Started

We're going to build off the `userapp` we created in the intro to sequelize. A bit of a recap on how to start an express sequelize app:
1. Create a directory for your app
2. `cd` into that directory
3. Create your express route entry point (often `index.js`, `app.js`, or `server.js`)
4. Initialize npm with `npm init -y`
5. Install your dependencies `npm i express pg sequelize`
6. Create your Database (either using sequelize-cli or in your psql shell)
7. Initialize Sequelize with `sequelize init`
8. Edit your `config.json` file

## Creating A Model

There are a few things to remember when creating models. Models shall be lowercase and singular. Sequlize will automatically create plural tables when any migrations are run. Also id, createdAt, and updatedAt fields are given for you. When we created our user, we ran this command:

```
sequelize model:create --name user --attributes firstName:string,lastName:string,age:integer,email:string
```

When creating a table that will reference another table, use the following format, `parentId`, when adding the foreign key to the table. This format is necessary for some of built in methods of Sequelize.

```
sequelize model:create --name pet --attributes name:string,species:string,description:text,userId:integer
```

### Adding the Associations

The following lines need to be inserted into the author and post models respectively in the `associate` function. The comment line is where you will insert it.

Insert into **models/user.js**, inside the `associate` function

```js
associate: function(models) {
  models.user.hasMany(models.pet);
}
```

Insert into **models/pet.js**, inside the `associate` function

```js
associate: function(models) {
  models.pet.belongsTo(models.user);
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

We can use the `createPet` method to create a new post associated with an author. Remeber to use the `.then` promise.

```js
db.user.findOne().then(function(user) {
  user.createPet({
    name: 'Spot',
    species: 'Mutt Dog'
  }).then(function(dog) {
    console.log(dog.name);
  });
});
```

### Loading associated items using `getModels`

We can manually get all pets of a user by calling `.getPets()` on a user instance. Remember this query is asynchronous and takes time, so we have to  use a `.then()` promise too.

```js
db.user.findOne().then(function(user) {
  //load pets for this user
  user.getPets().then(function(pets) {
    //do something with pets here
  });
});
```

### Other methods

`setModel` and `addModel` are used to associate an existing record. If you created a pet and later wanted to add an association to an user this is how you'd do it.

```js
db.pet.findOrCreate({
  where: {
    name: 'Simba',
    species: 'Ginger Cat'
  },
  defaults: {
    description: 'Traumatised by a very jealous toy aussie, Simba is very cute but rarely comes out to play'
  }
}).then(function([pet, created]) {
  db.user.findOne().then(function(user) {
    //associate previously loaded pet instance
    user.addPet(pet);
    console.log('User ' + user.firstName + ' is the owner of ' + pet.name);
  });
});
```

## Using `include`

Sequeize supports "eager loading", meaning it can load all of the pets for us in advance if we know we need them. We let it know what we need by using `include`.

```js
db.user.findAll({
  include: [db.pet]
}).then(function(users){
  // users will have a .pets key with an array of pets
  console.log(users[0].pets);
});
```
