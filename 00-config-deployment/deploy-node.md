# Deploy - Node/Sequelize

## Heroku Deployment with Node + Sequelize

### Objectives

* Describe what Platform as a Service \(PaaS\) is
* Identify other methods of deployment, and their benefits and drawbacks
* Take a working Node/Sequelize app and deploy it to Heroku
* Make changes to an existing deployment
* Utilize methods for debugging server errors

### Introduction

When we have finished developing a version of our app, we likely want to put it on the internet for other people to see.

You can use our Auth Boilerplate app for deployment.

#### Localhost

Most of what we've developed so far has just run on our own computers. Both our database and our web server have been on our computer. We've done this because it's much easier to develop locally because we don't actually need an internet connection. However, people can't access it easily unless they are also on our local network.

Options?

**Buy Another Computer**

We could just buy another computer somewhere else and use it to run our applications - or even more than one, if needed, and by the way, a server is a computer. We could connect this other computer to the internet and with a bit of configuration, we could allow people to connect to it using a URL.

However, we'd have to buy and look after this computer, have somewhere to store it and ensure that it was working and always connected to the internet. Also, if someone hit an error when they used our app, we might have to stop and start it? Maybe there is a better way?

**Use a Cloud Computing Platform**

We could also use Amazon Web Services or similar cloud services, which provide the servers needed to host applications via the cloud. While many companies use AWS for deployment \(such as Netflix\), we are expected to not only deploy our system, but also set up the system architecture for our application. This includes logging in to the remote server, setting up the web server, and managing configuration and databases. While this provides a lot of flexibility for larger applications, there's a large learning curve that leans towards Linux system administration. Luckily, there is an even better way.

**Abstracting Cloud Computing**

Heroku is a cloud-based, Platform as a Service \(PaaS\). Essentially it's a group of virtual machines that run on Amazon Web Services \(EC2\) and hosts your application code in the cloud. By using git, you can deploy your code directly to Heroku's machines - they call them "dynos" - and seconds later your changes will be live in production.

To deploy an app to Heroku, it's a fairly straightforward step-by-step process.

First you need to link your machine to your Heroku account - a similar process to what we did with Github.

### Before Deploying

#### Check Your Github Repo

Do you notice a folder called "node\_modules"? Or your .env file with your environment variables?

Oops! That's not supposed to be there! node\_modules and .env should never escape from your local machine. It's going to goof up our stuff and cause errors if we leave it in there when we deploy to Heroku, so let's get rid of them!

* If you don't already have a `.gitignore` file, create it now in the top-level
* Make sure `node_modules` folder is included in .gitignore. This ensures that once we delete the `node_modules` folder, git won't find it again.
* Delete the `node_modules` folder in your local repo \(don't worry - you can get it back by running `npm install`\)
* You will need to make sure git knows to remove the `node_modules` folder from the repo. Use the following command:

    **git rm -r node\_modules**

* Ensure that your .env file, \(if you have one\) is also NOT included in your Github repo.
  * Repeat steps to remove from git with the git rm command
  * Add this file to .gitignore so git doesn't find it again.
* Commit and push these changes to your Github repo!
* Last, let's run npm install to recreate that `node_modules` folder.
* Try running your app with nodemon.
  * Does it work? Great, you're all done!
  * Do you get an error that looks like "xyz module is not found"? This is because originally, we forgot to npm install a module. This might happen for things that you've globally installed when we originally installed it \(with the -g flag\). Run the following command for each module you're missing:

      **npm install xyz**

TL;DR: Don't have `node_modules` in your repo, you'll have a bad time.

#### Get a Heroku account!

1. Make sure you have an account with heroku: [https://www.heroku.com/](https://www.heroku.com/)
2. Make sure you have installed the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

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
  * In terminal, run `touch Procfile`. Must be called with a capitol P
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

### Heroku Envionment variables

Next we want to make sure we have config variables. This is Heroku's version of a `.env` file or environment variables. Any variable names that are found in your local `.env` file should have a corresponding variable on Heroku.

In your javascript code, you might have something like `process.env.GOOGLE_KEY`. In order to add environment variables to Heroku. We can run a Heroku command to set it per item in our .env file \(see [docs](https://devcenter.heroku.com/articles/config-vars#set-a-config-var) for more on configuring environment vars in heroku\)

```text
heroku config:set S3_KEY=8N029N81 S3_SECRET=9s83109d3+583493190
```

Alternatively, you can set these fields in the Heroku GUI under the settings tab and then click "Reveal Config Vars".

### Connect a DB with Sequelize

You may notice that while you have a valid URL and the site is deployed, your site likely does not work when you visit it. This is because Heroku is not yet aware of our database and model structure. Let's make it aware. See [Heroku Postgres Docs](https://elements.heroku.com/addons/heroku-postgresql) for more.

* In terminal, install the add-on for postgres: `heroku addons:create heroku-postgresql:hobby-dev`
* Make sure your production variables in `config/config.json` are set like this \(pay attention to the production setting\).

**config/config.json**

```javascript
{
  "development": {
    "database": "projectdb",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "test": {
    "database": "projectdb",
    "host": "127.0.0.1",
    "dialect": "postgres"
  },
  "production": {
    "use_env_variable": "DATABASE_URL"
  }
}
```

* Add and commit your changes to git, then push your changes to heroku using `git push heroku main`
* So that we don't have to deal with configuring [SSL](https://www.globalsign.com/en/ssl-information-center/what-is-an-ssl-certificate), we need to add one more heroku config variable: `heroku config:set PGSSLMODE=no-verify`
* Now run your migrations by typing in terminal `heroku run sequelize db:migrate` and you should have all your tables set up in a heroku hosted database
* NOTE: If you have any seeder files to run, do that here as well! Simply type `heroku run` followed by the command you want to run on the production server.
* Try opening your app now, with the command `heroku open` or, simply visit the website in your browser.

**NOTE:** You may notice that the data on your local machine does not travel up to Heroku. This is by design! Generally you're not going to want your development data to affect your production data! That said, there may be times when you want to seed data. Investigate the db:seed command of the [Sequelize CLI](https://github.com/sequelize/cli).

You can view your brand new database by executing the `psql` command you know and love on Heroku. Do this by typing **heroku pg:psql**

## DEBUGGING HELP

### Something is broken?!?!?!?!

Don't panic! Type `heroku logs` to see the error and info messages from the Heroku server! Find the error and Google it if the meaning isn't readily apparent! Some fixes to common errors are found below!

#### Version Conflicts

**WARNING \(2017\) Edited \(2018, 2019\):** At one point, sequelize-cli, sequelize, and pg modules were not playing nicely with each other. It continues to be an intermittent issue that crops up every time one of these modules makes a new version with a breaking change. Be mindful that many modules you use are maintained by individual third parties and issues like this may come up!

This problem is unfortunately difficult to recognize since the error message is pretty much random each time. This time around it was:

```text
TypeError [ERR_INVALID_ARG_TYPE]: The "url" argument must be of type string. Received type undefined
```

Last time it was something along the lines of `rows is undefined`. Regardless, after some Googling of the error it seems to be related to Sequelize or Postgres, this is probably the underlying issue.

**So How to fix it?**

The fix to this problem is a bit of an inconvenience. The gist is that we will ensure we have versions of those 3 modules we are sure will work together properly. Then we need to delete the Heroku app and recreate it from scratch \(repeating the steps above regarding creating and migrating the database and setting all the config variables\).

As of January 2019, here is a dependencies list \(for a package.json\) that worked together. This will need to be updated for every one or two new classes.

```text
"dependencies": {
    "bcryptjs": "^2.4.3",
    "connect-flash": "^0.1.1",
    "dotenv": "^6.2.0",
    "ejs": "^2.6.1",
    "express": "^4.16.4",
    "express-ejs-layouts": "^2.5.0",
    "express-session": "^1.15.6",
    "passport": "^0.4.0",
    "passport-facebook": "^2.1.1",
    "passport-local": "^1.0.0",
    "pg": "^7.7.1",
    "sequelize": "^4.42.0",
    "sequelize-cli": "^4.1.1"
}
```

#### BCrypt Something Something...

Bcrypt is finicky. Try using `bcryptjs` if you haven't switched already. Older computers sometimes also have issues with the BCrypt module, which may mean you will need to look up a work-around.

#### Can't Find Module XYZ

Look in your local `package.json` and see if the module it says is missing is in the dependencies section. If not, run `npm install XYZ` \(replace XYZ with whatever your actual error message says\). Git add, commit, and push to Heroku to see if the error is resolved.

Alternatively, another cause of this error is when you are trying to require a local file or folder \(e.g., like your `models` folder\), and you have forgotten to put `./` in front of it. If you forget the `./` it thinks you mean a module rather than a local path, and it will go looking for a module called that and probably not find one \(hence the error\).

### Overview

* App deployment
  * Login to Heroku using the Heroku CLI \(only do once\)
  * Create a Procfile and fetch your port in your app
  * Create a Heroku app
  * Push application to Heroku
* Sequelize setup
  * Install Heroku's postgres addon
  * Set all config variables on Heroku
  * Set the production database variable in `config/config.json`
  * Install a local version of `sequelize-cli` to the `package.json` file
  * Push application to Heroku
  * Run migrations on Heroku

### Resources

For all resources Heroku-related, check out the documentation on Heroku's website.

[https://devcenter.heroku.com/articles/getting-started-with-nodejs](https://devcenter.heroku.com/articles/getting-started-with-nodejs)

Some interesting \(and free\) addons you can add to your app:

* [New Relic](https://elements.heroku.com/addons/newrelic)
  * Application monitoring
* [Papertrail](https://elements.heroku.com/addons/papertrail)
  * Logging management
* [Loader.io](https://elements.heroku.com/addons/loaderio)
  * Load testing for web applications
* [Deploy Hooks](https://elements.heroku.com/addons/deployhooks)
  * Send messages to Slack, Email, or an HTTP endpoint on deployment
* [Heroku Scheduler](https://elements.heroku.com/addons/scheduler)
  * Schedule tasks, similar to `cron`
* [Mailgun](https://elements.heroku.com/addons/mailgun)
  * API for sending emails
* [Cloudinary](https://elements.heroku.com/addons/cloudinary)
  * API for image uploads and delivery

