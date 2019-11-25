# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) SQLAlchemy

### Learning Objectives
*After this lesson, you will be able to:*
- Understand SQL transactions
- Created Models and migrate them to a Postgres database
- Perform CRUD Operations with SQLAlchemy
- Create relationships between models

## Overview

SQLAlchemy is python SQl toolkit and an ORM. Often used with Flask, it abstracts the SQL commands while still leaving the control in the developer's care.

From [the SQLAlchemy website](https://www.sqlalchemy.org/):
> ...Instead of hiding away SQL and object relational details behind a wall of automation, all processes are fully exposed within a series of composable, transparent tools. The library takes on the job of automating redundant tasks while the developer remains in control of how the database is organized and how SQL is constructed.

## Setting up

Python likes to install things globally. One of the ways we get around that is by setting up a **Virtual Environment**. It allows us to specify the version of certain tools and helps to maintain consistancy in our projects.

### Setting up the Virtual Environment

Make a directory called `sqlalchemy_pets`. `cd` into that directory then run the command to create a virtual environment.
```bash
python3 -m venv savenv
```
This will create a folder called `savenv` which will hold all the relevant information on our virtual environment.

To start up the virtual environment, run the command in the command line:
```bash
. savenv/bin/activate
```

You should see some indication that you're in a virtual environment in your shell (on my ZShell, I have the virtual environment name show up on the right hand side.)

>If you want to leave your virtual environment, just use the command `deactivate`

Now that we have a virtual environment set up, we need to install some things:

* `sqlalchemy`—The ORM that we'll be using
* `psycopg2`—It's a python driver for our postgres database

## Models

Create a new python file in the root directory. We'll call it `models.py`. We're going to use this file to create our models.

At the top of our script, we'll import `sqlalchemy`. 

The first thing we need to do is describe the database tables we'll be interacting with and then defining the classes that will be mapped to them. SQLAlchemy does these together using a system known as **Declarative** which allows us to describe the database tables in the classes that will be mapped to them.

From the docs:
> Classes mapped using the Declarative system are defined in terms of a base class which maintains a catalog of classes and tables relative to that base - this is known as the declarative base class. Our application will usually have just one instance of this base in a commonly imported module

```python
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
```

This is importing a base class that all our class models will inherit. Unlike Sequelize which has a separate file for migration and general use, SQLAlchemy does it all in one class. In order to tell the database how to formulate the table, we need to import some things from `sqlalchemy`

```python
from sqlalchemy import Column, Integer, String, Sequence
```

Now, let's set up our `User` class. We're going to define the class, inherit the `Base`, define the tablename, create the schema, and write a method that returns a viewable string when we want to see our user.

```python
class User(Base):
  __tablename__= 'users'

  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  email = Column(String)
  nickname = Column(String(50))

  def __repr__(self):
    return f'<User(id={self.id} name="{self.name} email="{self.email} nickname="{self.nickname}")>'
```

When a class uses a Declarative (`Base`), it needs, at minimum, a `__tablename__` and an `id` Column. Any specifications for the column goes into the `Column()` method imported. On the `id` we specify it as a primary key, and also tell SQLAlchemy that we want the ORM to generate sequential ids.
From the docs:
> SQLAlchemy doesn’t generate or assume [new primary key identifiers] without being instructed. For that, you use the Sequence construct

We have also made `name` a required field and limited the `nickname` field to 50 characters.

The `__repr__` function is an optional method that will, when we query the user object, will print out that string rather than `<__main__.User object at 0x1025c2390>`

## Connecting to the Database

In order to connect to the database, sqlalchemy needs to create "an instance of Engine [which] represents the core interface to the database, adapted through a dialect that handles the details of the database and DBAPI in use."

The engine needs a database url to point it to the relevant database. Create a postgres database called `sqlalchemy_test` so we have something to connect to.

In your `models.py`, import `create_engine` from sqlalchemy. At the top of our script, we'll define an `engine` by calling `create_engine` and passing in our database url and `echo=True` which logs the SQL commands into our terminal so we can see what SQLAlchemy is doing.

After our class models, we'll apply the migrations by running a method in the metadata of the `Base` Declarative and passing in our engine. 

```python
from sqlalchemy import create_engine

engine = create_engine('postgresql://localhost/sqlalchemy_test', echo=True)

...

# Basically migrates everything
Base.metadata.create_all(engine)
```

## CRUDdy Alchemy

Make a new file in the root called `server.py`. Import `sqlalchemy` at the top and define a `main()` function where all our logic will live. This helps abstract our logic a bit and, if we want to, allows us to import the script in another `.py` file without automatically running it. 

In order to do anything with the database, we need to open what SQLAlchemy calls a `Session`, which is a SQL transaction. We get the `sessionmaker()` function from the `sqlalchemy.orm` and create a new class of Session and configure it to be bound to the engine we created in the `models.py` folder (in order to do this in a new file, we'll have to import the engine from `models`).

The next step is, within our `main` to create a session using the `Session` class.

```python
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import engine

Session = sessionmaker(bind=engine)

def main():
  session = Session()
  
# This line allows us to import the script without calling main. 
# It's magic, don't know how it works yet
if __name__ == '__main__':
  main()
```
#### TL;DR of Transactions

Why session? Because transactions! Transactions came as a response to a problem that happened back when you interacted with databases back in the day. Let's say you want to increment a value; you read the value from the database, increment it, and write it back. This works well until multiple people want to increment at the time. Two or more will read the value and increment it, but when they write it back to the database, it only increments once rather than by all users. Bad news bears, that's some invalid data! Enter transactions. Transactions basically create a fork of the database and then, when that transaction is finished, it commits it to the database. If there are merge conflicts, the 2nd script fails and runs again.

The session works very similarly to our git workflow. A session is opened, CRUD operations are done, the changes we make get flushed up to the database and change it, but the changes aren't applied until we do `session.commit()`.

#### Create

We'll want to import any models that we want to use from our `models` as well, then call a new instance of that class. We'll save it in a variable so we can futz with it before we save it to the database.

```python
from models import engine, User

def main():
  session = Session()

  tosspot = User(name='Gavin Callandar', email='gavin.callandar@ga.co', nickname='Gav')

```
If we want to add it to the database, we use the session and call the `add()` method. We can also add a list of users with the method `add_all()`

```python
# Add one
session.add(tosspot)
# Add LOADS
session.add_all([User(name='Wendy Williams', email='wendwil@gmail.com', nickname='Windy'), User(name='Steven Peters', email='steven.peters@ga.co', nickname='Stevie'), User(name='Mary Contrary', email='marycontrary@gmail.com', nickname='Mar'), User(name='Michael Schull', email='mikeyboi@gmail.com', nickname='Mike'), User(name='Madison Edminston', email='madison.edminston@ga.co', nickname='Mads')])
```
If you want to see the new inserts currently staged we can `print(session.new)`.

At this point, we say that the instances are pending; no SQL has yet been issued and the object is not yet represented by a row in the database. The Session will issue the SQL to persist the users as soon as is needed, using a process known as a flush. If we query the database, all pending information will first be flushed, and the query is issued immediately thereafter. `session.new` won't show changes that have been flushed.

#### Read

SQLAlchemy is a written for developers who know what is going on behind the scenes, so many of the querying syntax is reminiscent of raw SQL commands.

Let's load Mads into a variable called `go_to_gal`.
```python
go_to_gal = session.query(User).filter_by(nickname='Mads').first() 
```
This command queries the session using the `User` model, applies the filter `WHERE nickname = 'Mads'`, and returns us the first of the results. Queries can be crafted to be more or less specific. [See the Documentation on it](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying).

> Note, if you print out `session.new` after querying, it'll be empty because querying flushes all pending instances

#### Update

Let's say that we want to update Mad's email to show the change to a longer and more verbose email ending.

```python
go_to_gal.email = 'madison.edminston@generalassemb.ly'
```
Done! We can see all the changes the session is tracking by using `session.dirty`.

#### Destroy

There are a few different ways to delete, either by tacking the method onto the end of a query or by passing in a user object. Let's delete Mary contrary and Gavin.
```python
session.query(User).filter_by(nickname='Mar').delete()
session.delete(tosspot)
```
If we want to see if it worked, we can print out a query count before and after the delete:

```python
print(session.query(User).filter(User.nickname.in_(['Mar', 'Gav'])).count())
```

## Relationships

Tables are cool and all, but what's the point of a SQL database without some relationhips? Read more information on the relationships [here](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#relationship-patterns).

Let's start off by giving our users the ability to add their pets! This will be a one to many relationship because even if multiple people own a pet, that pet chooses who _really_ is the owner.

### One to Many

Using the same syntax that we used for `User`, make a `Pet` model with the following fields:
* id: Integer, PK,
* name: String, NOT NULL
* species: String, NOT NULL
* age: Integer

Next, we'll need to import some things. 

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
```

Then we'll add another column to link our Pet to the primary key of the user using this syntax

```python
user_id = Column(Integer, ForeignKey('users.id'))
```

The last thing we need to do is use a second directive, known as `relationship()` to tell the ORM that the Pet class itself should be linked to the User class, using the attribute Pet.user.

```python
user = relationship("User", back_populates="pets")
```
The `back_populates` parameter tells SQLAlchemy to do some magic and assume the relationship on the user side as well. We'll need to add a relationship to the user model as well.

At the end of it, our models should look like this:

```python
class User(Base):
  ...
  pets = relationship('Pet', back_populates='user')
  ...

class Pet(Base):
  __tablename__ = 'pets'

  id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
  name = Column(String, nullable=False)
  species = Column(String, nullable=False)
  age = Column(Integer)
  user_id = Column(ForeignKey('users.id'))

  user = relationship('User', back_populates='pets')

  def __repr__(self):
    return f'<Pet(id={self.id} name="{self.name} species="{self.species} age={self.age} user_id={self.user_id})>'
```

Now, because we've changed the structure of our database, we need to run the `models.py` file again. When we're done, when we check our psql shell we'll see we have a new table called pets!

##### Add some pets

At the end of our `main()` function in our `server.py`, let's try printing all of the pets associated with Mads by printing `go_to_gal.pets`. We should get an empty list printing in our terminal.

So lets add Emmy to the list! We can do this by simply attributing a value to the `pets` parameter of our User object.

```python
go_to_gal.pets = [Pet(name='Emmy', species='dog', age=2)]
```

If we want to see if it worked, we can print `print(go_to_gal.pets)` and see all the qualities of Emmy! You'll see that the `user_id` is None. That's because this Pet instance is pending. If we query, it'll flush anything that's pending and create the relationship in the database.

```python
go_to_gal.pets = [Pet(name='Emmy', species='dog', age=2)]
print(go_to_gal.pets)
print(session.query(User).filter_by(nickname='Mads').first().pets)
```

With a bidirectional relationship, elements added in one direction automatically become visible in the other direction.

```python
go_to_gal.pets[0].user
# -> <User(id=213 name="Madison Edminston email="madison.edminston@generalassemb.ly" nickname="Mads")>
```

Now we can add pets to our users! If we want to add another pet to an already existing array of pets, we can use the same syntax, but just add the lists together.

```python
go_to_gal.pets += [Pet(name='Ballad', species='dog', age=9), Pet(name='Blub', species='fish')]
```

##### Querying with Joins
There are a couple of ways we can query with joins, [more on it here](https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying-with-joins)

```python
# If we want to get the user and the pet
session.query(User, Pet).filter(User.id==Pet.user_id).filter(Pet.name=='Emmy').all()
# -> [(<User(id=213 name="Madison Edminston email="madison.edminston@generalassemb.ly nickname="Mads")>, <Pet(id=205 name="Emmy species="dog age=2 user_id=213)>)]

# If we want to get the user based on pet information
session.query(User).join(Pet).filter(Pet.name=='Emmy').all()
# -> [<User(id=213 name="Madison Edminston email="madison.edminston@generalassemb.ly nickname="Mads")>]
```

##### Deleting with 1:M
Unless we tell SQLAlchemy to delete associated relationships, it won't. So if we deleted Mads, all her Pets would still exist in the database. If we want to _cascade_ delete, we have to tell the ORM in the parent model when establishing the relationship.

```python
User(Base):
  ...
  pets = relationship('Pet', back_populates='user', cascade="all, delete, delete-orphan")
  ...
```

If we want to see if it works, we can put this at the end of our `main()`

```python
print(session.query(User).filter_by(nickname='Mads').count())
# -> 1
print(session.query(Pet).filter(Pet.name.in_(['Emmy', 'Ballad', 'Blub'])).count())
# -> 3

# Delete Mads
session.delete(go_to_gal)

print(session.query(User).filter_by(nickname='Mads').count())
# -> 0
print(session.query(Pet).filter(Pet.name.in_(['Emmy', 'Ballad', 'Blub'])).count())
# -> 0
```

### Many to Many

For a plain many-to-many, we need to create an un-mapped Table construct to serve as the association table.

We're going to make some toys for our pets! Let's make an association table under our Pet class. Since we won't really be accessing the association table, we can make it using SQLAlchemy's `Table` class.

```python
from sqlalchemy import Table
# association table
pet_toys = Table('pet_toys', Base.metadata, 
                  Column('pet_id', ForeignKey('pets.id'),
                  primary_key=True), Column('toys_id', 
                  ForeignKey('toys.id'),
                  primary_key=True)
                )
```

**NOTE:** This association table only contains columns which reference the two sides of the relationship—Pet and Toy; if it has any other columns, SQLAlchemy requires a different usage pattern called the “association object”. Read more about [Association Objects](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#association-object).

We'll need to edit our Pet class and make a Toy class to establish relationships.

```python
class Pet(Base):
  ...
  toys = relationship('Toy', secondary=pet_toys, back_populates='pets')
  ...
  
class Toy(Base):
  __tablename__ = 'toys'

  id = Column(Integer, Sequence('toy_id_seq'), primary_key=True)
  toy = Column(String(50), nullable=False, unique=True)
  
  pets = relationship('Pet', secondary=pet_toys, back_populates='toys')

  def __repr__(self):
    return f'<Toy(id={self.id}, toy="{self.toy}")'
```

Run the `models.py` and check for errors. **Note**: Because both `Toy` and `Pet` have a secondary parameter in the relationship that relies on the `pet_toys` variable, we'll need to assign it before the `Pet` and `Toy` class declarations.

Back in your `server.py`, create a variable to hold Emmy, Madison's dog. You can do this via a query or via referencing the relevant index in the Madison object. Print it out to make sure your console is printing out what you want.

Let's add a ball to Emmy's favorite toys list. We can do this by appending a new Toy to the toys relationship reference!

```python
emmy.toys.append(Toy(toy='ball'))
print("🎾", emmy.toys)
session.commit()
```

Boom! New toy. 

## More docs

This is a fairly minimal coverage of what can be accomlished with SQLAlchemy. If you want more:

* [Querying](https://docs.sqlalchemy.org/en/13/orm/query.html)
* [Relationship Configuration](https://docs.sqlalchemy.org/en/13/orm/relationships.html)
* [Mapper Configuration](https://docs.sqlalchemy.org/en/13/orm/mapper_config.html)
* [Using a session](https://docs.sqlalchemy.org/en/13/orm/session.html)
