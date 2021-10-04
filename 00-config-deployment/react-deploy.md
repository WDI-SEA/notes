# Deploy React

## Objectives

* Install `create-react-app` tool
* Create a fresh React app with `create-react-app`
* Use create-react-app-buildback to deploy app to Heroku

## Documentation

[https://github.com/facebookincubator/create-react-app](https://github.com/facebookincubator/create-react-app)

[https://github.com/mars/create-react-app-buildpack\#quick-start](https://github.com/mars/create-react-app-buildpack#quick-start)

## Create a React App with create-react-app

It's very, very, very, very easy to start up a React app and deploy it to Heroku. Developers have created tools to automate the entire process.

Use the `npx create-react-app` command in your terminal to create an app, then `cd` into the directory and you can immediately deploy it using a Heroku "buildpack" someone has designed to automatically configure React apps to work on Heroku.

Replace `$APP_NAME` with whatever you want to call your app directory, and what your want your app's subdomain to be when it's deployed on Heroku.

```text
npx create-react-app $APP_NAME
cd $APP_NAME
```

Now set up a github and start git tracking this app!

## Deploy

In terminal, run the following from _inside your react app directory_:

```text
heroku create $APP_NAME --buildpack https://github.com/mars/create-react-app-buildpack.git
git add -A
git commit -m "new react app"
git push heroku main
heroku open
```

After seeing lots of command line wizardry happen before your eyes you should see Heroku print out a URL to the console. Visit that URL and you'll see your site all up and running.

Wow. Just wow.

