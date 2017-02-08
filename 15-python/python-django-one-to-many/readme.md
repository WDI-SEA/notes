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

class Album(models.Model):
  title = models.CharField(max_length=100)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Song(models.Model):
  title = models.CharField(max_length=100)
  album = models.ForeignKey(Album, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
```

Now that these models are defined, have Python detect the changes and use
`manage.py` to create migrations and run them:

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Now that relationships have been set up you can create models on the server
and save models as fields of other models:

```python
weezer = Artist()
weezer.name = "Weezer"
weezer.save()

album = Album()
album.title = "Pinkerton"
album.artist = weezer
album.save()

song = Song()
song.title = "El Scorcho"
song.artist = weezer
song.album = album
song.save()
```

## User Associations
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
