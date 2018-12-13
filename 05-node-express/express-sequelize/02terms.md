# Key terms + definitions

#### ORM

An ORM (Object Relational Mapper) is a piece/layer of software that creates a map between our database into javascript objects that represent our data. This means we can just use JavaScript to create and work with our data instead of writing raw SQL queries.

You can read some more about the benefits of using an ORM [here](http://stackoverflow.com/questions/1279613/what-is-an-orm-and-where-can-i-learn-more-about-it)

**Exercise:** What are 3 pros of an ORM? What are 3 cons?

#### Sequelize

From the Sequelize docs "To put it in a nutshell, it's an ORM (Object-Relational-Mapper). The library is written entirely in JavaScript and can be used in the Node.JS environment." In other words, Sequelize is an ORM that works with relational databases and Node.js. It allows us to do many things including:

- Represent models and their data.
- Represent associations between these models.
- Validate data before they gets persisted to the database.
- Perform database operations in an object-oriented fashion.

#### Model

A model is an object that maps to the data relation (table) and potentially bridges tables. You can think of a model as the blueprint for what each row of data is going to contain. Unlike a migration, you perform CRUD on instances of your models.

#### Migration

Migrations (also known as 'schema evolution' or 'mutations') are a way of changing your database schema from one version into another. You can think of a migration as the creation or changes you want to make to a database table or column. Before you can start manipulating your models, you need to create and run a migration. Examples of migrations are creating, deleting and altering tables (and their existing columns).
