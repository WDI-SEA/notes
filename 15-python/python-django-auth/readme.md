# Django Authentication
One benefit of using Django is it comes with built-in, easy-to-use
user models and authentication. Django comes with pre-defined models of what a
user is, and comes with ways to create users.

Let's see it all in action:

## The User Model
The primary attributes of Django's built-in user model are:

* username
* password
* email
* first_name
* last_name

Django comes with a built-in `create_user()` function that can be imported
and used through your application

Here's how the User model works in action:

```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user(username='john', password='secret')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
>>> user.first_name = 'John'
>>> user.last_name = 'Lennon'
>>> user.email = 'johnlennon@beatlesreuniontour.net'
>>> user.save()
```

## The Auth Module
Django has a built in auth module that builds off the User model, and uses
session and middleware to keep track of users while they move through the site.
You'll have to import the auth module, then you have access to these handy
methods:

* `user = auth.authenticate(username, password)` - checks whether a password
  matches what's stored with a username. Returns an instance of a User model
  if it matches.
* `auth.login(request, user)` - This method takes a `user` instance returned
  from the `auth.authenticate()` function and attaches user information to
  the servers session and middleware.  This is what keeps users logged in.
  You can reference user information all over the place off `request.user`
  after using this to log a user in.
* `auth.logout()` - This un-attaches user information from the server session
  and middleware. `request.user` won't be available anymore.

Now, creating users in your application is as simple as creating an HTML form
to gather user information, and creating a route that accepts the form's POST
request, picks out the user information and calls the `create_user()` method.

Django also comes with an easy way to authenticate users. Running the
`auth.authenticate(username='john', password='secret')` function providing
a username and a password will return an instance of a user model.

```python
from django.contrib import auth

user = auth.authenticate(username='john', password='secret')
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

Finally, Django provides an easy way to remember that a user is actually logged
in. Import the `login` function from Django's auth library.

The `login(request, user)` function will attach user information to the request
so that they remain authenticated and logged in through an application.

Django uses it's own **session** information and **middleware** to keep track of
users that have been logged in via the `login()` function. We should be familiar
with **session** and **middleware** from our experience with other web servers,
like Express.

```python
from django.contrib import auth

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
```

## Server vs Client
Notice that everything we've seen here is happening on the server. We're
just grabbing all of the user information from a POST request. The POST
request is probably coming from a form, or an AJAX request. It doesn't
matter.

As with all web development frameworks, if you can get text from the client to
the server then you're golden!

## Summary
**python-django-todo/todoapp/urls.py**:
```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
]
```

**python-django-todo/todoapp/views.py**:
```python
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'todoapp/signup.html', context)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.create_user(username=username, password=password)
            if user is not None:
                # run the login method to automatically log in user
                # as they sign up.
                return login(request)
        except:
            context["error"] = f"Username '{username}' already exists."
            return render(request, 'todoapp/signup.html', context)
    
def login(request):
    context = {"error": False}
    if request.method == "GET":
        return render(request, 'todoapp/login.html')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
            
def logout(request):
    auth.logout(request)
    return redirect('index')
```

**python-django-todo/todoapp/templates/todoapp/signup.html**:
```html
{% extends 'todoapp/base.html' %}

{% block content %}
  {% if error %}
    <div class="alert alert-warning">
      <strong>Error!</strong> {{error}}
    </div>
  {% endif %}

  <h1>Sign Up</h1>
  <form action="/signup" method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="username"/>
    <input type="password" name="password" placeholder="password"/>
    <input type="submit" value="Sign Up"/>
  </form>
{% endblock %}
```

**python-django-todo/todoapp/templates/todoapp/login.html**:
```html
{% extends 'todoapp/base.html' %}

{% block content %}
<h1>Login</h1>
<form action="/login" method="POST">
  {% csrf_token %}
  <input type="text" name="username" placeholder="username"/>
  <input type="password" name="password" placeholder="password"/>
  <input type="submit" value="Login"/>
</form>
{% endblock %}
```


**python-django-todo/todoapp/templates/todoapp/signup.html**:
```html
{% extends 'todoapp/base.html' %}

{% block content %}
  {% if error %}
    <div class="alert alert-warning">
      <strong>Error!</strong> {{error}}
    </div>
  {% endif %}

  <h1>Sign Up</h1>
  <form action="/signup" method="POST">
    {% csrf_token %}
    <input type="text" name="username" placeholder="username"/>
    <input type="password" name="password" placeholder="password"/>
    <input type="submit" value="Sign Up"/>
  </form>
{% endblock %}
```
