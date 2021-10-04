# Models, Migrations

## The New & Improved Cat Collector Code-Along, Part 2

Thanks for coming back! In this installment of Cat Collector we will be connecting Django to a database and starting to work with models and the Django ORM. Remember that the Django ORM provides functions for accessing the database without using straight SQL.

### Connecting Django and Postgres

There are a few settings we need to edit in order to have Django connect to our running Postgres. We'll start with the `catcollector/settings.py` file. Open it up and find the DATABASES section. Make it look like this:

```python
# catcollector/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'cats',
    }
}
```

This sets the database driver to be the one for Postgres and sets the name of the database `cats`. We will create this database shortly. Before that, though, we will need to install another Python module to make Postgres work with Django. Open your terminal and enter this command:

```bash
pip3 install psycopg2
```

That's all we need to do for Django. Now let's use a nice psql shortcut for creating a new database. Open your terminal and run this command:

```bash
createdb cats
```

This is a way we can create the database without being inside the psql command-line interface. With the database created, we are all set to start modeling data in our app.

## Connecting a model to our view

1. Let's create a `model` of our Cat instead of storing it hardcoded in our `views.py`. In our `main_app/models.py` file, change the code to reflect the following:

   ```python
   # main_app/models.py
   from django.db import models

   class Cat(models.Model):
       name = models.CharField(max_length=100)
       breed = models.CharField(max_length=100)
       description = models.CharField(max_length=250)
     age = models.IntegerField()
   ```

2. Once we create or modify any model that we want to use in Django, we must run a database `migration`. A migration is a database action that makes any necessary changes to your db tables to prepare for storing specific data attributes of your models. If we create a new model, the migration is what actually creates the table in the database. If we change the structure of a model, the migration makes the changes in the database.

Migrating is a two step process: First we create a migration file with the following command in our terminal:

```bash
python3 manage.py makemigrations
```

This migration file contains all the database changes that will need to be done to implement your code changes. To execute the migration, run this command:

```bash
python3 manage.py migrate
```

Splitting it into separate steps let you review the migration before you actually run `migrate`, if necessary. Once we've made our model, made our migrations, and executed our migrations, the data is ready to use in Django. Before we get into loading it into our pages, let's play with the data using Django ORM functions that we can run in a Django command shell.

Open the `Django Interactive Shell` to play with the database for our Cats! Enter this terminal command:

```bash
python3 manage.py shell
```

In order to get access to the cat data, we must import the Cat model that we just made. We do this in the standard Python way but we can type it right into the shell:

```bash
from main_app.models import Cat
```

To see all of our Cat objects, enter this command:

```bash
Cat.objects.all()
```

Looks like we have an empty list, which means we have no data yet! Lets add some data!

```bash
c = Cat(name="Biscuit", breed='Sphinx', description='Evil looking cuddle monster. Hairless', age=2)
c.save()
```

If you call `Cat.objects.all()` again you'll see a Cat object exists now! Let's add a `__str__` method in our model. This is a function that we can add to any `class` and it will control what happens when we pass this object into a `print()` statement. In this case, we will set it up to return the cat's name attribute:

```python
# main_app/models.py
...
def __str__(self):
    return self.name
```

### Common ORM Operations

#### Create One New Record

As we did above, we can create a new cat for insertion by simply using the Cat model class to instantiate a new Cat with the desired attributes:

```bash
c = Cat(name="Maki", breed='Flamepoint Siamese', description='Lazy but ornery', age=9)
```

A new Cat is initialized and is stored in the variable `c`. Now to write that data to our table, we just call the `save()` function:

```bash
c.save()
```

Because `c` was an object made from out Cat model class, Django automatically knows that when we save it we are writing it to the `cats` table in the `cats` database.

#### Read All Records

We saw above how we can access all the objects in a data table. We use the name of the model and then add `.objects.all()` and this function will return all Cat objects from the table.

```bash
Cat.objects.all()
```

#### Read One Record

Another very common data operation is to read one specific record from the table based on some provided value, usually an ID. Instead of the `all()` function, we can use the `get()` function:

```bash
Cat.objects.get(id=1)
```

This allows us to specify a value for one or more of the columns. Django iterates through the rows to find the records that have a matching values in those columns and returns those records.

Django's ORM isn't so bad, right? In fact, it's rather understandable and easy to use. Now let's update our `main_app/views.py` to use our models! Remember to remove your Cat class definition, we won't need that anymore. Instead we will import our Cat model:

```python
# main_app/views.py
from django.shortcuts import render
# add this line...
from .models import Cat

def cats_index(request):
        cats = Cat.objects.all()
        return render(request, 'cats/index.html', { 'cats':cats })

# remove the cat class and list at the bottom...
```

Reload your page and you should see a single Cat displayed from your database! You're a wizard, Harry!

![](https://media.giphy.com/media/IN8gg3Gci335S/giphy.gif)

## I am the ADMIN!

One last really really REALLY neat thing: Django comes with a built-in super user account! Let's use it!

The super user or administrator is basically the owner of the site. When you are logged in to this account, you can access the admin interface, add additional users, and manipulate data. Run this command in the terminal:

```bash
python3 manage.py createsuperuser
```

You will prompted to enter a username, email address, and a password. You are now creating a 'web master' for your site!

Now go to your webpage and head over to the `/admin` route to see an admin portal!

Did you mess up your password? It's okay. Forgive yourself. Go back to your terminal and use this handy-dandy command:

```bash
python3 manage.py changepassword <user_name>
```

In order to mess with our Cat data in the admin interface, we need to **register** our Cat model. To do this let's alter our `main_app/admin.py` file to allow our model to be seen:

```python
    from django.contrib import admin
    # import your models here
    from .models import Cat

    # Register your models here
    admin.site.register(Cat)
```

Now when we go back to our admin page, we'll see a link to our Cat model. We can add, update, and remove Cat objects at our leisure from this section. Neat!

### Adding the Cat "show" Page

Our `index.html` should still be showing valid Cat data because all we changed was where it was getting its data. But now that we know the function for reading the data of a single Cat, we can now implement that route in our project.

The difference between an `index` page and a `show` or `details` page is `index` shows all cats on one page and `show` shows all details about one cat. Frequently, we want to limit the data shown about each Cat in the list of all Cats. But we provide a way to link from that list to an individual page for each Cat that can show all of the detailed data about that Cat. Together, these two routes comprise the only `read` operations we will do on our database: Read one object, or Read all objects.

The pattern of creating a new url in `urls.py`, a new view function in `views.py`, and a new html file in `/templates` will apply here. However, think about what we know about the "Read One" operation: the only way we can find the one Cat we are interested in is by knowing its ID. That means that we need a way to have a variable in our URL that can hold any valid Cat ID. Django provides syntax for setting this up.

1. Let's add a `show` url with a variable that can hold the ID that the user is interested in. Open `main_app/urls.py`:

   ```python
   # main_app/urls.py
   from django.urls import path
   from . import views

   urlpatterns = [
       ...
           # add this line...
       path('cats/<int:cat_id>/', views.cats_show, name='cats_show')
   ]
   ```

   The stuff in the pointy brackets is how we read URL parameters in Django. We say the data will be an integer \(int\) and then identify it with a variable named `cat_id`.

2. In our `main_app/views.py` file we will need to write a function to handle the HTTP Request received for the details page of a particular item. Lets update our file to include this function:

```python
    # main_app/views.py
    ...
    def cats_show(request, cat_id):
        cat = Cat.objects.get(id=cat_id)
        return render(request, 'cats/show.html', {'cat': cat})
```

```text
You'll notice that we are searching by id. Django automatically assigns our models incrementing id numbers to organize our tables. Thanks Django!  That way we can look up every single cat by their unique `id` given to us. That `id` will travel with every model so we don't have to worry about assigning them one or trying to maintain it in the back-end! SO SWEET!

After we have made the DB call to retrieve our model, we will render a new view of the `show.html` template and pass in our model as an object for the template to use.
```

1. We will now create a `show.html` template page in `templates/cats` to render our single model view:

   ```markup
   <!-- main_app/templates/cats/show.html -->
   {% load staticfiles %}
   <!DOCTYPE html>
   <html>
     <head>
       <title>catcollector</title>
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css">
       <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
     </head>
     <body>
       <h1>catcollector</h1>

       <h2> Name: {{ cat.name }}</h1>
       <p> Breed: {{ cat.breed }}</p>
       <p> Description: {{ cat.description }}</p>
       <p> Age: {{ cat.age }}</p>
     </body>
   </html>
   ```

2. We can now view a single Cat on its dedicated show page! Awesome! To make our application actually useful, we need to create a link from our `index.html` listing of the Cats over to our `show.html` page. Wrap the entire iteration of each Cat in an anchor tag in our `index.html` page:

   ```markup
   <!-- main_app/templates/cats/index.html -->
   ...
   {% for cat in cats %}
     <a href="/{{cat.id}}">
       <p>Name: {{ cat.name }}</p>
     {% if cat.age > 0 %}
       <p>Age: {{ cat.age }}</p>
     {% else %}
       <p>Age: Kitten</p>
     {% endif %}
     </a>
       <hr />
   {% endfor %}
   ```

   Now we can navigate to the show from the index! Make the `catcollector` header a link that goes back to our index to make our site fully navigable.

### Let's get partial!

We're beginning to see repeated code in our html templates so it makes sense to break our templates into partials to save on code reuse and increase scalability. We'll use a base template to hold our initial `head` code, our `header` section, and our `footer` section. The partials will only contain the necessary html for each specific task.

1. Create a new `base.html` file within our templates folder. This will be our base 'layout' html file:

   ```markup
   {% load staticfiles %}
   <!DOCTYPE html>
   <html>
     <head>
       <title>catcollector</title>
       <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css">
     </head>
     <body>
           <h1>catcollector</h1>
       <hr />

           {% block content %}
           {% endblock %}

         <footer>
           All Rights Reserved, catcollector 2018
         </footer>
     </body>
   </html>
   ```

   The `block content` and `endblock` statements are the placeholders for where our 'child' html will load into our base.html template.

2. In `cats/index.html` we will tell the templating language to send our html to `base.html` with a single line added to the top of the page. We will also wrap our pertinent Cat iterator in the `block content` and `endblock` template tags to designate what gets loaded into our `base.html` dynamically.

   ```markup
   <!-- main_app/templates/cats/index.html -->
   {% extends 'base.html' %}
   {% load staticfiles %}

   {% block content %}
       ... index's iterator code goes in here ...
   {% endblock %}
   ```

   Now try out our root route on the browser and you should see no change. Apply this code refactor to our show.html as well. Good work!

