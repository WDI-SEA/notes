# Django One-to-Many Relationships
Django makes it easy to attach different types of data to your models
that define what is saved in your database. It's easy to add integers,
floats, dates, datetimes, short text, long text and lots of stuff.

Oh, here's a link to all of the fields Django provides for models, and links
to their documentation on one-to-many and many-to-many relationships:

* <https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types>
* <https://docs.djangoproject.com/en/1.10/topics/db/models/#many-to-one-relationships>
* <https://docs.djangoproject.com/en/1.10/topics/db/models/#many-to-many-relationships>

Of course, Django also has ways to hook up one-to-many and many-to-many
relationships. Django establishes one-to-many relationships using a
`model.ForeignKey()` field.

You'll need to add a ForeignKey field to a model to set up the association,
then, after that's added, create and run some migrations.

Here's an example that shows how to model Arists, Albums and Songs and hook
them up to each other:

```python
from django.db import models

class Artist(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

class Album(models.Model):
  title = models.CharField(max_length=100)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return self.title

class Song(models.Model):
  title = models.CharField(max_length=100)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

  def __str__(self):
    return self.title
```

Now that these models are defined, have Python detect the changes and use
`manage.py` to create migrations and run them:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Now that relationships have been set up you can create models on the server
and save models as fields of other models. Let's practice creating relations
by firing up the Django shell. You'll need to import the models from your
app to have access to them in the shell.

```bash
python3 manage.py shell
```

```python
# import the application models.
from songs.models import *

# Create an artist, and make sure to save it.
# Other models can't refer to another model until it's saved and has an id.
weezer = Artist(name="Weezer")
weezer.save()

# Create an album with a reference to the artist that's been created.
pinkerton = Album(title="Pinkerton", artist=weezer)
pinkerton.save()

# Save a few songs that were on Pinkerton
song1 = Song(title="El Scorcho", album=pinkerton, artist=weezer)
song1.save()

song2 = Song(title="Getchoo", album=pinkerton, artist=weezer)
song2.save()

song3 = Song(title="No Other One", album=pinkerton, artist=weezer)
song3.save()
```

Run a query to grab all of the song objects and make sure they're
saved and retrieved properly. Use a for loop to iterate through
each of the songs and print out the songs title, the title of
the album, and the name of the artist:

```python
songs = Song.objects.all()
for song in songs:
  print(f'"{song.title}" on {song.album.title} by {song.artist.name}')
```

## Customizing Admin Panel

## User Associations
If you ever want to associate models to a specific user then you can import
Django's built-in User model and reference it as a ForeignKey just like any
other model.

Import Django's `User` model from their auth model module, then use that model
when you declare a ForeignKey field.

```python
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.text
```
