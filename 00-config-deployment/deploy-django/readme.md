# Deploying Django Apps on Heroku

We'll walk through deploying your Django app on Heroku. Order of operations will be as follows:

* Install `pipenv`
* Set up Pipfile
* Install `gunicorn`
* Create Procfile
* Static Assets & Whitenoise
* Database settings / Split settings
* Generate Lockfile, `Pipfile.lock`
* Deploy to Heroku
    - Create App
    - Set Config Vars
    - Provision Database
    - Push code
    - Collectstatic for Static Assets

## Pipenv

Install `pipenv` via your terminal. 

```
pip install pipenv
```

> Protip: Pipenv is a package that will help us manage Pipfiles. We can also install packages with pipenv, which will be similar to how regular `pip` install works, but it also automatically adds the package to the Pipfile.

## Get your Pipfile

Your Pipfile is a list of dependencies for your Django app. It replaces the old way of keeping track of this, where you would use a freeze command to create a `requirements.txt` file. Now instead we will have `Pipfile` and `Pipfile.lock`. We'll cover the lock file in a moment. For now, let's set up your Pipfile.

> Tip: You may see a lot of code on the internet that still uses requirements.txt. Remember, Pipfiles are a reaplcement for this. We do not need a requirements.txt!

#### What goes in the Pipfile?

According to the [Pipenv docs](https://docs.pipenv.org/basics/), when you run the `pipenv --python 3` command, if you don't have a Pipfile already, one will be generated for youthat looks like this:

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]

[requires]
python_version = "3.6"
```

This is a pretty good start. The only section we really need to put any thinking into is the `[packages]` section. Here, we just need to include any packages we actually import and use. This means, don't worry about sub-dependencies as they will be installed automatically!

## Gunicorn

Gunicorn is a server that supports concurrent processes. It will make your Heroku app feel faster and be better utilized.

```
pipenv install gunicorn
```

The command above both installs gunicorn and adds it to the Pipfile. If after your app is up and running, you are experiencing performance issues, take a read through [Heroku's Docs regarding Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn) and configure WEB_CONCURRENCY and/or preload settings accordingly.

## Procfile

Now that we have Gunicorn installed, let's use it! Create a file called `Procfile` in the top level folder of you app.

> Remember the capital `P` in `Procfile`!

Your Procfile should look like the following:

```
web: gunicorn yourappname.wsgi
release: python manage.py migrate
```

Obviously, replace `yourappname` with your actual app name. The release command will do any database migrations that are needed upon deployment.

## Static Assets and Whitenoise

Unfortunately, Django makes you jump through some hoops to get static files working in the production environment.

You can follow the directions on [their docs](http://whitenoise.evans.io/en/stable/django.html) to get it set up.

After you're done with that, run the following commnd to collect your assets into the static folder:

```
heroku run python manage.py collectstatic
```

## Set up Database Settings

There's no one way to do this, but you'll eventually find that you need different settings between a development environment and a production environment. We'll need to set up our database settings in `settings.py` to be configured for our production environment. These settings will be different than our development environment settings. There are a couple ways to go about this.

First option is that you can comment/uncomment the production code right before you push each time. This can get tedious after awhile.

The second option is to make separate settings.py files for development and production environments. 

The third option is to make an environment variable that you check in your settings.py file and load things you need within conditional statements.

The fourth option is to use a third party tool that handles it for you.

> NOTE: In a professional setting, you'll have a test environment (and possibly a staging environment) too! Test environments typically mirror production and act as a place you can test things outside of your local machine so that code doesn't go straight from development to production.

#### Splitting up settings

This website has [directions and code examples for all three options](https://www.webforefront.com/django/configuredjangosettings.html). Enjoy!

## Lock that Pipfile

We'll use `pipenv` to lock up our Pipfile, creating a file called `Pipfile.lock`. You will want to relock your Pipfile any time you make changes to it. Regenerate your lock file with the following command:

```
pipenv lock
```

> Warning: Never change your `Pipfile.lock`! It is always to be generated and never to be touched!


## Deploy!

#### Before Deploying...

At this point in the process, the Pipfile looks something like this

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]
django = "*"
gunicorn = "*"
django-heroku = "*"
django-cors-headers = "*"
dj-database-url = "*"

[requires]
python_version = "3.6.5"
```

Make sure you've locked the latest version of the Pipfile before pushing to Heroku!

```
pipenv lock
```

#### Create Heroku App

You can use the heroku CLI to create an app in your terminal. This will automatically hook up the remote correctly from the folder you run the command in (make sure you're in the root/top-level!).

```
heroku apps:create yourappnamehere
```

#### Config variables

Remember to add any config variables!

```
heroku config:set MY_ENV_VAR=123
```

You can also do this in the Heroku dashboard in your web browser if you wish! If you didn't use any environment variables, you can skip this step. Alternatively, if you forget this step or end up adding variables later, you can do this step again any time as it is not a part of the deployment process!

#### Provision your database

Heroku uses an addon to support Postgres. You can add it with the following command:

```
heroku addons:create heroku-postgresql:hobby-dev
```

#### Push the code!

Once that's done, go ahead and push to Heroku using git.

```
git add .
git commit -m "Deploying Django App"
git push heroku master
```

This will trigger a build. The first build will take the longest. After that, it will start to cache some of your packages to make it faster.

> NOTE: The caching behavior can be a blessing or a curse. While going faster is great a majority of the time, if you somehow get the wrong version of a package installed, you may have a difficult or impossible time trying to get it to wipe that version from its cache. 

## Troubleshooting

As normal, check your heroku logs to see what errors have come up. Logs will also contain any print statements you've left in your code (which you definitely should take out once you've debugged!) You can access the logs by typing `heroku logs` in your terminal while in the folder containing your Django app (top level).

## Resources

* [Pipfile Docs](https://github.com/pypa/pipfile) - this includes an explanation about why Pipfile is superior to requirements.txt
* [Pipenv Docs](https://docs.pipenv.org/basics/) - this includes more info on default settings
* [Pipenv Guide](https://realpython.com/pipenv-guide/) - more explanations of best practices in less technial language
* [Heroku's Docs regarding Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn)
* [Provisioning Postgres DB on Heroku](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres)
* [Django-configurations](https://django-configurations.readthedocs.io/en/stable/) - Official docs on settings.py
* [Configure Django Settings](https://www.webforefront.com/django/configuredjangosettings.html) - A helpful tool that explains how to set up your settings.py in layman's terms!
* [Django Whitenoise Docs](http://whitenoise.evans.io/en/stable/django.html)
