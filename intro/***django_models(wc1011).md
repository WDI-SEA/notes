<img src="https://i.imgur.com/s8QeOpo.png">

# Intro to Django Models

## Learning Objectives

| Students will be able to: |
|---|
| Define a Django Model for a data entity |
| Generate migrations when Models are added or updated |
| Run pending migrations |
| Implement a Details page for a single model instance |

## Roadmap

1. Review Django Architecture
2. Review the Starter Code
3. What's a Model?
4. Models in Django
5. Making and Running Migrations
6. Performing CRUD Using Django's ORM
7. On to the Code!
8. I am the Admin!
9. Adding a Cat "Details" Page

## The Model Layer in the Django Architecture

<img src="https://i.imgur.com/1fFg7lz.png">
	
This lesson focuses on the **Model layer** which provides **Views** with access to the **database**.

## Review the Starter Code

Feel free to use your own code from the previous lesson or pull down the latest code on the [CatCollector](https://git.generalassemb.ly/r-sei-12/catcollector) repo.

The only change to the starter code from where the last lesson left off is that the `home` view now renders a **home.html** template instead of using `HttpResponse` to send back a string.

Note that since the `HttpResponse` function is no longer being used in **views.py**, its import has been removed.

## Get Ready to Code

Remember that in our Python projects we need to make sure our work (and especially any packages we install) is done within an activated virtual environment. Do you remember how to activate it?

```
$ source .env/bin/activate
```

If successful, your terminal prompt should begin with `(.env)`. If it were Brock's, it would look like this:

```
(.env) ⋋| ◉ ͟ʖ ◉ |⋌  catcollector 
$ 
```

## What's a Model?

**Models** are used to perform CRUD data operations on a database.

Remember **entities** in the Entity-Relationship-Diagrams?

A Django Model represents a single entity from the ERD.

Thus, a Model has a one-to-one mapping with a table in the database and is what allows us to perform create, read, update and delete data operations on that table.

When we retrieve data from the database (using a Model of course), we will have **model objects**, each of which represents a row in a database table. Model objects are also called _instances_ of the Model.  We can work with these instances of the Model just like how we worked with Mongoose documents.

> Note: Since a "model" can technically refer to the Model class or an instance of that class, we will try to use "Model" (capitalized) to refer to a Model class we use to perform CRUD with and "model" (lowercased) to refer to a model instance.

## Models in Django

Each Model is defined as a Python class that inherits from `django.db.models.Model`.

Here's the **Cat** entity from an ERD and the code to define the equivalent Model:

<img src="https://i.imgur.com/gwlOAXc.png">

All of the Models for an app are defined in the app's `models.py` file.

Let's create the `Cat` Model by typing in the above code.

Note that each field (attribute) is represented by a Field class, e.g., `CharField`. Here are the [docs of available Field types](https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types) - there's plenty of options.

It's important to note that the Field types for a Model don't just determine the column's data type in the table, Django also uses this information:

- To implement some validation in automatically-generated forms.
- To determine the default HTML [widget](https://docs.djangoproject.com/en/2.1/ref/forms/widgets/) to render in forms for the Model. For example, a `CharField` uses a `<input type="text">` as its _widget_, whereas, a `TextField` uses a `<textarea>`.

#### Review Questions

<details>
	<summary>
		In Django, what is used to perform CRUD database operations?
	</summary>
	<p><strong>A Model</strong></p>
</details>

<details>
	<summary>
		How is a Model defined in Django?
	</summary>
	<p><strong>With a Python class</strong></p>
</details>

<details>
	<summary>
		An ERD Entity maps to a _____ in Django, which maps to a _____ in the database.
	</summary>
	<p>An ERD Entity maps to a <strong>Model</strong> in Django, which maps to a <strong>table</strong> in the database.</p>
</details>

## Making and Running Migrations

#### What are Migrations?

[Migrations](https://docs.djangoproject.com/en/2.1/topics/migrations/) are used to synchronize a database's schema with the app's Models.

Migrations are used to evolve a database over time - as the requirements of the application change.  However, they can be "destructive" (cause a loss of data), so be careful with migrations if you're working with an application in _production_.

Migrations in Django are Python files that are created by running a command Django in Terminal.

#### Making Migration Files

Okay, we've defined a `Cat` Model, but the database does not yet have a table to hold all of our furry model instances (rows). 

The following command creates migration files for all Models that have been added or changed since the last migration:

```bash
$ python3 manage.py makemigrations
```

The output in the terminal informs us that the following migration file was created: `main_app/migrations/0001_initial.py`

A `migrations` directory is created for an **app** the first time you run `makemigrations`.

You don't have to do anything with the migration files, but since this is the first time we've made one, let's open it and take a peek.

> You should rarely need to edit migration files by hand, but it’s entirely possible to do so if you ever need to.

#### Running Migrations

Simply creating migration files does not update the database's schema.

To synchronize the database with the code in the migration files, we "migrate" using this command:

```bash
$ python3 manage.py migrate
```

`OK` messages are a good thing 😊

#### What Exactly Was Created in the Database?

To checkout the tables we have in our database, open psql:

```
$ psql catcollector
```

List the tables:

```sql
\d
```

You'll find quite a few tables named like `django_*`.  These tables are used by the framework to track migrations, server-side sessions, etc.

You'll also find several tables named like `auth_*`.  These were created by the `dango.contrib.auth` app that's listed in the `INSTALLED_APPS` variable within `settings.py`.

Finally, there's our `main_app_cat` table that maps to our `Cat` Model. It's empty now - we'll change that in a bit, but first...

#### Review Questions

<details>
	<summary>
		What are used to update a database's schema over time as an application's functionality evolves?
	</summary>
	<p><strong>Migrations</strong></p>
</details>

<details>
	<summary>
		When is it necessary to make and run migrations?
	</summary>
	<p><strong>Whenever a Model is added or updated in a way that impacts the database's schema.</strong></p>
</details>

## Performing CRUD Using Django's ORM

#### What's an ORM?

ORM stands for Object-Relational-Mapper.

It's called that because it creates Python objects from rows in a relational database table and vice-versa.

The ORM allows developers to write object-oriented code to CRUD data instead of using SQL directly.

ORMs make application developers more productive.

The fact is, the ORM in Django can generate SQL that even the most experienced developer would struggle to write.

Another benefit is that the ORM & Model layer abstracts away the differences between the flavors of SQL that exists - we get to write the same Python code to perform CRUD operations, regardless of which database is being used.

#### Django's ORM

The Django ORM is automatically going to generate, a plethora of methods for each Model.

Django's ORM includes methods for performing:

- Filtering (querying based on criteria)
- Ordering
- Even accessing the data from related Models!

Django refers to the ORM functions available as its [database API](https://docs.djangoproject.com/en/2.1/topics/db/queries/). Additional documentation can be [found here](https://docs.djangoproject.com/en/2.1/ref/models/).

## Let's Get Coding!

Time to add some of this ORM magic to the  Cat Collector app!

Currently, we are "faking" the data with a `list` of cats.

Time to update **main_app/views.py**...

First let's be sure to remove the `class Cat...` and the `cats` list.

Now let's write the code that uses the `Cat` Model to read all of the cat objects:

```python
# main_app/views.py

from django.shortcuts import render
from .models import Cat

...

def cats_index(request):
  cats = Cat.objects.all()
  return render(request, 'cats/index.html', { 'cats': cats })
```

Don't forget to import the `Cat` Model too!

Refresh the page and you should see something like this:

<img src="https://i.imgur.com/FN26kDm.png">

Nice!

## I am the Admin!

But wait, there's another really REALLY neat thing about Django - it comes with built-in administrator functionality! Remember that `django.contrib.auth` in the `INSTALLED_APPS`? Let's use it!

A _super user_ is an administrator for the site. When you are logged in to this account, you can access the Admin app to add additional users and manipulate Model data.

Run this command in the terminal:

```bash
$ python3 manage.py createsuperuser
```

Django will want you to create a password that's at least 8 characters long and complex, however, you can bypass it by typing `y` at the warning prompt.

You will be prompted to enter a username, email address, and a password.

Now go to your webpage and head over to the `/admin` route to see an _administration_ portal!  

Did you mess up your password? It's okay - no big fish. Go back to your terminal and use this handy command:

```bash
python3 manage.py changepassword <user_name>
```

But I don't see **Cats**!  That's because in order to manipulate Cat data, we need to "register" the `Cat` Model so that the admin portal knows about.

We register our Models in the `main_app/admin.py` file:

```python
from django.contrib import admin
# import your models here
from .models import Cat

# Register your models here
admin.site.register(Cat)
```

No need to restart the server - just refresh that beauty portal!

We can add, edit, and remove data objects anytime we need to by browsing to `/admin`. Neat!

## Adding a Cat "Details" Page

Typically, the _index_ page showing all cats would only show a "summary" of each cat's info.  For example, just their "name" perhaps.

Then, it would be commonplace to show the "details" for a data object using a separate page that results from the user clicking on that summary info - in this case, the cat's "card" in **index.html**.

#### Typical Process to Add Functionality to an App

Remember, nothing is going to happen unless an HTTP request leaves the browser informing the server what the app wants to do.

When adding additional functionality to a web app we need to do the following:

1. With Django, decide the appropriate URL for the route.  Because Django does not follow the RESTful routing methodology, you are free to name the URLs as you see fit. 
2. Add the UI that is going to trigger the HTTP request to be sent to the server. For example, adding a `<form>` to submit a new cat.
3. Code the route on the server.  In the case of Django, this is done by adding an additional `path(...)` to the `urlpatterns` list within the app's `urls.py` module. **Each entry in `urlpatterns` determines what code will run when the URL matches an HTTP request**.
4. Now you need to add the _view function_ referenced by the `path(...)` inside of the **views.py** module. The _view function_ contains the code to perform CRUD, etc. It ultimately is responsible for responding to the client's request...
5. If data was changed, respond with a **redirect**. Otherwise, you'll typically **render** a _template_, optionally passing data to it. If a _template_ is required, time to write it, and you're done - other than debugging.

Make it a habit to follow the steps above anytime you need new functionality in your app.

##### Step 1

In Django, we don't worry about the HTTP method (verb), unless we're writing a `<form>` to do searching, in which case, we would switch from the form's default method of `POST` to a `GET`.

So what's the URL for viewing a single cat's detail page?

For sure we need to "capture" the `id` of the cat we want the details for in the URL. In Django, we use angle brackets to declare a _URL parameter_ to capture values within the _segments_ of a URL as follows.

Let's go with this: `cats/<int:cat_id>/`

The `int:` part is called a converter and it's used to match and convert the captured value from a string into, in this case, an integer. If the info in the segment does not look like an integer, then it will not be matched - this is different than what we saw in Express where the type of info in a segment didn't matter.

##### Step 2

As far as the UI is concerned, clicking on a cat's "card" in the **index.html** should trigger the request to the server to view the details of a cat.

We can accomplish this by wrapping the card's content with an `<a>` tag and setting its `href` appropriately:

```html
<div class="card">
  <!-- add this single line below -->
  <a href="/cats/{{ cat.id }}">
    <div class="card-content">
      <span class="card-title">{{ cat.name }}</span>
      <p>Breed: {{ cat.breed }}</p>
      <p>Description: {{ cat.description }}</p>
      {% if cat.age > 0 %}
        <p>Age: {{ cat.age }}</p>
      {% else %}
        <p>Age: Kitten</p>
      {% endif %}
    </div>
  <!-- and this following one as well -->
  </a>
</div>
```

The above is pretty similar to what we did in EJS templates.

After refreshing the page, hover over a cat card and check the URL in the bottom-left of the browser window. It should look something like:<br>`localhost:8000/cats/2`.

Cool, on to the next step...

##### Step 3

Now that clicking a cat card is going to send a request like `GET /cats/1`, we need to add a new route entry to the `urlpatterns` list in **urls.py** that will match this request:

```python
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='index'),
  # new route below 
  path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
]
```

We've decided that the newly added route will invoke an appropriately named _view function_, `cats_detail`.  That's next...

##### Step 4

As you know, _view functions_ are defined within **views.py**.

Here's the new `cats_detail` function:

```python
# main_app/views.py

...

def cats_detail(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/detail.html', { 'cat': cat })
```

The `cats_detail` function is using the `get` method to obtain the cat object by its `id`.

> Django will pass any captured URL parameters as a named argument to the view function!

**What determined the parameter name of cat_id in the cars_detail view function?**

##### Step 5

So we want to render the cat data within a **detail.html** template...

The `cats_detail` view function is passing a dictionary of data (called the _context_) to a template called **detail.html**.

Create that **detail.html** template:

```
$ touch main_app/templates/cats/detail.html
```

Now let's add the following template code:

```html
{% extends 'base.html' %}
{% block content %}

<h1>Cat Details</h1>

<div class="card">
  <div class="card-content">
    <span class="card-title">{{ cat.name }}</span>
    <p>Breed: {{ cat.breed }}</p>
    <p>Description: {{ cat.description }}</p>
    {% if cat.age > 0 %}
      <p>Age: {{ cat.age }}</p>
    {% else %}
      <p>Age: Kitten</p>
    {% endif %}
  </div>
</div>

{% endblock %}
```

It's basically the same cat "card" from **index.html**, except the wrapping `<a>` tags have been removed.

**What's that `{% extends 'base.html' %}{% block content %}` business about?**

Okay, let's refresh and check it out!

<img src="https://i.imgur.com/mee5Cxv.png">

##### Removing Hand-coded URLs in Templates

Although everything works nicely, hand-coding the URLs in templates, is not considered a good practice because during development, URL's may change.

For example, in **index.html**, we find:

```html
...
<div class="card">
  <a href="/cats/{{ cat.id }}">
  ...
```

Django has a better way!

Let's take another look at the `urlpatterns` in **urls.py**:

```python
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('cats/', views.cats_index, name='index'),
  path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
]
```

That `name` argument within each `path` is used to obtain the correct URL in templates using DTL's `url` template tag!

In **index.html**, replace this code:

```html
<a href="/cats/{{cat.id}}">
```

With this code:

```html
<a href="{% url 'detail' cat.id %}">
```

The above is the Django way.

**Congrats on coding the Django `Cat` Model and adding the _detail_ functionality for the Cat Collector.**

## Lab

For practice, do everything we did in this lesson on your Finch Collector project!

Don't forget to make commits.

## Resources

[Django Model API](https://docs.djangoproject.com/en/2.1/ref/models/)

Last commit Dalton Hart General Assembly GIT HUB enterprise 1/27/21
