# Deploy React

## Deploy React to Heroku

### Objectives

* Install `create-react-app` tool
* Create a fresh React app with `create-react-app`
* Use create-react-app-buildback to deploy app to Heroku

## Documentation

[https://github.com/facebookincubator/create-react-app](https://github.com/facebookincubator/create-react-app)

[https://github.com/mars/create-react-app-buildpack\#quick-start](https://github.com/mars/create-react-app-buildpack#quick-start)

## Create a React App and Deploy It

It's very, very, very, very easy to start up a React app and deploy it to Heroku. Developers have created tools to automate the entire process.

Download and install a command line tool `create-react-app` with npm and make it available globally with the -g flag:

```text
npm install -g create-react-app
```

Now, use the new `create-react-app` command in your terminal to create an app, then `cd` into the directory and you can immediately deploy it using a Heroku "buildpack" someone has designed to automatically configure React apps to work on Heroku.

Replace $APP\_NAME with whatever you want to call your app directory, and what your want your app's subdomain to be when it's deployed on Heroku.

```text
create-react-app $APP_NAME
cd $APP_NAME
git init
heroku create $APP_NAME --buildpack https://github.com/mars/create-react-app-buildpack.git
git add -A
git commit -m "new react app"
git push heroku master
heroku open
```

After seeing lots of command line wizardry happen before your eyes you should see Heroku print out a URL to the console. Visit that URL and you'll see your site all up and running.

Wow. Just wow.

