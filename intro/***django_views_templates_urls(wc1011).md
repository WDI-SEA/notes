<img src="https://i.imgur.com/iohZqCp.png">

# Django URLs, Views, and Templates

## Learning Objectives

| Students Will Be Able To: |
|---|
| Describe the Django Request/Response Cycle |
| Start a new Django project and create an app |
| Use a URL configuration (URLconf) to define routes |
| Define basic View functions |
| Define a Django template |
| Use template inheritance (partial templates) |
| Include static files in a template |
| Render data in a template |

## Learning Django Game Plan

All lessons this week are 100% Django!

The lessons will add features, piece-by-piece, to a modern full-stack reference app named **CatCollector**.

Let me show you the final version we're going to build this week.

Then, after the lessons, you will use lab time to repeat what you saw in the lesson by building your own app named anything you want, say - **FinchCollector**.

Here's an overview of the high-level topics we'll be covering this week, in order:

1. Django URLs, Views, and Templates
2. Data Models and Migrations
3. One-to-Many Models & ModelForms
4. Many-to-Many Models
5. Django Authentication

Let's get on with part 1...

## Minimalist vs. Full-featured Frameworks

#### Review The Philosophy of Express

Express was a minimalist framework that didn't provide much functionality out of the box.

It gave us a way to define routes, map controller actions to those routes, and render dynamic views.

Express didn't have many rules, for example, we could name files anything and put them anywhere we wanted.

If we did need additional capability, it usually meant installing and configuring additional middleware.

#### The Philosophy of Django

Unlike Express, Django, is a full-featured web framework that provides a lot of built-in functionality.

However, Django has many _conventions_, i.e., it expects us to follow its rules.

You will find that Django has all sorts of _helper_ classes, methods, etc. 

What Express has to offer can be grasped in a matter of days, whereas Django could take weeks to feel comfortable with what it has to offer.

Luckily for us though, the basics aren't too bad though, as long as you don't try to learn every little detail about each helper, etc.

## The Request/Response Cycle in Django

In Unit 2, we learned that in a full-stack web application:

- Clicking links and submitting forms on the front-end (browser) sends HTTP requests to the web app running on a web server.
- The web server has a routing mechanism that matches HTTP requests to code.
- That code typically performs CRUD, then either:
	- Renders dynamic templates for Read data operations.
	- Redirects the browser in the case of Create, Update or Delete data operations. 

Once again, let's review this diagram that shows how a request flows through a Django project:

<img src="https://i.imgur.com/1fFg7lz.png">

## We Do: Start the **CatCollector** Project

Let's start by making a directory for our project:

```bash
$ mkdir catcollector
$ cd catcollector
```

#### Create the Environment

Let's also build a virtual environment. Virtual environments allow us to have virtual installation of python and
multiple versions of Python on the same system so we can have different versions
of both Python and the packages we are using on our computers.

We will use the `venv` module, bundled with Python v3.3 and higher, to create our virutal environment:

```bash
$ python3 -m venv .env
$ source .env/bin/activate
```

Let's also install some dependencies and save them. Django doesn't utilize a
`Gemfile` or a `package.json`. Instead, we just use a text file that lists all
of our dependencies. The `pip freeze` command saves the dependencies in our `virtualenv` to
that file.

```bash
$ pip3 install django
$ pip3 install psycopg2
$ pip3 freeze > requirements.txt
```
> You may need to also install `pip3 install psycopg2-binary`

> If you run into an error install psycopg `env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" pip3 install psycopg2`

Django is, of course, the framework we are using. `psycopg2` allows us to use
PostgreSQL within Django.

If you are downloading and running a Python project, you can usually install
its dependencies with `pip3 install -r requirements.txt`.

#### Create the Project

Let's go ahead and create our project. `django-admin` gives us commands to
generate some of our project for us.

```bash
$ django-admin startproject catcollector_project . # Do not forget the 'dot' at the end.
```

Take a minute to look at the generated files.

#### Create the App

A Django _project_ contains Django _apps_.

Django _apps_ represent major functionality in a project.

Realistically, however, we can think of the catcollector project as our web application.

Take a look at the `INSTALLED_APPS` list in **catcollector/settings.py**. Those pre-installed apps provide services such as the admin app and the ability to serve static files.

For catcollector, as well as for your project 3, you will need an app to implement the main functionality, in this case collecting cats 😊

It makes sense to name the main app generically, so let's do it:

```
$ python3 manage.py startapp main_app
```

You'll now find a **main_app** folder within the top-level project folder. That folder has been configured to be a Python module.

Let's include it as part of the catcollector project by adding it to the `INSTALLED_APPS` in **settings.py**:

```python
INSTALLED_APPS = [
	'main_app',
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
]
```

Let's check to make sure the project starts up:

```
$ python3 manage.py runserver
```

Ignore the red message about unapplied migrations, we'll take care of those in a bit.

Browse to `localhost:8000` and make sure you see the rocket on the page:

<img src="https://i.imgur.com/RozMgJ0.png">

#### Create the database

Databases are not automatically created by Django.

Let's use a command installed with PostgreSQL to create the database for the CatCollector project:

```
$ createdb catcollector
```

#### Connecting to the Database

Earlier we created a dedicated `catcollector` PostgreSQL database.

A Django project's configuration lives in **settings.py**. Let's update it to use our `catcollector` database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'catcollector',
    }
}
```

> Note: By default, Django uses SQLite, a lightweight database that is not recommended for deployment.  Be sure to make the above changes in your Django projects so that PostgreSQL is used instead.

Now let's test our database connection by getting rid of the red unapplied migration message:

```
$ python3 manage.py migrate
```

The `migrate` command is used to update the database schema over time as the application evolves - we will cover migrations in more detail this afternoon.

Nice.  Now let's code our first feature: a HOME page.

## Defining Routes - URLs

As you learned with Express, there needs to be a route defined that matches each HTTP request coming from the browser.

Also, we know that the purpose of a route is to map an HTTP request to code.

We also know that Django's routing system matches the URL (path) of the request **only** and ignores the HTTP method/verb.

For the HOME page functionality, we'll use the root route (`http://localhost:8000`) - let's see how...

#### One-time URL Setup

In Django, routes are defined within **URLconf** modules named **urls.py**.

There's an existing project **catcollector/urls.py** that we could add additional routes to, but it's a best practice for each Django app to define its own and **include** those URLs in the project's URLconf.

> FYI, There are some helpful comments at the top of **catcollector/urls.py**.

So, let's start by setting up **main_app**'s own **urls.py**:

1. Create the URLconf module:

	```
	$ touch main_app/urls.py
	```

2. Include it in the project's **catcollector/urls.py**

	```python
	from django.contrib import admin
	# Add the include function to the import
	from django.urls import path, include
	
	urlpatterns = [
	    path('admin/', admin.site.urls),
	    # In this case '' represents the root route
	    path('', include('main_app.urls')),
	]
	```
	Be sure to import the `include` function near the top.
	
	Each item in the `urlpatterns` list defines a URL-based route or, as in the case above, mounts the routes contained in other URLconf modules.
	
	Note that similar to how Express appends paths defined in a router module to the path in `app.use`, the paths defined in `'main_app.urls'` will be appended to the path specified in the `include` function.
	
	You can close **catcollector/urls.py** since all routes we define from this point forward will be defined within **main_app/urls.py**.

3. Now for the boilerplate needed in **main_app/urls.py**:

	```python
	from django.urls import path
	from . import views
	
	urlpatterns = [
	
	]
	```
	We've imported the `path` function that will be used to define each route.
	
	We've also created the required `urlpatterns` list that will hold each route we define for `main_app`.

#### Define `main_app`'s Home Page URL & View

With the setup done, we're ready to define the route to display the Home page.

In **main_app/urls.py**:

```python
urlpatterns = [
  path('', views.home, name='home'),
]
```

The above code defines a root path using an **empty string** and maps it to the `view.home` view function that does not exist yet - making the server unhappy.

The `name='home'` kwarg is optional but will come in handy for referencing the URL in other parts of the app, especially from within templates.

The Home page route has been defined!  On to the view...

## Defining View Functions

❓ **What is the equivalent to a Django View Function in Express?**

In the URL for the Home page we referenced a view function named `home`.

Let's define it where we will define all of the app's views, in **main_app/views.py**:

```python
from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')
```

> Note that in order to use the `HttpResponse` function, we must import it like the others we've used so far.

Just a baby step for now. What we've done is define a view function that responds to the browser's HTTP request by sending a string (that resembles a cat).

All view functions need to define a positional parameter to accept a _request_ object Django will be passing in.  This _request_ object is very much like the `req` object we worked with in Express controller actions.  As shown above, the parameter is typically named `request`.

The function `HttpResponse` is the simplest way to send something back in response to a request. It's like `res.send()` was in Express.

We will learn some more powerful ways to respond shortly when we start rendering templates.

Now when browsing to `localhost:8000`, we should see our welcoming cat instead of seeing the rocket page!

### Practice - Define another URL and View Function

Take 5 minutes to:

1. Define another route with a path of `about/`.  Define it **exactly** as shown (with a trailing slash instead of a leading slash).  This is the convention for Django.

2. Name the route `'about'`.

3. Map the route to a view named `views.about`.

4. Define the `about` view function referenced in step 3 so that it displays the following text:  `<h1>About the CatCollector</h1>`

Test it by browsing to `localhost:8000/about`:

<img src="https://i.imgur.com/K8jpo14.png">

## Using Django Templates

So, we just finished responding to requests by using `HttpResponse()` to send back a string of HTML (just like we did when using Express for the first time using `res.send()`).

Now let's move beyond the baby step by rendering a template instead.

Just like how Express can use different templating engines (Jade, EJS, etc.), so can Django.

Django has two templating engines built-in:

- Its own Django Template Language (DTL), and
- [Jinja2](http://jinja.pocoo.org/), a Python template engine, inspired by Django's DTL.

Not surprisingly, a Django project is pre-configured to use DTL, which is very capable, so we'll be using it throughout.

#### One-time Template Setup

By default, a Django project is configured to look for templates inside of a `templates` folder within each app's folder (`main_app` in this case).

Let's create that `templates` folder for `main_app` to hold all of its template files:

```
$ mkdir main_app/templates
```

#### Create an `about.html` Template

Let's start with a simple template for the About page:

1. Create the template:

	```
	touch main_app/templates/about.html
	```
	Note that Django templates have a simple `.html` file extension.


2. Open **about.html** and add the boilerplate (`! + tab`) and update the `<title>`:

	```html
	<!DOCTYPE html>
	<html lang="en">
	<head>
	  <meta charset="UTF-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1.0">
	  <meta http-equiv="X-UA-Compatible" content="ie=edge">
	  <title>Cat Collector</title>
	</head>
	<body>
	  
	</body>
	</html>
	```

3. Add a bit of custom markup within the `<body>`:

	```html
	<h1>About the Cat Collector</h1>
	<hr />
	<p>Hire the Cat Collector!</p>
	<footer>All Rights Reserved, &copy; 2019 Cat Collector</footer>
	```

4. Now update the `about` view in **views.py** to `render` the **about.html** template instead of sending a string response:

	```python
	# main_app/views.py
	from django.shortcuts import render
	
	...
	
	def about(request):
	  return render(request, 'about.html')
	```
	Much like Express' `res.render()`, except for the positional `request` arg. Also, the `.html` extension is required.
	

Browsing to `localhost:8000/about` will now render the new **about.html** template!

So far, so good, but we haven't yet used any of DTL's power to dynamically render data, perform control flow, etc.

Next, before we go any further and break the DRY principle by repeating the boilerplate in future templates, let's see how we can use what Django calls **template inheritance**.

## Template Inheritance (Partials)

Django has a [template inheritance](https://docs.djangoproject.com/en/2.1/ref/templates/language/#template-inheritance) feature built-in.

Template inheritance is like using partials in EJS with Express, except they're more flexible.

The reason Django calls it template _inheritance_ is because:

- You can declare that a template **extends** another template.
- Extending another template results in defined **blocks** _overriding_ (replacing) blocks defined in the template being extended.

<img src="https://i.imgur.com/ZajRcLx.jpg">

Here's how it works in practice. First let's create a **base.html** template (named by convention):

```
$ touch main_app/templates/base.html
```

This is the template that will hold all of the boilerplate and markup that belongs on every page, such as the `<head>`, navigation, even a footer if you wish.

This will be our sweet boilerplate for now:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Cat Collector</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">
</head>
<body>
  <header class="navbar-fixed">
    <nav>
      <div class="nav-wrapper">
        <ul>
          <li><a href="/" class="left brand-logo">&nbsp;&nbsp;CatCollector</a></li>
        </ul>
        <ul class="right">
          <li><a href="/about">About</a></li>
        </ul>
      </div>
    </nav>
  </header>
  <main class="container">
    {% block content %}
    {% endblock %}
  </main>
  <footer class="page-footer">
    <div class="right">All Rights Reserved, &copy; 2019 Cat Collector &nbsp;</div>
  </footer>
</body>
</html>
```

Note that we'll once again be using the [Materialize CSS Framework](https://materializecss.com/) for quick styling.

However, the most important part of the boilerplate in regards to template inheritance is:

```html
{% block content %}
{% endblock %}
```

Hey, that's our first look at DTL **template tags**, `block` & `endblock`, enclosed within the template tag delimiters `{% %}`.

Django [template tags](https://docs.djangoproject.com/en/2.1/ref/templates/builtins/#ref-templates-builtins-tags) control logic within a template.  Depending upon the tag, they may, or may not, result in content being emitted in the page. 

Whenever another template **extends** this **base.html**, that other template's `{% block content %}` will replace the same block in **base.html**.

To see template inheritance in action, let's update **about.html** so that it extends **base.html**:

```html
{% extends 'base.html' %}
{% block content %}

<h1>About the Cat Collector</h1>
<hr />
<p>Hire the Cat Collector!</p>

{% endblock %}
```

Refresh. Yeah, it's not great (yet), but the template inheritance is working and we can stay nice and DRY.

## Including Static Files in a Template

As you know, web apps usually have static files such as `.css`, `.js`, image files, etc.

If we want Cat Collector to look better, we're going to have to be able to define some custom CSS.

Django projects are pre-configured with a `'django.contrib.staticfiles'` app installed for the purpose of serving static files.

At the bottom of **settings.py**, there is a `STATIC_URL = '/static/'` variable that declares what folder within apps to look for static files in.

We need that, so let's create it:

```
$ mkdir main_app/static
```

Next, let's create a folder within `static` dedicated to CSS:

```
$ mkdir main_app/static/css
```

Now let's create a `style.css`:

```
$ touch main_app/static/css/style.css
```

For now, just to make sure that **style.css** is properly loaded, let's put in a touch of hideous CSS:

```css
body {
  background-color: red;
}
```

All we have to do is tweak **base.html** by first adding the `load` template tag at the top:

```html
{% load static %}

<!DOCTYPE html>
```

Finally, add this `<link>` below the Materialize CDN:

```html
<link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
```

The `static` DTL template tag ensures that the correct URL is assigned to the `href`.

Refresh - and red city tells us that **style.css** is being loaded.  Let's update it with the following more pleasing CSS:

```css
body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

main {
  flex: 1 0 auto;
}

footer {
  padding-top: 0;
  text-align: right;
}
```

That's better!

<img src="https://i.imgur.com/ChPjvKm.png">

## Render Data in a Template

To see how data is rendered dynamically using Django templating, we're going to implement the following user story:

_As a User, when I click the **View All My Cats** link, I want to see a page listing all of my cats._

#### Step 1 - Identify the "Proper" Route

First, let's be clear on the fact that Django's URL-based routing is **not** RESTful routing - **why is this the case?**

For this **index** page user story, what would have been the RESTful path works for Django's URL only routing as well: `cats/`

#### Step 2 - Create the UI

For the UI, it makes sense to add the **View All My Cats** link to the navigation bar in **base.html**:

```html
<li><a href="/about">About</a></li>
<!-- new markup below -->
<li><a href="/cats">View All My Cats</a></li>
```

**IMPORTANT: Be sure to continue to use leading slashes in the HTML!**

A quick refresh and we have our link:

<img src="https://i.imgur.com/4DZVGiI.png">

#### Step 3 - Define the Route

Now let's add the new route to **main_app/urls.py**:

```python
urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('cats/', views.cats_index, name='index'),
]
```

We only have a single **views.py**, so by naming the view `cat_index` we're anticipating that there might be another _index_ view for a different resource in the future (_toys_ maybe?).

Of course, by referencing a nonexistent view, the server's not happy.

#### Step 4 - Code the View (Controller Action)

When working in Django, we'll just have to get used to calling _controller actions_, **views** instead.

Let's type in the `cats_index` view inside of **views.py**:

```python
# Add new view
def cats_index(request):
  return render(request, 'cats/index.html', { 'cats': cats })
```

Two interesting things above:

1. We're namespacing the `index.html` template by putting it in a new `templates/cats` folder for organizational purposes - just like we did in Express.

2. Similar to how we passed data to a template in Express using a JS object, we pass a dictionary as a third positional argument in Django's `render` function.

Now for the cat data...

We're going to use a `Cat` class to simulate a Cat Model and use it to create some cats in a `cats` list:

```python
# Add the Cat class & list and view function below the imports
class Cat:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

cats = [
  Cat('Lolo', 'tabby', 'foul little demon', 3),
  Cat('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Cat('Raven', 'black tripod', '3 legged cat', 4)
]
```

> Note: Everything in a Python module is automatically exported, thus, the `Cat` class and the `cats` list will be accessable in other modules.

#### Step 5 - Respond to the Client's HTTP Request

We've already written the code to respond using the `render` method in the view.

However, we need to create the **cats/index.html** template we want to render.

First we need the `templates/cats` folder we'll use to organize cat related templates:

```
$ mkdir main_app/templates/cats
```

Now create the **cats/index.html** template file:

```
$ touch main_app/templates/cats/index.html
```

Now the fun stuff. We'll type it in if there's time, otherwise we'll copy/paste and review:

```html
{% extends 'base.html' %}
{% block content %}

<h1>Cat List</h1>

{% for cat in cats %}
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
{% endfor %}

{% endblock %}
```

There are two control flow template tag constructs you'll use quite a bit:

- The `{% for %}` / `{% endfor %}` block used to perform looping
- The `{% if %}` / `{% elif %} / {% else %} / {% endif %}` block used for branching.

> Important: Django template tags are designed to mimic very closely their Python counterparts, however, they are not embedding Python the way EJS embedded JavaScript.

For example, Python does not have `endfor` or `endif` as part of the language.

Next notice how double curly brace syntax `{{}}` is used to print the values of variables and object properties.

> Note: If the property on an object is a method, it is automatically invoked by the template engine without any arguments and we **do not** put parens after the method name.  For example, assuming a person object has a `getFullName` method, it would be used like this `{{ person.getFullName }}` in the template. This is another example of how DTL is its own language and not Python.

Some of you have probably already clicked the link and are understandably grinning:

<img src="https://i.imgur.com/Aak87k4.png">

## Summary

You now have a minimal but functional application that renders an **index** page that dynamically displays a hardcoded list of Cat objects.

You now know pretty much all there is to know about URLs and the overall structure of a Django app.

However, we've only touched upon the basics of views and DTL templating.

We're going to get our first look at Models in the next lesson where we'll use one to replace the current `Cat` class so that we can save cats in the database!

## Lab

The lab for this lesson is repeating everything we just did, except you'll collect something else like Finches and call the project something like finchcollector, or whatever.

The final version of your "Finch Collector" project will be a deliverable.

Because your completed Finch Collector app will be fairly comprehensive and be a nice addition to your portfolio, you should **create it outside of the class repo** so that you can make it a repo in your personal GitHub account.

## References

[Django Template Docs](https://docs.djangoproject.com/en/3.0/ref/templates/builtins/)

[Django Static Files](https://docs.djangoproject.com/en/3.0/howto/static-files/)
