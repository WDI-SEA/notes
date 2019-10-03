# Deploying Flask Apps on Heroku

In this lesson we'll cover:

* Pipfiles
* Procfiles
* Configuration

## Prerequisites

Before we get started, we need a couple tools. Let's install a few things and set them up.

### Pipenv

Install `pipenv` via your terminal. 

```
pip install pipenv
```

> Protip: Pipenv is a package that will help us manage Pipfiles. We can also install packages with pipenv, which will be similar to how regular `pip` install works, but it also automatically adds the package to the Pipfile.

### Create Your Pipfile

Your Pipfile is a list of dependencies for your Flask app. It replaces the old way of keeping track of this, where you would use a freeze command to create a `requirements.txt` file. Now instead we will have `Pipfile` and `Pipfile.lock`. We'll cover the lock file in a moment. For now, let's set up your Pipfile.

> Tip: You may see a lot of code on the internet that still uses requirements.txt. Remember, Pipfiles are a reaplcement for this. We do not need a requirements.txt!

#### What goes in the Pipfile?

According to the [Pipenv docs](https://docs.pipenv.org/basics/), when you run the `pipenv --python 3` command, if you don't have a Pipfile already, one will be generated for youthat looks like this:

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]

[requires]
python_version = "3.7"
```

This is a pretty good start. The only section we really need to put any thinking into is the `[packages]` section. Here, we just need to include any packages we actually import and use. This means, don't worry about sub-dependencies as they will be installed automatically!

### Gunicorn

Gunicorn is a server that supports concurrent processes. It will make your Heroku app feel faster and be better utilized.

```
pipenv install gunicorn
```

The `pipenv` command above both installs gunicorn *and* adds it to the Pipfile. If you installed with the `pip` or `pip3` commands, you will need to manually type the name gunicorn into your Pipfile. We're also going to want to type in `flask` as a package we are using. Your Pipfile should not look something like this:

```
[[source]]
name = "pypi"
url = "https://pypi.org/simple"
verify_ssl = true

[dev-packages]

[packages]
flask = "*"
gunicorn = "*"

[requires]
python_version = "3.7"
```

> Solving Performance Issues: If after your app is up and running, you are experiencing performance issues, take a read through [Heroku's Docs regarding Gunicorn](https://devcenter.heroku.com/articles/python-gunicorn) and configure WEB_CONCURRENCY and/or preload settings accordingly.

### Procfile

Now that we have Gunicorn installed, let's use it! Create a file called `Procfile` in the top level folder of you app.

> Remember the capital `P` in `Procfile`!

Your Procfile should look like the following:

```
web: gunicorn server:app
```

The "server" in the above command refers to the name of your entry point. So, it assumes you called your main file `server.py`. If you called your main file `app.py` then it would look like `web: gunicorn app:app`

> Tip: You can add a release step as well, which runs after the build succeeds. For example, this is often used for database migrations.

## Deploy!

Now we're ready to deploy! Create a Heroku app, then add, commit, and push to Heroku.

```
heroku apps:create <your-app-name-here>
git add -A
git commit -m "Ready for deployment!"
git push heroku master
```

### Configuration Variables

You can add configuration variables from the command line or via the GUI if you log into Heroku's website.

```
heroku config:set FLASK_ENV=production
heroku config:set FLASK_SECRET=SuperSecretKey
```

## Resources

* [Medium Article: Walk-through with Example Code](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)
