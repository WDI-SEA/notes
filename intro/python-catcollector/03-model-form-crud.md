# Model Form CRUD

In today's lesson we will be seeing how Django provides powerful forms that we can use to enable any CRUD operation on our data quickly and easily. These are sort of Django's alternative to providing 100% proper RESTful routing support but it does end up saving us a lot of time even if the naming conventions aren't quite RESTful.

## Learning Objectives \(Students will be able to...\)

1. Add generic editing views for CREATE, UPDATE and DELETE operations.
2. Use the `form_valid()` function for accessing request details.
3. Create forms and URLs for the editing views

## Model CRUD in Django

In more minimalist frameworks, the duty of creating proper RESTful routes and forms for all operations on every resource in our app falls on us - the developers. But larger frameworks like Django or Rails often provide a quick way to cut through all the boilerplate and let us just deliver a form that is already made for creating or updating our data. Django's solution is `ModelForms` and `generic editing views` which are classes that we can use to make a form that is already connected to our models and allows the easiest possible editing of our data.

We have already worked two READ operations into our app: `read all` and `read one`. Now let's add in the ability to `create` cats, `update` cats, and `delete` cats.

## Creating, Modifying, Deleting Cats

In order for any creation or modification of a data object to be possible via the web, we need to follow a process:

1. The browser must be sent a page with a form on it.
2. The form must be filled out and submitted by the user.
3. The form data is then returned to the server via a POST request.
4. The server reads the form data, validates it, and writes it to the table.

This is a fairly complicated process to get right when we do it ourselves but Django handles most of this internally in the form classes it provides us.

Open your `main_app/views.py` file and we will add the following code:

```python
# add these lines to the imports at the top
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect

class CatCreate(CreateView):
  model = Cat
  fields = '__all__'
  success_url = '/cats'

class CatUpdate(UpdateView):
  model = Cat
  fields = ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.save()
    return HttpResponseRedirect('/cats/' + str(self.object.pk))

class CatDelete(DeleteView):
  model = Cat
  success_url = '/cats'
```

By using these generic editing forms and linking them to our `Cat` model, Django will automatically create forms with all the correct fields to represent our model and will keep track of which form is being used so it know which operation is being performed.

Let's examine these. Each is a `class` that inherits from some kind of `View` class. There is one for creating, one for updating, and one for deleting. With each class, we must include a variable `model` that will determine how the form will be built and what data it should attach to. For the `create` and `update` forms, you must tell it which fields need to be mapped to the form. You can simply say `__all__` for having every field show up, like in `create`, or you can pass in a list of fields to include, as we have done for `update`. Lastly, all editing form classes need to have a `success_url` or a redirect configured which is where the browser is sent after the create or update operation. For `create` and `delete` we can simply redirect back to the collection index. But for the `update` we need a little more control. Typically after a data update operation, we redirect back to the details for the data object that we just modified. We must pass the Cat's ID into the redirect URL to make this happen, so we must use a built-in but optional function in the class called `form_valid()`. This function is a kind of hook that is executed after the form data is validate but before it is written to the database. We use it because it is the only way to access the Cat's primary key which was passed in as part of the original request. It's stored in `self.object.pk` but we don't have access to that unless we use the `form_valid()` function. So we use that function, save the form data into `self.object`, call `self.object.save()` to write the update to the database, then we redirect using `HttpResponseRedirect` and tell it to go to the path for listing this specific Cat's details. We just need to access the `pk` member and turn it into a string.

That takes care of all the View code, but each of these views need a form template to be made. The `delete` operation needs a special form that asks if the user is sure they want to delete something. The `create` and `update` operations can share one form. Let's create some templates! Inside `templates` these forms are expected to be in a folder with the same name as our app so let's create a `main_app` folder. Inside there, make a `cat_form.html` file and give it these contents:

```markup
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

There is a lot of Django template syntax in here so let's go over it. We are still putting our relevant content inside the \`

`section. Inside there we see an HTMLelement with some things inside it. The`

`is a security measure that makes it more difficult to forge illegal requests against our server. It is called a Cross-Site Request Forgery token. Django generates it for every potential form submission and the form must return it to Django in order to be accepted. All we must do is include that line and everything works! Then we have an HTMLwith some Django syntax inside it. We add in`\` which creates a table for us and generates the form fields inside that table. The last thing we add is a "submit" button.

This form will be used for both `creating` and `updating`. The `delete` operation wants another file present. It will be used to confirm the deletion, basically asking the user if they are sure about what they are doing. In the same directory, create `cat_confirm_delete.html` and fill it thusly:

```markup
{% extends 'base.html' %}

{% block content %}
  <h1>Delete Cat</h1>

  <p>Are you sure you want to delete this cat: {{ cat }}?</p>

  <form action="" method="POST">
    {% csrf_token %}
    <input type="submit" value="Yes, delete.">
  </form>
{% endblock %}
```

Here we see a much more simple form. This is a Django convention. Every time we use these `generic editing views` we need to provide Django with everything it expects, and this is one of the things it expects - a confirmation form for the delete operation. But this is all we need to provide. Django takes care of when to show these forms for us.

Now on to the URLs. Open up `main_app/urls.py` and add these views to the `urlpatterns`:

```python
path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
```

We can see some routes here that use Django's syntax for variable in URLs. But in this case, we cannot choose what we name them. They must always be type `int` and be named `pk`. This stands for `primary key` and it is the variable name that Django expects the Cat ID to be in. This is another Django convention that we must accept. The only other parameter of note is the one that links the URL to the view. Basically, it is saying to look in the `views.py` file, find the relevant form class in there, then use it as the view function for this URL.

But now we are done! These are our data access URLs. Whenever we want to add a new Cat, we can hit `http://localhost:8000/cats/create` and Django will send us a form with all the fields in it for adding a new Cat to the database. When we fill out the form and submit it, Django will receive the data, validate it, and write it to the database if it passes validation. The same stuff happens if we want to modify a Cat: we hit the URL `http://localhost:8000/cats/3/update`, passing in whichever Cat's ID we want to use. Then a form with that Cat's data is sent to us so we can edit the values. Then we submit that back to the server where it is validated and stored. The form classes that we used make all this happen automatically.

## Testing it all in the browser

With these changes in place we should be able to run the server and test all these routes. Make sure of the following:

1. Your server runs.
2. All previously working routes still work.
3. Your new `CREATE` route adds a Cat that you can see in the collection index.
4. Your new `UPDATE` route takes existing Cat data, let's you change it, and submits visible changes back to the database.
5. Your new `DELETE` route entirely removes a Cat from both the database and the Cats collection index page.

## Making it more user friendly

Sure, we can type full URLs into our address bar but no user should be expected to do that. We should make nice navigation links in our pages so people can get around easily. The obvious question is: where should these `create`, `update`, and `delete` links for our Cats go? Certainly there are intuitive places we can place the links so let's talk about that for a moment.

### Create

When we create a new Cat, it really has nothing to do with any other Cat in the database so it doesn't make sense to have our `New Cat` link appearing in any of the data sections for the other Cats. Instead, having a single place to add a new Cat somewhere on the collection index page makes the most sense. Let's add a single link to "Add a new cat" to our cat collection index page above our Cat list:

```markup
  <!-- templates/cats/index.html -->
  ...
  <h1>Cat List</h1>
  <!-- After the header, add this line -->
  <a href="/cats/create">Add a New Cat!</a>
```

Now on the page where Django loops through all of our Cats and renders them all into the page, at the top will be a link for adding a new Cat. Clicking it will send the user a form for adding a new Cat.

### Update & Delete

The `Update` and `Delete` operations work on only one Cat at a time so these make more sense to have as part of each Cat's data section on the collection index. However, these are both `destructive` database operations, which means that they have the capability of changing or removing data in an irreversible way. As a result, we usually add a little bit more exclusivity to these operations because we don't want anyone doing them by accident. Instead of having them on the main Cats index page, let's put them into the `show/details` page for each Cat so you must view a Cat's details in order to have the links for updating and deleting that Cat to appear.

```markup
<!-- templates/cats/detail.html -->
<div class="card-content">
    <span class="card-title">{{ cat.name }}</span>
    <p>Breed: {{ cat.breed }}</p>
    <p>Description: {{ cat.description }}</p>
    {% if cat.age > 0 %}
        <p>Age: {{ cat.age }}</p>
    {% else %}
        <p>Age: Kitten</p>
    {% endif %}

    <!-- Add links for update and delete here... -->
    <a href="{% url 'cats_update' cat.id %}">Update Details</a> | 
    <a href="{% url 'cats_delete' cat.id %}">DELETE This Cat</a>
</div>
```

Remember this syntax? We can use the Django template syntax for referring to a named URL. These new links will appear at the bottom of each Cat's detail card and take advantage of data that was passed into the page originally: the Cat ID. When we pass in a Cat object that we got from the database, it will include an `id` field and we use that when we make the links to edit or delete that Cat. Whatever the Cat's ID is, we use it in the link for editing that Cat. This makes sure we only ever edit or delete the Cat whose details we are currently viewing.

## Conclusion

Though Django doesn't use fully RESTful URL paths or routes, it does provide some built-in classes that perform the specific CRUD operations on our Models, saving us a bunch of time writing and testing. By using these `generic editing views` we can enable specific CRUD operations for any of our models. We must provide the model that the forms act on, specify which fields to include on the form, and tell Django where to redirect after the operation but once we do all of this we can sit back and relax. Django will take care of all sending, validating, and saving the data of the forms.

