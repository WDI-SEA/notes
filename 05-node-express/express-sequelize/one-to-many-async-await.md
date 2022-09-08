# 1:M RelationshipsWith Async/Await

_Updated for ECMAScript 2017 async/await and Sequelize 6_

## Objectives

* utilize table relationships in a database
* add a 1:M association using Sequelize
* use helper methods to add and access a related model
* understand the purpose of eager loading when accessing a model's associations

Today we're going to cover how to setup a one to many relationship, using more than one table. This will allow data in one table to be associated with data in another.

## Getting Started

We're going to build off the `userapp` we created in the intro to sequelize. A bit of a recap on how to start an express sequelize app: 1. Create a directory for your app 2. `cd` into that directory 3. Create your express route entry point \(often `index.js`, `app.js`, or `server.js`\) 4. Initialize npm with `npm init -y` 5. Install your dependencies `npm i pg sequelize` 6. Create your Database \(either using sequelize-cli or in your psql shell\) 7. Initialize Sequelize with `sequelize init` 8. Edit your `config.json` file

## Creating A Model

There are a few things to remember when creating models. Models shall be lowercase and singular. Sequlize will automatically create plural tables when any migrations are run. Also id, createdAt, and updatedAt fields are given for you. When we created our user, we ran this command:

```text
sequelize model:create --name user --attributes firstName:string,lastName:string,age:integer,email:string
```

When creating a table that will reference another table, use the following format, `parentId`, when adding the foreign key to the table. This format is necessary for some of built in methods of Sequelize.

```text
sequelize model:create --name pet --attributes name:string,species:string,description:text,userId:integer
```

### Adding the Associations

The following lines need to be inserted into the author and post models respectively in the `associate` function. The comment line is where you will insert it.

Insert into **models/user.js**, inside the `associate` function

```javascript
    static associate(models) {
      // define association here
      models.user.hasMany(models.pet)
    }
```

Insert into **models/pet.js**, inside the `associate` function

```javascript
    static associate(models) {
      // define association here
      models.pet.belongsTo(models.user)
    }
```

Finally, let's run create all the necessary tables from our models by migrating the database.

```text
sequelize db:migrate
```

Read more: [Sequelize docs - One to Many](https://sequelize.org/master/manual/assocs.html#one-to-many-relationships)

## Using the association

Once the association is set up, we can use the `createModel`, `getModels`, `setModel`, and `addModel` helper methods. "Model" in each of these is replaced with the model name you create.

[There are quite a few of these in the docs!](https://sequelize.org/master/manual/assocs.html#special-methods-mixins-added-to-instances)

### Creating an associated item with `createModel`

We can use the `createPet` method to create a new pet associated with a user. Remeber to use an `async function` and `await` the promise.

```javascript
async function newPet() {
  try {
    // literally just find the first user
    const user = await db.user.findOne()
    // now that we found them, lets give them a pet!
    const newPet = await user.createPet({
      name: 'Spot',
      species: 'Mutt Dog'
    })
    // look at the dog!!!
    console.log(newPet)
  } catch (error) {
    console.log(error)
  }
}
// don't forget to invoke your function
newPet()
```

### Loading associated items using `getModels`

We can manually get all pets of a user by calling `.getPets()` on a user instance. Remember this query is asynchronous and takes time, so we have to use a `async function` and `await` the promise too.

```javascript
async function printPets() {
  try {
    // literally just find the first user
    const user = await db.user.findOne()
    // get thier pets!
    const pets = await user.getPets()
    // now that we got them, lets do something with thier them a pets!
    pets.forEach(pet=>{
      console.log(`${user.firstName}'s pets:`)
      console.log(pet.name)
  })
  } catch (error) {
    console.log(error)
  }
}
```

### Other methods

`setModel` and `addModel` are used to associate an existing record. If you created a pet and later wanted to add an association to an user this is how you'd do it.

```javascript
async function associatePets() {
  try {
    // lets make this pet!
    const options = {
      where: {
        name: 'Simba',
        species: 'Ginger Cat'
      },
      defaults: {
        description: 'Traumatised by a very jealous toy aussie, Simba is very cute but rarely comes out to play'
      }
    }
    // remember that wierd 'array destructuring' thing with findorCreate?
    const [pet, created] = await db.pet.findOrCreate(options)
    // lets find a user and give them this pet
    const user = await db.user.findOne()
    // you get a pet!
    await user.addPet(pet);
    console.log('User ' + user.firstName + ' is the owner of ' + pet.name);

  } catch (error) {
    console.log(error)
  }
}

associatePets()
```

## Using `include`

Sequelize supports "eager loading", meaning it can load all of the pets for us in advance if we know we need them. We let it know what we need by using `include`.

```javascript
async function eagerBeaver() {
  try {
    // find everyone!
    const users = await db.user.findAll({
      include: [db.pet]
    })
    // users will have a .pets key with an array of pets
    users.forEach(user=>{
      console.log(`${user.firstName}'s pets:`)
      // nested forEach! 
      user.pets.forEach(pet=>{
          console.log(pet.name)
      })
    })
  } catch (error) {
    console.log(error)
  }
}

eagerBeaver()
```

