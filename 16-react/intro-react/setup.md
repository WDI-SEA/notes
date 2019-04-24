# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Hello World exercise - We do!


### Learning Objectives
*After this lesson, you will be able to:*
- Build a React app using `create-react-app`
- View `create-react-app` working locally

## Initial Setup

Let's jump right in! We'll create a skeleton React project and walk through it as we go.

An easy way to start React projects is to use a Terminal program called `create-react-app`. This excellent tool, created by Facebook, will help you set up a bare-bones React app instantly. We can simply install the package and start coding.

Let's use `npm` to install it globally so we'll always have it available in our Terminal. Run:

```sh
$ npm i -g create-react-app
```

Once it's installed, create a new directory to store the app you're about to write and `cd` to the folder. Then, use the tool to create a new React app. You'll have to give your new app a name; we're calling the example app "hello_world", since that'll be our first project.


```sh
$ create-react-app hello_world
```

The tool creates a new directory for your app, so move into it...

```sh
$ cd hello_world
```

Use `npm start` to start a server that will serve your new React application!

```sh
$ npm start
```

> You have now set up a Hello World app that you will continue working on during this lesson's exercises!

After running `$ npm start`, you can view the app at `http://localhost:3000`

> Note: If you ever need to stop the server, you can hit `ctrl-c` in the terminal window.

You'll notice the web page for our app automatically refreshes every time we save a file in the directory. This is an awesome feature of `create-react-app`


You can look in the directory and see the structure that `create-react-app` provides for us. It looks like this:

```sh
├── README.md
├── package.json
├── public
│   ├── favicon.ico
│   └── index.html
└── src
    ├── App.css
    ├── App.js
    ├── App.test.js
    ├── index.css
    ├── index.js
    └── logo.svg
```

Most of the important files are in the `src` directory. Specifically, we'll be using `src/App.js` and `src/index.js`.

---

## Stop / Catch Up / Investigate

Take some time and look at what's been generated. Specifically pay attention to `src/App.js` and `src/index.js`

Make small changes to the code in `src/App.js`, `src/index.js`, and `public/index.html` just to see what happens.

Your basic React app is up and running. Now you're ready to add complexity.
