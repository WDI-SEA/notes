# Django URLs, Views, and Templates

We will be working on a full-stack app in Django all week, adding to it piece by piece as we learn how to implement the common features found in modern web applications. The seven parts break down as follows:

1. Django URLs, Views, and Templates
2. Data Models and Migrations
3. Django Model Forms and CRUD Operations
4. One-to-Many (1:m) Data Relationships
5. Many-to-Many (m:m) Data Relationships
6. Cloud Image Storage with AWS
7. Django Authentication

In this first part, we will look at adding routes to our controller that allow us to serve different pages. We will also see the beginnings of the Django Templating Language that will allow us to dynamically create pages using a combination of HTML and Python and send them to the client.

Let's dive in!

## Creating URLs

Just like in Express, and other web server frameworks, Django gives us the ability to define specific routes that represent the URLs in our web app. While Express calls these *routes*, Django refers to them as *urls*.

1. From your terminal window, navigate to your `code\unit4\` directory and create a new Django project with the following command:

	```bash
	django-admin startproject catcollector
	```

	This will create a folder named `catcollector` as well as a few support files and a folder within with the same name. Let's look at some of the key files:

	- settings.py will hold the settings for our project. Things like our database connection info and other Python modules that we want to use go in here.
	- urls.py is the main routing file for our project.
	- manage.py gives us access to common functions we'll perform on our app (running the server, applying migrations, etc.)

2.  To see the barebones website that Django made for us, run the following command:

	```bash
	python3 manage.py runserver
	```

	This will throw some migration errors which we can ignore for now. Head to the location given in your terminal and you should see a boilerplate greeting page for Django!

3.  We have created a Django project but a project is not really an application. It is more of a way to organize one or many related smaller apps. In Django, we create a project and then we create our primary app inside it. Let's do that now with the manage.py utility `startapp` to create our first app inside our Django project:

	```bash
	django-admin startapp main_app
	```

	This will create a folder for `main_app` with many support files inside. Let's review some of the main ones:
	- models.py is where we define all of our data models. We will see that this afternoon.
	- views.py is where we write the logic that happens when someone requests one of our URLs.

  We need to make sure we add this new app to our Django project. It doesn't happen automatically. In  `catcollector/catcollector/settings.py` include our 'main_app':

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

4.  We will now work on our first view. A view is a function that takes in a web request and returns a web response. Together with the URL patterns we define in our `urls.py` file, these make up the `Controller` portion of the Model-View-Controller design pattern. Django's use the the term "view" to describe controller actions is actually at odds with the rest of the MVC framework world. Only in Django does the word "view" refer to router functions. Everywhere else, the `View` portion of MVC refers to the front-end, or what the client sees. But in Django, when we write a view function, we are basically writing how our server will respond when a client requests a specific resource. **In Express, the URL and the route function are usually referred to collectively as the route. However, we have seen that it is possible to separate these out in Express. This is exactly what Django is doing: separating the declaration of the URL from the function that runs when the URL is requested.**

	```python
    # main_app/views.py
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
      return HttpResponse('<h1>Hello World! /ᐠ｡‸｡ᐟ\ﾉ</h1>')
	```

    What we've done is add a function that sends a simple string of an ASCII cat waving in response to the request from the client. The function `HttpResponse` is the simplest way to send something back in response to a request. We will learn some more powerful ways shortly. In order to use `HttpResponse`, we must import it into the file so we also added that line at the top under the import for `render`.

5.  Now we will map this particular view to a URL. We do this by adding a URL that will call this function. We will use the route `/index` for now as an example. You will need to create a `urls.py` file inside `main_app` and we'll declare our URLs for this app in there. We will also import our view functions from the `views.py` file in `main_app`:

	```python
    # main_app/urls.py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
	```

	Let's look at this line by line: First we import the `path` function which is the main function we use to create a URL in Django. Then we import the view we just made. That line says to import all of the views from the current module, which is our `main_app`. Then we define a `urlpatterns` list and add a `path()` call to it. In the `path()` function, the first argument is the relative path for the URL from the root of the server. The second argument is the specific path to the view function we want to associate with our route. The `name` parameter provides an identifier we can use in other parts of Django to refer to this URL.

6. With this route created, we can include it into our project. There are two `urls.py` files in Django: one for the project, and one for our app. Actually, if we create more than one app (which we won't do in this class) then all of them could have URLs that would be imported into the project. Here's how we do that:

```python
  # catcollector/catcollector/urls.py

  # add include to the line below...
  from django.urls import path, include
  from django.contrib import admin

  urlpatterns = [
    path('admin/', admin.site.urls),
    # Add the line below...
    path('', include('main_app.urls'))
  ]
```

This is how we write the root route in Django: with an empty string: `''` Now head to the `/` root route and you should see our greeting! Django is nice enough to restart its development server each time it detects that we save a source file so all you need to do is refresh your browser page to see the new index.

So we added a URL! Well, we kinda already had the URL responding but we changed what it did. We pointed the root URL to our own view function and by doing that we cn control exactly what is sent back to the browser.

# Add Another Route

Now that we've made this route, we can reflect on the process we followed and use it to make another route. The thing to keep in mind when making new routes is that you need to do three things. The first two are:

1. Add a URL pattern to your application's `urls.py` file.
2. Add a view function that the URL will call in your application's `views.py` file.

(These can really be done in either order. Netiher one will work without the other so both must be complete for anything to happen.) The third step is to add a template page that the route will render and send to the client. Before we get into that step for our routes, though, let's add another route to practice the process:

We already have our project importing our `main_app` URLs into the main URL dispatcher so we can focus entirely on adding routes to `main_app/urls.py`.

1. Open the `main_app/urls.py` file and add another URL pattern:

  ```python
  ...
  urlpatterns = [
    path('', views.index, name='index'),
    # Add this line below...
    path('about/', views.about, name='about')
  ]
  ```
  We'll make an "about" URL that can show some info about the author, you web developer you!

2. Open the `main_app/views.py` file and create a new view function:

  ```python
  def about(request):
    return HttpResponse('<h1>I am Steve the developer</h1>')
  ```

  When someone requests the `about` URL then we will send them a message saying who I am.

# Using Django Templates

This is all well and good, but we very rarely ever just send a simple string as the reponse to an HTTP request. Normally, entire pages of content are served up in response. Django, like many other web frameworks, allows the use of a templating engine. When we make a page using a template engine, we actually use code on the back-end to determine what the file will contain. Perhaps we want a header and a footer on all pages but what appears in the main content area between them will be determined by some Python code, and can change each time the page is built and sent! This is super-exciting because it gives us a new level of control over the content in our pages. The only thing we need to do is learn a few bits of syntax that make the templates work.

**This is, of course, Django's version of EJS or JSX. It functions a bit more like EJS in that the template code is parsed and removed before the final resulting page is sent.

Let's start with a simple template for our "about" page.

1. Create a `templates` directory within the `main_app` directory.

2. Create an `about.html` file inside your `templates` folder and fill it with some basic html:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>About the catcollector...</title>
  </head>
  <body>
    <h1>About the catcollector...</h1>
    <hr />
    <p>Hire the catcollector!</p>
    <footer>All Rights Reserved, catcollector 2018</footer>
  </body>
</html>
```

3. In our `views.py` we will now be **rendering** our template instead of sending HTTP responses, so so we can update our `views.py` to comment out the import of `HttpResponse`.

4. Finally, in our index function in our `views.py` file, lets update the render to show our about.html:

```python
# main_app/views.py
from django.shortcuts import render

...

def about(request):
  return render(request, 'about.html')
```
Our render function isn't doing very much here. We haven't added any code in our HTML that requires any rendering. But the render function is able to send out a plain HTML file even if it has no templating code inside it. Not all of our pages will need dynamic content and we can use this function in either case.

You can think of this function as doing the same thing as `HttpResponse` in the end because they both end up delivering a string of code to the browser. However, when we use `render` we can control data that gets injected into the file and then the whole file will be sent out as a long string to the browser.

With that in place, we can move on to the `index.html` and follow roughly the same procedure.

1. Create an `index.html` file inside your `templates` folder and fill it with some basic HTML but be sure to include a link that points to `/cats`:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>catcollector</title>
  </head>
  <body>
    <h1>catcollector</h1>
    <hr />
    <a href="/cats">View All My Cats!</a>
    <footer>All Rights Reserved, catcollector 2018</footer>
  </body>
</html>
```

2. Update the view function for index:

```python
def index(request):
  return render(request, 'index.html')
```

Now we have two rather plain pages that don't do much on our site. However, the index page links to `/cats` which is what we will work on next. We haven't hooked up a database yet but we can simulate some data by creating a class and some objects of that class and pretending that they have been returned to us from a database query. With some mock data to play with, we can actually see how we insert it into a template.

1.  In `views.py` lets create a Cat class with all of the attributes we want to see displayed on our index page. We can also create an array of Cat objects to act as our dataset. Add this code to the bottom of the file:

	```python
    # main_app/views.py
    
    ...
    
    class Cat:
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

Now, recall: What are the steps in making a new route?

### Create the URL for the route.

We will be making a route to show all cats. If we are following RESTful naming conventions then we need all Cat-related URLs to begin with `/cats`. Also recall that if we want to GET ALL CATS then we make an HTTP GET request to the URL that is the name of the collection: `/cats`. If we want to GET ONE CAT then we make an HTTP GET request to the URL of the collection plus an ID: `/cats/123`.

So open your `main_app/urls.py` file and add the following line to the `urlpatterns`:

```python
path('cats/', views.cats_index, name='cats_index'),
```

### Write a view function for the URL.

This view function will be a little different. We will need to pass some data in that our page will render. Add a third argument to your `render()` function. It is a dictionary and we are including a key named `'cats'` that has a value of the cats list that we just put into the views:

```python
# main_app/views.py
...
def cats_index(request):
    return render(request, 'cats/index.html', {'cats': cats})
```

This **third** argument is the actual data we want to display! Now we can make an `index.html` template.

### Write the HTML template.

Make a directory in your `templates` directory called `cats`. Create an `index.html` file inside your `cats` folder and fill it with some basic html:

```html
<!-- templates/cats/index.html -->
<!DOCTYPE html>
<html>
  <head>
    <title>catcollector</title>
  </head>
  <body>
    <h1>the catcollector's cats</h1>
    <hr />

    <footer>All Rights Reserved, catcollector 2018</footer>
  </body>
</html>
```

In this file we will use specific Django templating language to iterate and display our data in `cats`. Add this code under the `<hr />`:

```html
  {% for cat in cats %}
    <p>Name: {{ cat.name }}</p>
    <p>Age: {{ cat.age }}</p>
    <hr />
  {% endfor %}
```

Here we see the brackets and percent symbols that delimit our Python template code. We made a `for-loop` - the top line is `{% for cat in cats %}` and the bottom line is `{% endfor %}`. We cannot write an actual Python for-loop in a Django template so we use these Django template delimiters to achieve the same result. We iterate over each `cat` in the `cats` collection and put the values of its name and age into p tags in our page. To do this, we wrap the variable in double curly braces: `{{ }}` Check out our index file on your browser and you should see our cats displayed on the screen!

Let's rafactor this and add some conditional expressions to change the way our page renders based on data. If a cat has an age of 0, let's set it to display 'Kitten'. Update the code you just added with the following:

```html
  {% for cat in cats %}
    <p>Name: {{ cat.name }}</p>
    {% if cat.age > 0 %}
      <p>Age: {{ cat.age }}</p>
    {% else %}
      <p>Age: Kitten</p>
    {% endif %}
      <hr />
  {% endfor %}
```

We can see how conditionals work in Django templates. We begin an `if` statement with this line:

```python
{% if cat.age > 0 %}
```

We add an `else` with this line:

```python
{% else %}
```

And we close it off with this line:

```python
{% endif %}
```

These are just the basics of templating but now that we know how to loop, branch, and evaluate variables in our pages, we have a staggering amount of control over what is and isn't in our page and how it all looks. All of this template code is evaluated before the page is returned to the client so they will never see it. Django just reads our template code, decides what needs to go in the page based on the logic we write, and then replaces all the template code with the appropriate HTML. It's like having someone that will rewrite our pages for us based on any data we like.

## Django staticfiles

We should spruce up the look and feel of our app with some style! This templating is cool but how do we add our CSS to it? We need to utilize Django's static asset pipeline. Templates may look a lot like HTML but they go through a processor and sometimes we just want Django to leave our files alone. When we have a file that won't change all the time, like an image or stylesheet, typically a web framework gives us a special place to store these and a way to access them when needed. Django has a special directive we can use in our templates called `staticfiles`.

First, we need to understand that Django expects us to put these files in a very specific place. In fact, if we don't put them where Django wants, none of it will work. And we cannot tell Django to look in a different place. So do the following and don't change any of it:

1. Create a `static` directory in the `main_app` directory. This will house all of our static files.
2. Create a `style.css` file within the `static` folder.
3. Inside your `style.css`, create a simple property for an h1 tag to check to see if our style is loaded in our HTML file:

	```css
	h1 {
	  color: turquoise;
	}
	```

4. In our index.html we need to load our static folder and files with our templating language. We do so by declaring our usage of static files at the top of the page. We'll also show you how to link your style.css file as well:

```html
  <!-- Add the following line... -->
  {% load staticfiles %}
  <!DOCTYPE html>
  <html>
    <head>
      <title>catcollector</title>
      <!-- Add the following line... -->
      <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
    </head>
  ...
```

When we link in our stylesheet, we set the href like above. Using the `static` keyword basically says, "Look in the staticfiles folder for a file called style.css". We can do the same with images or JavaScript files.

5. We can also add in a CSS framework like Materialize in the normal way:

	```html
	{% load staticfiles %}
	<!DOCTYPE html>
	<html>
	  <head>
	    <title>catcollector</title>
	    <link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">
	    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.css">
	  </head>
	...
	```

You should now have a boring but completely functional application that will pull data from a hardcoded array of Cat objects and display it on your index view. Congrats! What fun!

