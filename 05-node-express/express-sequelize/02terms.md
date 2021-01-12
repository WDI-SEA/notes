# Terminology

## ORM

An ORM \(Object Relational Mapper\) is a piece/layer of software that creates a map between our database into javascript objects that represent our data. This means we can just use JavaScript to create and work with our data instead of writing raw SQL queries.

You can read some more about the benefits of using an ORM [here](http://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it)

**Exercise:** What are 3 pros of an ORM? What are 3 cons?

## Sequelize

From the Sequelize docs "To put it in a nutshell, it's an ORM \(Object-Relational-Mapper\). The library is written entirely in JavaScript and can be used in the Node.JS environment." In other words, Sequelize is an ORM that works with relational databases and Node.js. It allows us to do many things including:

* Represent models and their data.
* Represent associations between these models.
* Validate data before they gets persisted to the database.
* Perform database operations in an object-oriented fashion.

## Model

A model is a javascript class that maps to a database table. You can think of a model as the blueprint for what each row of data is going to contain. Each instance of your model is a javascript object that represents one row of data. The ORM allows you perform CRUD on instances of your models which will then map to the equivalent changes in your database.

Read more about Sequelize models [here](https://sequelize.org/master/manual/model-basics.html#:~:text=Models%20are%20the%20essence%20of,(and%20their%20data%20types).)

## Migration

Migrations \(also known as 'schema evolution' or 'mutations'\) are a way of changing your models from one version into another. A migration file lays out a plan to change your _model_. When the migration is _run_, it changes your model _and_ uses your ORM to map those changes into your database so your database is alterred accordingly.

