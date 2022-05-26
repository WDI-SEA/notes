# ERDs

## Reading Diagrams
In ERDs, so much information can be shared at a glance if you know how to read the specific arrows and shapes used. 

![Key to ERD entities and relationship arrows](https://i.imgur.com/tPU3Oxn.png)

You can indicate entities, relationships, and attributes by differing their shapes, as shown below.

![Shapes in ERDs](https://i.imgur.com/AGkezz1.png)

### Arrows
Crow's feet notation shows the maximum (*cardinality*) and minimum (*ordinality*) number of times an instance of an entity can relate to instances of another entity.

![ERD crows feet arrow notation](https://i.imgur.com/w1pV6YR.png)


While this is all useful information when planning, today we'll focus on the use of crow's feet to indicate the relationships between entities.

## Making Diagrams
Our approach today will represent entities as tables, with columns as their attributes. We'll use crow's feet notation to indicate the relationships.

For every model you have, you'll want to create a table in your ERD. If the models have a 1:M relationship, store the PK (primary key) of the 1 as an FK (foreign key) on the many table. If you have a N:M, store the PKs of each model in a join table. 

Think of all the information you can:
* table name
* relationship between models/entities
* attribute name
* attribute data type

### Ex 1: school with students and classes
Models: student, class, school


We want to know the name and location of the school, and how many classes they offer, so imagine a `schools` table:

| id     | name | location | classCount |
| ------ | ---- | -------- | ---------- |
| Number | String | String     | Number     |


Now imagine a `students` table to track a name, email, and an enrollment status:
| id     | name   | email  | enrolled | schoolId |
| ------ | ------ | ------ | -------- | -------- |
| Number | String | String | Boolean  | Number   |

And a `classes` table will hold information on that class instance:
| id     | instructor | course | title  | schoolId |
| ------ | ---------- | ------ | ------ | -------- |
| Number | String     | Number | String | Number   |

One instance of a school can have many students, and one student should go to only one school, so the relationship is 1:M. The students is the many side, so that table gets the foreign key.

One instance of a class should only belong to one school, but one school could have many classes, so the relationship is 1:M. The classes is the many side so that table gets the foreign key.

One instance of a student can have many classes, and one instance of a class can have many students -- we have a N:M relationship! 

To store records of which students are enrolled in which classes, we'll need a JOIN table, `students_classes`:


| id     | studentId | classId |
| ------ | --------- | ------- |
| Number | Number    | Number  |


### Ex 1. Final ERD

![ERD for school, student, class models](https://i.imgur.com/JLFsccZ.png)


### Ex 2. projects, categories, users
Lets make an ERD for the express-project-organizer, with category and project models, and new model: user. 

`projects` table:
| id     | githubLink | name   | deployLink | description | userId |
| ------ | ---------- | ------ | ---------- | ----------- | ------ |
| Number | String     | String | String     | String      | Number |

`categories` table:
| id     | name   |
| ------ | ------ |
| Number | String |

`users` table:
| id     | email | password |
| ------ | ----- | -------- |
| Number | String  | String     |

#### Relationships:
* there is no relationship between users and categories
* one instance of an user could have zero or many projects, but an instance of a project should belong to just one user -- 1:M, where `projects` gets the FK.
* one instance of a project could have zero or many categories. one category could have zero or many projects associated -- N:M, so we need a join table! 

`categoriesProjects` table:

| id     | categoryId | projectId |
| ------ | ---------- | --------- |
| Number | Number     | Number    |


### Ex 2. Final ERD
![ERD for category, project, user models](https://i.imgur.com/DCjrdLZ.png)


### ERD Resources

[Drawio VSCode Extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)

[Video: Using Drawio](https://www.youtube.com/watch?v=lAtCySGDD48&ab_channel=Dr.DanielSoper)
