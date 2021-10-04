# Many-to-Many Relations

## Learning Objectives

1. Use Django's `ManyToManyField` to enable a m:m relationship
2. Use `mainmodel.submodels` and `submodel.mainmodel_set` to access related data from either Model.

Yesterday we learned the first of two common types of data relations: `One-to-Many` or 1:m. In this relationship, one model is said to "own" multiple objects of another model. It's a very common relationship and we can readily think of examples: one customer has many orders; one conference has many attendees; one restaurant has many menu items; one collector has many cats.

The next kind of relationship we will learn about is the `Many-to-Many` relationship, often abbreviated `m:m` or `n:m`. You can think of this as a two-way one-to-many relationship where each model "owns" multiple objects of the other model. Some examples of this include: one band can have many genres of music that they play, and one genre has many bands in it; one article has many category tags, and each category tag is linked to many articles; and today's example - one cat can have many toys, and each toy could be owned by multiple cats.

If we were writing all of this ourselves we would normally need an intermediary table, called a `join table`, to enable the references between tables. We use a join table because if we didn't, the nature of a many-to-many relationship would require one of our related tables to contain duplicate data. BAD!

We aren't writing it ourselves, though. \(Not yet, anyway.\) Django has a very easy way to link models together in a many-to-many relationship that takes care of the join table and references in the database for us. Let's see how it works.

## Adding the CatToy Model

We are creating a new model to represent toys that our cat owns. We will call it `CatToy`. Each `CatToy` can be owned by many `Cats` and each `Cat` can own many `CatToys`. Open up your `main_app/models.py` and add a class for the `CatToy` model above the `Cat` model class:

```python
class CatToy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cattoys_detail', kwargs={'cattoy_id': self.id})
```

We don't need to represent much data about the toys to set up the relationship. We've included a `__str__` method so that the Model will nicely print its name. We also included a `get_absolute_url()` method that will allow us to omit all the `success_urls` and redirect URLs from our generic editing views. Once we've added this, save the file, make new migrations, and run them:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

## Register the new model

Go ahead and add this model to the `main_app/admin.py`:

```python
# Add the CatToy model to this import line
from .models import Cat, CatToy

# Register the model below the others
...
admin.site.register(CatToy)
```

Now we can easily read, create, update, and delete CatToys via the admin interface. Let's now add some basic CRUD routes for it.

## CRUD Routes for the New CatToy Model

We do need the ability to create, read, update, and delete each CatToy since it is one of our models. Let's quickly set up URLs, views, and template forms for that just like we did in the CRUD Forms lesson:

### URLs

We will need 5 total routes for this new Model: read all, read one, create one, update one, delete one. The URLs will largely follow the same pattern as the ones for `Cat`. Here are all 5 that we need to add. In the interest of time, just paste these into the `urlpatterns` list in your `main_app/urls.py`:

```python
path('cattoys/', views.cattoys_index, name='cattoys_index'),
path('cattoys/<int:cattoy_id>', views.cattoys_detail, name='cattoys_detail'),
path('cattoys/create/', views.CatToyCreate.as_view(), name='cattoys_create'),
path('cattoys/<int:pk>/update/', views.CatToyUpdate.as_view(), name='cattoys_update'),
path('cattoys/<int:pk>/delete/', views.CatToyDelete.as_view(), name='cattoys_delete'),
```

## Views

We can also use the same patterns for our corrsponding view functions as we used for `Cat`. Don't forget to `import` your CatToy model, then add these into your `main_app/views.py`:

```python
# import the CatToy model
from .models import Cat, CatToy

# Add these CatToy Form classes

class CatToyCreate(CreateView):
    model = CatToy
    fields = '__all__'

class CatToyUpdate(UpdateView):
    model = CatToy
    fields = ['name', 'color']

class CatToyDelete(DeleteView):
    model = CatToy
    success_url = '/cattoys'

# Add these CatToy View functions

def cattoys_index(request):
    cattoys = CatToy.objects.all()
    return render(request, 'cattoys/index.html', { 'cattoys': cattoys })

def cattoys_detail(request, cattoy_id):
    cattoy = CatToy.objects.get(id=cattoy_id)
    return render(request, 'cattoys/detail.html', { 'cattoy': cattoy })
```

## Templates

Lastly, we need a few templates for this new model. We need the two forms for our generic editing views and we need an index and a details page. Our two forms will go into `main_app/templates/main_app`. One will be `cattoy_form.html` and the other will be `cattoy_confirm_delete.html`. Recall that this is the naming convention for these form templates when we are using `generic editing views`. Let's add those now:

```markup
<!-- main_app/templates/main_app/cattoy_form.html -->
{% extends 'base.html' %}

{% block content %}
    <form action="" method="post">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
        </table>
        <input type="submit" value="Submit!">
    </form>
{% endblock %}
```

```markup
<!-- main_app/templates/main_app/cattoy_confirm_delete.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Delete Cat Toy</h1>

    <h4>Are you sure you want to delete <strong>{{ cattoy }}</strong>?</h4>

    <form action="" method="POST">
        {% csrf_token %}
        <input type="submit" value="Yes - Delete!">
        <a href="{% url 'cattoys_detail' cattoy.id %}">Cancel</a>
    </form>
{% endblock %}
```

Now we'll add the two "read" pages, `cattoys\index.html` and `cattoys\detail.html`. We need to make a directory inside our `templates` directory named `cattoys` and our pages will go in there:

```markup
<!-- templates/cattoys/detail.html -->
{% extends 'base.html' %}
{% block content %}

<h1>Cat Toy Details</h1>

<div class="row">
    <div class="col s6">
        <div class="card">
            <div class="card-content">
                <span class="card-title">{{ cattoy.name }}</span>
                <p>Color: {{ cattoy.color }}</p>
            </div>
            <div class="card-action">
                <a href="{% url 'cattoys_update' cattoy.id %}">Edit</a>
                <a href="{% url 'cattoys_delete' cattoy.id %}">Delete</a>
            </div>
        </div>
    </div>
</div>
{% endblock %}
```

```markup
<!-- templates/cattoys/index.html -->
{% extends 'base.html' %}
{% block content %}

<h1>Cat Toy List</h1>

{% for cattoy in cattoys %}
    <div class="card">
        <a href="{% url 'cattoys_detail' cattoy.id %}">
            <div class="card-content">
                <span class="card-title">{{ cattoy.name }}</span>
                <p>Color: {{ cattoy.color }}</p>
            </div>
        </a>
    </div>
{% endfor %}

{% endblock %}
```

## TEST!

This is a great place to test what we've written. We've just added 5 new routes. We need to test them. Restart your server if it was running and let's test these routes:

1. Test `http://localhost:8000/cattoys/create` for creating new cat toys. Add a couple.
2. Test `http://localhost:8000/cattoys` for showing the toys you've added.
3. Click into one of the toys to test the `details` page.
4. Test the update link on one of the toys.
5. Test the delete link for one of the toys.

## Adding the Many-to-Many Field to the Model

With that code in place, we can start working on updating our existing Cat Model and pages. The way that we establish a m:m relationship is by adding a `ManyToManyField` to a model. Django requires only one of our models to have this field and it takes care of the rest. We must only decide which model to put the field into. I think we will mostly be viewing toys by looking at the Cat that owns them so let's add `cattoys` to the `Cat` model:

```python
class Cat(models.Model):
    ...
    # Add this line below the other fields
    cattoys = models.ManyToManyField(CatToy)
    ...
```

That is really all we need to do to set up the relationship. But we have changed a model so we now need to generate some new migrations and run them. Open up a terminal and run these commands from your project folder:

```bash
python3 manage.py makemigrations
```

...then...

```bash
python3 manage.py migrate
```

Now we need to update our `CatCreate` and `CatUpdate` view classes to include the new field:

```python
# main_app/views.py
class CatCreate(CreateView):
    model = Cat
    # Update the line below - add 'cattoys'
    fields = ['name', 'breed', 'description', 'age', 'cattoys']

class CatUpdate(UpdateView):
    model = Cat
    # Update the line below - add 'cattoys'
    fields = ['name', 'breed', 'description', 'age', 'cattoys']
```

Save everything, restart the server if necessary and visit the Cat Create page. Yay! Now we can add multiple cat toys to any of our Cats.

## Add `cattoys` to the Cat detail page

In the style of our detail pages so far, let's add something to show toys. Right above the `for` block for the photos in `cats/detail.html`, add this code:

```markup
<!-- templates/cats/detail.html -->
<!-- above section for photos -->
...
{% for cattoy in cat.cattoys.all %}
    <div>{{cattoy.name}}, Color: {{cattoy.color}}</div>
{% empty %}
    <div>Cat Has No Toys :(</div>
{% endfor %}
...
```

## Add Cat owners to CatToy detail page

Because this is a many-to-many, it probably makes sense to show all the related Cats that own any particular toy. Let's update the `cattoys/detail.html` page.

```markup
<!-- templates/cattoys/detail.html -->
<!-- above section for photos -->
...
        </div>
        <!-- New Code below here -->
        Owned by:
        {% for cat in cattoy.cat_set.all %}
            <div>{{cat.name}}</div>
        {% empty %}
            <div>Nobody Has This Toy</div>
        {% endfor %}
        <!-- New Code above here -->
    </div>
</div>
{% endblock %}
...
```

## Conclusion

Congratulations! You've completed a substantial full-stack app in Python and Django.

