# Heroku Deployment with Node + Sequelize

## Objectives
* Describe what Platform as a Service (PaaS) is
* Identify other methods of deployment, and their benefits and drawbacks
* Take a working Node/Sequelize app and deploy it to Heroku
* Make changes to an existing deployment
* Utilize methods for debugging server errors

## Introduction

When we have finished developing a version of our app, we likely want to put it on the internet for other people to see.

You can use our Taco CRUD app for deployment. https://github.com/WDI-SEA/tacoapp

### Localhost

Most of what we've developed so far has just run on our own computers. Both our database and our web server have been on our computer. We've done this because it's much easier to develop locally because we don't actually need an internet connection. However, people can't access it easily unless they are also on our local network.

Options?

#### Buy Another Computer

We could just buy another computer somewhere else and use it to run our applications - or even more than one, if needed, and by the way, a server is a computer. We could connect this other computer to the internet and with a bit of configuration, we could allow people to connect to it using a URL.

However, we'd have to buy and look after this computer, have somewhere to store it and ensure that it was working and always connected to the internet. Also, if someone hit an error when they used our app, we might have to stop and start it? Maybe there is a better way?

#### Use a Cloud Computing Platform

We could also use Amazon Web Services or similar cloud services, which provide the servers needed to host applications via the cloud. While many companies use AWS for deployment (such as Netflix), we are expected to not only deploy our system, but also set up the system architecture for our application. This includes logging in to the remote server, setting up the web server, and managing configuration and databases. While this provides a lot of flexibility for larger applications, there's a large learning curve that leans towards Linux system administration. Luckily, there is an even better way.

#### Abstracting Cloud Computing

Heroku is a cloud-based, Platform as a Service (PaaS). Essentially it's a group of virtual machines that run on Amazon Web Services (EC2) and hosts your application code in the cloud. By using git, you can deploy your code directly to Heroku's machines - they call them "dynos" - and seconds later your changes will be live in production.

To deploy an app to Heroku, it's a fairly straightforward step-by-step process.

First you need to link your machine to your Heroku account - a similar process to what we did with Github.


## Before Deploying

### Check Your Github Repo

Do you notice a folder called "node_modules"? Or your .env file with your environment variables?

Oops! That's not supposed to be there! node_modules and .env should never escape from your local machine. It's going to goof up our stuff and cause errors if we leave it in there when we deploy to Heroku, so let's get rid of them!

* If you don't already have a .gitignore file, create it now in the top-level
* Make sure node_modules folder is included in .gitignore. This ensures that once we delete the node_modules folder, git won't find it again.
* Delete the node_modules folder in your local repo (don't worry - you can get it back by running "npm install")
* You will need to make sure git knows to remove the node_modules folder from the repo. Use the following command:
    **git rm -r node_modules**
* Ensure that your .env file, (if you have one) is also NOT included in your Github repo.
    * Repeat steps to remove from git with the git rm command
    * Add this file to .gitignore so git doesn't find it again.
* Commit and push these changes to your Github repo!
* Last, let's run npm install to recreate that node_modules folder.
* Try running your app with nodemon.
    - Does it work? Great, you're all done!
    - Do you get an error that looks like "xyz module is not found"? This is because originally, we forgot to include the --save flag when we originally npm installed it. Run the following command for each module you're missing:
        **npm install xyz --save**

TL;DR: Don't have node_modules in your repo, you'll have a bad time.

###Get a Heroku account!
1. Make sure you have an account with heroku: https://www.heroku.com/

2. Make sure you have installed the heroku toolbelt - [https://toolbelt.heroku.com/](https://toolbelt.heroku.com/)

###Install Heroku Toolbelt

This is a command-line tool that allows us to use commands in the terminal, similar to the way that we use git.

Once it is installed, you need to login with your heroku credentials:

```
heroku login
Enter your Heroku credentials.
Email: adam@example.com
Password (typing will be hidden):
Authentication successful.
```

We'll have the ability to create free applications using Heroku, but with limitations. Most of those limitations are related to the size of the databases, as well as uptime for the dynos. For free applications, dynos will "go to sleep" when unused for a period of time. This will lead to slow start times when restarting the dynos.

##DEPLOY!

![deploy](snail_deploy.gif)

### To start:

* Create a `Procfile` in the root of your Node application
  * In terminal, run `touch Procfile`. Must be called with a capitol P
  * make sure it is named "Procfile" (no extention)
  * make sure your Procfile is in the same folder as your index.js file)
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

Where `sitename` is the name of your app. This will create a url like: `http://sitename.herokuapp.com` - you'll find that you have to come up with a completely unique name.

* Commit and push all your data at this point (`git push`).

* To push to Heroku, enter the following command

```
git push heroku master
```

(You can skip this step because it's a default setting)
* In terminal after you deploy your app, type in `heroku ps:scale web=1`
  * this will scale a dyno up

## Connect a DB with Sequelize

You may notice that while you have a valid URL and the site is deployed, your site likely does not work when you visit it. This is because Heroku is not yet aware of our database and model structure. Let's make it aware.

* In terminal, install the add-on for postgres: `heroku addons:create heroku-postgresql:hobby-dev`
* Set your NODE_ENV variable to 'production' by running this command in terminal: `heroku config:set NODE_ENV='production'`
* Make sure your production variables in `config/config.json` are set like this (pay attention to the production setting).

**config/config.json**
```js
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

* To migrate our live database we need a local version of `sequelize-cli` module in our package json. Add it by running `npm install sequelize-cli --save`

* Add and commit your changes to git, then push your changes to heroku using `git push heroku master`

* Now run your migrations by typing in terminal `heroku run node_modules/.bin/sequelize db:migrate` and you should have all your tables set up in a heroku hosted database

* Try opening your app now, `heroku open`

**NOTE:**
You may notice that the data on your local machine does not travel up to Heroku. This is by design! Generally you're not going to want your development data to affect your production data! That said, there may be times when you want to seed data. Investigate the db:seed command of the [Sequelize CLI](https://github.com/sequelize/cli).

You can view your brand new database by executing the `psql` command you know and love on Heroku. Do this by typing
    **heroku pg:psql**
    
**WARNING (2017) Edited (2018):**
At one point, sequelize-cli, sequelize, and pg modules were not playing nicely with each other. Luckily, this issue (for version Sequelize 4) has been resolved and we can resume using the current versions of both. In the future, be mindful that many modules you use are maintained by individual third parties and issues like this may come up! 

If you used to use Sequelize 3, keep in mind that Sequelize 4 has breaking changes! If you need to upgrade your app, refer to these [docs](http://docs.sequelizejs.com/manual/tutorial/upgrade-to-v4.html#breaking-changes), which guide you in the update process.

## Heroku Envionment variables

In your javascript code, you might have something like `process.env.GOOGLE_KEY`.
In order to add environment variables to github. We will run a heroku command to set it per item in our .env file

```
heroku config:set S3_KEY=8N029N81 S3_SECRET=9s83109d3+583493190
```

## Something is broken?!?!?!?!

Don't panic! Type **heroku logs** to see the error and info messages from the Heroku server! Find the error and Google it if the meaning isn't readily apparent!

## Review
* App deployment
  * Login to Heroku using the Heroku toolbelt (only do once)
  * Create a Procfile and fetch your port in your app
  * Create a Heroku app
  * Push application to Heroku
* Sequelize setup
  * Install Heroku's postgres addon
  * Set the NODE_ENV variable on Heroku
  * Set the production database variables in `config/config.json`
  * Save a local version of `sequelize-cli` to the `package.json` file
  * Push application to Heroku
  * Run migrations on Heroku


## Resources

For all resources Heroku-related, check out the documentation on Heroku's website.

https://devcenter.heroku.com/articles/getting-started-with-nodejs

Some interesting (and free) addons you can add to your app:

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
