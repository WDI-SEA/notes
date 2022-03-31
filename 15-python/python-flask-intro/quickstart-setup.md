# Flask Setup Steps:

The [flask docs](https://flask.palletsprojects.com/en/1.1.x/) are great!

Here are the steps to spin up a flask server:

* First create a virtual environment for your project from the steps outlined [here](15-pythonpython-virtual-enviroments/readme.md)
* install the needed packages for your flask app:
  * `pip install flask` `pip install python-dotenv`
* touch the main entrypoint for your flask app, such as `app.py`
* touch `.flaskenv` and populate it with the needed environmental variables to config flask 
  * .flaskenv doesn't need to be in the .gitignore, it is for flask configuration only. But if you have any API keys or other secrets, you can touch a `.env` file and put them in there.
```sh
# example .flaskenv
# this will enable debug mode in flask
FLASK_ENV=development
# this is main entry point for the flask app
FLASK_APP=app.py
# this is the port to listen on (default is 5000 if you don't specify)
FLASK_RUN_PORT=3000
```
* populate your flask app's entry point file:
```python
# in app.py

# import flask
from flask import Flask

# config app
app = Flask(__name__)

# make route!
@app.route('/')
def hello_world():
  return 'Hello from Flask 👋'
```
* use `flask run` to run your app!
* If you have secret API keys in a `.env` file, you can access them like this:
```python
# import dotenv
from dotenv import load_dotenv
# import the operating system
import os

# this is how you get environmental variables
print(os.environ['MY_BIG_SECRET'])
```
* the corresponding `.env` file would look like this:
```sh
# in .env
MY_BIG_SECRET='pls dont tell anyone my secrets 🙏🏻😳' 
```

*If you add environmental variables while your flask app is running, you need to stop the server with `control + c` and restart it with `flask run` to read them* 
