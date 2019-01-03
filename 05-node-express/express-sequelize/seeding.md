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
* In the command line, run `sequelize seed:generate --name demo-dinos`. Now check out the file that was generated in the `seeders` folder of your project! Just like migrations, seeders have and `up` and a `down` function for seeding and unseeding.

