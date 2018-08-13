# Deploy Node + MongoDB to Heroku

## Objectives

* Deploy a MEAN app to a production server using Heroku
* Use the mLab addon and connect to a mLab instance

First, let's deploy the Node app to Heroku.

## Deploying the app

* Create a `Procfile` in the root of your Node application
  * In terminal, run `touch Procfile`. Must be called with a capitol P
  * make sure it is named "Procfile" (no extention) 
  * make sure your Procfile is in the same folder as your index.js file
  * in terminal type `echo "web: node index.js" >> Procfile`

* In your `index.js` file, where you get your server started, include the port number in your app.listen function. Example:

```js
app.listen(process.env.PORT || 3000)
```

This ensures that when we set the PORT config variable, Heroku will run on it instead of the 3000 port (Heroku automatically includes a port that's public-facing).

* Your package.json file is **crucial** - when you deploy your application, Heroku will check the package.json file for all dependencies so whenever you install anything with npm make sure to use `--save`. You can always check your package.json to see if you are missing anything.

* Before you create your app in Heroku, be sure your project is being tracked via a git repository.

* Create a Heroku app via the command line

```
heroku apps:create sitename
```

Where `sitename` is the name of your app. This will create a url like: `http://sitename.herokuapp.com`

* Commit and push all your data at this point (`git push`).

* To push to Heroku, enter the following command

```
git push heroku master
```

* In terminal after you deploy your app, type in `heroku ps:scale web=1`
  * this will scale a dyno up

## Connecting to a MongoDB Database

Before connecting the Node app to a MongoDB database, we'll need to install an addon called [mLab](https://elements.heroku.com/addons/mongolab). mLab is a cloud-hosted MongoDB database service that we can connect to.

In order to add the instance, you can use the Heroku toolbelt by typing this command:

```
heroku addons:create mongolab:sandbox
```

This will create a free database instance, limited to 496 MB in storage. Keep this in mind.

#### Configuring Mongoose

After creating the mLab addon, you'll be able to access an environment variable called `MONGODB_URI`. You'll want to connect to this URI on production. Alter your Mongoose connection to read this environment variable, but use the localhost string if the variable doesn't exist. Below is an example.

```js
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost/mydbname');
```

## Connecting to a mLab instance using Robomongo/Mongohub (or similar)

In order to view the contents of your MongoDB database using a GUI client like Robomongo, you can use the `MONGODB_URI`. This URI contains the connection information and credentials needed to connect.
