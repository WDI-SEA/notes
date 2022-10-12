# Deploy - Node/MongoDB

## MEN Stack Deploy Jam

Instructions for how to deploy MEN stack apps using MongoDB Atlas and Heroku

### Overview

* We will be using [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) to host our database.

> MongoDB Atlas is a free database service provided by MongoDB. We will have to sign up for an account and configure our server to use MongoDB Atlas when it is deployed.

* We will be using [Heroku](https://www.heroku.com/) to host our express server.

> Heroku is a free hosting service that supports deployment for a variety of apps. We will have to sign up for an account and configure our environment variables here.

### Before We Start

If you don't already have a `.gitignore` file, create it now in the top-level

* Make sure `node_modules` folder is included in `.gitignore`. This ensures that once we delete the `node_modules` folder, git won't find it again.
  * If you've forgotten to use `.gitignore` and accidentally checked in the `node_modules` folder to git, you can remove it with the following command: `git rm -r node_modules`
* Also make sure `.env` is included in `.gitignore`
  * If you've accidentally checked in your `.env` file to git, you can remove it from git with the `git rm .env` command
* Make sure your modules are all installed with `npm i`
* Make sure your code runs using `nodemon`
  * Do you get an error that looks like "xyz module is not found"? We might be missing some dependencies! Run the following command for each module you're missing:

    `npm install xyz`
* git `add`, `commit`, and `push` all your code to github! 

### MongoDB Atlas

Let's setup our application to use MongoDB Atlas rather than localhost for the database!

1. [Create an account](https://account.mongodb.com/account/register) at MongoDB Atlas
2. Create a free tier cluster by following [these instructions](https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/)
   * For the Cluster Name, choose a descriptive name, like the name of your project!
3. Go to Securty &gt; Network Access \(from menu on left of page\) to [Whitelist an IP address](https://docs.atlas.mongodb.com/tutorial/whitelist-connection-ip-addres/)
   * Click on the _allow access from anywhere_ button to add `0.0.0.0/0` as an accepted IP address.
4. Go to Security &gt; Database Access to [add a user](https://docs.atlas.mongodb.com/tutorial/create-mongodb-user-for-cluster/)
   * **Note:** Make sure you keep track of this password, we'll need it later!
5. Go to Databases &gt; Connect &gt; Connect your application to find your MongoDB connection string
   * It will look similar to this: `mongodb+srv://cluster_name:your_db_users_password@cluster0.9hqnh.mongodb.net/<database_name>?retryWrites=true&w=majority`
6. Add the connection string to `.env`
   * Replace `<cluster_name>, <your_db_users_password>`, and `<db_name>` with your values.
   * `MONGODB_URI=mongodb+srv://cluster_name:your_db_users_password@cluster0.9hqnh.mongodb.net/<database_name>?retryWrites=true&w=majority`

#### Connect our Express app to MongoDB Atlas

In `models/index.js`:

```javascript
const mongoose = require('mongoose');

// Fire off the connection to Mongo DB
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  useCreateIndex: true,
  useFindAndModify: false
});


mongoose.connection.on('connected', () => {
  console.log(`Mongoose connected to ${mongoose.connection.host}:${mongoose.connection.port}`);
});

mongoose.connection.on("error", (err) => {
  console.log("Could not connect to MongoDB!", err);
});
```

Run `nodemon` to see if your application has successfully connected to MongoDB Atlas!

You should see in your terminal a message similar to:

```text
Mongoose connected to sei-shard-00-02.cqysw.mongodb.net:27017
```



<!-- 
### Heroku

#### Get a Heroku account and install the CLI tool!

1. [Create an account](https://www.heroku.com/) at heroku
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

#### Log in

This is a command-line tool that allows us to use commands in the terminal, similar to the way that we use git.

Once it is installed, you need to login with your heroku credentials:

* You may see an option to login via your browser: ![heroku cli](../.gitbook/assets/heroku-cli.png) ![heroku website](../.gitbook/assets/heroku.png)
* Or you may see an option to log in inside the cli

  ```text
  heroku login
  Enter your Heroku credentials.
  Email: name@example.com
  Password (typing will be hidden):
  Authentication successful.
  ```

We'll have the ability to create free applications using Heroku, but with limitations. Most of those limitations are related to the size of the databases, as well as uptime for the dynos. For free applications, dynos will "go to sleep" when unused for a period of time. This will lead to slow start times when restarting the dynos.

## Deploy!

![deploy](../.gitbook/assets/snail_deploy.gif)

#### To start:

* Create a `Procfile` in the root of your Node application
  * In terminal, run `touch Procfile`. Must be called with a capitol P
  * make sure it is named "Procfile" \(no extention\)
  * make sure your Procfile is at the same directory level as your server.js file
  * in terminal type `echo "web: node server.js" >> Procfile` (this assumes your main entry point is called `server.js` - if it's `index.js` or something else, replace that part of the command accordingly)
* In your `server.js` file, where you get your server started, include the port number in your app.listen function. Example:

```javascript
app.listen(process.env.PORT || 8000)
```

This ensures that when we set the PORT config variable, Heroku will run on it instead of the 3000 port \(Heroku automatically includes a port that's public-facing\).

> Now git add, commit, and push all of your changes!

* Your package.json file is **crucial** - when you deploy your application, Heroku will check the package.json file for all dependencies. You can always check your package.json to see if you are missing anything.
* Before you create your app in Heroku, be sure your project is being tracked via a git repository.
* Create a Heroku app via the command line \(or, if you prefer you can use the website GUI to create it, then follow directions on the website to connect it to your git repo\)

```text
heroku apps:create <your_app_name>
```

In this case, `your_app_name` is the name of your app. This will create a url like: `http://your_app_name.herokuapp.com`.

* This name needs to be completely unique!
* `git add`, `commit` and `push` all your data at this point.
* To push to Heroku, enter the following command

```text
git push heroku main
```

This should push all your code to Heroku and trigger a build.

### Heroku Envionment variables

Next we want to make sure we have config variables. This is Heroku's version of a `.env` file or environment variables. Any variable names that are found in your local `.env` file should have a corresponding variable on Heroku.

In your javascript code, you might have something like `process.env.GOOGLE_KEY`. In order to add environment variables to Heroku. We can run a Heroku command to set it per item in our .env file \(see [docs](https://devcenter.heroku.com/articles/config-vars#set-a-config-var) for more on configuring environment vars in heroku\)

In this case, let's add our `MONGODB_URI` environment variable to heroku

```text
heroku config:set MONGODB_URI=MONGODB_URI=mongodb+srv://cluster_name:your_db_users_password@cluster0.9hqnh.mongodb.net/<database_name>?retryWrites=true&w=majority
```

Alternatively, you can set these fields in the Heroku GUI under the settings tab and then click "Reveal Config Vars".

> Finally run `heroku open` to open your hosted app in the browser!

### Debugging Tips

`heroku logs`

Displays the logs from the server

`heroku logs --tail`

Displays logs from the server in real-time.

`heroku run bash`

This command allows you to run a terminal shell _**on Heroku's server**_. This provides a handy way to poke around and run commands on the server side.
-->
