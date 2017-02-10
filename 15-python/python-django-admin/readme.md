# Django Admin Customization
Refer to this repo to see fully-implemented custom administrative interfaces:

<https://github.com/WDI-SEA/python-django-song-site>

Django generally creates a pretty good administrative interface. It
automatically reads the fields off models and creates forms for you
to edit your database on a professional-looking web-page.

Here's a look into how to customize Django Admin views. We're using techniques
described in the Django docs here:

<https://docs.djangoproject.com/en/1.10/intro/tutorial07/>

The repoo we're working with has models for Artists, Albums and Songs. The
models have one-to-many relationships set up between each other:

* each album refers to an artist
* each song refers to an album and an artist

If we go to the admin site the admin panel doesn't automatically show
all the songs on an album when we view an album. We have to manually
configure the admin panel to display this relationship.

# Show All Songs On An Album
Here's a simple example of how to display all the songs associated with
an album when you look at an album in an Admin interface. Basically,
you have to define how a Song is displayed when it's displayed "inline"
in another template. And, you have to tell the Album that it displays
Songs in it's template.

Django comes with lots of `ModelAdmin` classes that define how models
are shown in the Admin interface. By default a ModelAdmin class basically
iterates through the fields on a model and creates inputs and forms
that appear on a webpage to let users edit the values.

Django has a special sub-class of ModelAdmin called `InlineModelAdmin`.
An InlineModelAdmin gives us the ability to edit models on the same page
as a parent model. So, we can edit songs on their parent Album model.

There's two subclasses of InlineModelAdmin: `TabularInline` and
`StackedInline`.

* [ModelAdmin documentation](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#modeladmin-objects>)
* [InlineModelAdmin documentation](https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#inlinemodeladmin-objects

TabularInline is more compact. TabularInline displays all of the
properties of an inlined model in one row across columns. Songs
for an album would be displayed something like this:

```
Album: Pinkerton
Songs:
El Scorcho     4:04
Why Bother?    2:08
The Good Life  4:17
```

StackedInline iterates through the properties of an inlined model
and stacks them all on top of each other. Songs for an album would 
look something like this:

```
Album: Pinkerton
Songs:
El Scorcho
4:04

Why Bother?
2:08

The Good Life
4:17
```

## Tie It All Together
Here's an example of how you create an Inline interface for a Song. You
make a class called `SongInline`, have the class inherit `TabularInline`
and set a property `model = Song` inside the class.

Then, Create a custom Admin interface for Album. Create a class called
`AlbumAdmin` and have it extend `admin.ModelAdmin`. Create a variable
inside the class called `inlines` and set it equal to an array containing
all of it's inlined associations.

Finally, register the `Album` model with it's custom `AlbumAdmin` interface
and register the `Song` model and allow it to get a default Admin
interface.

Take a look!

```python
from django.contrib import admin
from .models import Artist, Album, Song

class SongInline(admin.TabularInline):
  model = Song

class AlbumAdmin(admin.ModelAdmin):
  inlines = [SongInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Song)
```


