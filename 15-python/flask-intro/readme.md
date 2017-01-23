# Intro to Flask

## Objectives
* Use the Flask microframework to create a Python web server
* Configure a GET route to send raw data
* Configure a GET route accept query parameters
* Configure the server to serve static content
* Use PyMongo to connect the server to a MongoDB database

<http://flask.pocoo.org/>
<http://api.mongodb.com/python/current/tutorial.html>

## Install Flask and Create a Minimal Server
Use your terminal's `pip3` command to install Flask for Python3.

```
pip3 install Flask
```

Now that Flask is install, create a file `server.py` that imports Flask and
configures a simple GET route at the server's root. You'll notice the way
Flask defines routes is very similar to how routes are defined in Express!

It's this simple:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

if __name__ == "__main__":
  app.run()
```

## Configure Route Variables
Like Express, Flask allows us to bake valuable information into our URL
structure. Embedding information into our URLs allows our web applications
to have beautiful URLs that users can remember easily.

Flask extracts the string in the part of the URL and passes it to the route
function as a parameter. It will automatically keep the value as a string
unless you specify another type, like `int`. If you specify a type Flask runs
the value through what it calls a "convertor". Flask comes with a few
convertors out of the box.

**IMPORTANT:** Flask expects every route to eventually return a String. Look at
the multiply route example. Although it specifies that it accepts two `ints` as
route variables it still must manually convert the mathematical result into a
String before the server sends a response.

| Convertor Name | Description |
| -------        | -----       |
| string         | accepts any text without a slash (the default) |
| int            | accepts integers |
| float          | like int but for floating point values |
| path           | like the default but also accepts slashes |
| any            | matches one of the items provided |
| uuid           | accepts UUID strings |

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"
  
@app.route("/profile/<username>")
def profile(username):
  return "You're viewing {}'s profile.".format(username)
  
@app.route("/r/<subreddit>")
def profile(subreddit):
  return "Welcome to the {} subreddit!".format(subreddit)
  
  
@app.route("/multiply/<int:num1>/<int:num2>")
def multiply(num1, num2):
  result = num1 * num2
  return str(result)

if __name__ == "__main__":
  app.run()
```

## Serve Static Content
The `app = Flask()` function includes useful parameters to customize how static
content is served. These two parameters define where your static directory is
located, and where that directory is made available as a URL on your server.

* **static_folder** defines the name of the directory containing static content.
* **static_url_path** defines what URL you have to direct your browser to to
  access the static content.
  
* if **static_url_path** is not defined then it defaults to `'static'` and
  an `index.html` in the static directory would be accessible at
  <http://127.0.0.1:5000/static/index.html>
* if **static_url_path** is set to `'public'` then your index page would be
  available at <http://127.0.0.1:5000/public/index.html>
* if **static_url_path** is set to an empty string `''` then your index page
  is available at the server root: <http://127.0.0.1:5000/> (this is most
  likely what you want.)
  
You can serve a simple index.html file that includes a script tag link to Angular
and now you've got a simple server serving an Angular app!
  
Application directory structure:

```
~/Code/my_flask_server/
--server.py
--static/
----index.html
```

**server.py**
```python
from flask import Flask
app = Flask(__name__, static_folder='static', static_url_path='')

if __name__ == "__main__":
  app.run()
```

## Connect to MongoDB
Flask recommends using a Python library called **PyMongo** to connect to and
interact with MongoDB. You'll find that PyMongo is "pythonic" in that it's easy
to use and it's designed to be readable. The syntax it uses almost seems like
you're writing inside the Mongo shell itself.

First, use `pip3` in your terminal to install PyMongo.

```
$ pip3 install pymongo
```

Remember to start your local MongoDB server:

```
$ mongod
```

**mongo-server.py**:
```python
from pymongo import MongoClient

# import datetime so we can have timestamps on things we add to the database.
import datetime

# import pprint so we can pretty print objects from the database.
import pprint

# pymongo connects to the default host and port if you don't specify any
# parameters to the constructor when it's initialized. If you need to connect
# to a non-default MongoDB on your local machine then simply specify the host
# and port:
# host = 'localhost'
# port = 27017
# client = MongoClient(host, port)
client = MongoClient()
db = client.test_database

# drop the collection if it already exists so here's a clean slate.
db.drop_collection("blogposts")

# grab a reference to a database, access a collection using "db.collectionname"
collection = db.blogposts

post1 = {"author": "Guido",
  "text": "Idea for a Programming Language",
  "tags": ["python", "release", "development"],
  "date": datetime.datetime(1989, 12, 23, 12)
}

post2 = {"author": "Mongo Team",
  "text": "Introducing MongoDB!",
  "tags": ["mongodb", "release", "development"],
  "date": datetime.datetime(2009, 11, 12, 12)
}

post3 = {"author": "Guido",
  "text": "Using MongoDB, Python and Flask",
  "tags": ["python", "mongodb", "pymongo", "development"],
  "date": datetime.datetime(2012, 2, 5, 12)
}

# insert one blog post to the collection.
post_id = db.blogposts.insert_one(post1).inserted_id

# verify the blog post has been added.
# find a document in collection in a few different ways.
db.blogposts.find_one()
db.blogposts.find_one({"author": "Guido"})
retrieved_post = db.blogposts.find_one({"_id": post_id})

print("Verifying Guido's post was created:")
pprint.pprint(retrieved_post)
print()

# Add several blog posts to the collection at once using .insert_many()
db.blogposts.insert_many([post2, post3])

# query for several blogposts
print("Finding all blog posts:")
for post in db.blogposts.find():
  pprint.pprint(post)
print()
  
print("Total posts:", db.blogposts.count())
print("Total posts by Guido:", db.blogposts.find({"author": "Guido"}).count())
print()

# use mongo's "dollar-sign" query operators
print("Finding blog posts after the year 2000:")
d = datetime.datetime(2000, 1, 1, 12)
for post in db.blogposts.find({"date": {"$gt": d}}).sort("author"):
  pprint.pprint(post)
```

Refer to MongoDB documentation to find out more details about how to interact
with MongoDB through PyMongo.

You'll find that methods are probably called just about what you expect them
to be called. Here's some popular methods:

* insert_one
* insert_many
* find_one
* find_many
* fine_one_and_update
* fine_one_and_delete
* update_one
* update_many
* delete_one
* delete_many

Entire API: <http://api.mongodb.com/python/current/api/index.html>
Collection level docs: <http://api.mongodb.com/python/current/api/pymongo/collection.html>

# Last Remarks
There you go! That's the basics of using Python together with Flask. Remember,
Flask calls itself a "microframework". It tries to do provide developers with
just what they need to create a simple web server and nothing more. It stays
out of the way of making major development decisions for you and relies on
developers creating powerful web servers by choosing their own components to
deal with things like Database management and whatever else you'd need.

Flask adheres to the [Unix Philosphy](https://en.wikipedia.org/wiki/Unix_philosophy)
where they "strive to do one thing and do it well."

Here's a summary of the Unix Philosophy:

* Write programs that do one thing and do it well.
* Write programs to work together.
* Write programs to handle text streams, because that is a universal interface.

# Microframework vs Monolithic Framework
In contrast, we'll also learn about another Python web framework: Django.
Django is a "monolithic" framework that involves itself in much more in the
configuration and operation of a web server. Whereas Flask makes zero decisions
for you and relies on developers importing lots of Third-party libraries, Django
comes with LOTS of tools in it's box. Django uses it's own template system,
has it's own Object Relation Model (ORM) that it uses to interact with databases
and even includes it's own administrative tools, that are actually really
awesome and allow you to easily build websites where you get an administrative
panel where you can edit entries in your database within the website.

Both frameworks have their advantages. If you're looking to pop something up
quick and light, then use Flask and follow their motto of bringing in
dependencies, "drop by drop." If you're looking to build a site that would
benefit from already-integrated user accounts, and batteries-included
administrative tools, then Django might be a better choice.

Happy developing.
