# Seeding with Sequelize

Seeding data is the process of bulk-inserting data into your database. In this lesson we will create a new Node/Sequelize app and use sequelize to seed data into our database.

## 1. Set up your app
* Create a new node project called `seeding-dinosaurs`.
* npm install `pg`, `pg-hstore`, and `sequelize`.
* initialize `sequelize`

## 2. Set up your database
* create a database called `seedy-dinosaurs`
* edit the `config.json`file
* create a `Dinosaur` model with `name:string`, and `type:string`
* run the migration

## 3. Set up the seed file
* **Generate Seed File:** In the command line, run `sequelize seed:generate --name demo-dinos`. Now check out the file that was generated in the `seeders` folder of your project! 
* **Set Up Seeder Functions:** Just like migrations, seeders have an `up` and a `down` function for seeding and unseeding. Sequelize gives us a clear example of how to finish out these functions. Follow their prompt, substituting in the correct model:

```js
'use strict';

module.exports = {
  up: (queryInterface, Sequelize) => {
      return queryInterface.bulkInsert('Dinosaurs', [{
        name: 'General Dino',
        type: 'Assemblasaurus'
      }], {});
  },

  down: (queryInterface, Sequelize) => {
      return queryInterface.bulkDelete('Dinosaurs', null, {});
  }
};
```

## 4. Seed the data!
* In the command line, run `sequelize db:seed:all`.

Uh oh! What happened? Looks like seeding data doesn't automatically generate values for the `createdAt` and `updatedAt` columns. Let's add those fields:

```js
'use strict';

module.exports = {
  up: (queryInterface, Sequelize) => {
      return queryInterface.bulkInsert('Dinosaurs', [{
        name: 'General Dino',
        type: 'Assemblasaurus',
        createdAt: new Date(),
        updatedAt: new Date()
      }], {});
  },

  down: (queryInterface, Sequelize) => {
      return queryInterface.bulkDelete('Dinosaurs', null, {});
  }
};
```

Now run the seed again. ***Voila!*** Check your database to view your newly seeded dinosaur.

What if we want to unseed this data? Simply run `sequelize db:seed:undo:all`. ***Poof!*** Check your database to see that your demo data was removed.

---

## Exercise

Add more dinos to seed! Try editting your seed file to insert all the the dinosaurs below. Run the seed to make sure it added all the dinosaurs to your database correctly.

```js
[
  {
    name:"Littlefoot",
    type:"apatosaurus",
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    name:"Cera",
    type:"triceratops",
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    name:"Ducky",
    type:"saurolophus",
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    name:"Petrie",
    type:"pteranodon",
    createdAt: new Date(),
    updatedAt: new Date()
  },
  {
    name:"Spike",
    type:"stegosaurus",
    createdAt: new Date(),
    updatedAt: new Date()
  }
]
```
