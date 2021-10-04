# Django Auth

## Django Authentication

### Learning Objectives

1. Explain what is meant by local session authentication
2. Add the Django User model to an app
3. Implement the common auth pages \(signup, login, logout, profile\)
4. Protect routes from unauthorized access

### Django Local Session Authentication

It's important to understand the flow of how a user is authenticated in a web app. There are many ways to do it and we will learn a few over the cohort. What Django uses is called `local session authentication`. The `local` part means that the authentication, \(the validation of a username and password\), happens in our own server. We store the password and we do the checking to see if it matches. The `session` part refers to how the server keeps track of who is logged in and what they have access to. The `session` is just another object stored in memory. Usually it only contains a user's ID but any additional information can be stored in the session object.

Django has a great pre-built authentication module that we can use but it is still good to understand what is happening:

#### Signing up a New User

One of the simpler views that we will write, basically all this does is check to see if a user credential \(like a user name\) is available and, if it is, it creates a new user record with an encrypted password and stores it in the database. This action typically also logs the new user in.

#### Logging In

Once a user is created, they are able to log in. This is done via a login form that is sent to the user. The user fills it out and it is sent to Django where the submitted password is checked against the one in the database. If it matches, a new session is created in the server. This session is the "proof" that a user has been authorized. Each time that user sends a new request to the server, it is sent with a session cookie that allows the server to look up that user's session. As long as the session cookie is present and neither it nor the session have reached their expiration date, the user should continue to have access.

#### Logging Out

This is as simple as deleting the session. We do this in Django through a simple `logout()` function. Once the session is gone, the user must create a new one and the only way to do that is by successfully logging in and having your credentials verified.

Though this may sound complicated, much of it is hidden from us by the power of the Django framework. Let's see how we put this together:

### Adding Users

In `main_app/models.py`, let's include Django's built-in User model from their auth library:

```python
  from django.contrib.auth.models import User
```

While we are adding in the User Model, we can actually add the relationship to the Cat model so each user can have their own Cat Collection! What fun! We saw how one-to-many relationships worked yesterday. We need to add a foreign key to the Cat and set it as the User. This establishes the 1:m relationship:

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

Now run the migration by running:

```bash
python3 manage.py migrate
```

The reason this happened is because we effectively added a column to our table that holds our Cats. We put a new attribute called `user` into the model and this created a column in the table with no data in it. Django was asking us what we wanted to put in there since a foreign key field usually isn't allowed to be blank. We told it to just use the number 1 which will link all of our cats to user number 1, which is probably your superuser account.

The one cool thing that we can see immediately is in our admin interface: We can now assign Cats a user value! Play with our Admin view and bask in the joy of being able to create Users and assigning Users to Cats! Go ahead and assign all of your Cats if you like.

Now go to your `main_app/views.py` file and lets update our view for the cats:

```python
# main_app/views.py
...
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/cats/' + str(self.object.pk))
...
```

In our `CatCreate` form, we need to change our list of fields to leave out the user's ID. Otherwise, we won't be able to submit the form. I've only listed the fields relevent to adding a new cat. Then we can use the `form_valid()` function to add in the user's ID pulled from the request object. This way, we always add the ID of the user currently logged in to this session.

### How do we login?

To implement a user login system, we'll follow the pattern of URL, Form, View, then Template.

In `main_app/urls.py` add the login route:

```python
...
path('login/', views.login_view, name="login")
...
```

In `main_app/forms.py`, add a login form below the others:

```python
class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())
```

Let's add the `login_view` function in `main_app/views.py`:

```python
...
# Add LoginForm to this line...
from .forms import CatForm, LoginForm
# ...and add the following line...
from django.contrib.auth import authenticate, login, logout
...
def login_view(request):
    if request.method == 'POST':
        # if post, then authenticate (user submitted username and password)
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user. is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print("The account has been disabled.")
            else:
                print("The username and/or password is incorrect.")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
```

Finally, we'll add a new file for the `login.html` template:

```markup
{% extends 'base.html' %}

{% block content %}
<h1>Login</h1>
<form method="POST" action=".">
  {% csrf_token %}
  {{ form.as_p}}
  <input type="submit" value="Submit" />
</form>

{% endblock %}
```

Go ahead and test out the login route! I hope you remembered one of your user's passwords...

## Log Out!

This will be a similar pattern of URL and view, but no form or template.

In `main_app/urls.py`:

```python
...
path('logout/', views.logout_view, name="logout"),
...
```

Create the corresponding `main_app/views.py` logout\_view function:

```python
...
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
...
```

Finally, let's add the log in and log out links to our site. Let's add it to our `base.html` since we want it to be accessible from every view. Add these lines under the link for "View All My Cats":

```markup
{% if user.is_authenticated %}
    <li> | </li>
    <li><a href="{% url 'profile' user.username %}">Hello, {{ user.username }}!</a></li>
    <li> | </li>
    <li><a href="{% url 'logout' %}">Logout</a></li>
{% else %}
    <li> | </li>
    <li><a href="{% url 'login' %}">Login</a></li>
    <li> | </li>
    <li><a href="{% url 'signup' %}">SignUp</a></li>
{% endif %}
```

Awesome! Now we have login and logout functionality and the ability to see if you're currently logged in!

### Signup

In `main_app/urls.py` add a signup url:

```python
path('signup/', views.signup, name='signup'),
```

In `main_app/views.py` add a signup view function:

```python
# add this line
from django.contrib.auth.forms import UserCreationForm

# add this function
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
```

In `templates` add a new file `signup.html`:

```markup
{% extends 'base.html' %}

{% block content %}
  <h2>Sign up</h2>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign up</button>
  </form>
{% endblock %}
```

### Protecting Routes

Now that we have nicely authenticated users accessing the site, we should look at limiting access to some of our routes. There are many different and complicated ways to do this in Django, but the easiest is probably to use `decorators`. These are statements that we put before functions or classes to change their characteristics. The `decorators` we will be using are `login_required` and `method_decorator`.

In `main_app/views.py` add this :

```python
# Import both decorators
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
...

# Above the class CatDelete, add this line
@method_decorator(login_required, name='dispatch')
class CatDelete(DeleteView):
...

# Above the profile function, add this line
@login_required
def profile(request, username):
...
```

Let's look at this code. We import both of the decorators and then we use the `@method_decorator` to protect our `generic editing view` for deleting cats. This is the one to use when protecting a class-based view. We tell the `method_decorator` what action we want \(`login_required` in this case\) and we also pass in the name of the method to protect \(the `dispatch` method.\) The `dispatch()` method is what sends the data from our class to the browser. It's normally hidden but by referring to it by name here we can effectively prevent our form from sending anything out if someone isn't logged in.

The `@login_required` decorator is what we use on plain view functions \(the kind that start with `def`\). It does basically the same thing - you must be logged in to view someone's profile.

Now deleting a cat and viewing a user's profile actually require you to **authenticate**! We have protected our cats!

### Seeing the user's cats

Now we need to add a view to see a User's profile. This will repeat the same, familiar pattern:

1. Set up a URL in `urls.py`
2. Create a view in `views.py`
3. Make an HTML template in `/templates`

Let's go to `main_app/urls.py` folder and update our `urlpatterns`:

```python
# main_app/urls.py
...
path('user/<username>/', views.profile, name='profile'),
...
```

The stuff in the angle brackets lets us grab a passed-in username and store it in a variable called `username`. Let's add to our `main_app/views.py` file:

```python
...
# add this line
from django.contrib.auth.models import User
...
# add this function
def profile(request, username):
    user = User.objects.get(username=username)
    cats = Cat.objects.filter(user=user)
    return render(request, 'profile.html', {'username': username, 'cats': cats})
```

Lastly, let's create a `profile.html` template to show a single User and all of the Cats they have collected:

```markup
{% extends 'base.html' %}

{% block content %}

<h1>{{ username }}'s collection:</h1>

{% for cat in cats %}
<a href="/{{ cat.id }}">
  <h3>{{ cat.name }}</h3>
</a>

{% endfor %}
{% endblock %}
```

Let's also update our `cats/index.html` page to allow us to inspect each user. Put this below the closing `<div>` in the card:

```markup
<!-- main_app/templates/index.html -->
<a href="/user/{{cat.user.username}}">
    <p>Adopted By: {{cat.user.username }}</p>
</a>
```

### Conclusion

That was the whirlwind tour of Django authentication. There is a lot more you could spend time learning about authentication but this takes care of what you will need to meet project requirements. Django makes the process very simple. When we get into authentication with Node/Express, you will get a deeper understanding of how authentication works and a new perspective from learning a new auth strategy: OAuth.

Authentication is incredibly important in web development. We make public-facing, data-aware products that can contain very sensitive information. Authentication helps us protect that information as well as protecting our server or clients from being used in larger cyber attacks. I urge you all to learn as much as you can about security.

### Further Reading

[Django Authentication System](https://docs.djangoproject.com/en/2.1/topics/auth/default/) [OWASP Top 10 Security Concerns](https://www.owasp.org/images/7/72/OWASP_Top_10-2017_%28en%29.pdf.pdf) [OWASP Session Management](https://www.owasp.org/index.php/Session_Management_Cheat_Sheet)

