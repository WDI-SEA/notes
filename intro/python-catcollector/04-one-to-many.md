# One-to-Many Relations

Back for more? Perfect! Part 4 of Cat Collector will take us through setting up a `one-to-many` \(or 1:m\) relationship in our database. Right now we have a bunch of cats and we can perform all basic CRUD functions on the cats. But since this is Cat Collector we really need to associate cats to their collectors, or users. Each single user will be able to have many cats in their collection, and this is what defines this as a one to many relationship: one user to many cats.

## Let's Get a User!

In `main_app/models.py`, let's include Django's built-in User model from their auth library:

```python
  from django.contrib.auth.models import User
```

We will use this `user` again later when we implement the ability to log in. This user will have an ID and we will use that to link the user to their cats. This means that we need to add the `user_id` to the `Cat` model so that we know which user each Cat belongs to. Because this is a key from another table, we call it a `foreign key` when we reference it from our `Cat` model. The foreign key in the `Cat` model connects to a user's ID which is the `primary key` in the `User` model. This connection of primary key to foreign key creates the relationship and because a cat can only ever have one collector it makes a `one to many` relationship.

```python
  # main_app/models.py (in Cat model)
  ...
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  ...
```

We should now run the `python3 manage.py makemigrations` command to integrate our foreign key. We will get a prompt from Django asking for one of two options. You should see something like this:

```text
You are trying to add a non-nullable field 'user' to a cat without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:
```

Let's choose option 1.

This will create a 'dummy' field of User that will be populated with null value row for us. We want this.

It will ask you one more time to enter a default value:

```bash
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
```

Go ahead and enter the number `1`. This will set a row to simply `1`. This will then trigger a migration file creation called `XXXX_cat_user.py`. Excellent!

Now run the migration by running

```bash
python3 manage.py migrate
```

Play with our Admin view and bask in the joy of being able to create Users and assigning Users to Cats! Make that assignment for all of your Cats.

Our cats are not being associated with users by default. Later when we implement authentication this will happen based on who is logged in. We can update our view function now, however, to make this complete.

Go to your `main_app/views.py` file and modify the `class CatCreate` view:

```python
# main_app/views.py
class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect('/cats')
```

Also make sure to add this line up at the top:

```python
from django.http import HttpResponseRedirect
```

Okay, what is this? We added a `form_valid()` function that will fire after Django validates the form. Inside this function we are saving the form _without committing it to the database_, we are adding the current user's ID onto that saved data, **then** we are saving it to the database, then we redirect to the cat list.

### Create the User Profile URL

All the model code is in place but we can't really see any of this outside of the admin interface, which is nice for us but isn't very useful for our users. We should add a route to view one user, like a user profile page.

This will repeat the same pattern of:

1. Set up a URL in `urls.py`
2. Create a view in `views.py`
3. Make an HTML template in `/templates`

Let's go to our `main_app/urls.py` folder and update our `urlpatterns`:

```python
# main_app/urls.py
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:cat_id>/', views.show, name='show'),
  path('post_url/', views.post_cat, name='post_cat'),
  # add the line below...
  path('user/<username>/', views.profile, name='profile'),
]
```

The stuff in the angle brackets lets us grab a passed-in username and store it in a variable called `username`. Lets add to our `main_app/views.py` file:

```python
# add this line to the imports
from django.contrib.auth.models import User

# add this new view function
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})
```

Lastly, we create a `profile.html` template to show a single User and all of the Cats they have collected:

```markup
{% extends 'base.html' %}
{% load staticfiles %}

{% block content %}

<h1>{{ username }}'s collection:</h1>

{% for cat in cats %}
<a href="/{{ cat.id }}">
  <h3>{{ cat.name }}</h3>
</a>

{% endfor %}

{% endblock %}
```

Let's also update our `cats/index.html` page to allow us to inspect each user:

```markup
<!-- main_app/templates/index.html -->
{% extends 'base.html' %}
{% load staticfiles %}

  {% block content %}
  {% for cat in cats %}
    <a href="/{{cat.id}}">
      <p>Name: {{ cat.name }}</p>
    </a>
    <a href="/user/{{cat.user.username}}"
      <p>Adopted By: {{cat.user.username }}</p>
    </a>
    {% if cat.age > 0 %}
      <p>Age: {{ cat.age }}</p>
    {% else %}
      <p>Age: Kitten</p>
    {% endif %}
    <hr />
  {% endfor %}
  <form action="post_url/" method="post">
      {% csrf_token %}
      {{ form.as_p }}
      <input type="submit" value="Submit" />
  </form>
{% endblock %}
```

