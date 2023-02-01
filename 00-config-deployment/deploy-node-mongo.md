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
  // !IMPORTANT: these two options are mission critical for the deployment to work
  useNewUrlParser: true,
  useUnifiedTopology: true,
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

#### Get a Heroku account!

1. Make sure you have an account with heroku: [https://www.heroku.com/](https://www.heroku.com/)
  * **_YOU SHOULD SIGN UP WITH YUOR GITHUB ACCOUNT_**
2. Make sure you have installed the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
3. Follow this [link](https://devcenter.heroku.com/articles/eco-dyno-hours) to set up 'eco dyno hours' which is Heroku's least expensive postgres service tier.

#### Install Heroku CLI

This is a command-line tool that allows us to use commands in the terminal, similar to the way that we use git.

Once it is installed, you need to login with your heroku credentials:

```text
heroku login
Enter your Heroku credentials.
Email: adam@example.com
Password (typing will be hidden):
Authentication successful.
```

We'll have the ability to create free applications using Heroku, but with limitations. Most of those limitations are related to the size of the databases, as well as uptime for the dynos. For free applications, dynos will "go to sleep" when unused for a period of time. This will lead to slow start times when restarting the dynos.

### DEPLOY!

![deploy](../.gitbook/assets/snail_deploy%20%281%29.gif)

#### To start:

* Create a `Procfile` in the root of your Node application
  * In terminal, run `touch Procfile`. Must be called with a capitol `P`
  * make sure it is named "Procfile" \(no extention\)
  * make sure your Procfile is in the same folder as your index.js file
  * in terminal type `echo "web: node index.js" >> Procfile`
* In your `index.js` file, where you get your server started, include the port number in your app.listen function. Example:

```javascript
app.listen(process.env.PORT || 3000)
```

This ensures that when we set the PORT config variable, Heroku will run on it instead of the 3000 port \(Heroku automatically includes a port that's public-facing\).

* Your package.json file is **crucial** - when you deploy your application, Heroku will check the package.json file for all dependencies. You can always check your package.json to see if you are missing anything.
* To migrate our live database we need a local version of `sequelize-cli` module in our package json. Add it by running `npm install sequelize-cli`
* Before you create your app in Heroku, be sure your project is being tracked via a git repository.
* Create a Heroku app via the command line \(or, if you prefer you can use the GUI to create it and follow its directions to connect it to your git repo\)

### Git Integration

There are two ways to handle git integration on heroku: the first is by creating a heroku git remote and pushing up to it. This way requires you to commit some changes and push up to trigger a redeploy, which can be a drawback. The second links your github repo to heroku in a `CI/CD` or _continuous integration/continuos deployment_ setup. Heroku will automatically deploy when it sees changes on github, and allows you to manually trigger a redeploy, which can be useful.

**_YOU ONLY NEED TO DO ONE OF THESE_**

#### First Way: Heroku Remote

```text
heroku apps:create sitename
```

In this case, `sitename` is the name of your app. This will create a url like: `http://sitename.herokuapp.com` - you'll find that you have to come up with a completely unique name.

* Commit and push all your data at this point \(`git push`\).
* To push to Heroku, enter the following command

```text
git push heroku main
```

This should push all your code to Heroku and trigger a build.

#### Second Way: `CI/CD`

1. (if needed)  Navigate to the `Deploy` tab on your Heroku dashboard and click the 'Connect to Github' button if needed. Follow the prompts to integrate your github.

![connect to gh](./imgs/connect-to-gh.png)

2. Search for your repo name, and click the connect button once you find it. Choose a branch to deploy from the dropdown menu and click 'Enable Automatic Deploys'. It will look something like this:

![all done](./imgs/all-done.png)

If you ever need to manually trigger a redeploy, scroll to the bottom of the deploy tab and click the 'Deploy Branch' button.

![manual deploy](./imgs/manual-deploy.png)

Finllay, return to your local command line and in the project directory run the command `heroku git:remote -a < your heroku app name >` to link your command line with the app on heroku.

### Heroku Envionment variables

Next we want to make sure we have config variables. This is Heroku's version of a `.env` file or environment variables. Any variable names that are found in your local `.env` file should have a corresponding variable on Heroku.

In your javascript code, you might have something like `process.env.GOOGLE_KEY`. In order to add environment variables to Heroku. We can run a Heroku command to set it per item in our .env file \(see [docs](https://devcenter.heroku.com/articles/config-vars#set-a-config-var) for more on configuring environment vars in heroku\)

```text
heroku config:set S3_KEY=8N029N81 S3_SECRET=9s83109d3+583493190
```
Run with 'code -' to read from stdin (e.g. 'ps aux | grep code | code -').
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
