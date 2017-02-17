# Django Cheatsheet
As much as Python and Django strive to be readable and strive to configure
things "explicitly" rather than "implicitly" there's still a lot of code
we have to remember out of thing air. This cheatsheet aims to help you there.

We try to put good stuff in this cheatsheet but it doesn't have everything!
Refer to this repo to see a fully-fleshed out Django app:

<https://github.com/WDI-SEA/python-django-todo>

### Creating A New Site
```bash
django-admin startproject boardgamesite
cd boardgamesite
python3 manage.py startapp boardgames

createdb boardgamesite
```

**boardgamesite/boardgamesite/settings.py**
```
INSTALLED_APPS = [
    'boardgames.apps.BoardgamesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'boardgamesite',
				'HOST': 'localhost'
    }
}

TIME_ZONE = 'America/Los_Angeles'
```

**boardgamesite/boardgamesite/urls.py**
```python
urlpatterns = [
  url(r'^admin/', admin.site.urls),
  url(r'^boardgames/$', include('boardgames.urls'))
  url(r'^', include('boardgames.urls'))
]
```

**boardgamesite/boardgames/urls.py**
```python
urlpatterns = [
  url(r'^$', views.index, name="index"),
  url(r'^new/$', views.create, name="create"),
  url(r'^(?P<boardgame_id>[0-9]+)/$', views.details, name="details"),
  url(r'^(?P<boardgame_id>[0-9]+)/edit$', views.edit, name="edit")
]
```

**boardgamesite/boardgames/views.py**
```python
from django.shortcuts import render, redirect
from .models import BoardGame

def index(request):
  if request.method == "GET":
		context = {
			"games": BoardGame.objects.all()
		}
		return render(request, 'boardgames/index.html', context)
  elif request.method == "POST":
    game = Boardgame()
    game.name = request.POST["name"]
    game.rating = request.POST["rating"]
    game.review = request.POST["review"]
    game.save()

		return redirect(request, f'/boardgames/{game.id}/')

def create(request, game_id):
  return render(request, 'boardgames/create_form.html')

def details(request, game_id):
  # look up a game by it's primary key.
  game = Boardgame.objects.get(pk=game_id)
	context = {
    "game": game
	}
  return render(request, 'boardgames/details.html', context)

def edit(request, game_id):
  game = Boardgame.objects.get(pk=game_id)
	context = {
    "game": game
	}
  return render(request, 'boardgames/edit_form.html', context)
```
